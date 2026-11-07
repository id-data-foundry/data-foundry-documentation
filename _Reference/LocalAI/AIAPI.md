---
layout: default
title: Chat Completion API
parent: Local AI Reference
nav_order: 2
has_toc: true
---

# Text-to-Text

Our LocalAI API can be reached at `{{ site.external_base_urls.datafoundryurl }}/v1/chat/completions`. You can start by leaving the model parameter as `default` (or empty) and for more specific tasks choose different models. To check what models are available on your Data Foundry instance, see the Model Overview:

{% include df-link.html text="Model Overview" path="/tools/models" %}

## Examples

### Python Example:

You can send chat completion requests or run interactive conversations using Python:

[Download Python Script]({% link assets/files/chat-completion/chat.py %}){: .btn .btn-green download="chat.py"}

```python
import requests

api_key = "df-abcdef1234567890abcdef1234567890abcdef123456789="
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": "default",
    "messages": [
        {"role": "system", "content": "You are a helpful design research assistant."},
        {"role": "user", "content": "What is physical computing in interactive design?"}
    ],
    "temperature": 0.7,
    "max_tokens": 1000
}

response = requests.post(
    "{{ site.external_base_urls.datafoundryurl }}/v1/chat/completions",
    headers=headers,
    json=payload
)

if response.status_code == 200:
    result = response.json()
    reply = result["choices"][0]["message"]["content"]
    print("Response:\n", reply)
else:
    print(f"Error {response.status_code}:", response.text)
```

### JavaScript Example:

```js
var api_key = "df-abcdef1234567890abcdef1234567890abcdef123456789=";
var messages = [{"role": "user", "content": "What is physical computing in interactive design?"}];
var model = "default";

fetch("{{ site.external_base_urls.datafoundryurl }}/v1/chat/completions", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${api_key}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    messages: messages,
    model: model
  })
})
  .then((response) => response.json())
  .then((json) => {
    console.log("Chat response:", json.choices[0].message.content);
  });
```

### Command Line Example:

You can send API requests directly from any prototype or device that can make HTTP requests:

```bash
curl -X POST "{{ site.external_base_urls.datafoundryurl }}/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer df-abcdef1234567890abcdef1234567890abcdef123456789=" \
  -d '{
    "messages": [
      {"role": "user", "content": "What is physical computing in interactive design?"}
    ],
    "model": "default"
  }'
```
