---
layout: default
title: Local AI
nav_order: 6
has_children: true
has_toc: true
---

# Local AI How-To Guides

This section contains task-oriented guides for working with the AI features of Data Foundry. These guides assume you have a basic understanding of the platform. For a more conceptual overview and details on available models, check out the [Local AI learning section]({% link _Learning/LocalAI/index.md %}).

{% if site.external_base_urls.datafoundry == null %}
{: .warning}
The Local AI functionality in the examples only works *live* with a Data Foundry instance that is configured with API keys and a gateway to a local AI runtime server. Otherwise, you can still browse the example and check their source code, but the AI requests will not work.
{% endif %}

## Guides

* **[Designing Custom Chatbots]({% link _Guides/LocalAI/Chatbots.md %})**: Learn how to create and configure your own AI chatbot with specific personalities and knowledge bases.

## Getting Started with the Examples

These examples are here for you to explore and play with! You can try them out directly to see what the different AI features can do. We encourage you to experiment by typing in your own prompts and tweaking settings like "temperature" to see how the AI's personality and responses change. If you find something you like, you are more than welcome to copy the code and use it as a starting point for your own wonderful projects. If you would like to use the examples in your prototyping, make a copy and upload them to a new Data Foundry project (see [tutorial](https://miro.com/app/board/uXjVIajSnpo=/?share_link_id=802305677504)).

## Examples

The following examples demonstrate various capabilities of the Local AI features. Click on the titles to open the examples in a new tab.

### [Example 1: Prompt 101](examples/index.html#example1.html){: target="_blank" }
This example introduces the basics of interacting with a Large Language Model (LLM). You'll learn how to send a simple text prompt to the model and receive a response. It also demonstrates how to adjust the 'temperature' setting to control the creativity or randomness of the output.

### [Example 2: Data + Prompt](examples/index.html#example2.html){: target="_blank" }
Here, we explore how to combine raw data with a specific instruction in your prompt. You will practice providing a dataset (like a list) and asking the AI to transform or interpret it. This is useful for tasks like formatting, summarization, or creative reinterpretation of existing information.

### [Example 3: Data + Prompt Chain](examples/index.html#example3.html){: target="_blank" }
Complex tasks are often better handled by breaking them down into smaller steps. This example demonstrates a "chaining" technique where the output of one prompt becomes the input for the next. You will guide data through three distinct transformation stages to achieve a final result.

### [Example 4: Photo + Prompt](examples/index.html#example4.html){: target="_blank" }
This example connects the physical world with AI by allowing you to capture a photo using your device's camera. You can then write a prompt to ask the AI to describe, analyze, or creatively interpret the image you just took. It showcases the model's multi-modal capabilities, processing visual input alongside text.

### [Example 5: Audio to Text](examples/index.html#example5.html){: target="_blank" }
Learn how to convert spoken words into written text using the `soundToText` feature. This example lets you record audio directly in the browser and sends it to the server for transcription. It's a great starting point for building voice-controlled interfaces or transcription tools.

### [Example 6: Prompt to Image](examples/index.html#example6.html){: target="_blank" }
Visual creativity is at your fingertips with this example, which uses a text prompt to generate images. You will see how describing a scene, style, or object can produce a unique visual output. Experimenting with different descriptive words and negative prompts helps refine the artistic results.

### [Example 7: Text to Speech](examples/index.html#example7.html){: target="_blank" }
Give your application a voice by converting written text into spoken audio. This example demonstrates how to select different voice profiles to read out your prompts. It illustrates how easily text generation can be turned into an auditory experience.

### [Example 8: Translation](examples/index.html#example8.html){: target="_blank" }
LLMs are powerful tools for language translation. This example focuses on translating text from one language to another while maintaining specific constraints, like brevity or tone. It highlights how prompt engineering can refine the quality and style of translations.

### [Example 9: Translate and Speak](examples/index.html#example9.html){: target="_blank" }
This example combines two powerful features: translation and text-to-speech. You will build a workflow that first translates your text into Italian and then speaks it aloud using an appropriate voice. It serves as a practical introduction to multi-step AI workflows.

### [Example 10: Explore Different Models](examples/index.html#example10.html){: target="_blank" }
Not all AI models are the same; they vary in speed, capability, and personality. This example allows you to switch between different available models to compare their responses to the same prompt. It's an excellent way to understand which model best fits your specific needs.

### [Example 11: System Prompt](examples/index.html#example11.html){: target="_blank" }
Take control of the AI's persona and behavior using a "system prompt." This example shows how to set a hidden instruction that guides *how* the model acts, rather than just *what* it answers. You'll see how defining a role or style upfront changes the entire interaction.

### [Example 12: Benchmarking Tool](examples/index.html#example12.html){: target="_blank" }
This tool allows you to run a system and user prompt through multiple AI models for a set number of iterations. The results are displayed in a table for easy comparison of model outputs.
