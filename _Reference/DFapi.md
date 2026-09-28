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

Here is a step-by-step guide on how to enable API access for your Data Foundry account:

1. Login to your Data Foundry account.
2. Open your profile settings in the bottom left corner.
3. Click the "API Access" tab.
4. Scroll down to your "User API access token" in the section "Personal Access".
5. Click "Reveal" to see your API key.
6. Copy your API key and use it in your API requests.

All APIs work with the same API key. So, once you have generated a key for your project, you can use it with all available APIs.

## API Reference

The full API reference is available via the Swagger documentation on your Data Foundry instance.

{% include df-link.html text="Local Swagger API" path="/api/v2/docs/datafoundry.html" %}

### Chatbot API

The Chatbot API provides access to custom chatbots you have designed in Data Foundry. These bots can be configured with specific instructions and their own knowledge base (RAG).

*   **[Chatbot API Specification]({% link _Reference/LocalAI/AIAPI.md %}#chatbot-api)**
