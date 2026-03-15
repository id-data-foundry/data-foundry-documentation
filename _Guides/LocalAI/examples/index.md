---
layout: default
title: Local AI Examples
parent: Local AI
nav_order: 0
has_children: true
has_toc: true
---

## Examples

The following examples demonstrate various capabilities of the Local AI features. Click on the titles to open the examples in a new tab.

### [Example 1: Prompt 101]({%link _Guides/LocalAI/examples/1.Prompt101.md %})
This example introduces the basics of interacting with a Large Language Model (LLM). You'll learn how to send a simple text prompt to the model and receive a response. It also demonstrates how to adjust the 'temperature' setting to control the creativity or randomness of the output.

### [Example 2: Data + Prompt]({%link _Guides/LocalAI/examples/2.DataPrompt.md %})
Here, we explore how to combine raw data with a specific instruction in your prompt. You will practice providing a dataset (like a list) and asking the AI to transform or interpret it. This is useful for tasks like formatting, summarization, or creative reinterpretation of existing information.

### [Example 3: Data + Prompt Chain]({%link _Guides/LocalAI/examples/3.PromptChain.md %})
Complex tasks are often better handled by breaking them down into smaller steps. This example demonstrates a "chaining" technique where the output of one prompt becomes the input for the next. You will guide data through three distinct transformation stages to achieve a final result.

### [Example 4: Photo + Prompt]({%link _Guides/LocalAI/examples/4.Image-to-Text.md %})
This example connects the physical world with AI by allowing you to capture a photo using your device's camera. You can then write a prompt to ask the AI to describe, analyze, or creatively interpret the image you just took. It showcases the model's multi-modal capabilities, processing visual input alongside text.

### [Example 5: Audio to Text]({%link _Guides/LocalAI/examples/5.Speech-to-Text.md %})
Learn how to convert spoken words into written text using the `soundToText` feature. This example lets you record audio directly in the browser and sends it to the server for transcription. It's a great starting point for building voice-controlled interfaces or transcription tools.

### [Example 6: Prompt to Image]({%link _Guides/LocalAI/examples/6.Text-to-Image.md %})
Visual creativity is at your fingertips with this example, which uses a text prompt to generate images. You will see how describing a scene, style, or object can produce a unique visual output. Experimenting with different descriptive words and negative prompts helps refine the artistic results.

### [Example 7: Text to Speech]({%link _Guides/LocalAI/examples/7.Text-to-Speech.md %})
Give your application a voice by converting written text into spoken audio. This example demonstrates how to select different voice profiles to read out your prompts. It illustrates how easily text generation can be turned into an auditory experience.

### [Example 8: Translation]({%link _Guides/LocalAI/examples/8.Translation.md %})
LLMs are powerful tools for language translation. This example focuses on translating text from one language to another while maintaining specific constraints, like brevity or tone. It highlights how prompt engineering can refine the quality and style of translations.

### [Example 9: Translate and Speak]({%link _Guides/LocalAI/examples/9.Translate-Talk.md %})
This example combines two powerful features: translation and text-to-speech. You will build a workflow that first translates your text into Italian and then speaks it aloud using an appropriate voice. It serves as a practical introduction to multi-step AI workflows.

### [Example 10: Explore Different Models]({%link _Guides/LocalAI/examples/10.Models.md %})
Not all AI models are the same; they vary in speed, capability, and personality. This example allows you to switch between different available models to compare their responses to the same prompt. It's an excellent way to understand which model best fits your specific needs.

### [Example 11: System Prompt]({%link _Guides/LocalAI/examples/11.SystemPrompt.md %})
Take control of the AI's persona and behavior using a "system prompt." This example shows how to set a hidden instruction that guides *how* the model acts, rather than just *what* it answers. You'll see how defining a role or style upfront changes the entire interaction.

### [Example 12: Benchmarking Tool]({%link _Guides/LocalAI/examples/12.benchmarking.md %})
This tool allows you to run a system and user prompt through multiple AI models for a set number of iterations. The results are displayed in a table for easy comparison of model outputs.
