#!/usr/bin/env python3
"""
Data Foundry LocalAI Structured Output & Tool Calling Client

Demonstrates how to enforce structured JSON schema outputs and handle
function/tool calling using Data Foundry LocalAI chat completions.

Requirements:
    pip install requests

Usage:
    # 1. Enforce Structured JSON Schema output:
    python extract_structured_data.py --mode schema "Pick a random warm sunset color" --token YOUR_API_TOKEN

    # 2. Tool / Function Calling simulation:
    python extract_structured_data.py --mode tool "It's getting pretty dark in here."
"""

import os
import sys
import json
import argparse
import requests


def call_structured_output(
    prompt: str,
    api_token: str,
    server: str = "https://data-foundry.net",
    model: str = "default",
) -> dict:
    """Enforce a strict JSON Schema on the AI response."""
    url = f"{server.rstrip('/')}/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    # Define a JSON Schema blueprint
    color_schema = {
        "name": "color_picker",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Descriptive name of the color"
                },
                "hex": {
                    "type": "string",
                    "description": "Hexadecimal color code (e.g., #FF5733)"
                },
                "rgb": {
                    "type": "array",
                    "items": {"type": "integer"},
                    "description": "RGB values [r, g, b]"
                },
                "mood": {
                    "type": "string",
                    "description": "Associated emotion or vibe"
                }
            },
            "required": ["name", "hex", "rgb", "mood"],
            "additionalProperties": False
        }
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": color_schema
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        raise RuntimeError(
            f"API request failed with status {response.status_code}: {response.text}"
        )

    result = response.json()
    content = result["choices"][0]["message"]["content"]
    return json.loads(content)


def call_tool_calling(
    prompt: str,
    api_token: str,
    server: str = "https://data-foundry.net",
    model: str = "default",
) -> dict:
    """Demonstrate function/tool definition and invocation detection."""
    url = f"{server.rstrip('/')}/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    tools = [
        {
            "type": "function",
            "function": {
                "name": "setLightLevel",
                "description": "Adjust the room smart lighting brightness level.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "level": {
                            "type": "integer",
                            "description": "Brightness percentage from 0 (off) to 100 (maximum brightness)"
                        },
                        "room": {
                            "type": "string",
                            "description": "Target room or zone, e.g. 'living_room', 'design_studio'"
                        }
                    },
                    "required": ["level"]
                }
            }
        }
    ]

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are an intelligent room automation assistant."},
            {"role": "user", "content": prompt}
        ],
        "tools": tools,
        "tool_choice": "auto"
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        raise RuntimeError(
            f"API request failed with status {response.status_code}: {response.text}"
        )

    result = response.json()
    message = result["choices"][0]["message"]
    tool_calls = message.get("tool_calls", [])

    return {
        "content": message.get("content"),
        "tool_calls": tool_calls
    }


def main():
    parser = argparse.ArgumentParser(
        description="Data Foundry LocalAI Structured Output & Tool Calling Client"
    )
    parser.add_argument(
        "prompt",
        nargs="?",
        default="Pick a random warm sunset color palette item",
        help="Input prompt (default: 'Pick a random warm sunset color palette item')",
    )
    parser.add_argument(
        "--mode",
        choices=["schema", "tool"],
        default="schema",
        help="Execution mode: 'schema' for strict JSON output or 'tool' for tool calling (default: 'schema')",
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
        help="Model identifier (default: 'default')",
    )

    args = parser.parse_args()

    if not args.token:
        print(
            "Error: API token must be provided via --token or DATAFOUNDRY_API_TOKEN environment variable.",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        if args.mode == "schema":
            print(f"Requesting structured JSON output for prompt: '{args.prompt}'...")
            data = call_structured_output(
                prompt=args.prompt,
                api_token=args.token,
                server=args.server,
                model=args.model,
            )
            print("\nParsed JSON Object:")
            print(json.dumps(data, indent=2))
        else:
            print(f"Submitting tool calling prompt: '{args.prompt}'...")
            res = call_tool_calling(
                prompt=args.prompt,
                api_token=args.token,
                server=args.server,
                model=args.model,
            )
            tool_calls = res.get("tool_calls", [])
            if tool_calls:
                print("\n[AI Tool Call Triggered!]")
                for call in tool_calls:
                    fn = call.get("function", {})
                    fn_name = fn.get("name")
                    fn_args = json.loads(fn.get("arguments", "{}"))
                    print(f"Function: {fn_name}")
                    print(f"Arguments: {json.dumps(fn_args, indent=2)}")
                    print(f"=> Executing action: {fn_name}(**{fn_args})...")
            else:
                print("\nStandard text response (no tool triggered):")
                print(res.get("content"))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
