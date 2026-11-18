#!/usr/bin/env python3
"""
Data Foundry LocalAI Image-to-Image Client

Transform an existing image using a natural language prompt via the
Data Foundry LocalAI image-to-image endpoint (/v1/images/image-to-image).

Requirements:
    pip install requests

Usage:
    python image_to_image.py coffee-cup.jpg "Place a cute young cat sitting inside the coffee cup" --token YOUR_API_TOKEN
    python image_to_image.py sketch.png "Photorealistic minimalist desk lamp" --strength 0.75 -o render.png
"""

import argparse
import mimetypes
import os
import sys
from typing import Optional

import requests


def transform_image(
    image_path: str,
    prompt: str,
    api_token: str,
    server: str = "https://data-foundry.net",
    model: str = "default",
    strength: float = 0.7,
    width: int = 512,
    height: int = 512,
    steps: int = 20,
    negative_prompt: Optional[str] = None,
    seed: Optional[int] = None,
    output_path: Optional[str] = None,
) -> dict:
    """Send an input image and prompt to Data Foundry's image-to-image endpoint."""
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Input image not found: {image_path}")

    url = f"{server.rstrip('/')}/v1/images/image-to-image"
    headers = {
        "Authorization": f"Bearer {api_token}",
    }

    mime_type, _ = mimetypes.guess_type(image_path)
    mime_type = mime_type or "image/png"

    data = {
        "model": model,
        "prompt": prompt,
        "strength": str(max(0.0, min(1.0, strength))),
        "width": str(max(64, min(2048, width))),
        "height": str(max(64, min(2048, height))),
        "steps": str(max(1, min(50, steps))),
    }
    if negative_prompt:
        data["negativeprompt"] = negative_prompt
    if seed is not None:
        data["seed"] = str(seed)

    with open(image_path, "rb") as img_file:
        files = {
            "image": (os.path.basename(image_path), img_file, mime_type),
        }
        response = requests.post(url, headers=headers, files=files, data=data)

    if response.status_code != 200:
        raise RuntimeError(
            f"API request failed with status {response.status_code}: {response.text}"
        )

    result = response.json()
    image_url = result.get("image_url")

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
        description="Transform an image with a prompt using Data Foundry LocalAI Image-to-Image API"
    )
    parser.add_argument("image", help="Path to the source image (PNG, JPEG, or WEBP)")
    parser.add_argument("prompt", help="Text prompt describing the transformation")
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Optional local file path to save the transformed image (e.g., 'output.png')",
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
        "--strength",
        type=float,
        default=0.7,
        help="Transformation strength between 0.0 and 1.0 (default: 0.7)",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=512,
        help="Output width in pixels (default: 512)",
    )
    parser.add_argument(
        "--height",
        type=int,
        default=512,
        help="Output height in pixels (default: 512)",
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
        help="Optional negative prompt describing what to avoid",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional random seed for reproducible results",
    )

    args = parser.parse_args()

    if not args.token:
        print(
            "Error: API token must be provided via --token or DATAFOUNDRY_API_TOKEN environment variable.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Transforming '{args.image}' with prompt '{args.prompt}' on {args.server}...")
    try:
        result = transform_image(
            image_path=args.image,
            prompt=args.prompt,
            api_token=args.token,
            server=args.server,
            model=args.model,
            strength=args.strength,
            width=args.width,
            height=args.height,
            steps=args.steps,
            negative_prompt=args.negative_prompt,
            seed=args.seed,
            output_path=args.output,
        )

        image_url = result.get("image_url", "")
        print(f"\nTransformed Image URL:\n{image_url}")

        if "saved_path" in result:
            file_size = os.path.getsize(result["saved_path"])
            print(f"Image saved locally to: {result['saved_path']} ({file_size:,} bytes)")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
