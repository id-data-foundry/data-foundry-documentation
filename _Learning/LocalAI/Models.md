---
layout: default
title: Model Categories
parent: Data Foundry AI
nav_order: 1
---

# Model Categories

Data Foundry classifies its hosted AI models into several categories based on their size and intended use cases. Choosing the right category helps balance performance, response time, and token cost. Check the link below to find out what models are available on your instance.

{% include df-link.html text="Model Overview" path="/tools/models" %}

## Tiny Models
Tiny models (e.g., Llama 3.2 1b) are extremely fast and efficient. They are ideal for simple tasks like text classification, summarization of short texts, or basic conversational interfaces on low-power devices.

## Small Models
Small models (e.g., Gemma 4 E4B, Hermes 2 Llama 3) offer a good balance between reasoning capabilities and speed. They are suitable for more complex instructions and general-purpose chat applications.

## Medium Models
Medium models (e.g., Qwen3.5 9b, Apertus 8b, Mistral Small 3.2) provide significant reasoning power, multilingual support, and tool calling for handling nuanced prompts and complex data structures.

## Large and Specialized Models
These models (e.g., Qwen3.6 35b, Qwen3.8 27b, Gemma4 26b, OpenAI GPT OSS) are designed for the most demanding tasks, including multimodal vision analysis, agentic coding, and long-context reasoning.

## Generic Placeholders
Instead of hardcoding a specific model ID in your code, you can use a generic placeholder configured on the Data Foundry server (`default`, `chat`, `text`, `coding`, `vision`, `translate`, or `image`). The `/tools/models` overview highlights which live model currently backs each placeholder.
