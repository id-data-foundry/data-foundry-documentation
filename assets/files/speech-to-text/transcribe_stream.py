#!/usr/bin/env python3
"""
Data Foundry LocalAI Real-Time Streaming Speech-to-Text (STT) Client

Stream live microphone audio or a local WAV file over a persistent WebSocket
connection to Data Foundry's real-time STT endpoint (`/v1/audio/transcriptions/stream`),
receiving low-latency partial hypotheses and committed final segments.

Requirements:
    pip install websockets
    pip install sounddevice   # Only required for live microphone capture (--mic)

Usage:
    # Stream a WAV file (16-bit PCM)
    python transcribe_stream.py recording.wav --token YOUR_API_TOKEN
    python transcribe_stream.py recording.wav --token YOUR_API_TOKEN --realtime

    # Stream live audio from your microphone (press Ctrl+C to stop and flush)
    python transcribe_stream.py --mic --token YOUR_API_TOKEN
    python transcribe_stream.py --mic --duration 10 --token YOUR_API_TOKEN
"""

import argparse
import array
import asyncio
import base64
import inspect
import json
import os
import signal
import sys
import urllib.parse
import wave
from typing import AsyncIterator, Callable, List, Optional, Tuple


def build_ws_url(server: str) -> str:
    """Convert an HTTP(S) or WS(S) Data Foundry server URL to the streaming STT WebSocket URL."""
    raw = (server or "https://data-foundry.net").strip().rstrip("/")
    if not raw.startswith(("http://", "https://", "ws://", "wss://")):
        raw = f"https://{raw}"

    parsed = urllib.parse.urlparse(raw)
    ws_scheme = "wss" if parsed.scheme in ("https", "wss") else "ws"
    base_path = parsed.path.rstrip("/")
    if base_path.endswith("/v1/audio/transcriptions/stream"):
        ws_path = base_path
    elif base_path.endswith("/v1"):
        ws_path = f"{base_path}/audio/transcriptions/stream"
    else:
        ws_path = f"{base_path}/v1/audio/transcriptions/stream"

    return urllib.parse.urlunparse((ws_scheme, parsed.netloc, ws_path, "", "", ""))


def _connect_kwargs(connect_fn, api_token: str) -> dict:
    """Build version-compatible WebSocket auth header kwargs for `websockets.connect`."""
    headers = {"Authorization": f"Bearer {api_token}"}
    try:
        params = inspect.signature(connect_fn).parameters
        if "additional_headers" in params:
            return {"additional_headers": headers}
        if "extra_headers" in params:
            return {"extra_headers": headers}
    except (TypeError, ValueError):
        pass
    return {"additional_headers": headers}


def _downmix_pcm16_to_mono(pcm_bytes: bytes, channels: int) -> bytes:
    """Average multi-channel 16-bit little-endian PCM frames to mono without `audioop`."""
    if channels <= 1 or not pcm_bytes:
        return pcm_bytes

    samples = array.array("h")
    samples.frombytes(pcm_bytes)
    if sys.byteorder != "little":
        samples.byteswap()

    frame_count = len(samples) // channels
    mono = array.array("h", [0] * frame_count)
    for i in range(frame_count):
        base = i * channels
        total = 0
        for ch in range(channels):
            total += samples[base + ch]
        mono[i] = int(total / channels)

    if sys.byteorder != "little":
        mono.byteswap()
    return mono.tobytes()


def read_wav_chunks(
    wav_path: str,
    chunk_ms: int = 128,
) -> Tuple[int, List[bytes]]:
    """Read a 16-bit PCM WAV file into mono PCM16 chunks and return `(sample_rate, chunks)`."""
    if not os.path.exists(wav_path):
        raise FileNotFoundError(f"Audio file not found: {wav_path}")

    with wave.open(wav_path, "rb") as wf:
        channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        sample_rate = wf.getframerate()
        if sampwidth != 2:
            raise ValueError(
                f"Unsupported WAV sample width ({sampwidth * 8}-bit). Please provide a 16-bit PCM WAV file."
            )

        frames_per_chunk = max(1, int(sample_rate * max(20, chunk_ms) / 1000))
        chunks: List[bytes] = []
        while True:
            raw_frames = wf.readframes(frames_per_chunk)
            if not raw_frames:
                break
            chunks.append(_downmix_pcm16_to_mono(raw_frames, channels))

    return sample_rate, chunks


async def iter_wav_stream(
    chunks: List[bytes],
    sample_rate: int,
    realtime: bool = False,
) -> AsyncIterator[bytes]:
    """Yield WAV PCM chunks asynchronously, optionally paced in real time."""
    for chunk in chunks:
        yield chunk
        if realtime and sample_rate > 0:
            chunk_seconds = (len(chunk) // 2) / float(sample_rate)
            await asyncio.sleep(chunk_seconds)


async def iter_mic_stream(
    sample_rate: int = 16000,
    chunk_ms: int = 128,
    duration: Optional[float] = None,
    stop_event: Optional[asyncio.Event] = None,
) -> AsyncIterator[bytes]:
    """Capture 16-bit mono PCM chunks from the default microphone using `sounddevice`."""
    try:
        import sounddevice as sd
    except ImportError as exc:
        raise RuntimeError(
            "Microphone streaming requires `sounddevice`. Install it with: pip install sounddevice"
        ) from exc

    loop = asyncio.get_running_loop()
    queue: asyncio.Queue[Optional[bytes]] = asyncio.Queue()
    blocksize = max(256, int(sample_rate * max(20, chunk_ms) / 1000))

    def audio_callback(indata, frames, time_info, status):  # noqa: ARG001
        if status:
            print(f"\n[Audio warning: {status}]", file=sys.stderr)
        pcm_bytes = bytes(indata)
        loop.call_soon_threadsafe(queue.put_nowait, pcm_bytes)

    stream = sd.RawInputStream(
        samplerate=sample_rate,
        blocksize=blocksize,
        channels=1,
        dtype="int16",
        callback=audio_callback,
    )

    start_time = loop.time()
    with stream:
        while True:
            if stop_event is not None and stop_event.is_set():
                break
            if duration is not None and (loop.time() - start_time) >= duration:
                break
            try:
                chunk = await asyncio.wait_for(queue.get(), timeout=0.1)
            except asyncio.TimeoutError:
                continue
            if chunk is None:
                break
            yield chunk


async def stream_audio(
    audio_chunks: AsyncIterator[bytes],
    api_token: str,
    server: str = "https://data-foundry.net",
    sample_rate: int = 16000,
    on_partial: Optional[Callable[[str], None]] = None,
    on_final: Optional[Callable[[str], None]] = None,
) -> str:
    """
    Stream 16-bit mono PCM chunks over WebSocket to `/v1/audio/transcriptions/stream`.

    Note: Data Foundry's Play WebSocket endpoint uses JSON text frames, so PCM audio
    is base64-encoded inside JSON (`{"audio": "...", "sample_rate": ...}`).
    """
    try:
        import websockets
    except ImportError as exc:
        raise RuntimeError(
            "Streaming STT requires `websockets`. Install it with: pip install websockets"
        ) from exc

    ws_url = build_ws_url(server)
    connect_kwargs = _connect_kwargs(websockets.connect, api_token)
    finals: List[str] = []
    last_partial: str = ""

    async with websockets.connect(ws_url, **connect_kwargs) as ws:
        await ws.send(json.dumps({"action": "start", "sample_rate": int(sample_rate)}))

        async def receiver() -> None:
            nonlocal last_partial
            try:
                async for raw_msg in ws:
                    if not isinstance(raw_msg, str):
                        continue
                    try:
                        event = json.loads(raw_msg)
                    except json.JSONDecodeError:
                        continue

                    ev_type = event.get("type")
                    text = (event.get("text") or "").strip()

                    if ev_type == "partial" and text:
                        last_partial = text
                        if on_partial:
                            on_partial(text)
                    elif ev_type == "final" and text:
                        last_partial = ""
                        finals.append(text)
                        if on_final:
                            on_final(text)
                    elif ev_type == "error" or "error" in event:
                        err_val = event.get("message") or event.get("error") or "Streaming STT error"
                        raise RuntimeError(str(err_val))
            except Exception as exc:
                # Normal WebSocket close ends the async iterator; propagate unexpected errors.
                if exc.__class__.__name__ != "ConnectionClosedOK":
                    raise

        async def sender() -> None:
            try:
                async for chunk in audio_chunks:
                    if not chunk:
                        continue
                    payload = {
                        "audio": base64.b64encode(chunk).decode("ascii"),
                        "sample_rate": int(sample_rate),
                    }
                    await ws.send(json.dumps(payload))
            finally:
                try:
                    await ws.send(json.dumps({"action": "stop"}))
                except Exception:
                    pass

        recv_task = asyncio.create_task(receiver())
        send_task = asyncio.create_task(sender())

        await send_task
        try:
            await asyncio.wait_for(recv_task, timeout=3.0)
        except asyncio.TimeoutError:
            recv_task.cancel()

    if finals:
        return " ".join(finals).strip()
    return last_partial


def _make_terminal_callbacks() -> Tuple[Callable[[str], None], Callable[[str], None], Callable[[], None]]:
    """Create terminal callbacks that update partial hypotheses in place and print final lines."""
    last_len = 0

    def clear_partial() -> None:
        nonlocal last_len
        if last_len > 0:
            sys.stdout.write("\r" + (" " * last_len) + "\r")
            sys.stdout.flush()
            last_len = 0

    def on_partial(text: str) -> None:
        nonlocal last_len
        line = f"[partial] {text}"
        pad = max(0, last_len - len(line))
        sys.stdout.write(f"\r{line}{' ' * pad}")
        sys.stdout.flush()
        last_len = len(line)

    def on_final(text: str) -> None:
        clear_partial()
        print(f"[final]   {text}", flush=True)

    return on_partial, on_final, clear_partial


async def _run_cli(args: argparse.Namespace) -> int:
    stop_event = asyncio.Event()
    loop = asyncio.get_running_loop()

    def request_stop() -> None:
        stop_event.set()

    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, request_stop)
        except (NotImplementedError, RuntimeError):
            pass

    on_partial, on_final, clear_partial = _make_terminal_callbacks()

    if args.mic:
        sample_rate = args.sample_rate
        print(f"Connecting to {build_ws_url(args.server)} (microphone @ {sample_rate} Hz)...")
        print("Speak into your microphone. Press Ctrl+C to stop and flush.\n")
        audio_iter = iter_mic_stream(
            sample_rate=sample_rate,
            chunk_ms=args.chunk_ms,
            duration=args.duration,
            stop_event=stop_event,
        )
    else:
        sample_rate, chunks = read_wav_chunks(args.audio_file, chunk_ms=args.chunk_ms)
        mode_label = "real-time paced" if args.realtime else "fast"
        print(
            f"Streaming '{args.audio_file}' ({len(chunks)} chunks @ {sample_rate} Hz, {mode_label}) "
            f"to {build_ws_url(args.server)}...\n"
        )
        audio_iter = iter_wav_stream(chunks, sample_rate=sample_rate, realtime=args.realtime)

    transcript = await stream_audio(
        audio_chunks=audio_iter,
        api_token=args.token,
        server=args.server,
        sample_rate=sample_rate,
        on_partial=on_partial,
        on_final=on_final,
    )
    clear_partial()

    print("\nFull Transcript:")
    print("----------------")
    print(transcript)
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Real-time streaming Speech-to-Text via Data Foundry WebSocket API"
    )
    parser.add_argument(
        "audio_file",
        nargs="?",
        default=None,
        help="Path to a 16-bit PCM WAV file to stream (omit when using --mic)",
    )
    parser.add_argument(
        "--mic",
        action="store_true",
        help="Capture and stream live audio from the default microphone (requires sounddevice)",
    )
    parser.add_argument(
        "--token",
        default=os.environ.get("DATAFOUNDRY_API_TOKEN"),
        help="Data Foundry API token (or set DATAFOUNDRY_API_TOKEN env var)",
    )
    parser.add_argument(
        "--server",
        default=os.environ.get("DATAFOUNDRY_URL", "https://data-foundry.net"),
        help="Data Foundry server URL (default: https://data-foundry.net)",
    )
    parser.add_argument(
        "--sample-rate",
        type=int,
        default=16000,
        help="Microphone capture sample rate in Hz (default: 16000)",
    )
    parser.add_argument(
        "--chunk-ms",
        type=int,
        default=128,
        help="Audio chunk duration in milliseconds (default: 128)",
    )
    parser.add_argument(
        "--realtime",
        action="store_true",
        help="Pace WAV file streaming in real time instead of sending chunks immediately",
    )
    parser.add_argument(
        "--duration",
        type=float,
        default=None,
        help="Optional recording duration in seconds when using --mic",
    )

    args = parser.parse_args()

    if not args.token:
        print(
            "Error: API token must be provided via --token or DATAFOUNDRY_API_TOKEN environment variable.",
            file=sys.stderr,
        )
        sys.exit(1)

    if not args.mic and not args.audio_file:
        parser.error("Provide a WAV file path or pass --mic for live microphone streaming.")

    if args.mic and args.audio_file:
        parser.error("Specify either an audio_file or --mic, not both.")

    try:
        sys.exit(asyncio.run(_run_cli(args)))
    except KeyboardInterrupt:
        print("\nStopped.", file=sys.stderr)
        sys.exit(0)
    except Exception as exc:
        print(f"\nError: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
