---
layout: default
title: Text-to-Speech API
parent: Local AI Reference
nav_order: 4
has_toc: true
---
# Text-to-Speech

Text-to-Speech (TTS) is the synthesis of spoken audio from textual input. Data Foundry provides an OpenAI-compatible speech synthesis endpoint supporting both natural neural speech powered by **Kokoro** and zero-latency robotic voices powered by **FreeTTS** diphone and DSP synthesis:

- **`model: "kokoro"`**: High-quality natural human neural speech (voices: `af_heart`, `am_adam`, `bf_emma`, etc.).
- **`model: "robot"`**: Built-in, zero-latency in-process robotic speech synthesis (input limited to 1,024 characters for performance and security):
  - `voice: "retro"` or `"computer"` (default): Crisp 16kHz diphone synthetic computer voice powered by FreeTTS.
  - `voice: "dalek"`: FreeTTS processed through a 45 Hz ring modulator (classic *Doctor Who* Dalek).
  - `voice: "cyborg"`: FreeTTS processed through a metallic comb filter / flanger chassis.
  - `voice: "vintage"` or `"sam"`: Authentic 8-bit retro formant voice (1982 SAM / Commodore 64 style).

The modern speech generation endpoint is OpenAI-compatible and streams the resulting audio (`audio/mpeg`) directly back in the HTTP response. Different voices and languages can be configured via request parameters.

[**Text-to-Speech Example**]({% link _Guides/LocalAI/examples/example7.html %}){: .btn}

## Examples

### Python Example:

You can synthesize speech by sending a `POST` request to `/v1/audio/speech`:

[Download Python Script]({% link assets/files/text-to-speech/synthesize.py %}){: .btn .btn-green download="synthesize.py"}

```python
import requests

api_key = "df-abcdef1234567890abcdef1234567890abcdef123456789="
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "kokoro",
    "voice": "af_heart",  # e.g., 'af_heart', 'am_adam', 'bf_emma'
    "lang": "en",        # e.g., 'en', 'nl', 'de', 'fr', 'es'
    "input": "This is Data Foundry Local AI neural text-to-speech!"
}

response = requests.post(
    "{{ site.external_base_urls.datafoundryurl }}/v1/audio/speech",
    headers=headers,
    json=data,
    stream=True
)

if response.status_code == 200:
    with open("output.mp3", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print("Audio successfully saved to output.mp3")
else:
    print(f"Error {response.status_code}:", response.text)
```

### Command Line Example:

```bash
curl -X POST "{{ site.external_base_urls.datafoundryurl }}/v1/audio/speech" \
  -H "Authorization: Bearer df-abcdef1234567890abcdef1234567890abcdef123456789=" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kokoro",
    "voice": "af_heart",
    "lang": "en",
    "input": "This is Data Foundry Local AI neural text-to-speech!"
  }' \
  --output output.mp3
```

### JavaScript Example:

You can find a working interactive example in the [Text-to-Speech Guide]({% link _Guides/LocalAI/examples/7.Text-to-Speech.md %}). For more information on client methods, see the [Data Foundry JavaScript Library reference]({% link _Reference/LocalAI/JSAPI.md %}#foundrytexttospeech).
