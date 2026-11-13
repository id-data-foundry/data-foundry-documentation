---
layout: default
title: Building an Agentic Chatbot
parent: Local AI 101
nav_order: 1
has_toc: true
---

# Tutorial: Building Your First Agentic Chatbot

In this hands-on tutorial, you will build a personal **Design Research Study Companion** powered by an agentic local AI model. 

Unlike a standard chatbot that simply produces an immediate text reply, your agentic companion will use a **"Think-and-Act" loop**: it will actively reason about your questions, search project reference documents only when needed, remember important facts about you across conversation sessions, and save private research notes directly to Markdown files.

{: .info}
Want the big picture behind agents, tools, and memory? Read **[AI Agents: How Agentic Chatbots Work]({% link _Learning/LocalAI/AgenticChatbots.md %})** anytime.

---

## What You Will Learn
* How an agentic chatbot works using the Think-and-Act process.
* How to configure operational guidelines and memory rules using `AGENTS.md`.
* How to upload reference documents for on-demand knowledge retrieval.
* How to inspect live memory, tool traces, and document citations using the **Test Bot** workbench.

**Estimated Time:** 10–15 minutes.  
**Prerequisites:** An account on Data Foundry and a project created.

---

## Step 1: Create Your Chatbot & Enable Agentic Mode

1. Navigate to your **Project Home** in Data Foundry.
2. In the **Scripts** section, click **add script**.
3. Scroll down to **"Add a chatbot"**.
4. Enter a name for your bot: `Design Study Companion`.
5. Click **Create chatbot**.

You will arrive at the chatbot configuration page. Look for the **Chatbot Engine Mode** card near the top and click the switch from **Standard** to **Agentic**.

The page will update to show the **Agentic mode** card and the **🤖 Agent Guidelines & Memory Configuration (`AGENTS.md`)** card below. In the **Agentic mode** card, check that **User Memory & Notes** is set to **Enabled** (it is on by default for new bots), then click **Save Settings**.

---

## Step 2: Configure Operational Guidelines in `AGENTS.md`

In Agentic mode, your bot follows an operational handbook stored in an `AGENTS.md` file. This file tells the assistant who it is, what facts to listen for, and how to organize notes.

1. On the configuration page, scroll down to the card titled **🤖 Agent Guidelines & Memory Configuration (`AGENTS.md`)**.
2. Click the **"📋 Insert Starter Template"** button.
3. Review the template. Notice how it defines:
   * **Persona & Role:** An intelligent, proactive assistant.
   * **Memory Directives:** Instructions to call `update_user_memory` whenever you mention your name, research topic, academic field, or preferences.
   * **Notes Management:** Instructions to call `write_user_file` when asked to draft outlines or take notes.
   * **Knowledge Base Search:** Instructions to call `search_knowledge_base` when questions relate to uploaded project materials.
4. Let's customize the persona slightly for design research. Replace the first few lines with:

```markdown
# Persona & Role
You are an encouraging, structured Design Research Study Companion at TU/e. 
Your goal is to help students explore user-centered design ideas, review project literature, 
and organize their research plans.
```

5. Click **Save AGENTS.md**. A green confirmation message will appear (`✓ AGENTS.md saved and agent reloaded!`). Changes are applied right away!

---

## Step 3: Upload a Project Knowledge Document

Now let's give your bot some project-specific knowledge. We will create a small sample document containing design principles.

1. On your computer, create a text file named `inclusive_design.md` with the following content:

```markdown
# Inclusive Design Guidelines for Interactive Wearables

1. Prioritize Physical Comfort:
Wearable devices must account for varying body shapes and sensitivities. Straps should 
be breathable and adjustable with one hand.

2. Multimodal Feedback:
Never rely solely on visual alerts. Always pair visual cues with tactile (haptic) vibration 
or gentle audio signals so users with visual impairments are not excluded.

3. User Data Transparency:
Users must always know when physiological sensors are active. Continuous data recording 
requires clear visual indicators on the device casing.
```

2. In the chatbot designer, click on the **📚 Knowledge Base** tab.
3. Drag and drop your `inclusive_design.md` file into the upload zone on the right (or click to browse).
4. After uploading, look at the document list on the left: your file will appear with an **Indexed ✅** badge. The bot can now search this document on demand!

---

## Step 4: Test in the Interactive Workbench

Before chatting in full-screen mode, let's explore how the bot thinks and acts using the **Test Bot** workbench.

1. At the top right of the page, click the **Test Bot** button.
2. Notice the sections on this page:
   * **💡 How this Assistant Works:** A visual diagram showing the flow of information.
   * **🧠 Live User Memory & Notes:** Shows the facts and files currently saved for you. Right now, it should say *"No profile facts stored yet"*.
   * **Prompt Input & Quick-Test Prompts:** Your testing interface.

### Test 1: Teaching the Bot Facts About You
In the user prompt box, type:
> *"Hello! My name is Jordan, and my research project is on smart haptic feedback vests for cyclists."*

Click **Submit user prompt** (or press Enter).

**What happens?**
* The bot greets you and acknowledges your research focus.
* Notice the **🧠 Live User Memory & Notes** card at the top! It updates automatically to show your new facts:
  * `user_name`: Jordan
  * `research_topic`: smart haptic feedback vests for cyclists
* Expand the **🤖 Assistant Activity & Tool Trace** under the reply to see that the bot proactively called `update_user_memory`.

### Test 2: On-Demand Knowledge Base Search
Now ask a question that requires consulting your uploaded guide:
> *"What does our project guide say about multimodal feedback for wearable devices?"*

Click **Submit user prompt**.

**What happens?**
* The bot recognizes that this question requires document information and invokes `search_knowledge_base`.
* In its answer, notice the clickable citation tag: `[1] inclusive_design.md (85%)`.
* Click the citation tag! A modal dialog appears showing the exact quoted excerpt from your `inclusive_design.md` file.

### Test 3: Private Note-Taking
Now ask the bot to draft a study note for you:
> *"Can you write a 3-bullet research plan for testing haptic vests and save it to notes.md?"*

Click **Submit user prompt**.

**What happens?**
* The bot outlines your plan and calls `write_user_file("notes.md", ...)`.
* Look at the **Saved Notes & Files** section in the memory card: you will see `📄 notes.md`.
* Click `📄 notes.md` to expand it and review the formatted notes the bot created for you!

### Test 4: Memory Recall
Finally, test whether the bot remembers you without needing you to repeat yourself:
> *"What is my name, what is my research topic, and what do I have in my notes?"*

The bot will effortlessly recall your name (Jordan), your project topic (smart haptic vests), and summarize your saved `notes.md` file!

---

## Step 5: Start a Live Chat & Share

1. Click the **Start Chat** button in the header.
2. You will be taken to the clean, full-screen chat interface.
3. Your bot will greet you, already knowing who you are and retaining your notes.
4. When you're ready to share your bot with classmates or colleagues:
   * Go back to **Edit Bot**.
   * Toggle the privacy switch to **Public (Shared)**.
   * Click **Save Settings**.
   * Copy the public link from the **Share** button and send it to your team!

---

## Summary & Next Steps

Congratulations! You have built and tested an autonomous agentic chatbot in Data Foundry. You learned how:
* The **Think-and-Act loop** allows the bot to search documents and manage memory dynamically.
* `AGENTS.md` provides instant operational guidelines for customizing persona and behavior.
* Knowledge base documents provide grounded source citations with clickable passage previews.
* Private per-user memory creates personalized, continuous research experiences while protecting privacy.

**Ready for more?** Try the **[Advanced: Diary Study Companion]({% link _Tutorials/LocalAI/DiaryStudyCompanion.md %})** tutorial to design custom rules, structured logs, and participant testing, or explore the **[Designing Custom Chatbots]({% link _Guides/LocalAI/Chatbots.md %})** guide and **[AI Agents: How Agentic Chatbots Work]({% link _Learning/LocalAI/AgenticChatbots.md %})**.
