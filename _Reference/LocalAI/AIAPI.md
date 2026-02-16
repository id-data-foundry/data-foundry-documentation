---
layout: default
title: Local AI API
parent: Local AI Reference
nav_order: 0
has_toc: true
---

# Data Foundry AI APIs

## LocalAI API

The LocalAI API works the same as the OpenAI API. Just replace `https://<YOUR-DF-INSTANCE>/api/vendor/openai/<PROJECT_ID>` in the examples below with `https://<YOUR-DF-INSTANCE>/api/vendor/localai/<PROJECT_ID>`. You can start by leaving the model parameter empty (but still include it!) and for more specific cases you can choose different models. Not all models on that page are currently deployed in Data Foundry. Check with support if you have questions about available models.

## OpenAI API

The OpenAI API gives you access to advanced AI and Large Language Models (LLMs) that can perform a variety of tasks based on textual prompts.

In the following, we explain the basics of sending requests to the API, which is documented in more depth in the OpenAI for scripts page.

### Example OpenAI: Data Foundry Scripting

You can use the OpenAI API in scripts on Data Foundry. All API capabilities are available for direct HTTP API calls, as well as access from Python and JavaScript.

### Example OpenAI: Command Line

You can send API requests directly from any prototype that can access the web and send HTTP requests, e.g., an ESP32 or Raspberry Pi. Below is an example of a command-line call for Mac/Linux:

```bash
curl -X POST -H 'Content-Type: application/json' \
-d '{"api_token": "df-123456789....", "task": "completion",  "model": "ada",  "prompt": "Imagine you are a tomato, what is your biggest goal in life?"}' \
 https://<YOUR-DF-INSTANCE>/api/vendor/openai/<PROJECT_ID>
```

#### Requirements

* **Project ID**: This must match the generated API key. The Project ID needs to be appended to the URL; replace `<PROJECT_ID>` with the actual number.
* **JSON Request**: The completion, chat, or moderation request must be in JSON format, which is the same format used in scripting.

### Example OpenAI: Python

```python
import requests

api_key = 'df-abcdef1234567890abcdef1234567890abcdef123456789='
messages = []
headers = {'Content-Type': 'application/json'}

# Add user prompt to history
messages.append({'role':'user', 'content': 'This is a mouse, who are you?'})

# Check the OpenAI for scripting docs for more details
data = {
	'api_token': api_key,
	'task': 'chat',
	'messages': messages
}
response = requests.post('https://<YOUR-DF-INSTANCE>/api/vendor/openai/<PROJECT-ID>', headers=headers, json=data)

# Raw response output for debugging
print(response.text)

# Use response parsed as JSON
jsonResponse = response.json()
print(jsonResponse['content'])
```

### Example OpenAI: JavaScript

```js
var api_key = "df-abcdef1234567890abcdef1234567890abcdef123456789="
var messages = [{"role": "user", "content": "This is a mouse, who are you?"}]

// Send a POST request to the API
fetch("https://<YOUR-DF-INSTANCE>/api/vendor/openai/<PROJECT-ID>", {
	method: "POST",
	cache: "no-cache",
	headers: {
		"Content-Type": "application/json"
	},
	referrerPolicy: "no-referrer",
	body: JSON.stringify({
		"api_token": api_key, 
		"task": "chat",
		"messages": messages
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

## Chatbot API

The Chatbot API provides programmatic access to your custom chatbots, including their RAG (Retrieval-Augmented Generation) capabilities and knowledge bases. It uses an OpenAI-compatible format.

**Endpoint:** `POST /api/v1/chatbots/:id/chat`

### Authentication

Use your **Project API Key** as a Bearer token in the Authorization header.

```bash
Authorization: Bearer df-abcdef1234567890...
```

### Request Parameters

| Name | Type | Description |
| :--- | :--- | :--- |
| `message` | String | **Required**. The user's input message. |
| `conversationId` | String | **Optional**. A UUID to continue a conversation. If provided, the bot will use its chat history from the cache. |

### Example Request (cURL)

```bash
curl -X POST -H 'Content-Type: application/json' \
-H 'Authorization: Bearer YOUR_PROJECT_API_KEY' \
-d '{"message": "What is mentioned in the project documents about sustainability?", "conversationId": "7b8e-4a2c-9d1f"}' \
 https://<YOUR-DF-INSTANCE>/api/v1/chatbots/<CHATBOT_ID>/chat
```

### Example Response

```json
{
  "id": "chatcmpl-a1b2c3d4",
  "object": "chat.completion",
  "created": 1708012345,
  "model": "hermes-2-pro-llama-3-8b",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Based on the uploaded documents, the sustainability goals include..."
      },
      "finish_reason": "stop"
    }
  ],
  "conversationId": "7b8e-4a2c-9d1f"
}
```

## Text-to-Speech

Text-to-Speech (TTS) is the synthesis of speech from textual input. For example, TTS will turn the sentence "This is a dog, not a cat" into an audio file containing the spoken words. Currently, we use the tool `espeak` for this, which is very fast and convenient, though it does not always sound natural. `espeak` supports different languages, which you can access with the `lang` request parameter. English is the default; other languages can be configured using their two-character country code (e.g., `nl` for Dutch, `de` for German, `fr` for French). We are working on an improved TTS pipeline with better voice control.
 and synthesis options. Stay tuned.

Successful TTS API calls will return a JSON response that contains a token which can be used to download the generated audio file. The audio files are kept on the server for about 10 minutes, after which they are deleted.

### Example TTS: DF scripting

The use of the TTS API is very simple in DF scripts: Just call the DF.api function with the API type t2s as the first parameter and the api_key and text to speak as the second parameter.

```js
let result = DF.api("t2s", {
  "api_token": "df-abcdef1234567890abcdef1234567890abcdef123456789",
  "lang": "en", // or "nl" for Dutch, "de" for German, etc.
  "text": "this is a test, do your best!"
})
DF.print(result)
```

### Example TTS: Command line

``` bash
curl -X POST -H 'Content-Type: application/json' \
	-d '{"api_token": "df-123456789....", "text": "this is a test, do your best!"}' \
	https://<YOUR-DF-INSTANCE>/api/vendor/t2s/<PROJECT_ID>
```
If the call is successful, the response is a JSON object with a token that you can use to download the generated audio file:
```bash
curl -O https://<YOUR-DF-INSTANCE>/api/vendor/t2s/<TOKEN>
```

### Example TTS: Python

```python
import requests

api_key = 'df-abcdef1234567890abcdef1234567890abcdef123456789='
headers = {'Content-Type': 'application/json'}

# check the OpenAI for scripting docs for more details
data = {
	'api_token': api_key,
  'lang': 'en', # or 'nl' for Dutch, 'de' for German, etc.
	'text': 'this is a test, do your best!'
}
response = requests.post('https://<YOUR-DF-INSTANCE>/api/vendor/t2s/<PROJECT-ID>', headers=headers, json=data)

# raw response output for debugging
print(response.text)

# use response token to construct download link
print("https://<YOUR-DF-INSTANCE>/api/vendor/t2s/" + jsonResponse['content'])
```

### Example TTS: JavaScript

```js
// send a POST request to the API
fetch("https://<YOUR-DF-INSTANCE>/api/vendor/t2s/<PROJECT-ID>", {
  method: "POST",
  cache: "no-cache",
  headers: {
    "Content-Type": "application/json"
  },
  referrerPolicy: "no-referrer",
  body: JSON.stringify({
      api_token: "df-abcdef1234567890abcdef1234567890abcdef123456789", 
		  lang: "en", // or "nl" for Dutch, "de" for German, etc.
      text: "this is a test, do your best!"
  }),
})
.then((response) => response.json())
.then((json) => {
  // check content of response
  console.log(json)
  // json.text contains the token that you can use to create the download link
  downloadLink = "https://<YOUR-DF-INSTANCE>/api/vendor/t2s/" + json.text
});
```

When you use the TTS API on a website, you can use the download link in an <audio> element. Just set the src attribute of the element and you have an audio player for the generated speech.

## Speech-to-Text

Speech-to-Text (STT) is the translation of an audio recording of speech, e.g., as a .wav or .mp3 file, into the text that was spoken. While this is pretty straight-forward for humans (provided that they are speaking the right language and are not eating a delicious hamburger at the moment), but it's hard for machines. In the past years there was some progress in this area. And today, we can do this easily on a server or even locally on a mobile device. In the following, we will explain how you can make use of this API in your designs. Note: We currently do not support SST in scripting, because the processing of images in scripts is not well-developed enough.

We are currently using the Whisper technology that was open-sourced by OpenAI, and we are running this on the Data Foundry server, not somewhere else in the cloud. That means, you can safely use this service for STT, even for personal data (provided you have an appropriate and signed ERB form).

Whenever you submit a piece of audio to the server, the Whisper model needs to start, process and return the extracted text. That means, it can take a few seconds to return API calls. The longer the audio that you submit, the longer the wait will be. Also, transmit audio chunks that are longer than 3-5 seconds, otherwise the model does not have enough context to properly extract speech.
STT: JavaScript

We first built this API for JavaScript and web access. Even then, the handling of audio is not the easiest. Check out the full example below for some ideas:

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Audio API Test</title>
	<link rel="stylesheet" href="https://unpkg.com/@picocss/pico@1.*/css/pico.min.css">
    <script src="https://www.WebRTC-Experiment.com/RecordRTC.js"></script>
</head>
<body>
	<main class="container">
		<h2>Audio API Test</h2>
		<p>
			Welcome to the test page, click button to start recording and the transcription will appear automatically:
		</p>
		<p>
			<button id="recordButton">Record!</button>
		</p>
		<p>
			<code id="dataDisplay"></code>
		</p>		
	</main>
	<script type="text/javascript">
		document.addEventListener("DOMContentLoaded", (event) => {

			// register button handler
			document.querySelector('#recordButton').addEventListener('click', (event) => {
				startRecording()
			})

			let recordAudio;

			function startRecording() {
				// make use of HTML 5/WebRTC, JavaScript getUserMedia()
				// to capture the browser microphone stream
				navigator.mediaDevices.getUserMedia({
					audio: true
				}).then(function(stream) {
					recordAudio = RecordRTC(stream, {
						type: 'audio',
						mimeType: 'audio/webm',
						sampleRate: 44100,
						recorderType: StereoAudioRecorder,
						numberOfAudioChannels: 1,
						desiredSampRate: 16000,

						// get intervals based blobs
						// value in milliseconds
						// as you might not want to make detect calls every seconds
						timeSlice: 10000, // <--- this is the only value you can change

						ondataavailable: function(blob) {
							var reader = new window.FileReader();
							reader.readAsDataURL(blob);
							reader.onloadend = function() {
								base64data = reader.result;

								fetch("https://<YOUR-DF-INSTANCE>S/api/vendor/s2t/<PROJECT-ID>", {
										method: "POST",
										mode: "cors",
										cache: "no-cache",
										headers: {
											"Content-Type": "application/json",
										},
										redirect: "follow",
										referrerPolicy: "no-referrer",
										body: JSON.stringify({
											api_token: "df-abcdef1234567890abcdef1234567890abcdef123456789=",
											audio: base64data
										}),
									})
									.then((response) => response.json())
									.then((json) => {
										console.log(json)

										// write the recognized speech to HTML element
										dataDisplay.innerHTML += json.text.replace("-", "")
									});
							}
						},
					})

					recordAudio.startRecording();
				}).catch((err) => {
					// always check for errors at the end.
					console.error(`${err.name}: ${err.message}`);
				});
			}
		});
	</script>
</body>
</html>
```
