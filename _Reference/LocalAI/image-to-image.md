---
layout: default
title: Image-to-Image API
parent: Local AI Reference
nav_order: 9
has_toc: true
---
# Image‑to‑Image

Image‑to‑image transforms an existing input picture using a natural language prompt. You can use it to restyle a photograph or add elements to a scene using diffusion models running directly on the Data Foundry Local AI infrastructure.

[**Image-to-Image Example**]({% link _Guides/LocalAI/examples/17.Image-to-Image.md %}){: .btn}

## How it works

The client sends an HTTP `POST` request to `/v1/images/image-to-image` (or `/v1/images/edits`) with either:
- `multipart/form-data` containing an `image` file (`PNG`, `JPEG`, or `WEBP`), a `prompt`, `strength` (`0.0`–`1.0`), and optional parameters (`model`, `steps`, `width`, `height`, `cfg`, `seed`, `negativeprompt`), or
- `application/json` with `image` encoded as a Base64 Data URL (or a previously returned `/v1/images/<token>` URL).

The server returns a JSON object containing the `image_url` for downloading the generated PNG image.

## Examples

### Python Example:

You can transform a local image file and optionally download the result using Python:

[Download Python Script]({% link assets/files/image-to-image/image_to_image.py %}){: .btn .btn-green download="image_to_image.py"}

```python
import requests

api_key = "df-abcdef1234567890abcdef1234567890abcdef123456789="
headers = {
    "Authorization": f"Bearer {api_key}",
}

with open("coffee-cup.jpg", "rb") as img:
    response = requests.post(
        "{{ site.external_base_urls.datafoundryurl }}/v1/images/image-to-image",
        headers=headers,
        files={"image": ("coffee-cup.jpg", img, "image/jpeg")},
        data={
            "model": "default",
            "prompt": "Place a cute young cat sitting inside the coffee cup on the table",
            "strength": "0.7",
            "width": "512",
            "height": "512",
            "steps": "20",
        },
    )

if response.status_code == 200:
    result = response.json()
    image_url = result.get("image_url")
    print(f"Transformed Image URL: {image_url}")

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
curl -X POST "{{ site.external_base_urls.datafoundryurl }}/v1/images/image-to-image" \
  -H "Authorization: Bearer df-abcdef1234567890abcdef1234567890abcdef123456789=" \
  -F "image=@coffee-cup.jpg" \
  -F "model=default" \
  -F "prompt=Place a cute young cat sitting inside the coffee cup on the table" \
  -F "strength=0.7" \
  -F "width=512" \
  -F "height=512" \
  -F "steps=20"
```

### JavaScript Example:

You can find an interactive browser example in the [Image-to-Image Guide]({% link _Guides/LocalAI/examples/17.Image-to-Image.md %}). For details on all JavaScript client options, see the [Data Foundry JavaScript Library reference]({% link _Reference/LocalAI/JSAPI.md %}#foundryimagetoimage).
