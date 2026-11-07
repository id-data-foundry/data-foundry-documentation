---
layout: default
title: Text-to-Image API
parent: Local AI Reference
nav_order: 6
has_toc: true
---
# Text‑to‑Image

Text‑to‑image is the process of generating a visual representation from a natural language description. This allows you to generate images from textual prompts using diffusion models running directly on the Data Foundry Local AI infrastructure.

[**Text-to-Image Example**]({% link _Guides/LocalAI/examples/example6.html %}){: .btn}

## How it works

The function sends an HTTP POST request to `/v1/images/generations` with a JSON payload containing the prompt, dimensions (`width`, `height`), inference `steps`, and optional parameters (such as `negative_prompt` and `seed`). The server runs a diffusion model and returns a JSON object containing the `image_url` for downloading the generated PNG image.

## Examples

### Python Example:

You can generate an image and optionally download the resulting file using Python:

[Download Python Script]({% link assets/files/text-to-image/generate_image.py %}){: .btn .btn-green download="generate_image.py"}

```python
import requests

api_key = "df-abcdef1234567890abcdef1234567890abcdef123456789="
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "prompt": "Cool data foundry dinosaur in cyberpunk style",
    "width": 512,
    "height": 512,
    "steps": 20
}

response = requests.post(
    "{{ site.external_base_urls.datafoundryurl }}/v1/images/generations",
    headers=headers,
    json=data
)

if response.status_code == 200:
    result = response.json()
    image_url = result.get("image_url")
    print(f"Generated Image URL: {image_url}")

    # Optionally download and save the image locally:
    img_data = requests.get(image_url).content
    with open("output.png", "wb") as f:
        f.write(img_data)
    print("Saved to output.png")
else:
    print(f"Error {response.status_code}:", response.text)
```

### Command Line Example:

```bash
curl -X POST "{{ site.external_base_urls.datafoundryurl }}/v1/images/generations" \
  -H "Authorization: Bearer df-abcdef1234567890abcdef1234567890abcdef123456789=" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Cool data foundry dinosaur in cyberpunk style",
    "width": 512,
    "height": 512,
    "steps": 20
  }'
```

### JavaScript Example:

You can find a working interactive example in the [Text-to-Image Guide]({% link _Guides/LocalAI/examples/6.Text-to-Image.md %}). For more information on JavaScript client methods, see the [Data Foundry JavaScript Library reference]({% link _Reference/LocalAI/JSAPI.md %}#foundrytexttoimage).
