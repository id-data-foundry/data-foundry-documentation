---
layout: default
title: Speech-to-Text API
parent: Local AI Reference
nav_order: 5
has_toc: true
---
# Speech-to-Text

DataFoundry provides two complementary Speech-to-Text (STT) services designed for different interaction paradigms:

1. **Real-Time Streaming STT (`foundry.transcribeLive`)**:
   - **Protocol:** Persistent WebSocket connection (`/v1/audio/transcriptions/stream`).
   - **Latency:** Sub-100ms interim partial hypotheses as words are spoken.
   - **Use cases:** Live dictation, voice conversational agents, interactive prototypes, speech command interfaces.

2. **Longform Batch Transcription (`foundry.transcribeFile` or HTTP POST `/v1/audio/transcriptions`)**:
   - **Protocol:** HTTP POST multipart file upload.
   - **Features:** High-accuracy transcription of long audio recordings (.wav, .mp3, .m4a), speaker diarization (`diarization=true`), and monotonic segment timestamps.
   - **Use cases:** Recorded interviews, audio lectures, meeting transcripts, podcast analysis.

[**Speech-to-Text Live Example**]({%link _Guides/LocalAI/examples/example5.html %}){: .btn}

## Modes & JavaScript Usage

### 1. Real-Time Streaming Transcription (`transcribeLive`)

Stream audio from the user's microphone in real-time over WebSocket, receiving continuous partial hypotheses followed by committed sentences:

```javascript
// Start streaming microphone audio
await foundry.transcribeLive({
  api_token: "df-abcdef1234567890abcdef1234567890abcdef123456789=",
  server: "{{ site.external_base_urls.datafoundryurl }}",
  onPartial: (partialText) => {
    // Real-time interim hypothesis (updates as words are spoken)
    document.querySelector("#status").innerText = partialText;
  },
  onFinal: (finalSegment) => {
    // Committed sentence / phrase
    document.querySelector("#output").innerText += " " + finalSegment;
  },
  resultElementSelector: "#output"
});

// Stop streaming when done
await foundry.stopLive();
```

### 2. File Upload Batch Transcription (`transcribeFile`)

Upload an entire audio file for full transcription:

```javascript
const file = document.querySelector("#audioInput").files[0];

const fullText = await foundry.transcribeFile({
  api_token: "df-abcdef1234567890abcdef1234567890abcdef123456789=",
  server: "{{ site.external_base_urls.datafoundryurl }}",
  file: file,
  model: "parakeet_v3",
  lang: "en",
  timestamps: false,
  diarization: false,
  resultElementSelector: "#fileOutput"
});

console.log("Transcribed text:", fullText);
```

### 3. Unified Helper (`soundToText`)

The classic `soundToText` function acts as a backwards-compatible dispatcher:
- Setting `type: "record"` triggers real-time streaming microphone capture.
- Setting `type: "file"` transcribes an uploaded audio file.

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Audio API Test</title>
	<link rel="stylesheet" href="/assets/stylesheets/picoCSS/pico.jade.min.css">
	
	<!-- Add Local AI library scripts -->
	<script src="/assets/javascripts/local-ai/latest/local-ai.min.js"></script>
	<script src="/assets/javascripts/hark.bundle.js"></script>
</head>
<body>
	<main class="container">
		<h2>Audio API Test</h2>
		<p>
			Welcome to the test page, click button to start recording and the transcription will appear automatically:
		</p>
		<p>
			<button id="recordButton">Start Recording</button>
		</p>
		<p>
			<code id="dataDisplay"></code>
		</p>		
	</main>
	<script type="module">
		let recording = false;

		document.addEventListener("DOMContentLoaded", (event) => {
			document.querySelector('#recordButton').addEventListener('click', async (e) => {
				// Toggle recording state
				recording = !recording;

				// Update button text visually
				document.querySelector('#recordButton').innerText = recording ? "Stop Recording" : "Start Recording";

				// Use the foundry utility to handle the recording and transcription
				foundry.soundToText({
					server: "{{ site.external_base_urls.datafoundryurl }}", 
					api_token: "df-abcdef1234567890abcdef1234567890abcdef123456789=",
					type: "record",
					resultElementSelector: "#dataDisplay",
					loadingElementSelector: "#dataDisplay",
					logging: false,
					stopRec: !recording
				});
			});
		});
	</script>
</body>
</html>
```

### Python Example (Batch File Upload):

You can transcribe an audio file by sending a `POST` request to `/v1/audio/transcriptions` with `multipart/form-data`:

[Download Python Script]({% link assets/files/speech-to-text/transcribe.py %}){: .btn .btn-green download="transcribe.py"}

```python
import requests

api_key = 'df-abcdef1234567890abcdef1234567890abcdef123456789='
headers = {
    "Authorization": f"Bearer {api_key}"
}

audio_path = "recording.mp3"  # .mp3, .wav, .m4a, etc.

# Optional parameters supported by the STT service:
# model: e.g., 'parakeet_v3' (default), 'whisper-base', 'whisper-medium', 'whisper-large'
# lang: optional language hint (e.g., 'en', 'nl')
# timestamps: 'true' to include segment timecodes
data = {
    'model': 'parakeet_v3',
    'lang': 'en'
}

with open(audio_path, 'rb') as audio_file:
    files = {
        'file': audio_file
    }
    response = requests.post(
        '{{ site.external_base_urls.datafoundryurl }}/v1/audio/transcriptions',
        headers=headers,
        files=files,
        data=data
    )

if response.status_code == 200:
    result = response.json()
    print("Transcription:", result.get("text"))
else:
    print(f"Error {response.status_code}:", response.text)
```

### Python Example (Real-Time Streaming):

For low-latency streaming over WebSocket (`/v1/audio/transcriptions/stream`), send JSON text frames containing base64-encoded 16-bit mono PCM audio chunks (`{"audio": "<base64>", "sample_rate": 16000}`), and finish with `{"action": "stop"}` to flush the final words:

[Download Streaming Python Script]({% link assets/files/speech-to-text/transcribe_stream.py %}){: .btn .btn-green download="transcribe_stream.py"}

```bash
# Install dependencies (sounddevice is only needed for --mic live capture)
pip install websockets sounddevice

# Stream a 16-bit PCM WAV file in real time
python transcribe_stream.py recording.wav --token YOUR_API_TOKEN --realtime

# Stream live audio from your microphone (press Ctrl+C to stop and flush)
python transcribe_stream.py --mic --token YOUR_API_TOKEN
```

```python
import asyncio
import base64
import json
import wave
import websockets

api_key = "df-abcdef1234567890abcdef1234567890abcdef123456789="
server_url = "{{ site.external_base_urls.datafoundryurl }}"
ws_url = (
    server_url.replace("https://", "wss://")
    .replace("http://", "ws://")
    .rstrip("/")
    + "/v1/audio/transcriptions/stream"
)

async def stream_wav(wav_path: str):
    headers = {"Authorization": f"Bearer {api_key}"}
    with wave.open(wav_path, "rb") as wf:
        sample_rate = wf.getframerate()
        chunk_frames = int(sample_rate * 0.128)  # ~128ms chunks (16-bit mono PCM)

        async with websockets.connect(ws_url, additional_headers=headers) as ws:
            await ws.send(json.dumps({"action": "start", "sample_rate": sample_rate}))

            async def receive():
                async for msg in ws:
                    event = json.loads(msg)
                    if event.get("type") == "partial":
                        print(f"\r[partial] {event.get('text', '')}", end="", flush=True)
                    elif event.get("type") == "final":
                        print(f"\n[final]   {event.get('text', '')}", flush=True)

            recv_task = asyncio.create_task(receive())
            while True:
                pcm = wf.readframes(chunk_frames)
                if not pcm:
                    break
                await ws.send(json.dumps({
                    "audio": base64.b64encode(pcm).decode("ascii"),
                    "sample_rate": sample_rate,
                }))
                await asyncio.sleep(0.128)

            await ws.send(json.dumps({"action": "stop"}))
            await asyncio.wait_for(recv_task, timeout=3.0)

asyncio.run(stream_wav("recording.wav"))
```

### Command Line Example:

```bash
curl -X POST "{{ site.external_base_urls.datafoundryurl }}/v1/audio/transcriptions" \
  -H "Authorization: Bearer df-abcdef1234567890abcdef1234567890abcdef123456789=" \
  -F "file=@recording.mp3" \
  -F "model=parakeet_v3" \
  -F "lang=en"
```
