---
layout: default
title: Designing Custom Chatbots
parent: Local AI
nav_order: 2
---

# Designing Custom Chatbots

Data Foundry allows you to create **Custom Chatbots** (sometimes called "Custom GPTs") that run on local AI models. These bots can be configured with specific personalities, instructions, and even their own knowledge base from documents you upload.

This guide will walk you through creating, configuring, and sharing your own chatbot.

## 1. Creating a Chatbot

To create a new chatbot, navigate to your **Project Home**.

1.  Look for the **Scripts** section in your project overview.
2.  Click on **add script**.
3.  On the "Add script" page, scroll down to the **"Add a chatbot"** section.
4.  Enter a name for your bot (e.g., "Creative Writing Assistant", "Project Helper") and click **Create chatbot**.

You will be redirected to the chatbot's configuration page.

## 2. Configuring Your Bot

The configuration page is where you design your bot's behavior. Here are the key settings:

### Bot Identity
*   **Bot Name:** The display name of your chatbot.
*   **Description:** A short summary of what the bot does. This is helpful for you and others to understand its purpose at a glance.

### Instructions (System Prompt)
This is the most important part! The **Instructions** tell the AI how to behave. You can define:
*   **Role:** "You are an expert data scientist..." or "You are a helpful primary school teacher..."
*   **Tone:** "Answer in a funny, pirate-like style..." or "Be concise and professional..."
*   **Constraints:** "Never mention..." or "Always explain technical terms..."

> **Tip:** Be specific! The better your instructions, the better the bot will perform.

### AI Model
Choose the **AI Model** (the "brain") that powers your bot. Different models have different strengths:
*   Some are better at reasoning and logic.
*   Some are faster but less detailed.
*   Some are specialized for coding or creative writing.

### Conversation Settings
*   **Greeting Message:** The first message the bot sends when a chat starts. (e.g., "Hello! How can I help you with your project today?")
*   **Suggested User Input:** Pre-fills the user's input box with a starter question or template.

## 3. Adding Knowledge (Knowledge Base)

You can give your chatbot a "memory" or specific knowledge by uploading documents. This is technically known as **RAG (Retrieval-Augmented Generation)**.

1.  Scroll to the **Upload Documents** section.
2.  Drag and drop **PDF files** (e.g., research papers, manuals, project reports).
3.  The system will process these files and index them.

When you chat with the bot, it will:
1.  Search your uploaded files for information relevant to your question.
2.  Read the relevant "chunks" of text.
3.  Use that information to answer your question.

### Tuning the Knowledge Base
In the **Advanced Options**, you can tweak how the bot uses these files:
*   **Max References:** How many text chunks should the bot read? (Default is usually fine, increase if you need it to synthesize information from many places).
*   **Relevance Threshold:** How strict should the search be? Higher values (closer to 1.0) mean the bot only looks at very exact matches. Lower values (e.g., 0.5) allow for broader context.

## 4. Testing Your Bot

Before sharing, you should test if your instructions and knowledge base are working as expected.

*   Click **Test Bot** to run quick, single-turn tests. This is great for checking if it retrieves the right information from your PDFs.
*   Click **Start Chat** to have a full conversation with your bot in a chat interface.

## 5. Sharing Your Chatbot

Once you are happy with your bot, you can share it!

*   **Private (Only me):** Only you (logged in) can access the bot.
*   **Public (Shared):** Any user logged into Data Foundry can use the bot if you send them the link.
    *   Toggle the switch to **Public**.
    *   Copy the link from the **Start Chat** button or the "this link" text in the settings.

## 6. Saving Conversations

By default, chats might be temporary. If you want to keep a log of all interactions (e.g., for research data collection):
1.  Toggle **Save all chats** to ON.
2.  The logs will appear in the **Saved Conversations** list on the configuration page.
3.  You can download these logs as JSON files.

## 7. Programmatic Access (API)

You can interact with your custom chatbots programmatically using the Data Foundry API. This allows you to integrate your RAG-enabled chatbot into your own websites, mobile apps, or hardware prototypes.

To use the API, you will need:
*   **The Chatbot ID:** Found in the URL of the chatbot configuration page.
*   **A Project API Key:** Enabled in your project's API Access settings.

The API is OpenAI-compatible and supports maintaining conversation history. For detailed technical specifications and examples, see the **[Chatbot API Reference]({% link _Reference/LocalAI/AIAPI.md %}#chatbot-api)**.

---

**Happy Bot Building!** 🤖
