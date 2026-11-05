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
| `conversationId` | String | **Optional**. A unique identifier (UUID or session string, up to 64 chars `^[a-zA-Z0-9_-]+$`) to continue a multi-turn conversation. In Agentic mode, this preserves conversation history across requests. |
| `user` (or `userId`) | String | **Optional**. A unique identifier representing your end-user (1–64 characters `^[a-zA-Z0-9_.-]+$`). When provided in Agentic mode, enables persistent user memory and strictly isolates each end-user's facts and notes so one user cannot access another user's memory. |

### Chat and Memory Isolation

* **Chat Isolation:** To keep conversation history separate between users, generate and provide a unique `conversationId` (e.g. UUID) for each user thread. Conversation turns and transcripts are strictly scoped by chatbot and conversation ID.
* **Memory Isolation:** In Agentic mode, provide the `user` parameter when calling with a shared Project API Key or Dataset API Token. DataFoundry sandboxes each end-user's profile facts and note files in a dedicated, collision-free directory. User A cannot read, overwrite, or access User B's memories.

### Example Request (cURL)

```bash
curl -X POST -H 'Content-Type: application/json' \
-H 'Authorization: Bearer YOUR_PROJECT_API_KEY' \
-d '{
  "message": "What is mentioned in the project documents about sustainability?",
  "conversationId": "7b8e-4a2c-9d1f",
  "user": "student_jordan_101"
}' \
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
  "conversationId": "7b8e-4a2c-9d1f",
  "user": "student_jordan_101"
}
```
