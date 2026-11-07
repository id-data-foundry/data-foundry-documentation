---
layout: default
title: Image-to-Text API
parent: Local AI Reference
nav_order: 7
has_toc: true
---
# Image-to-Text

Image‑to‑text (also called visual question answering or image captioning) turns a picture into a natural language description. This allows models to interpret and interact with real-world visual content, taking AI interactions past plain text. Data Foundry provides vision-capable models (such as LLaVA) via an OpenAI-compatible multimodal endpoint.

[**Image-to-Text Example**]({% link _Guides/LocalAI/examples/example4.html %}){: .btn}

## How it works

The client sends an HTTP `POST` request to `/v1/chat/completions` with a JSON payload containing the image encoded as a base64 data URL inside the `messages` content list, along with your text prompt. A multimodal vision model processes both the image and text and returns the response.

To see which vision models are deployed on your instance, check the model overview:

{% include df-link.html text="Model Overview" path="/tools/models" %}

## Examples

### Python Example:

You can send an image and a prompt using Python:

[Download Python Script]({% link assets/files/image-to-text/describe_image.py %}){: .btn .btn-green download="describe_image.py"}

```python
import base64
import mimetypes
import requests

api_key = "df-abcdef1234567890abcdef1234567890abcdef123456789="
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Encode a local image as a base64 data URL
image_path = "image.jpg"
mime_type, _ = mimetypes.guess_type(image_path)
mime_type = mime_type or "image/jpeg"

with open(image_path, "rb") as image_file:
    b64_image = base64.b64encode(image_file.read()).decode("utf-8")

data_url = f"data:{mime_type};base64,{b64_image}"

payload = {
    "model": "llava-llama-3-8b-v1_1",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": data_url
                    }
                },
                {
                    "type": "text",
                    "text": "What do you see in this image? Describe it in detail."
                }
            ]
        }
    ]
}

response = requests.post(
    "{{ site.external_base_urls.datafoundryurl }}/v1/chat/completions",
    headers=headers,
    json=payload
)

if response.status_code == 200:
    result = response.json()
    print("Description:\n", result["choices"][0]["message"]["content"])
else:
    print(f"Error {response.status_code}:", response.text)
```

### Command Line Example:

```bash
# Prepare image payload as base64
IMAGE_B64=$(base64 -w 0 image.jpg)

curl -X POST "{{ site.external_base_urls.datafoundryurl }}/v1/chat/completions" \
  -H "Authorization: Bearer df-abcdef1234567890abcdef1234567890abcdef123456789=" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llava-llama-3-8b-v1_1",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,'"$IMAGE_B64"'"}},
          {"type": "text", "text": "Describe what you see in this image."}
        ]
      }
    ]
  }'
```

### JavaScript Example:

You can find a working interactive example in the [Image-to-Text Guide]({% link _Guides/LocalAI/examples/4.Image-to-Text.md %}). For more information on JavaScript client methods, check the [Data Foundry JavaScript Library reference]({% link _Reference/LocalAI/JSAPI.md %}#foundryimagetotext).
