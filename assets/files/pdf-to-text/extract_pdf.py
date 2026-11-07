#!/usr/bin/env python3
"""
Data Foundry LocalAI PDF-to-Text Client

Extract clean textual content from PDF documents using the
Data Foundry LocalAI document extraction endpoint.

Requirements:
    pip install requests

Usage:
    python extract_pdf.py paper.pdf --token YOUR_API_TOKEN
    python extract_pdf.py report.pdf -o report.txt
"""

import os
import sys
import argparse
from typing import Optional
import requests


def extract_pdf_text(
    pdf_path: str,
    api_token: str,
    server: str = "https://data-foundry.net",
    output_path: Optional[str] = None,
) -> str:
    """Send a PDF file to Data Foundry's PDF-to-text extraction endpoint.

    Args:
        pdf_path: Path to the local PDF file
        api_token: Data Foundry AI API token
        server: Base URL of the Data Foundry instance
        output_path: Optional path to save the extracted text to disk

    Returns:
        str: Extracted text content
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    url = f"{server.rstrip('/')}/v1/pdf/text"
    headers = {
        "Authorization": f"Bearer {api_token}",
    }

    with open(pdf_path, "rb") as f:
        files = {
            "file": (os.path.basename(pdf_path), f, "application/pdf")
        }
        response = requests.post(url, headers=headers, files=files)

    if response.status_code != 200:
        raise RuntimeError(
            f"API request failed with status {response.status_code}: {response.text}"
        )

    result = response.json()
    extracted_text = result.get("text", "")

    if output_path:
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as out_f:
            out_f.write(extracted_text)

    return extracted_text


def main():
    parser = argparse.ArgumentParser(
        description="Extract text from PDF files using Data Foundry LocalAI PDF-to-Text API"
    )
    parser.add_argument(
        "pdf_file",
        help="Path to the PDF file to extract text from (.pdf)",
    )
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Optional local path to save the extracted text (.txt)",
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

    print(f"Submitting '{args.pdf_file}' to {args.server} for text extraction...")
    try:
        text = extract_pdf_text(
            pdf_path=args.pdf_file,
            api_token=args.token,
            server=args.server,
            output_path=args.output,
        )

        if args.output:
            print(f"Extracted {len(text)} characters and saved to: {args.output}")
        else:
            print("\nExtracted Text:")
            print("---------------")
            print(text)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
