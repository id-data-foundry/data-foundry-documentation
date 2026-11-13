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
* **Memory Isolation:** In Agentic mode, provide the `user` parameter when calling with a Project/User API Key or Dataset API Token. Data Foundry isolates each end-user's profile facts and note files in a separate per-user directory so User A cannot read, overwrite, or access User B's memories.

#### Identity & Memory Support

| Token / Identity | Conversation History | Persistent User Memory & Notes |
| :--- | :---: | :---: |
| **Project / User API Key** (with `user` parameter) | Yes | **Yes** (isolated per `user`) |
| **Project / User API Key** (no `user` parameter) | Yes | **Yes** (scoped to the key owner) |
| **Dataset API Token** (with `user` parameter) | Yes | **Yes** (isolated per `user`) |
| **Dataset API Token** (no `user` parameter) | Yes | **No** (no individual user identity) |
| **Study Participation Token** | Yes | **No** (not supported yet; passing `user` returns `403`) |

### Rate Limits

API requests are rate-limited per caller identity (and per `user` value when provided). Exceeding the burst limit returns HTTP `429 Too Many Requests` (`Rate limit exceeded`).

### Python Example:

You can interact with your custom chatbot and preserve conversation sessions using Python:

[Download Python Script]({% link assets/files/chatbot/chat.py %}){: .btn .btn-green download="chat.py"}

```python
import requests

api_key = "df-abcdef1234567890abcdef1234567890abcdef123456789="
chatbot_id = 42

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "message": "What is mentioned in the project documents about sustainability?",
    "conversationId": "7b8e-4a2c-9d1f",
    "user": "student_jordan_101"
}

response = requests.post(
    f"{{ site.external_base_urls.datafoundryurl }}/api/v1/chatbots/{chatbot_id}/chat",
    headers=headers,
    json=payload
)

if response.status_code == 200:
    result = response.json()
    reply = result["choices"][0]["message"]["content"]
    print("Chatbot Reply:\n", reply)
else:
    print(f"Error {response.status_code}:", response.text)
```

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
