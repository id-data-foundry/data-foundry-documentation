#!/usr/bin/env python3
"""
Data Foundry LocalAI Speech-to-Text (STT) Client

Transcribe audio files (.wav, .mp3, .m4a, .webm, etc.) using the
Data Foundry LocalAI audio transcription API endpoint.

Requirements:
    pip install requests

Usage:
    python transcribe.py audio.mp3 --token YOUR_API_TOKEN
    python transcribe.py audio.mp3 --token YOUR_API_TOKEN --model parakeet_v3 --lang en --timestamps
"""

import os
import sys
import argparse
from typing import Optional
import requests


def transcribe_audio(
    audio_path: str,
    api_token: str,
    server: str = "https://data-foundry.net",
    model: str = "parakeet_v3",
    lang: Optional[str] = None,
    timestamps: bool = False,
    diarization: bool = False,
) -> dict:
    """Send an audio file to Data Foundry's STT endpoint.
    
    Args:
        audio_path: Path to the local audio file (.wav, .mp3, etc.)
        api_token: Data Foundry AI API token
        server: Base URL of the Data Foundry instance
        model: Model identifier (default: 'parakeet_v3', options: 'whisper-base', 'whisper-medium', 'whisper-large')
        lang: Optional two-letter language code hint (e.g., 'en', 'nl')
        timestamps: Whether to request segment timestamps in the output
        diarization: Whether to request speaker diarization (if supported)

    Returns:
        dict: Parsed JSON response containing the transcription ('text')
    """
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    url = f"{server.rstrip('/')}/v1/audio/transcriptions"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }

    data = {
        "model": model,
        "timestamps": "true" if timestamps else "false",
        "diarization": "true" if diarization else "false",
    }
    if lang:
        data["lang"] = lang

    with open(audio_path, "rb") as audio_file:
        files = {
            "file": (os.path.basename(audio_path), audio_file)
        }
        response = requests.post(url, headers=headers, files=files, data=data)

    if response.status_code != 200:
        raise RuntimeError(
            f"API request failed with status {response.status_code}: {response.text}"
        )

    return response.json()


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe audio using Data Foundry LocalAI Speech-to-Text API"
    )
    parser.add_argument(
        "audio_file",
        help="Path to the audio file to transcribe (.mp3, .wav, .m4a, etc.)",
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
        default="parakeet_v3",
        help="Transcription model (default: 'parakeet_v3', options: 'whisper-base', 'whisper-medium', 'whisper-large')",
    )
    parser.add_argument(
        "--lang",
        default=None,
        help="Optional language hint code (e.g., 'en', 'nl', 'de')",
    )
    parser.add_argument(
        "--timestamps",
        action="store_true",
        help="Include timecodes in the transcription segments",
    )
    parser.add_argument(
        "--diarization",
        action="store_true",
        help="Enable speaker diarization placeholder (if supported by model)",
    )

    args = parser.parse_args()

    if not args.token:
        print(
            "Error: API token must be provided via --token or DATAFOUNDRY_API_TOKEN environment variable.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Submitting '{args.audio_file}' to {args.server} using model '{args.model}'...")
    try:
        result = transcribe_audio(
            audio_path=args.audio_file,
            api_token=args.token,
            server=args.server,
            model=args.model,
            lang=args.lang,
            timestamps=args.timestamps,
            diarization=args.diarization,
        )
        print("\nTranscription Result:")
        print("---------------------")
        print(result.get("text", ""))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
