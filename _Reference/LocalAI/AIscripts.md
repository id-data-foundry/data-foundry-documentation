# Using the AI APIs in scripts

Currently, we offer AI functionality in Data Foundry using a [LocalAI](https://localai.io) server.

---

**NOTE: The use of this API is controlled by Data Foundry and at the moment free. We will monitor the usage of the API and also log all prompts that are submitted for quality assurance and debugging purposes. If you suspect that your API key has somehow leaked, generate a new one (which invalidates the old one) and contact us for help. By using the API you acknowledge these terms.**

---

## Completion example

A *completion* needs a prompt and the API will return a completion of this prompt. [Read more about text completion](https://platform.openai.com/docs/guides/completion) in the OpenAI API docs. You will also find useful tips and tricks how to craft a good prompt.

Let's try a first example with LocalAI. We want to generate a tagline for a flower shop.

````Javascript
let result = DF.api("localai", {
  "api_token": "<API-KEY>"", 
  "task": "chat",
  "messages": "Write a tagline for a flower shop."
});
DF.print(result)
````

````json
{"role":"assistant","content":"\n\nFlowers for a global audience.","finishReason":"stop","cost":18}
````

#### Models

The Data Foundry API offers access to different models on both the LocalAI server.

For **LocalAI**, you can see what models your Data Foundry are running on the `/tools/models` page.
[Check what models are installed]{% include df-link.html text="Check what models are installed" path="/tools/models" %}
When this documentation was written, the `hermes-2-pro-llama-3-8b` was the model we use for chat and completions.

#### Moderation example

THe moderation API endpoint can be used to identify content that violates common policies and to filter it.

The first example should result in a "flagged" moderation result:

````Javascript
let result = DF.api("openai-gpt", {
  "api_token": "<API-KEY>", 
  "task": "moderation",
  "prompt": "testy banana"
})
DF.print(result)
````

The second example should result in a "non-flagged" moderation result:

````Javascript
let result = DF.api("openai-gpt", {
  "api_token": "<API-KEY>", 
  "task": "moderation",
  "prompt": "testy kiwi"
})
DF.print(result)
````



#### Chat example

THe chat completion API endpoint can be used to generate a new reply to an existing chat, i.e., a list of prior messages. The main difference to the "normal" completion is that the `messages` are provided in a list and each message has a `role` (who is speaking) and `content` (what are they saying).

The following example shows a simple continuation of a chat:

````Javascript
let result = DF.api("localai", {
  "api_token": "<API-KEY>", 
  "task": "chat",
  "messages": [
    { "role": "system", "content": "You are a helpful assistant." },
    { "role": "user", "content": "Who won the world series in 2020?" },
    { "role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020." },
    { "role": "user", "content": "Where was it played?" }
  ]
})
DF.print(result)
````


### API concepts

### Using AI using your own API key

Instead of using the Data Foundry API key, you can also use your own AI server API key, or access a commercial AI service directly, by configuring the right server and API key. You can use this key in all requests as shown above in the `api_token` field.

### API reference

There are more options available than explained above. We generally follow the OpenAI parameter names.

<!-- todo -->
All DF API requests follow the structure, with `openai` as the only currently available API: 

````Javascript
let result = DF.api("openai-gpt", {
  "api_token": "<API-KEY>", 
  "task": "completion or moderation or ...",
  "prompt": "...",
  ... more parameters...
})
````

#### Completion requests

You can use the following parameters: `prompt`, `temperature`, `presence_penalty`, `frequency_penalty`

Details in the [official reference](https://platform.openai.com/docs/api-reference/completions)


#### Moderation requests

You can use the following parameter: input --> `prompt`

Details in the [official reference](https://platform.openai.com/docs/api-reference/moderations)
