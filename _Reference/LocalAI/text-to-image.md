---
layout: default
title: Text-to-Image API
parent: Local AI Reference
nav_order: 6
has_toc: true
---
# Text‑to‑Image

Text‑to‑image is the process of generating a visual representation from a natural language description. This allows you to generate simple images from just a textual description. It's quite a simple process, but requires good prompting to get the image perfectly right. We now show you a simple implementation to do this in javascript, but this can be done from any device, including devices running Micropython. The Data Foundry local‑AI library exposes this capability through the **`foundry.textToImage({...})`** function.

[**Text-to-Image Example**]({%link _Guides/LocalAI/examples/example6.html %}){: .btn}

## How it works

The function sends an HTTP POST request to your project’s AI endpoint with a JSON payload that contains the prompt, optional negative prompt and generation parameters (steps, cfgScale, seed, size). The server runs a diffusion model such as Stable Diffusion or a custom model and returns a URL pointing at the generated image.

## Examples
### JavaScript Example:
You can find a working example of a website using [Image-to-Text here]({%link _Guides/LocalAI/examples/6.Text-to-Image.md%}) for more information on the request itself check the [Data Foundry Javascript Library reference page.]({% link _Reference/LocalAI/JSAPI.md %}#foundrytexttoimage)

### Python Example:

```python
import requests

api_key = 'df-abcdef1234567890abcdef1234567890abcdef123456789='
headers={
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# check the OpenAI for scripting docs for more details
data = {
	'prompt': 'Cool data foundry dinosaur',
	'width': 500,
	'height':500,
	'steps':5,
}
response = requests.post('https://{{ site.external_base_urls.datafoundry }}/v1/images/generations', headers=headers, json=data)

# Returns a link to your picture
print(response.text) 
```
