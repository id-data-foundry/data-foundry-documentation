---
layout: default
title: Image-to-Text API
parent: Local AI Reference
nav_order: 7
has_toc: true
---
# Image-to-Text
Image‑to‑text (also called image captioning or visual question answering) turns a picture into a natural language description. This allows you to easily describe images and create visual transcriptions and is as easy as sending a picture along with a prompt to the AI api. Image-to-Text allows your AI model to interpret and interact with the real world, taking AI interactions past just chatting. The Data Foundry local‑AI library for javascript exposes this capability through the **`foundry.imageToText({...})`** function.

[**Image-to-Text Example**]({%link _Guides/LocalAI/examples/example4.html %}){: .btn}

## How it works
The function sends an HTTP POST request to your project’s AI endpoint with a JSON payload that contains the image (as a URL or file) and optional prompts.  A multi-modal model such as LLaVA runs on the server, processes the image and returns a textual response which can be displayed in the browser. To see if a model has multi-modal capabilities, check the model cards of the models available at your data foundry instance. You can find an overview of all relevant models at the link below.

{% include df-link.html text="Model Overview" path="/tools/models" %}

## Examples
### Javascript example:

You can find a working example of a website using [Image-to-Text here]({%link _Guides/LocalAI/examples/4.Image-to-Text.md%}) for more information on the request itself check the [Data Foundry Javascript Library reference page.]({% link _Reference/LocalAI/JSAPI.md%}#foundryimagetotext)

### Python Example:
```python
import requests
import base64

api_key = 'df-abcdef1234567890abcdef1234567890abcdef123456789='
messages = []
headers = {"Authorization": f"Bearer {api_key}"}
model = "llava-llama-3-8b-v1_1"  # Vision-capable model on the TU/e LocalAI server

# Load and encode a local image as base64
image_path = "image.jpg"  # Replace with your image path
with open(image_path, "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode("utf-8")

# Add user prompt with image to history
# The image is passed as a base64-encoded data URL inside the content list
messages.append({
    'role': 'user',
    'content': [
        {
            'type': 'image_url',
            'image_url': {
                'url': f"data:image/jpeg;base64,{image_data}"
            }
        },
        {
            'type': 'text',
            'text': 'What do you see in this image? Describe it in detail.'
        }
    ]
})

# Check the localai for scripting docs for more details
data = {
    'messages': messages,
    'model': model
}

response = requests.post('https://{{ site.external_base_urls.datafoundry }}/v1/chat/completions', headers=headers, json=data)

# Raw response output for debugging
print(response.text)

# Use response parsed as JSON
jsonResponse = response.json()

# Chatbot response (on the next line in blue)
print("\033[1;32mChatbot Response: \n\033[35m" + jsonResponse["choices"][0]["message"]["content"])
```
