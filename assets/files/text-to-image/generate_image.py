#!/usr/bin/env python3
"""
Data Foundry LocalAI Text-to-Image Client

Generate images from natural language descriptions using the
Data Foundry LocalAI image generation endpoint.

Requirements:
    pip install requests

Usage:
    python generate_image.py "Cool data foundry dinosaur in cyberpunk style" --token YOUR_API_TOKEN
    python generate_image.py "A serene Japanese zen garden" -o garden.png
    python generate_image.py "Futuristic robot" --width 768 --height 768 --steps 30 -o robot.png
"""

import os
import sys
import argparse
from typing import Optional
import requests


def generate_image(
    prompt: str,
    api_token: str,
    server: str = "https://data-foundry.net",
    model: str = "default",
    width: int = 512,
    height: int = 512,
    steps: int = 20,
    negative_prompt: Optional[str] = None,
    seed: Optional[int] = None,
    output_path: Optional[str] = None,
) -> dict:
    """Send a text prompt to Data Foundry's image generation endpoint.

    Args:
        prompt: Natural language description of the image to generate
        api_token: Data Foundry AI API token
        server: Base URL of the Data Foundry instance
        model: Diffusion model identifier (default: 'default')
        width: Image width in pixels (default: 512)
        height: Image height in pixels (default: 512)
        steps: Diffusion inference steps (default: 20)
        negative_prompt: Optional concepts to exclude from the image
        seed: Optional random seed for reproducible generations
        output_path: Optional file path to automatically download and save the image

    Returns:
        dict: Parsed response containing 'image_url' and 'prompt'
    """
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    url = f"{server.rstrip('/')}/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    payload = {
        "prompt": prompt,
        "model": model,
        "width": width,
        "height": height,
        "steps": steps,
    }
    if negative_prompt:
        payload["negative_prompt"] = negative_prompt
    if seed is not None:
        payload["seed"] = seed

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise RuntimeError(
            f"API request failed with status {response.status_code}: {response.text}"
        )

    result = response.json()
    image_url = result.get("image_url")

    # Optionally download the generated image directly
    if output_path and image_url:
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        img_response = requests.get(image_url, stream=True)
        if img_response.status_code == 200:
            with open(output_path, "wb") as f:
                for chunk in img_response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            result["saved_path"] = output_path
        else:
            print(
                f"Warning: Image generated at {image_url} but download failed with status {img_response.status_code}",
                file=sys.stderr,
            )

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Generate images from text prompts using Data Foundry LocalAI Text-to-Image API"
    )
    parser.add_argument(
        "prompt",
        help="Text prompt describing the desired image",
    )
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Optional local file path to download and save the generated image (e.g., 'image.png')",
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
        help="Diffusion model identifier (default: 'default')",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=512,
        help="Image width in pixels (default: 512)",
    )
    parser.add_argument(
        "--height",
        type=int,
        default=512,
        help="Image height in pixels (default: 512)",
    )
    parser.add_argument(
        "--steps",
        type=int,
        default=20,
        help="Diffusion inference steps (default: 20)",
    )
    parser.add_argument(
        "--negative-prompt",
        default=None,
        help="Negative prompt describing what to avoid in the image",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional random seed for generation",
    )

    args = parser.parse_args()

    if not args.token:
        print(
            "Error: API token must be provided via --token or DATAFOUNDRY_API_TOKEN environment variable.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Generating image for prompt '{args.prompt}' on {args.server}...")
    try:
        result = generate_image(
            prompt=args.prompt,
            api_token=args.token,
            server=args.server,
            model=args.model,
            width=args.width,
            height=args.height,
            steps=args.steps,
            negative_prompt=args.negative_prompt,
            seed=args.seed,
            output_path=args.output,
        )

        image_url = result.get("image_url", "")
        print(f"\nGenerated Image URL:\n{image_url}")

        if "saved_path" in result:
            file_size = os.path.getsize(result["saved_path"])
            print(f"Image saved locally to: {result['saved_path']} ({file_size:,} bytes)")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
