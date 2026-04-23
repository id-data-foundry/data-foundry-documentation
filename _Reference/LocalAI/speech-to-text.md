---
layout: default
title: Speech-to-Text API
parent: Local AI Reference
nav_order: 5
has_toc: true
---
# Speech-to-Text

Speech-to-Text (STT) is the translation of an audio recording of speech, e.g., as a .wav or .mp3 file, into the text that was spoken. While this is pretty straight-forward for humans (provided that they are speaking the right language and are not eating a delicious hamburger at the moment), but it's hard for machines. In the past years there was some progress in this area. And today, we can do this easily on a server or even locally on a mobile device. In the following, we will explain how you can make use of this API in your designs. Note: We currently do not support SST in scripting, because the processing of images in scripts is not well-developed enough.

We are currently using the Whisper technology that was open-sourced by OpenAI, and we are running this on the Data Foundry server, not somewhere else in the cloud. That means, you can safely use this service for STT, even for personal data (provided you have an appropriate and signed ERB form).

Whenever you submit a piece of audio to the server, the Whisper model needs to start, process and return the extracted text. That means, it can take a few seconds to return API calls. The longer the audio that you submit, the longer the wait will be. Also, transmit audio chunks that are longer than 3-5 seconds, otherwise the model does not have enough context to properly extract speech.

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

								fetch("{{ site.external_base_urls.datafoundryurl }}/v1/audio/transcriptions", {
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
