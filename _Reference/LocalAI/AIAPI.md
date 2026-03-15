---
layout: default
title: Chat Completion API
parent: Local AI Reference
nav_order: 2
has_toc: true
---

# Text-to-Text

Our LocalAI API can be reached with `https://{{ site.external_base_urls.datafoundry }}/v1/chat/completions`. You can start by leaving the model parameter empty (but still include it!) and for more specific cases you can choose different models. Not all models on that page are currently deployed in Data Foundry, to check what models are available on your Data Foundry instance, use the Data Foundry model overview.

{% include df-link.html text="Model Overview" path="/tools/models" %}

## Examples
### Python Example

```python
import requests

api_key = "df-abcdef1234567890abcdef1234567890abcdef123456789="
messages = []
headers={"Authorization": f"Bearer {api_key}"}

# AI model ID you want to use
model="phi-2-dpo-7k"
# Add user prompt to history
messages.append({'role':'user', 'content': 'This is a mouse, who are you?'})

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

### JavaScript Example

```js
var api_key = "df-abcdef1234567890abcdef1234567890abcdef123456789="
var messages = [{"role": "user", "content": "This is a mouse, who are you?"}]
var model = "phi-2-dpo-7k"
// Send a POST request to the API
fetch("https://{{ site.external_base_urls.datafoundry }}/v1/chat/completions", {
	method: "POST",
	cache: "no-cache",
	headers: {
	  "Authorization": `Bearer ${api_key}`
	},
	referrerPolicy: "no-referrer",
	body: JSON.stringify({
		"messages": messages,
		"model":model
	}),
})
.then((response) => response.json())
.then((json) => {
	// check content of response
	console.log(json)
	// json.content contains the generated chat response
	chatResponse = json.content
});
```

### Command Line Example

You can send API requests directly from any prototype that can access the web and send HTTP requests, e.g., an ESP32 or Raspberry Pi. Below is an example of a command-line call for Mac/Linux:

```bash
curl -X POST \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer df-abcdef1234567890abcdef1234567890abcdef123456789=' \
  -d '{
    "messages": [
      {"role": "user", "content": "This is a mouse, who are you?"}
    ],
    "model": "phi-2-dpo-7k"
  }' \
  https://{{ site.external_base_urls.datafoundry }}/v1/chat/completions

```
