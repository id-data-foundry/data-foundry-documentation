---
layout: default
title: PDF-to-Text API
parent: Local AI Reference
nav_order: 8
has_toc: true
---
# PDF-to-Text

PDF-to-Text is the automated extraction of readable textual content from PDF files. This endpoint enables ingestion of documents, research papers, design briefs, and reports into Data Foundry for analysis, searching, or feeding into downstream AI models.

## How it works

The client sends a `POST` request with `multipart/form-data` containing the PDF file under the field name `file`. Data Foundry parses the document structure and returns a JSON payload containing the cleaned extracted plain text.

## Examples

### Python Example:

You can extract text from a PDF file using Python:

[Download Python Script]({% link assets/files/pdf-to-text/extract_pdf.py %}){: .btn .btn-green download="extract_pdf.py"}

```python
import requests

api_key = "df-abcdef1234567890abcdef1234567890abcdef123456789="
headers = {
    "Authorization": f"Bearer {api_key}"
}

pdf_path = "document.pdf"

with open(pdf_path, "rb") as pdf_file:
    files = {
        "file": ("document.pdf", pdf_file, "application/pdf")
    }
    response = requests.post(
        "{{ site.external_base_urls.datafoundryurl }}/v1/pdf/text",
        headers=headers,
        files=files
    )

if response.status_code == 200:
    result = response.json()
    print("Extracted Text:\n", result.get("text", ""))
else:
    print(f"Error {response.status_code}:", response.text)
```

### Command Line Example:

```bash
curl -X POST "{{ site.external_base_urls.datafoundryurl }}/v1/pdf/text" \
  -H "Authorization: Bearer df-abcdef1234567890abcdef1234567890abcdef123456789=" \
  -F "file=@document.pdf;type=application/pdf"
```
