#!/usr/bin/env python3
"""
Data Foundry Chatbot API Client

Communicate with custom RAG-enabled chatbots, supporting document knowledge base
retrieval, agentic reasoning, and persistent user memory.

Requirements:
    pip install requests

Usage:
    # Single message
    python chat.py 42 "What does the research guide say about prototyping?" --token YOUR_PROJECT_KEY

    # Isolate memory and notes per user
    python chat.py 42 "Remember that I am studying user engagement." --user student_alex_101

    # Interactive multi-turn conversation session
    python chat.py 42 --user student_alex_101
"""

import os
import sys
import uuid
import argparse
from typing import Optional
import requests


def send_chatbot_message(
    chatbot_id: int,
    message: str,
    api_token: str,
    server: str = "https://data-foundry.net",
    conversation_id: Optional[str] = None,
    user: Optional[str] = None,
) -> dict:
    """Send a message to a Data Foundry custom chatbot endpoint.

    Args:
        chatbot_id: Numeric identifier of the chatbot
        message: The user's input message
        api_token: Data Foundry Project API Key or Dataset API Token
        server: Base URL of the Data Foundry instance
        conversation_id: Optional UUID or thread identifier to maintain conversation history
        user: Optional end-user identifier for sandboxed profile memory & notes

    Returns:
        dict: Parsed JSON response containing the chatbot's completion message
    """
    if not message.strip():
        raise ValueError("Message cannot be empty.")

    url = f"{server.rstrip('/')}/api/v1/chatbots/{chatbot_id}/chat"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    payload = {
        "message": message,
    }
    if conversation_id:
        payload["conversationId"] = conversation_id
    if user:
        payload["user"] = user

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise RuntimeError(
            f"API request failed with status {response.status_code}: {response.text}"
        )

    return response.json()


def run_interactive_session(
    chatbot_id: int,
    api_token: str,
    server: str,
    conversation_id: Optional[str] = None,
    user: Optional[str] = None,
):
    """Run an interactive conversation loop in the terminal."""
    conv_id = conversation_id or str(uuid.uuid4())[:8]

    print(f"\n--- Data Foundry Chatbot #{chatbot_id} Interactive Session ---")
    print(f"Server: {server}")
    print(f"Conversation ID: {conv_id}")
    if user:
        print(f"User (Memory Isolation): {user}")
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

        try:
            result = send_chatbot_message(
                chatbot_id=chatbot_id,
                message=user_input,
                api_token=api_token,
                server=server,
                conversation_id=conv_id,
                user=user,
            )
            reply = result["choices"][0]["message"]["content"]
            print(f"\nBot > {reply}")
        except Exception as e:
            print(f"\nError: {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Interact with Data Foundry Custom Chatbot API"
    )
    parser.add_argument(
        "chatbot_id",
        type=int,
        help="Numeric ID of the custom chatbot",
    )
    parser.add_argument(
        "message",
        nargs="?",
        default=None,
        help="Message to send (if omitted, launches an interactive chat session)",
    )
    parser.add_argument(
        "--conversation-id",
        "-c",
        default=None,
        help="Optional conversation thread identifier (UUID or session string)",
    )
    parser.add_argument(
        "--user",
        "-u",
        default=None,
        help="Optional end-user ID to enable sandboxed profile memory & notes isolation",
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

    args = parser.parse_args()

    if not args.token:
        print(
            "Error: API token must be provided via --token or DATAFOUNDRY_API_TOKEN environment variable.",
            file=sys.stderr,
        )
        sys.exit(1)

    if args.message is None:
        run_interactive_session(
            chatbot_id=args.chatbot_id,
            api_token=args.token,
            server=args.server,
            conversation_id=args.conversation_id,
            user=args.user,
        )
        return

    try:
        result = send_chatbot_message(
            chatbot_id=args.chatbot_id,
            message=args.message,
            api_token=args.token,
            server=args.server,
            conversation_id=args.conversation_id,
            user=args.user,
        )
        reply = result["choices"][0]["message"]["content"]
        print(reply)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
