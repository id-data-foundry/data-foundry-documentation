---
layout: default
title: Text-to-Speech API
parent: Local AI Reference
nav_order: 4
has_toc: true
---
# Text-to-Speech

Text-to-Speech (TTS) is the synthesis of speech from textual input. For example, TTS will turn the sentence "This is a dog, not a cat" into an audio file containing the spoken words. Currently, we use the tool `espeak` for this, which is very fast and convenient, though it does not always sound natural. `espeak` supports different languages, which you can access with the `lang` request parameter. English is the default; other languages can be configured using their two-character country code (e.g., `nl` for Dutch, `de` for German, `fr` for French). We are working on an improved TTS pipeline with better voice control.
 and synthesis options. Stay tuned.

Successful TTS API calls will return a JSON response that contains a token which can be used to download the generated audio file. The audio files are kept on the server for about 10 minutes, after which they are deleted.

[**Text-to-Speech Example**]({%link _Guides/LocalAI/examples/example7.html %}){: .btn}
## Examples
### DF scripting Example:

The use of the TTS API is very simple in DF scripts: Just call the DF.api function with the API type t2s as the first parameter and the api_key and text to speak as the second parameter.

```js
let result = DF.api("t2s", {
  "api_token": "df-abcdef1234567890abcdef1234567890abcdef123456789",
  "lang": "en", // or "nl" for Dutch, "de" for German, etc.
  "text": "this is a test, do your best!"
})
DF.print(result)
```

### JavaScript Example:
You can find and download the [text-to-speech example here.]({% link _Guides/LocalAI/examples/7.Text-to-Speech.md %}) for more information on how this example has been implemented check the [Data Foundry Javascript Library reference page.]({% link _Reference/LocalAI/JSAPI.md %}#foundrytexttospeech)

### Python Example:

```python
import requests

api_key = 'df-abcdef1234567890abcdef1234567890abcdef123456789='
headers={"Authorization": f"Bearer {api_key}"}

# check the localai scripting docs for more details
data = {
    'model': 'kokoro',
    'lang': 'en', # or 'nl' for Dutch, 'de' for German, etc.
    'voice': 'af_heart',
	'input': 'this is a test, do your best!'
}
response = requests.post('https://{{ site.external_base_urls.datafoundry }}/v1/audio/speech', headers=headers, json=data)

# Output response as MP3 file
with open("output.mp3", "wb") as f:
    f.write(response.content)
```

### Command Line Example:

``` bash
curl -X POST -H 'Content-Type: application/json' \
	-d '{"api_token": "df-123456789....", "text": "this is a test, do your best!"}' \
	https://{{ site.external_base_urls.datafoundry }}/v1/audio/speech
```
If the call is successful, the response is a JSON object with a token that you can use to download the generated audio file:
```bash
curl -O https://{{ site.external_base_urls.datafoundry }}/api/vendor/t2s/<TOKEN>
```
