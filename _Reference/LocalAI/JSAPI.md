---
layout: default
title: JavaScript Library
parent: Local AI Reference
nav_order: 0
has_toc: true
---

# Local AI JS Library Reference

The `local-ai.js` library provides a convenient way to interact with Data Foundry's AI capabilities directly from your web applications.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Installation

To use the library, add a `script` tag in your HTML head:

```html
<script src="/assets/javascripts/local-ai/latest/local-ai.min.js"></script>
```

This reference explains first the main library functions which allow you to generate text, images or work with audio. Then we explain utility functions, the message history and finally, advanced functionality.

{: .warning}
This only works when you are hosting your website on Data Foundry, if you are hosting your file locally or somewhere else, you will have to download and import [this library]({%link assets/javascripts/local-ai/latest/local-ai.min.js%}) yourself.

### API key

To use the library functions you need to generate an API key in Data Foundry. API keys are linked to projects in Data Foundry, so you need to first create a project, then generate an API key on the "Edit Project" page.

API keys look like this: `df-abcdefghjkl1234567890abcdefghjkl1234567890=`

---

## Transformations

### foundry.textToText({...})

**Description:**

The `textToText` function is an asynchronous JavaScript function designed to interact with a large language model API. It sends a prompt or a series of messages to the model and retrieves a generated response. The function also supports optional logging, loading indicators, and displaying the result on a webpage.

**Parameters:**

- *`api_token` (string, required)*: The API key for authentication. The function will not execute without this.
- *`server` (string, optional)*: The server URL for the API. Defaults to the current document's origin.
- *`model` (string, optional)*: The model to use for the request. Defaults to "hermes-2-pro-llama-3-8b".
- *`prompt` (string, optional)*: The text prompt to send to the model. Used if `messages` is not provided.
- *`messages` (array, optional)*: An array of message objects (e.g., role and content) to send to the model. If not provided, the function creates a message using the `prompt`.
- *`temperature` (number, optional)*: Controls the randomness of the model's output. Defaults to 0.9.
- *`maxTokens` (number, optional)*: The maximum number of tokens to generate in the response. Defaults to 250.
- *`logging` (boolean, optional)*: Enables or disables logging to the console. Defaults to true.
- *`loadingElementSelector` (string, optional)*: A CSS selector for an element to indicate loading status.
- *`resultElementSelector` (string, optional)*: A CSS selector for an element where the result will be displayed.

**Returns:**
- A `Promise` that resolves to a `string` (the generated text).

**Error Handling:**

- If `api_token` is not provided, the function logs an error and exits.
- If neither `prompt` nor `messages` are provided, the function logs an error and creates an empty message.
- If the `loadingElementSelector` or `resultElementSelector` does not match any element, an error is logged.
- Any errors during the API request are caught and logged to the console.

**Example Usage:**

```javascript
foundry.textToText({
  api_token: "your_api_key_here",
  prompt: "What is the capital of France?",
  resultElementSelector: "#result-container"
});
```

### foundry.textToTextWithUsage({...})

**Description:**

Identical to `textToText`, but returns an object containing both the generated text and token usage statistics. This is useful for monitoring costs or estimating energy consumption.

**Parameters:**

- Same as `textToText`.

**Returns:**

- A `Promise` that resolves to an `object`:
  - `text` (string): The generated response.
  - `usage` (object):
    - `prompt_tokens` (number): Number of tokens in the prompt.
    - `completion_tokens` (number): Number of tokens in the generated response.
    - `total_tokens` (number): Total number of tokens used.

**Example Usage:**

```javascript
const result = await foundry.textToTextWithUsage({
  api_token: "your_api_key_here",
  prompt: "Explain nuclear fusion."
});
console.log(result.text);
console.log(result.usage.total_tokens);
```

**See also:** [Example 13: Token Usage & Energy Estimation]({% link _Guides/LocalAI/examples/13.TokenUsage.md %})

### foundry.chatbot({...})

**Description:**

The `chatbot` function is an asynchronous JavaScript function designed to interact with a Data Foundry custom chatbot. It supports RAG (Retrieval-Augmented Generation) based on uploaded documents and maintains conversation history using a `conversationId`. Like other library functions, it includes optional features for logging, loading indicators, and displaying the result on a webpage.

**Parameters:**

- *`api_token` (string, required)*: The Project API key for authentication.
- *`chatbotId` (number/string, required)*: The unique ID of the chatbot dataset.
- *`message` (string, required)*: The user's input message to send to the chatbot.
- *`conversationId` (string, optional)*: A UUID to continue an existing conversation. If provided, the chatbot will retrieve previous messages from the server's cache.
- *`server` (string, optional)*: The server URL for the API. Defaults to the current document's origin.
- *`logging` (boolean, optional)*: Enables or disables logging to the console. Defaults to `true`.
- *`loadingElementSelector` (string, optional)*: A CSS selector for an element to indicate loading status (sets `aria-busy="true"`).
- *`resultElementSelector` (string, optional)*: A CSS selector for an element where the result will be appended.

**Return Value:**

Returns a Promise that resolves to an object:
- `content` (string): The text response from the chatbot.
- `conversationId` (string): The ID of the conversation (useful for subsequent calls to maintain state).

**Example Usage:**

```javascript
// Start a new conversation
const response = await foundry.chatbot({
  api_token: "your_api_key_here",
  chatbotId: 123,
  message: "How do I setup my prototype?",
  loadingElementSelector: "#chat-loader",
  resultElementSelector: "#chat-history"
});

console.log("Response:", response.content);

// Continue the same conversation later
const nextResponse = await foundry.chatbot({
  api_token: "your_api_key_here",
  chatbotId: 123,
  message: "Tell me more about the first step.",
  conversationId: response.conversationId // Using the ID from the previous call
});
```

### foundry.textToImage({...})

**Description:**

The `textToImage` function is an asynchronous JavaScript function that generates an image based on a text prompt using an AI API. It sends a request to the server with the provided parameters and returns the generated image URL. This function also includes optional features like logging, loading indicators, and displaying the result in an HTML element.

**Parameters:**

- *`api_token` (required):* Your API key for authentication. The function will not run without this.
- *`server` (optional):* The server URL to send the request to. Defaults to the current origin.
- *`prompt` (required):* The text description of the image you want to generate.
- *`negativePrompt` (optional):* A description of what you do not want in the image. Defaults to an empty string.
- *`steps` (optional):* The number of steps for image generation. Higher values may improve quality but take longer. (Scale: 1-200, defaults to 20).
- *`cfgScale` (optional):* A number controlling how closely the image matches the prompt. (Scale: 0-20, defaults to 10). More [information](https://blogs.novita.ai/understanding-cfg-scale-in-stable-diffusion/).
- *`seed` (optional):* A number to control randomness. Defaults to -1 (random seed).
- *`width` and `height` (optional):* The dimensions of the generated image in pixels. Defaults to 512x512.
- *`logging` (optional):* A boolean to enable or disable console logs. Defaults to true.
- *`loadingElementSelector` (optional):* A CSS selector for an element to show a loading indicator.
- *`resultElementSelector` (optional):* A CSS selector for an `<img>` element to display the generated image.

**Error Handling:**

- If no `api_token` is provided, the function logs an error and stops execution.
- If the server response is not successful (e.g., HTTP error), an error message is logged to the console.
- If the response contains an error message, it is displayed as an alert.
- If the loading element is not found, an error is logged to the console.

**Example Usage:**

Here is an example of how to use the `textToImage` function:

```javascript
foundry.textToImage({
  api_token: "your_api_key_here",
  server: "{{ site.external_base_urls.datafoundryurl }}",
  prompt: "A futuristic cityscape at sunset",
  negativePrompt: "blurry, low quality",
  cfgScale: 12,
  steps: 20,
  width: 512,
  height: 512,
  logging: true,
  loadingElementSelector: "#loading-indicator",
  resultElementSelector: "#result-image"
});
```

In this example:
- The API key is provided as `"your_api_key_here"`.
- The prompt describes the desired image: "A futuristic cityscape at sunset".
- A negative prompt specifies what to avoid: "blurry, low quality".
- Other parameters like `cfgScale`, `seed`, and `steps` are customized.
- The loading indicator is shown on an element with the ID `#loading-indicator`.
- The generated image is displayed in an `<img>` element with the ID `#result-image`.

### foundry.textToSpeech({...})

**Description:**

The `textToSpeech` function is an asynchronous JavaScript function that converts text into speech using an external API. It sends a request to a server, processes the response, and plays the generated audio. This function is customizable with parameters like language, voice, and more, making it versatile for various use cases.

**Parameters:**

- *`api_token` (required)*: Your API key for authentication. The function will not run without this.
- *`server` (optional)*: The server URL where the API request is sent. Defaults to the current document's origin.
- *`prompt` (required)*: The text you want to convert into speech.
- *`voice` (optional)*: The voice style for the speech. Defaults to `"af_heart"`. You can choose from a [list of supported voices](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md).
- *`loadingElementSelector` (optional)*: A CSS selector for an element that shows a loading indicator. The function will set its `aria-busy` attribute to indicate processing.
- *`resultElementSelector` (optional)*: A CSS selector for an audio element where the generated speech will be played.
- *`logging` (optional)*: A boolean to enable or disable logging messages in the console. Defaults to `true`.

**Error Handling:**

- If no `api_token` is provided, the function logs an error and stops execution.
- If the `loadingElementSelector` does not match any element, an error is logged.
- If the API response is not successful (e.g., a network issue or server error), an error is logged.
- Any unexpected errors during execution are caught and logged in the console.

**Example Usage:**

Below is an example of how to use the `textToSpeech` function:

```javascript
foundry.textToSpeech({
  api_token: "your_api_key_here",
  server: "{{ site.external_base_urls.datafoundryurl }}",
  prompt: "Hello, world!",
  language: "en",
  voice: "af_heart",
  loadingElementSelector: "#loading-indicator",
  resultElementSelector: "#audio-player",
  logging: true,
});
```

In this example:
- The API key is provided as `"your_api_key_here"`.
- The text `"Hello, world!"` will be converted into speech.
- The loading indicator is linked to the element with the ID `"loading-indicator"`.
- The generated audio will play in the audio element with the ID `"audio-player"`.

### foundry.textToRobot({...})

**Description:**

The `textToRobot` function is an asynchronous JavaScript function designed to convert text into sound using an API. It takes several parameters, including an API token, project ID, and text prompt, and returns a link to the generated audio file. This function also includes optional features like logging, language selection, and loading/result indicators.

**Parameters:**

- *`api_token` (required)*: Your API key for authentication. The function will not run without this.
- *`server` (optional)*: The server URL where the API is hosted. Defaults to the current document's origin.
- *`projectId` (required)*: The unique identifier for your project. You can find this in your project's info section. The id and API key must be from the same project.
- *`prompt` (required)*: The text you want to convert into sound.
- *`language` (optional)*: The language code for the text-to-sound conversion. Defaults to "en" (English).
- *`loadingElementSelector` (optional)*: A CSS selector for an element that will display a loading indicator while the function runs.
- *`resultElementSelector` (optional)*: A CSS selector for an element (e.g., an audio tag) where the generated audio link will be set as the source.
- *`logging` (optional)*: A boolean value to enable or disable console logging. Defaults to true.

**Error Handling:**

- If `api_token` is missing, the function logs: `"No API key provided."`
- If `projectId` is missing, the function logs: `"No project ID provided. Please find your project ID at the info section of your project."`
- If the `loadingElementSelector` does not match any element, the function logs: `"Element selected for loading indicator not found."`
- If the API response does not include a valid result, the function logs: `"No result. It is possible your API Key and project ID are not matching."`
- Any other errors during the fetch request are logged to the console.

**Example Usage:**

Here is an example of how to use the `textToRobot` function:

```javascript
foundry.textToRobot({
  api_token: "your_api_key_here",
  server: "{{ site.external_base_urls.datafoundryurl }}",
  projectId: "your_project_id_here",
  prompt: "Hello, world!",
  language: "en",
  loadingElementSelector: "#loading-indicator",
  resultElementSelector: "#audio-player",
  logging: true,
});
```

In this example:
- The API key and project ID are required and must be replaced with your actual credentials.
- The text "Hello, world!" will be converted into sound.
- The language is set to English.
- An element with the ID `loading-indicator` will show a loading state while the function runs.
- The generated audio link will be set as the source of an element with the ID `audio-player`.

### foundry.imageToText({...})

**Description:**

This function uses a large language model to process an image and generate a text-based response. It sends the image and optional prompts to a server, retrieves the response, and optionally displays it on a webpage. It is designed to handle asynchronous operations and includes error handling for common issues.

**Parameters:**

- *`api_token` (required)*: Your API key for authentication. The function will not run without this.
- *`server` (optional)*: The server URL to send the request to. Defaults to the current page's origin.
- *`model` (optional)*: The name of the model to use. Defaults to `"llava-llama-3-8b-v1_1"`.
- *`prompt` (optional)*: A text prompt to guide the model's response.
- *`systemPrompt` (optional)*: A system-level prompt to set the context for the model.
- *`image` (optional)*: The image to process. Can be a file or URL.
- *`messages` (optional)*: Predefined messages to send to the model. If not provided, the function generates them based on the `prompt` and `image`.
- *`temperature` (optional)*: Controls the randomness of the model's output. Defaults to `0.8`.
- *`maxTokens` (optional)*: The maximum number of tokens (words or characters) in the response. Defaults to `250`.
- *`logging` (optional)*: If `true`, logs the process to the console. Defaults to `true`.
- *`loadingElementSelector` (optional)*: A CSS selector for an element to show a loading indicator.
- *`resultElementSelector` (optional)*: A CSS selector for an element to display the result.

**Error Handling:**

- If `api_token` is missing, the function logs an error and stops execution.
- If neither `image` nor `messages` are provided, the function logs an error and stops execution.
- If the `loadingElementSelector` does not match any element, an error is logged but the function continues.
- If the server response contains an error, it is displayed as an alert and the function stops execution.
- Any unexpected errors during execution are logged to the console.

**Example Usage:**

```javascript
foundry.imageToText({
  api_token: "your_api_key_here",
  server: "{{ site.external_base_urls.datafoundryurl }}",
  model: "llava-llama-3-8b-v1_1",
  prompt: "Describe the image",
  image: "https://example.com/image.jpg",
  temperature: 0.7,
  maxTokens: 200,
  logging: true,
  loadingElementSelector: "#loading-indicator",
  resultElementSelector: "#result-container"
});
```

In this example, the function sends an image URL and a prompt to the server. It uses the specified model and settings to generate a response. While the request is being processed, a loading indicator is shown, and the result is displayed in the element with the ID `result-container`.

### foundry.imageToTextWithUsage({...})

**Description:**

Identical to `imageToText`, but returns an object containing both the generated text and token usage statistics.

**Parameters:**

- Same as `imageToText`.

**Returns:**

- A `Promise` that resolves to an `object`:
  - `text` (string): The generated response.
  - `usage` (object): Same structure as `textToTextWithUsage`.

**Example Usage:**

```javascript
const result = await foundry.imageToTextWithUsage({
  api_token: "your_api_key_here",
  image: "https://example.com/image.jpg",
  prompt: "Describe this image."
});
console.log(result.text);
console.log(result.usage.total_tokens);
```

**See also:** [Example 13: Token Usage & Energy Estimation]({% link _Guides/LocalAI/examples/13.TokenUsage.md %})

### foundry.soundToText({...})

**Description:**

The `soundToText` function is an asynchronous JavaScript function designed to transcribe audio into text. It supports two modes: recording audio directly from the microphone or transcribing an uploaded audio file. The function uses an API for transcription and provides options for customization, such as logging, loading indicators, and displaying results on a webpage.

**Parameters:**

- *`api_token` (required)*: Your API key for accessing the transcription service.
- *`server` (optional)*: The server URL for the transcription API. Defaults to the current page's origin.
- *`type` (optional)*: Specifies the mode of operation. Use `"file"` for file uploads or `"record"` for live microphone recording. Defaults to `"file"`.
- *`sliceDuration` (optional)*: The duration (in milliseconds) for each audio slice when recording. Defaults to `5000`.
- *`file` (optional)*: The audio file to be transcribed. Required if `type` is `"file"`.
- *`resultElementSelector` (optional)*: A CSS selector for the HTML element where the transcription result will be displayed.
- *`loadingElementSelector` (optional)*: A CSS selector for the HTML element that will show a loading indicator while transcription is in progress.
- *`onTranscribe` (optional)*: A callback function that is triggered whenever a new transcription is available.
- *`logging` (optional)*: Set to `true` to enable console logging or `false` to disable it. Defaults to `true`.
- *`stopRec` (optional)*: Set to `true` to stop recording and return the complete transcription. Defaults to `false`.

**Error Handling:**

- If no `api_token` is provided, the function logs an error: `"No API key provided."`
- If the `loadingElementSelector` does not match any element, an error is logged: `"Element selected for loading indicator not found."`
- If the browser does not support microphone access or the user denies permission, an error is logged with the specific issue.
- If the transcription API request fails, the error message is logged to the console.

**Example Usage:**

```javascript
// Example: Transcribing an uploaded audio file
foundry.soundToText({
  api_token: "your_api_key_here",
  server: "{{ site.external_base_urls.datafoundryurl }}",
  type: "file",
  file: audioFile, // Replace with your audio file object
  resultElementSelector: "#transcriptionResult",
  loadingElementSelector: "#loadingIndicator",
  onTranscribe: (text) => {
    console.log("New transcription:", text);
  },
  logging: true,
});

// Example: Recording audio and transcribing in real-time
foundry.soundToText({
  api_token: "your_api_key_here",
  server: "{{ site.external_base_urls.datafoundryurl }}",
  type: "record",
  sliceDuration: 3000, // Transcribe every 3 seconds
  resultElementSelector: "#transcriptionResult",
  loadingElementSelector: "#loadingIndicator",
  onTranscribe: (text) => {
    console.log("New transcription:", text);
  },
  logging: true,
});

// Example: Stopping a recording and getting the full transcription
foundry.soundToText({
  api_token: "your_api_key_here",
  server: "{{ site.external_base_urls.datafoundryurl }}",
  stopRec: true,
}).then((completeTranscription) => {
  console.log("Complete transcription:", completeTranscription);
});
```

---

## Utility functions

### foundry.stopRec({...})

**Description:**

The `stopRec` function is an asynchronous function designed to stop a recording process and convert audio to text using a large language model. It interacts with the `foundry.soundToText` API. This function allows you to pass an API token and optional parameters for logging and UI elements.

**Parameters:**

- *`logging` (boolean, optional)*: Defaults to `true`. If set to `true`, logs will be generated during the process.
- *`loadingElementSelector` (string, optional)*: A CSS selector for an element that shows a loading indicator during the process.
- *`resultElementSelector` (string, optional)*: A CSS selector for an element where the transcription result will be displayed.

**Error Handling:**

Ensure that the `loadingElementSelector` and `resultElementSelector` point to valid elements in your HTML to avoid runtime errors.

**Example Usage:**

```javascript
// Example of using the stopRec function
foundry.stopRec({
  logging: true,
  resultElementSelector: "#transcriptionResult",
  loadingElementSelector: "#loadingIndicator"
});
```

### foundry.models({...})

**Description:**

The `models` function is an asynchronous JavaScript function that retrieves a list of available models from a server hosting a large language model. It sends a GET request to the `/v1/models` endpoint of the server and requires an API token for authentication. If successful, it returns the list of models in JSON format. This function is useful for interacting with APIs that provide machine learning or AI model services.

**Parameters:**

- **api_token** (required):  
  - A string representing the API token used for authentication.
  - If this parameter is not provided, the function will log an error message (`"No api token provided!"`) and return the same message.
- **server** (optional):  
  - A string representing the server's base URL.
  - Defaults to the current document's origin (`document.location.origin`) if not provided.

**Error Handling:**

- **Missing API Token:** If the `api_token` is not provided, the function logs an error message (`"No api token provided!"`) to the console and returns the same message.
- **Network or Server Errors:** If the server request fails (e.g., due to network issues, invalid API token, or server errors), the error is caught in the `catch` block and logged to the console.
- **Unexpected Response Format:** If the server response does not contain the expected `json.data` structure, the function may throw an error or return `undefined`.

**Example Usage:**

```javascript
const apiToken = "your_api_token_here";
const serverUrl = "{{ site.external_base_urls.datafoundryurl }}";

const models = await foundry.models(apiToken, serverUrl);

if (models) {
    console.log("Available Models:", models);
} else {
    console.log("Failed to retrieve models.");
}
```

**Explanation of Example:**

- Replace `"your_api_token_here"` with a valid API token.
- The function is called asynchronously using `await` to ensure the response is received before proceeding.
- If the function successfully retrieves the models, they are logged to the console. Otherwise, an error message is displayed.

### foundry.popup(...)

**Description:**

The `popup` function is an asynchronous JavaScript function that allows users to select a file from their device. It dynamically creates a hidden file input element if one does not already exist, configures it based on the specified file type (e.g., audio or image), and waits for the user to select a file. Once a file is selected, it returns the file object or processes it further if it is an image.

**Parameters:**

- **type** (optional): A string that specifies the type of file to be selected. Supported values are:
  - `"audio"` or `"sound"`: Restricts the file input to audio files.
  - `"image"`: Restricts the file input to image files.
  - Any other value or no value: Allows selection of any file type.
- **logging** (optional): A boolean value (default is `true`). If set to `true`, logs the selected file details to the console.

**Error Handling:**

- If the file input element cannot be found, the function rejects the promise with an error message: `"File input element not found"`.
- If an error occurs during image processing, the function rejects the promise with an error message: `"Error during image processing"`.
- Any other errors are logged to the console using `console.error`.

**Example Usage:**

```javascript
// Example: Allow the user to select an image file
foundry.popup("image").then((file) => {
  console.log("Selected file:", file);
}).catch((error) => {
  console.error("An error occurred:", error);
});
```

### foundry.processImage(...)

**Description:**

This `processImage` function processes an image from either a file or a URL. It resizes the image to a maximum of 800x800 pixels while maintaining its aspect ratio and reduces its quality to optimize size. The function returns the processed image as a Data URL.

**Parameters:**

- `source`: The image source, which can be a `File` object (e.g., from an input element) or a URL string.
- `logging` (optional): A boolean value. If set to `true`, logs the processed image details to the console. Default is `true`.

**Error Handling:**

- If the `source` is not a valid `File` or URL string, the function rejects with an error: `"Invalid image source"`.
- If there is an issue reading a file, it rejects with `"Error reading the image file"`.
- If there is an issue loading an image from a file or URL, it rejects with `"Error loading image from file"` or `"Error loading image from URL"`, respectively.

**Example Usage:**

```javascript
// Example with a File input
const fileInput = document.querySelector("#fileInput");
fileInput.addEventListener("change", async (event) => {
  const file = event.target.files[0];
  try {
    const processedImage = await foundry.processImage(file);
    console.log("Processed Image Data URL:", processedImage);

    // here you could call imageToText with the processedImage data

  } catch (error) {
    console.error("Error processing image:", error.message);
  }
});

// Example with a URL
const imageUrl = "https://example.com/image.jpg";
foundry.processImage(imageUrl)
  .then((processedImage) => {
    console.log("Processed Image Data URL:", processedImage);

    // here you could call imageToText with the processedImage data

  })
  .catch((error) => {
    console.error("Error processing image:", error.message);
  });
```
