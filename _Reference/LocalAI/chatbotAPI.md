---
layout: default
title: Chatbot AI API
parent: Local AI Reference
nav_order: 1
has_toc: true
---
# Chatbot API

The Chatbot API provides programmatic access to your custom chatbots—supporting both **Standard** and **Agentic** engines, on-demand document knowledge retrieval, and persistent user memory. It uses an OpenAI-compatible request and response format.

**Endpoint:** `POST /api/v1/chatbots/:id/chat`

### Authentication

Use your **Project API Key** as a Bearer token in the Authorization header.

```bash
Authorization: Bearer df-abcdef1234567890...
```

### Request Parameters

| Name | Type | Description |
| :--- | :--- | :--- |
| `message` | String | **Required**. The user's input message. |
| `conversationId` | String | **Optional**. A unique identifier (UUID or session string) to continue a multi-turn conversation. In Agentic mode, this preserves conversation history and sandboxed user memory across requests. |

### Example Request (cURL)

```bash
curl -X POST -H 'Content-Type: application/json' \
-H 'Authorization: Bearer YOUR_PROJECT_API_KEY' \
-d '{"message": "What is mentioned in the project documents about sustainability?", "conversationId": "7b8e-4a2c-9d1f"}' \
 {{ site.external_base_urls.datafoundryurl }}/api/v1/chatbots/<CHATBOT_ID>/chat
```

### Example Response

```json
{
  "id": "chatcmpl-a1b2c3d4",
  "object": "chat.completion",
  "created": 1708012345,
  "model": "hermes-2-pro-llama-3-8b",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Based on the uploaded documents, the sustainability goals include..."
      },
      "finish_reason": "stop"
    }
  ],
  "conversationId": "7b8e-4a2c-9d1f"
}
```
