---
layout: default
title: Speech-to-Text API
parent: Local AI Reference
nav_order: 5
has_toc: true
---
# Speech-to-Text

Speech-to-Text (STT) is the translation of an audio recording of speech, e.g., as a .wav or .mp3 file, into the text that was spoken. While this is pretty straight-forward for humans (provided that they are speaking the right language and are not eating a delicious hamburger at the moment), but it's hard for machines. In the past years there was some progress in this area. And today, we can do this easily on a server or even locally on a mobile device. In the following, we will explain how you can make use of this API in your designs.

Whenever you submit a piece of audio to the server, a machine-learning model needs to process and return the extracted text. That means, it can take a few seconds to return API calls. The longer the audio that you submit, the longer the wait will be. Also, transmit audio chunks that are longer than 3-5 seconds, otherwise the model does not have enough context to properly extract speech.

[**Speech-to-Text Example**]({%link _Guides/LocalAI/examples/example5.html %}){: .btn}

## Examples
### Javascript Example:
We first built this API for JavaScript and web access. Even then, the handling of audio is not the easiest. Check out the full example below for some ideas:

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Audio API Test</title>
	<link rel="stylesheet" href="/assets/stylesheets/picoCSS/pico.jade.min.css">
	
	<!-- Add Local AI library scripts -->
	<script src="/assets/javascripts/local-ai/latest/local-ai.min.js"></script>
	<script src="/assets/javascripts/hark.bundle.js"></script>
</head>
<body>
	<main class="container">
		<h2>Audio API Test</h2>
		<p>
			Welcome to the test page, click button to start recording and the transcription will appear automatically:
		</p>
		<p>
			<button id="recordButton">Start Recording</button>
		</p>
		<p>
			<code id="dataDisplay"></code>
		</p>		
	</main>
	<script type="module">
		let recording = false;

		document.addEventListener("DOMContentLoaded", (event) => {
			document.querySelector('#recordButton').addEventListener('click', async (e) => {
				// Toggle recording state
				recording = !recording;

				// Update button text visually
				document.querySelector('#recordButton').innerText = recording ? "Stop Recording" : "Start Recording";

				// Use the foundry utility to handle the recording and transcription
				foundry.soundToText({
					server: "{{ site.external_base_urls.datafoundryurl }}", 
					api_token: "df-abcdef1234567890abcdef1234567890abcdef123456789=",
					type: "record",
					resultElementSelector: "#dataDisplay",
					loadingElementSelector: "#dataDisplay",
					logging: false,
					stopRec: !recording
				});
			});
		});
	</script>
</body>
</html>
```

### Python Example:

You can transcribe an audio file by sending a `POST` request to `/v1/audio/transcriptions` with `multipart/form-data`:

[Download Python Script]({% link assets/files/speech-to-text/transcribe.py %}){: .btn .btn-green download="transcribe.py"}

```python
import requests

api_key = 'df-abcdef1234567890abcdef1234567890abcdef123456789='
headers = {
    "Authorization": f"Bearer {api_key}"
}

audio_path = "recording.mp3"  # .mp3, .wav, .m4a, etc.

# Optional parameters supported by the STT service:
# model: e.g., 'parakeet_v3' (default), 'whisper-base', 'whisper-medium', 'whisper-large'
# lang: optional language hint (e.g., 'en', 'nl')
# timestamps: 'true' to include segment timecodes
data = {
    'model': 'parakeet_v3',
    'lang': 'en'
}

with open(audio_path, 'rb') as audio_file:
    files = {
        'file': audio_file
    }
    response = requests.post(
        '{{ site.external_base_urls.datafoundryurl }}/v1/audio/transcriptions',
        headers=headers,
        files=files,
        data=data
    )

if response.status_code == 200:
    result = response.json()
    print("Transcription:", result.get("text"))
else:
    print(f"Error {response.status_code}:", response.text)
```

### Command Line Example:

```bash
curl -X POST "{{ site.external_base_urls.datafoundryurl }}/v1/audio/transcriptions" \
  -H "Authorization: Bearer df-abcdef1234567890abcdef1234567890abcdef123456789=" \
  -F "file=@recording.mp3" \
  -F "model=parakeet_v3" \
  -F "lang=en"
```
