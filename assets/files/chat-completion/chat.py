#!/usr/bin/env python3
"""
Data Foundry LocalAI Chat Completion Client

Send chat completions, query language models, and run interactive terminal
conversations using Data Foundry LocalAI text-to-text endpoints.

Requirements:
    pip install requests

Usage:
    # Single-shot query
    python chat.py "What is physical computing in design?" --token YOUR_API_TOKEN

    # Streaming token output in real-time
    python chat.py "Explain MQTT protocol step by step" --stream

    # Interactive multi-turn chat session
    python chat.py --system "You are an assistant for TU/e Industrial Design students."
"""

import os
import sys
import json
import argparse
from typing import List, Dict, Optional, Generator
import requests


def chat_completion(
    messages: List[Dict[str, str]],
    api_token: str,
    server: str = "https://data-foundry.net",
    model: str = "default",
    temperature: float = 0.7,
    max_tokens: int = 1000,
    stream: bool = False,
) -> Generator[str, None, None] | str:
    """Send a chat completion request to Data Foundry's text-to-text endpoint.

    Args:
        messages: List of message dicts: [{'role': 'user'|'system'|'assistant', 'content': '...'}]
        api_token: Data Foundry AI API token
        server: Base URL of the Data Foundry instance
        model: Model identifier (default: 'default')
        temperature: Sampling temperature (0.0 to 1.0)
        max_tokens: Maximum tokens in the output
        stream: If True, yields string tokens as they arrive via SSE

    Returns:
        str if stream=False, or a generator of string tokens if stream=True
    """
    url = f"{server.rstrip('/')}/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": stream,
    }

    response = requests.post(url, headers=headers, json=payload, stream=stream)

    if response.status_code != 200:
        raise RuntimeError(
            f"API request failed with status {response.status_code}: {response.text}"
        )

    if stream:
        def stream_generator():
            for line in response.iter_lines():
                if not line:
                    continue
                decoded_line = line.decode("utf-8").strip()
                if decoded_line.startswith("data: "):
                    data_str = decoded_line[6:].strip()
                    if data_str == "[DONE]":
                        break
                    try:
                        chunk = json.loads(data_str)
                        choices = chunk.get("choices", [])
                        if choices:
                            delta = choices[0].get("delta", {})
                            content = delta.get("content", "")
                            if content:
                                yield content
                    except json.JSONDecodeError:
                        continue
        return stream_generator()

    data = response.json()
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError) as err:
        raise RuntimeError(f"Unexpected response structure: {data}") from err


def run_interactive_chat(
    api_token: str,
    server: str,
    model: str,
    system_prompt: Optional[str] = None,
    temperature: float = 0.7,
    max_tokens: int = 1000,
    stream: bool = True,
):
    """Run an interactive conversation loop in the terminal."""
    messages: List[Dict[str, str]] = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})

    print(f"\n--- Data Foundry Interactive Chat ---")
    print(f"Server: {server} | Model: {model}")
    if system_prompt:
        print(f"System: {system_prompt}")
    print("Type 'exit', 'quit', or Ctrl+C to terminate.\n")

    while True:
        try:
            user_input = input("\nYou > ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit", "q"):
            print("Session ended.")
            break

        messages.append({"role": "user", "content": user_input})
        print("\nAI > ", end="", flush=True)

        try:
            if stream:
                full_reply = ""
                gen = chat_completion(
                    messages=messages,
                    api_token=api_token,
                    server=server,
                    model=model,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    stream=True,
                )
                for chunk in gen:
                    print(chunk, end="", flush=True)
                    full_reply += chunk
                print()
                messages.append({"role": "assistant", "content": full_reply})
            else:
                reply = chat_completion(
                    messages=messages,
                    api_token=api_token,
                    server=server,
                    model=model,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    stream=False,
                )
                print(reply)
                messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            print(f"\nError: {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Interact with Data Foundry LocalAI Chat Completion / Text-to-Text API"
    )
    parser.add_argument(
        "prompt",
        nargs="?",
        default=None,
        help="Prompt to send (if omitted, launches an interactive chat session)",
    )
    parser.add_argument(
        "--system",
        "-s",
        default=None,
        help="Optional system prompt to set model persona or instructions",
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
        default="default",
        help="Model identifier (default: 'default', e.g. 'phi-2-dpo-7k', 'llama-3-8b')",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.7,
        help="Sampling temperature (default: 0.7)",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=1000,
        help="Maximum generation tokens (default: 1000)",
    )
    parser.add_argument(
        "--stream",
        action="store_true",
        help="Stream response tokens in real-time",
    )

    args = parser.parse_args()

    if not args.token:
        print(
            "Error: API token must be provided via --token or DATAFOUNDRY_API_TOKEN environment variable.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Interactive session if no prompt is provided
    if args.prompt is None:
        run_interactive_chat(
            api_token=args.token,
            server=args.server,
            model=args.model,
            system_prompt=args.system,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            stream=args.stream,
        )
        return

    # Single-shot prompt
    messages = []
    if args.system:
        messages.append({"role": "system", "content": args.system})
    messages.append({"role": "user", "content": args.prompt})

    try:
        if args.stream:
            gen = chat_completion(
                messages=messages,
                api_token=args.token,
                server=args.server,
                model=args.model,
                temperature=args.temperature,
                max_tokens=args.max_tokens,
                stream=True,
            )
            for token in gen:
                print(token, end="", flush=True)
            print()
        else:
            reply = chat_completion(
                messages=messages,
                api_token=args.token,
                server=args.server,
                model=args.model,
                temperature=args.temperature,
                max_tokens=args.max_tokens,
                stream=False,
            )
            print(reply)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
