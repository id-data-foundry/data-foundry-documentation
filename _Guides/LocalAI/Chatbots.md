---
layout: default
title: LLM Chatbots
parent: Local AI
nav_order: 1
has_toc: true
---

# Designing Custom Chatbots

Data Foundry allows you to create **Custom Chatbots** (also known as Custom Assistants or Custom GPTs) powered by local AI models. These bots can be configured with distinct personalities, behavioral rules, uploaded knowledge reference documents, and persistent memory.

Whether you want a straightforward FAQ assistant or an autonomous research companion, Data Foundry offers two engine modes to fit your project.

---

## 1. Choosing Your Chatbot Engine

When creating or configuring a chatbot, you can toggle between two engine modes:

```
Standard  [—●]  Agentic
```

* **Standard Chatbot**: Operates as a direct conversational assistant. When a user asks a question, the assistant automatically searches any uploaded reference documents for relevant sections, places those excerpts into the context prompt, and generates an immediate response. It is simple, predictable, fast, and great for static document lookup.
* **Agentic Chatbot**: Operates as an autonomous assistant using a **"Think-and-Act" loop**. Instead of answering immediately, the bot thinks about what the user needs, decides whether it should use a tool (such as querying reference materials or saving a note), checks the tool result, and formulates its answer. It can remember personal facts about users across chats, create and read private note files, and follow detailed operational guidelines written in an `AGENTS.md` file.

### Engine Comparison at a Glance

| Feature | Standard Chatbot | Agentic Chatbot |
| :--- | :--- | :--- |
| **How it answers** | Direct reply based on your prompt and matching text | Thinks first, uses tools when needed, and searches documents on demand |
| **Document search** | Automatically includes matching text sections before answering | Searches uploaded documents only when your question relates to them |
| **Memory & Notes** | Forgets everything once a conversation ends | Remembers facts about you and saves private notes across chats |
| **Customization** | Instructions (System Prompt) | Instructions (System Prompt) + `AGENTS.md` guidelines |
| **Model & Temperature** | Pick any hosted AI model and temperature | Uses the platform's tool-calling coding model automatically |
| **Multiple chats** | One chat thread | Multiple separate conversation threads |
| **Best for** | Simple Q&A, FAQs, quick document reference | Personal research assistants, study partners, diary studies, interactive coaches |

> **Need a step-by-step walkthrough?** Start with **[Building Your First Agentic Chatbot]({% link _Tutorials/LocalAI/AgenticChatbot.md %})** (~15 min), or try the **[Advanced: Diary Study Companion]({% link _Tutorials/LocalAI/DiaryStudyCompanion.md %})** (~45 min) for a complete research case. For concepts, see **[AI Agents: How Agentic Chatbots Work]({% link _Learning/LocalAI/AgenticChatbots.md %})**.

---

## 2. Creating a Chatbot

To create a new chatbot:

1. Navigate to your **Project Home** in Data Foundry.
2. In the **Scripts** section, click on **add script**.
3. Scroll down to the **"Add a chatbot"** section.
4. Enter a name for your bot (e.g. *"Design Research Assistant"*, *"Study Buddy"*, or *"Project Guide"*).
5. Click **Create chatbot**.

You will be redirected to the chatbot configuration page where you can choose your engine mode and customize settings.

### Common Bot Settings
* **Bot Name:** The display name of your chatbot.
* **Description:** A short summary of what the bot does, displayed on your project overview and public pages.
* **Privacy:**
  * **Private (Only me):** Only you (when logged in) can access and test the bot.
  * **Public (Shared):** Any user logged into Data Foundry can chat with the bot via a direct link.
* **Chat Transcripts:**
  * **Save chat transcripts:** When turned on, all conversations are recorded and listed under the **Conversations** tab, where you can inspect or download them as JSON files for research analysis.

---

## 3. Configuring a Standard Chatbot

If you choose the **Standard** engine, configure the following options:

### AI Model & Temperature
* **Selected AI Model:** Choose the underlying language model ("brain") that powers the bot. Different models vary in speed, creative writing fluency, and reasoning capability.
* **Temperature (0.0 – 2.0):** Controls how creative or deterministic the answers are. Lower values (e.g. `0.2` – `0.5`) produce consistent, focused, and factual replies. Higher values (e.g. `0.8` – `1.2`) encourage creative, varied phrasing.

### Instructions (System Prompt)
The instructions tell the AI who it is and how to behave:
* **Role:** *"You are an experienced design tutor helping undergraduate students develop design briefs."*
* **Tone:** *"Be encouraging, ask probing questions, and avoid jargon."*
* **Constraints:** *"Always keep answers under three paragraphs. If you don't know the answer from the reference materials, say so."*
* **Current Date:** You can type `$DATE` anywhere in your prompt, and Data Foundry will automatically replace it with today's date (e.g. `10/4/26`).

### Knowledge Base & Document Search Tuning
When reference documents (PDFs, Markdown, or text files) are uploaded:
* **Max Reference Chunks:** How many text excerpts from your documents the bot reads before replying (typically `5` to `10`).
* **Relevance Threshold (0.0 – 1.0):** How closely document text must match the user's question to be included. Higher numbers (e.g. `0.75` – `0.85`) only include very close matches; lower values include broader background information.
* **Show/Hide Sources:** When turned on, the bot includes clickable source tags in its responses so users can see which document sections were used.

### Starter Prompts
* **Greeting Message:** The opening message sent automatically by the bot when a user begins a chat (e.g. *"Hi there! What design question can I help you explore today?"*).
* **Suggested User Input:** Pre-fills the user's text area with a starter question or template.

---

## 4. Configuring an Agentic Chatbot

The **Agentic** engine turns your chatbot into an active problem solver that can reason, look up information on demand, remember personal facts, and take private notes.

{: .info}
New to agents? Read **[AI Agents: How Agentic Chatbots Work]({% link _Learning/LocalAI/AgenticChatbots.md %})** for a beginner-friendly overview of tools, memory types, and limits.

In Agentic mode, Data Foundry automatically selects the platform's tool-calling coding model (so **AI Brain & Model Selection** is hidden). **User Memory & Notes** and **Multi-Session Support** are both enabled by default on new bots, and you can still set **Instructions (System Prompt)**, **Knowledge Base Retrieval (RAG)** tuning (**Max Reference Chunks**, **Relevance Threshold**, **Show/Hide Sources**), and **Starter Prompts**.

### How Agentic Chatbots Work: The "Think-and-Act" Loop
Standard chatbots generate an immediate text response as soon as you press enter. An agentic chatbot, by contrast, uses a **Think-and-Act loop** (often called ReAct):

```
User Prompt ──> [ 1. Think & Plan ] ──> Needs info / memory?
                       │
             ┌─────────┴─────────┐
            Yes                  No
             │                   │
             ▼                   ▼
     [ 2. Take Action ]     [ 3. Synthesize Final Reply ]
      • Search docs               • Friendly response
      • Save memory fact          • Clickable source tags
      • Write note file           • Tool activity chips
             │
             └──> [ Inspect Result ] ──> Repeat if needed
```

1. **Think & Plan:** The bot inspects your prompt along with any facts it already knows about you. It decides whether it can answer right away or needs to gather information first.
2. **Take Action:** When needed, the bot calls built-in tools:
   * `search_knowledge_base`: Looks up specific topics in your uploaded documents.
   * `update_user_memory` / `delete_user_memory`: Saves or removes a fact about you (such as your name, research topic, or preferences) in your persistent profile.
   * `write_user_file` / `read_user_file` / `delete_user_file`: Creates, reads, or deletes flat Markdown note files in your private space (e.g. `notes.md` or `diary.md`; subfolders are not allowed).
   * `reset_user_memory`: Clears all saved profile facts and note files when the user asks to wipe everything.
3. **Synthesize Final Reply:** Once the bot has the information it needs, it writes a cohesive answer, citing the documents it used and displaying friendly activity badges. Data Foundry caps each message at **10 think-and-act steps** so an agent cannot get stuck in an infinite loop.

### Crafting Guidelines with `AGENTS.md`
In Agentic mode, a dedicated card appears: **🤖 Agent Guidelines & Memory Configuration (`AGENTS.md`)**.

`AGENTS.md` acts as the operational manual for your agent. It defines how proactive the bot should be, what memory facts to listen for, and how to structure notes. Changes saved in `AGENTS.md` are **applied instantly**—you do not need to restart or recreate the bot.

{: .info}
**Tip:** You can also upload or manage `AGENTS.md` (or `.agents/AGENTS.md`) directly as a file in the dataset folder if you prefer to version or reuse guidelines across bots.

To get started quickly, click the **"📋 Insert Starter Template"** button in the designer.

#### Structure of an Effective `AGENTS.md`
An `AGENTS.md` file typically contains five key sections:

```markdown
# Persona & Role
You are an intelligent, supportive design research companion. You help designers 
explore ideas, synthesize literature, and structure their projects.

# Memory & Long-Term Knowledge Directives
1. Proactive Fact Extraction:
   - When the user mentions their name, academic department, research topic, 
     design methodologies, or project deadlines, immediately call update_user_memory.
   - Use clean, lowercase snake_case topic names: user_name, research_topic, 
     design_methods, target_audience.
   - Keep notes factual, concise, and clear.

# Notes & Document Management
1. When the user asks you to outline a plan, draft ideas, or take notes, call 
   write_user_file to save the content into notes.md or project_plan.md.
2. When the user asks what notes they have or requests a summary of past ideas, 
   call read_user_file.

# Knowledge Base Search
1. When questions touch upon design frameworks, research papers, or project 
   guidelines uploaded to this bot, call search_knowledge_base with a targeted query.

# Conversational Style
- When you remember a new fact about the user, briefly acknowledge it 
  (e.g., "I've noted your focus on wearable electronics in your profile.").
- Be structured, clear, and cite your sources.
```

### Knowledge Base Documents & Smart Search
Under the **📚 Knowledge Base** tab, you can upload reference materials for your bot:
* **Supported Formats:** PDF files (`.pdf`), Markdown files (`.md`), and plain text (`.txt`).
* **Status Badges:** Uploaded files display an **Indexed ✅** badge once they are indexed and ready for searching. Newly uploaded or deleted documents take effect right away without needing to re-save settings.
* **Markdown Chunking Tip:** Data Foundry splits Markdown documents at headings (`#`, `##`, `###`, `####`). Write one clear topic per `##` heading so search retrieves focused, accurate excerpts.
* **On-Demand Search:** Unlike standard bots that search on every single turn, agentic bots only call `search_knowledge_base` when a question actually requires document reference.
* **Interactive Citations:** When the agent retrieves information from a document, it attaches a citation tag (e.g. `[1] research_guide.pdf (82%)`). Clicking this tag opens a clean **Source Reference** modal showing the exact quoted passage and context.

### Adaptive User Memory & Private Notes
When **User Memory & Notes** is enabled (on by default in Agentic mode):
* **Privacy & Isolation:** Memory is isolated per user and per bot. Another user chatting with the same public bot cannot see your private facts or notes.
* **Designer Inspection:** Editors of the chatbot can switch between users via the **Viewing User Memory:** dropdown in **Test Bot** to review saved facts and note files (for example, during a user study). If you run a study, inform participants clearly in your consent form.
* **Profile Attributes:** Key-value facts remembered about you (such as your topic, background, or preferences).
* **Saved Notes & Files:** Flat private Markdown files (`.md`) created during conversation. In the **Test Bot** workbench, you can expand any saved file to view its full content.
* **User Control:** Users can click **🧠 Memory** in the chat bar (or use the **Test Bot** card) to delete individual memory topics (`❌`), delete specific note files (`❌`), or wipe all memory clean using **🗑️ Reset All Memory & Files**.

### Multi-Session Support
Enabling **Multi-Session Support** allows users to maintain multiple independent chat conversations with the same bot (e.g., one thread for brainstorming, another for literature review). The bot's persistent memory and private notes remain available across all of that user's sessions.

---

## 5. Testing Your Bot: The Test Workbench

Before sharing your bot, open the **Test Bot** page (`/tools/chatbots/:id/test`). The test page provides an interactive inspection workbench designed for testing both Standard and Agentic features:

1. **How this Assistant Works (Visual Overview):** A collapsible diagram showing the information flow between you, the assistant, the knowledge base, and memory.
2. **Live User Memory & Notes:** An auto-updating card showing all remembered facts and saved files. Whenever the bot updates a fact or note during a test chat, this card refreshes automatically.
3. **Quick-Test Prompts:** Clickable buttons to quickly verify core capabilities:
   * `🧠 Remember my topic`: Tests proactive memory extraction (`update_user_memory`).
   * `📝 Write notes.md`: Tests private file creation (`write_user_file`).
   * `🔍 Recall facts & notes`: Verifies that the bot recalls previously saved information.
   * `📚 Search Knowledge Base`: Verifies on-demand document search and citations.
4. **Assistant Activity & Tool Trace:** Under each response, expand the trace to inspect exactly which tools the bot called, the search queries it used, and the intermediate results it received.
5. **Multi-Turn Folding:** Earlier chat turns fold into tidy accordions automatically so you can focus on the latest response.

---

## 6. Sharing & Transcripts

* **Public Bot Links:** When **Public (Shared)** is toggled on, copy the link from the **Share** button or the configuration page. Anyone logged into your Data Foundry instance can use the bot.
* **Reviewing Transcripts:** If **Save chat transcripts** is enabled, all conversations appear under the **Conversations** tab. Click **Download** on any session to export the conversation history as a JSON file.

---

## 7. Programmatic Access (API)

Both Standard and Agentic chatbots can be queried programmatically via the Data Foundry REST API.

* **Endpoint:** `POST /api/v1/chatbots/:id/chat`
* **Format:** OpenAI-compatible JSON payload (`message`, `conversationId`).
* **Session Continuity:** Supplying a consistent `conversationId` allows the agentic engine to maintain multi-turn context and memory across API requests.

For code examples in cURL and JavaScript, see the **[Chatbot API Reference]({% link _Reference/LocalAI/chatbotAPI.md %})**.

---

**Happy Bot Building!** 🤖
