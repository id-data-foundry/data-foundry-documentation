---
layout: default
title: Local AI
nav_order: 3
has_children: true
has_toc: false
---

# Local AI

Data Foundry does not only provide tools to store, modify, and collect data; it also hosts its own AI models! Data Foundry is capable of hosting several [Open Weight]({% link _Learning/OpenSourceScience/index.md %}) AI models and providing access to the OpenAI API.

In addition to hosting models, Data Foundry provides the infrastructure to generate and share API keys and allows for token distribution on a project basis. Students can enable AI functionality for their projects and are given 5,000 tokens by default. Token cost is determined by the specific model used; local models are significantly more cost-effective than OpenAI models.

## What is Local AI?

Since summer 2024, we have local AI on Data Foundry. What does that mean? Local AI means running large language models (LLMs) that you might know as ChatGPT or Claude, not in the cloud but inside the servers that host Data Foundry.

The benefits are that we can safely work with all kinds of data, even personal information if you are careful, but also that we can run AI models that are smaller, faster or unsafe. Also, local AI uses less energy than what is commonly available in commercial services. The disadvantages are that local AI models are often less powerful and might take a bit longer to compute results. But that's something you can design with. To see Local AI in action, you can [create a custom chatbot]({% link _Guides/LocalAI/Chatbots.md %}) or explore the [API examples]({% link _Guides/LocalAI/index.md %}).

## How it works

Whenever you use large language models today, the most common use-case is that the models are not on your own computer or device, but on a powerful server (in the cloud). It's the same with our Local AI here; you are not running the models in your browser, but on the Data Foundry.

This means that your browser sends requests to the Data Foundry and it will receive responses back. So, when you want to generate text from a prompt using a LLM you send a request with the prompt and the Data Foundry server will then run the model (inference) and send the generated text back to your browser. The browser then displays the text.

Sending such requests is not very difficult to do, but it takes some code to do it right and also handle errors and missing responses. So, we have made a library that you can use to do this in a shorter and simpler way. You can find the library reference [here](../../_Reference/LocalAI/index.md).

## Local AI Models

Local AI models might be a bit less powerful than giant commercial ones like GPT-4 or Claude, but they are highly effective for many tasks. They are often faster, more energy-efficient, and provide better privacy since data stays on-campus.

Using locally hosted AI models offers several advantages:
- **Efficiency**: Smaller models respond faster and use fewer resources.
- **Versatility**: Local models often have fewer restricted "guardrails," allowing for more specialized or sensitive research.
- **Privacy**: Since models are hosted on-campus, we can ensure that data is handled with privacy in mind, according to local regulations.  

We categorize our models by size to help you choose the right one:

- **Tiny Models** (e.g., Llama 3.2 1b): Super fast and efficient. Ideal for simple tasks like text classification or basic chat.
- **Small Models** (e.g., Phi-2, Llama 3.2 3b): A good balance of speed and reasoning. Great for general-purpose chat.
- **Medium Models** (e.g., Qwen 8B): Capable of more complex reasoning and nuanced instructions.
- **Large and Specialized Models**: For demanding tasks like analyzing images or processing long documents.

Using these local models also offers advantages like fewer restrictions on research topics ("guardrails") compared to commercial services.

## Topics

- **[Model Categories]({% link _Learning/LocalAI/Models.md %})**: Understanding the different sizes and capabilities of hosted models.
- **[Convoscript]({% link _Learning/LocalAI/ConvoScript.md %})**: Understanding how the ConvoScript library works for scripting chatbots.

## Checking Available Models

The availability of specific AI models depends on the configuration of each Data Foundry instance and is managed by the administrator. Therefore, we do not provide a static list of models in this documentation. Instead, you can check which models are currently available on your instance in two ways:

### 1. Web Interface
For a human-readable list of models, you can visit the **AI Models** tool page on your Data Foundry instance.

{% include df-link.html text="Take the tour" path="/tools/models" %}

This page provides an overview of the active models, their capabilities, and their identifiers.

### 2. API Endpoint
For developers or when using the API programmatically, you can query the list of available models using the standard OpenAI-compatible endpoint.
*   **Endpoint:** `GET /v1/models`
*   **Response:** A JSON object listing the models and their details.

This endpoint allows your scripts or applications to dynamically discover which models can be used for generation or chat completion tasks.

## Next Steps

Now that you understand the concepts behind Local AI on Data Foundry, you are ready to start building.

*   **Build a Chatbot:** Follow our guide on [creating a custom chatbot]({% link _Guides/LocalAI/Chatbots.md %}) to put these concepts into practice.
*   **Explore Examples:** Check out the [Local AI Guides]({% link _Guides/LocalAI/index.md %}) for more practical examples and code snippets.
*   **API Reference:** detailed technical documentation can be found in the [Reference Section]({% link _Reference/LocalAI/index.md %}), including the [JS Library]({% link _Reference/LocalAI/JSAPI.md %}) and [API Endpoints]({% link _Reference/LocalAI/AIAPI.md %}).
