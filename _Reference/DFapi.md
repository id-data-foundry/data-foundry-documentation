---
layout: default
title: Data Foundry Developer API
nav_order: 1
parent: Reference
has_children: false
has_toc: false
---

# Data Foundry Developer API

For a long time now Data Foundry has not only been about storing data, but also about designing with data. That can mean that we need to interact with APIs (application programming interfaces) to unlock more or special functionality. On this documentation page, we collect the different APIs that have become available on Data Foundry in the last months.

Before we head into the different APIs and their usage, let's check out how to get any API access on Data Foundry: generate API keys.

## API Access

Here is a step-by-step guide on how to enable API access for one or more of your projects on Data Foundry:

1. Create a new project or use an existing project; important: you need to be the owner of the project.
2. Open the project edit page (pen icon on main project page).
3. Scroll down to the API Access section.
4. Read information carefully and click the button to generate a new API key.
5. Copy the API key; it should look like `df-AHFJed65hg09sdv098asdvadv98`.
6. Add a new script or open an existing script in the project.
7. Try a few of the examples below, using the copied API key for `<API-KEY>`.

All APIs work with the same API key. So, once you have generated a key for your project, you can use it with all available APIs.

## API Reference

The full API reference is available via the Swagger documentation on your Data Foundry instance.

### Chatbot API

The Chatbot API provides access to custom chatbots you have designed in Data Foundry. These bots can be configured with specific instructions and their own knowledge base (RAG).

*   **[Chatbot API Specification]({% link _Reference/LocalAI/AIAPI.md %}#chatbot-api)**