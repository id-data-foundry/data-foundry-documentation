#!/usr/bin/env python3
"""
Data Foundry LocalAI Text-to-Speech (TTS) Client

Synthesize speech from textual input into an MP3 audio file using the
Data Foundry LocalAI neural speech generation endpoint.

Requirements:
    pip install requests

Usage:
    python synthesize.py "Hello world, this is Data Foundry." --token YOUR_API_TOKEN
    python synthesize.py "Hello world" --voice af_heart --output hello.mp3
    python synthesize.py --file script.txt --voice am_adam -o speech.mp3
"""

import os
import sys
import argparse
from typing import Optional
import requests


def synthesize_speech(
    text: str,
    api_token: str,
    output_path: str = "output.mp3",
    server: str = "https://data-foundry.net",
    model: str = "kokoro",
    voice: str = "af_heart",
    lang: Optional[str] = "en",
) -> str:
    """Send text to Data Foundry's TTS endpoint and save the synthesized MP3 audio.

    Args:
        text: Text string to synthesize into speech
        api_token: Data Foundry AI API token
        output_path: Path where the resulting MP3 audio file should be saved
        server: Base URL of the Data Foundry instance
        model: TTS model identifier (default: 'kokoro')
        voice: Voice identifier (default: 'af_heart', options include 'af_heart',
               'af_bella', 'af_nicole', 'af_aoede', 'am_adam', 'am_michael',
               'bf_emma', 'bf_isabella', 'bm_george', 'bm_lewis')
        lang: Two-letter language hint code (e.g., 'en', 'nl', 'de', 'fr', 'es')

    Returns:
        str: Path to the saved MP3 file
    """
    if not text.strip():
        raise ValueError("Text input cannot be empty.")

    url = f"{server.rstrip('/')}/v1/audio/speech"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    payload = {
        "input": text,
        "model": model,
        "voice": voice,
    }
    if lang:
        payload["lang"] = lang

    response = requests.post(url, headers=headers, json=payload, stream=True)

    if response.status_code != 200:
        raise RuntimeError(
            f"API request failed with status {response.status_code}: {response.text}"
        )

    # Ensure output directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Synthesize speech from text using Data Foundry LocalAI Text-to-Speech API"
    )
    parser.add_argument(
        "text",
        nargs="?",
        default=None,
        help="Text to synthesize into speech (or use --file to read from a text file)",
    )
    parser.add_argument(
        "--file",
        "-f",
        default=None,
        help="Path to a text file containing the input text to synthesize",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="output.mp3",
        help="Path for saving the output MP3 file (default: 'output.mp3')",
    )
    parser.add_argument(
        "--token",
        default=os.environ.get("DATAFOUNDRY_API_TOKEN"),
        help="Data Foundry API token (can also be set via DATAFOUNDRY_API_TOKEN env var)",
    )
    parser.add_argument(
        "--server",
        default=os.environ.get("DATAFOUNDRY_URL", "https://data-foundry.net"),
        help="Data Foundry server URL (default: https://data-foundry.net)",
    )
    parser.add_argument(
        "--model",
        default="kokoro",
        help="TTS model (default: 'kokoro')",
    )
    parser.add_argument(
        "--voice",
        default="af_heart",
        help="Voice identifier (default: 'af_heart', e.g. 'af_bella', 'am_adam', 'bf_emma')",
    )
    parser.add_argument(
        "--lang",
        default="en",
        help="Language hint code (default: 'en', e.g. 'nl', 'de', 'fr', 'es')",
    )

    args = parser.parse_args()

    if not args.token:
        print(
            "Error: API token must be provided via --token or DATAFOUNDRY_API_TOKEN environment variable.",
            file=sys.stderr,
        )
        sys.exit(1)

    text_to_speak = ""
    if args.file:
        if not os.path.exists(args.file):
            print(f"Error: Input file not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        with open(args.file, "r", encoding="utf-8") as f:
            text_to_speak = f.read().strip()
    elif args.text:
        text_to_speak = args.text.strip()
    else:
        print(
            "Error: Please provide text as a positional argument or use --file <path>.",
            file=sys.stderr,
        )
        sys.exit(1)

    if not text_to_speak:
        print("Error: Input text is empty.", file=sys.stderr)
        sys.exit(1)

    print(
        f"Synthesizing {len(text_to_speak)} characters using voice '{args.voice}' to '{args.output}'..."
    )
    try:
        saved_file = synthesize_speech(
            text=text_to_speak,
            api_token=args.token,
            output_path=args.output,
            server=args.server,
            model=args.model,
            voice=args.voice,
            lang=args.lang,
        )
        file_size = os.path.getsize(saved_file)
        print(f"\nSuccess! Audio saved to: {saved_file} ({file_size:,} bytes)")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
