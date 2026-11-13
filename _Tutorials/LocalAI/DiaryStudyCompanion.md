---
layout: default
title: "Advanced: Diary Study Companion"
parent: Local AI 101
nav_order: 2
has_toc: true
---

# Tutorial: Build a Diary Study Companion (Agentic Chatbot)

In this tutorial, you will build and test an agentic chatbot for a real design research scenario: a **two-week winter cycling diary study**.

If you are brand new to agentic chatbots, start with the shorter **[Building Your First Agentic Chatbot]({% link _Tutorials/LocalAI/AgenticChatbot.md %})** tutorial (~15 minutes) first, then come back here when you are ready to design a full study bot.

**Estimated time:** 45 minutes.  
**Prerequisites:**
- A Data Foundry account and a project with AI enabled (projects start with 5,000 tokens by default).
- Basic familiarity with creating a chatbot (or completion of the beginner tutorial above).

---

## The Story: Why Sam Needs an Agentic Bot

Sam is an Industrial Design student running a **2-week diary study** with 8 participants about how they cycle in winter.

Sam tried a paper diary and a survey form before, and both had problems:
- Participants forgot what they wrote yesterday.
- A plain form cannot ask a follow-up question when someone writes *"wet ride, nothing else"*.
- Participants kept emailing Sam simple questions from the study instructions, like *"Can I skip a day if I am sick?"*

A **Standard** chatbot on Data Foundry cannot solve this either. Look at why:

| What Sam's study needs | Why a Standard bot fails | Which Agentic feature solves it |
| :--- | :--- | :--- |
| Remember each person's participant code, bike type, and commute | Standard bots forget everything once a chat ends | **User memory** (`update_user_memory`) |
| Keep a structured daily log per person across 14 days | Standard bots cannot save files | **Private notes** (`read_user_file`, `write_user_file`) |
| Answer rules questions from the study protocol, without pulling rules into every greeting | Standard bots inject document chunks on every single turn | **On-demand knowledge search** (`search_knowledge_base`) |
| Ask **one** short follow-up question if an entry is too brief | Needs conditional workflow rules, not only a persona | **Operational rules** in `AGENTS.md` |
| Keep Participant A's diary invisible to Participant B | — | **Per-user isolation** |
| Read everyone's diary and conversations at the end of the study | — | **Viewing User Memory** + **Save chat transcripts** |

If any of these terms are new to you, keep **[AI Agents: How Agentic Chatbots Work]({% link _Learning/LocalAI/AgenticChatbots.md %})** open in another tab as a companion guide.

---

## Part 1: Plan Before You Build

Good agent design starts on paper, not in the editor. Before opening Data Foundry, write down what the bot must **remember**, **save**, **look up**, and **never do**.

Here is Sam's plan:

| Question | Answer for the Diary Study Companion |
| :--- | :--- |
| **What should it remember about each user?** | `participant_code` (for example, `P01`), `bike_type`, and `commute_distance`. Never store real names. |
| **What should it save in notes?** | A daily log in one file called `diary.md`, with one `## Day N (YYYY-MM-DD)` heading per day. |
| **What should it look up in documents?** | Rules about duration, skipping days, privacy, and leaving the study (from `study_protocol.md`). |
| **What must it never do?** | Never give traffic-safety, legal, or medical advice. Never invent diary details. Never mention other participants. |

In Part 3, this four-row table turns directly into your `AGENTS.md` file.

---

## Part 2: Create the Bot and Turn On Agentic Mode

1. Open your project in Data Foundry.
2. Scroll to the **Scripts** section and click **add script**.
3. Scroll down to **Add a chatbot**.
4. Enter the name `Diary Study Companion` and click **Create chatbot**.

You are now on the chatbot configuration page under the **⚙️ Configuration & Prompts** tab.

5. Look at the **Chatbot Engine Mode** card at the top. Click the switch on the right from **Standard** to **Agentic**.

You should now see: the **Agentic** badge at the top of the page, a new **Agentic mode** card below **General Information**, and a new **🤖 Agent Guidelines & Memory Configuration (`AGENTS.md`)** card at the bottom. Notice that the model picker disappears.

{: .info}
**No model dropdown in Agentic mode?** That is normal. In Agentic mode, Data Foundry automatically uses the platform's tool-calling coding model, so you do not need to pick a model or temperature.

6. In the **General Information** card, enter a **Description** such as:  
   `Daily check-in companion for the 2-week winter cycling diary study.`
7. Leave **Private (Only me)** selected for now while you build and test.
8. Look at the **Agentic mode** card right below:
   - Check that **User Memory & Notes** is set to **Enabled** (it is on by default for new bots).
   - Check that **Multi-Session Support** is set to **Multi-Session** (also on by default, so participants can start a fresh thread each day while keeping the same memory).
9. Scroll to **Instructions (System Prompt)** and paste this text:

```text
You are the Diary Study Companion for a two-week winter cycling study at TU/e.
Today's date is $DATE.
Be warm, brief, and neutral. Never judge a participant's choices.
Always follow your AGENTS.md rules for memory, diary notes, and protocol questions.
```

10. Scroll to **💬 Behavior & Starter Prompts** and click it to expand the card.
11. Fill in both fields:
    - **Greeting Message:**
      `Hi! Welcome to the Winter Cycling Diary Study. If this is your first check-in, please share your participant code (for example P01), your bike type, and your usual commute distance. Otherwise, tell me about today's ride!`
    - **Suggested User Input:**
      `Day 1: `
12. Scroll down and click the green **Save Settings** button.

You should now see: `✓ Settings saved successfully` next to the button.

{: .info}
**What just happened?** You set up *who* the bot is (**Instructions (System Prompt)**) and enabled its persistent **User Memory & Notes** and **Multi-Session Support**. Including `$DATE` tells Data Foundry to insert today's date automatically. Read more in [System prompt vs. AGENTS.md]({% link _Learning/LocalAI/AgenticChatbots.md %}#6-system-prompt-vs-agentsmd).

---

## Part 3: Write the Agent Rules (`AGENTS.md`)

`AGENTS.md` is the bot's working manual. It tells the agent *when* to call its memory, notes, and search tools.

1. Scroll to the bottom of the **⚙️ Configuration & Prompts** tab to find the **🤖 Agent Guidelines & Memory Configuration (`AGENTS.md`)** card.
2. Click **📋 Insert Starter Template** to see the default structure.

Now look at how Sam's plan from Part 1 translates into clear rules. You will replace the template with rules tailored for the diary study:

- **Language rule:** *"Always reply in the same language the participant uses."* Useful when participants write in Dutch or English.
- **Pseudonymous memory:** Ask for `participant_code`, `bike_type`, and `commute_distance`—and tell the bot *not* to store real names.
- **Read before writing:** Tell the bot to call `read_user_file("diary.md")` before `write_user_file("diary.md", ...)`, because `write_user_file` overwrites the whole file. Note that Data Foundry only allows flat `.md` files (no subfolders).
- **Conditional follow-up:** Ask **one** follow-up question only when an entry has fewer than two sentences, then update `diary.md`.
- **Protocol lookup & boundaries:** Search the knowledge base for study rules, never give safety/legal/medical advice, and never mention other participants.

3. You can either download the finished file and paste it in, or copy the block below into the `AGENTS.md` text box:

[Download diary-AGENTS.md]({% link assets/files/chatbot/diary-AGENTS.md %}){: .btn .btn-green download="diary-AGENTS.md"}

```markdown
# Persona & Role

You are a calm, encouraging Diary Study Companion for a two-week winter cycling study at TU/e.
Your job is to collect one short daily entry from each participant and keep their diary organized.

# Language

- Always reply in the same language the participant uses (for example, English or Dutch).

# Memory & Long-Term Knowledge Directives

1. First contact:
   - When a participant mentions their participant code, bike type, or usual commute distance, call `update_user_memory` right away.
   - Use clear lowercase keys: `participant_code`, `bike_type`, `commute_distance`.
   - Ask for a participant code (such as `P01`) instead of a real name. If a participant shares their real name anyway, do not store it in memory.

2. Updating facts:
   - If a participant changes their bike or commute routine during the study, update the matching memory key with `update_user_memory`.

# Diary Notes (`diary.md`)

1. Saving daily entries:
   - Keep all entries for one participant in a single flat Markdown file named `diary.md`.
   - When a participant shares a trip or daily reflection, first call `read_user_file("diary.md")` so you do not overwrite earlier days.
   - Then call `write_user_file("diary.md", ...)` with all existing entries plus the new entry appended at the end under a heading like `## Day 1 (YYYY-MM-DD)` (use the day number and date the participant mentions, or ask if unclear).
   - Keep entries faithful to what the participant wrote. Do not invent details.

2. Follow-up questions:
   - If a participant's daily entry is shorter than two sentences, ask **one** short, friendly follow-up question (for example, about weather, comfort, lighting, or road conditions).
   - Once they reply, update that day's section in `diary.md` and thank them. Never ask more than one follow-up question per day.

3. Recalling or deleting entries:
   - When a participant asks what they wrote earlier, call `read_user_file("diary.md")` before answering.
   - Only delete `diary.md` (`delete_user_file("diary.md")`) if the participant clearly asks to remove their notes.

# Knowledge Base Search

- Whenever a participant asks about study rules, duration, skipping days, privacy, data deletion, or how to withdraw, call `search_knowledge_base` with a focused query before answering.
- If the study protocol does not cover their question, say so honestly and advise them to contact the researcher.

# Boundaries & Safety

- Never give traffic-safety, legal, or medical advice.
- Never share or guess information about other participants.
- Briefly confirm when you saved a fact or diary entry (for example, "I saved Day 1 to your diary.").
```

4. Click **Save AGENTS.md**.

You should now see: `✓ AGENTS.md saved and agent reloaded!` in green next to the button. Your new rules are active right away.

{: .info}
**What just happened?** You wrote clear triggers for the bot's tools (`update_user_memory`, `read_user_file`, `write_user_file`, `delete_user_file`, and `search_knowledge_base`) without needing to explain how those tools work under the hood. Read more in [Tools]({% link _Learning/LocalAI/AgenticChatbots.md %}#2-tools).

---

## Part 4: Upload the Study Protocol

Next, give the bot the official study rules so it can answer participant questions accurately.

Notice how the protocol below puts **one topic under each `##` heading**. Data Foundry splits Markdown documents into searchable chunks at headings, so clear headings make search results much sharper.

1. Download `study_protocol.md` (or save the text below as `study_protocol.md` on your computer):

[Download study_protocol.md]({% link assets/files/chatbot/study_protocol.md %}){: .btn .btn-green download="study_protocol.md"}

```markdown
# Winter Cycling Diary Study Protocol

## Study Duration and Goal

This diary study runs for 14 days (two weeks). We want to learn how winter weather affects daily cycling trips, gear choices, and comfort.

## What to Report Each Day

Write a short entry once a day after your last bike trip, or write "no trip today" if you did not cycle. Mention the day number, weather, and anything that felt easy or difficult. Two to four sentences are enough.

## Skipping Days and Catching Up

You may skip up to two days during the two weeks without leaving the study. If you miss a day, you can still write a short note the next day and mention which day it was for.

## Privacy and Who Can Read Your Diary

Your memory profile and `diary.md` file are kept separate from other participants. No other participant can see your entries. The researcher conducting this study can read your `diary.md` notes and saved chat transcripts to analyze the study results.

## Leaving the Study and Deleting Data

Participation is voluntary. You can stop at any time without giving a reason. To withdraw and have your diary notes deleted, email the researcher (`sam.researcher@example.edu`) with your participant code. You can also ask the bot to delete `diary.md`, or clear your own profile using the memory menu in the chat bar.
```

2. Click the **📚 Knowledge Base** tab near the top of the chatbot page.
3. Under **Upload Reference Documents**, drag and drop `study_protocol.md` into the upload area (or click it to choose the file).
4. Look at **Knowledge Base Documents** on the left.

You should now see: `study_protocol.md` listed with an **Indexed ✅** badge. (If it shows **Processing ⚙️**, wait a few seconds and refresh.) The top header chip also updates to `📚 1 Doc`, and the bot can search it right away.

5. Optional check: switch back to **⚙️ Configuration & Prompts** and open **Knowledge Base Retrieval (RAG)**. Check that **Show Sources** is turned on (this displays clickable citations in answers), then click **Save Settings** if you changed it.

{: .info}
**What just happened?** Data Foundry split `study_protocol.md` at its `##` headings into searchable chunks. Unlike a Standard bot, your Agentic bot will **not** read those chunks on every message—it only searches them when a question asks about the protocol. Read more in [Knowledge base search]({% link _Learning/LocalAI/AgenticChatbots.md %}#5-knowledge-base-search-retrieval).

---

## Part 5: Test as a Participant

Never share an agentic bot without running a repeatable test script. Click **Test Bot** in the top-right header to open the testing workbench.

Before typing, notice three helpful areas on the **Test Bot** page:
- **💡 How this Assistant Works (Visual Overview):** Click to expand a diagram of your bot's active setup.
- **🧠 Live User Memory & Notes:** Shows your saved facts and files, and updates automatically whenever the bot saves something.
- **Assistant Activity & Tool Trace:** Appears under each bot reply so you can inspect which tools ran and why.

Run these five test messages in order. Check every column before moving to the next message:

| # | Send this message | What the reply should do | What to check in **🧠 Live User Memory & Notes** and the **Tool Trace** |
|---|---|---|---|
| 1 | `Hi! I am P04. I ride an e-bike and my commute is 6 km each way.` | Greet P04 warmly and confirm the details were saved. | `participant_code`, `bike_type`, and `commute_distance` appear in saved profile facts. Tool Trace shows `update_user_memory`. |
| 2 | `Day 1: Cold headwind this morning and drizzle on the way back. My gloves got soaked after 10 minutes, so my hands were freezing.` | Confirm Day 1 was saved. No extra follow-up needed (the entry is already 2 sentences). | `📄 diary.md` appears under saved files. Click it to check that Day 1 is saved under a `## Day 1` heading. Tool Trace shows `read_user_file` + `write_user_file`. |
| 3 | `Day 2: Smooth ride.` | Save Day 2 and ask **one** short follow-up question (for example, about weather or gear). | Reply ends with one question. Now reply `Dry and 4 degrees, wore my warm jacket.` and verify `diary.md` updates Day 2 instead of deleting Day 1. |
| 4 | `Am I allowed to skip Sunday if I stay home?` | Say that skipping up to two days is allowed. | A clickable citation like `[1] study_protocol.md (...)` appears. Click it to view the exact quoted passage. Tool Trace shows `search_knowledge_base`. |
| 5 | Click **Reset Chat** in the top-right of Test Bot to start a fresh thread, then send: `What did I write on Day 1?` | Summarize your Day 1 cold-headwind entry accurately. | Tool Trace shows `read_user_file("diary.md")`, proving memory and notes work across separate chats. |

{: .info}
**What just happened?** Each reply went through the **Think-and-Act loop**: the bot reasoned about your message, chose only the tools needed for that turn, read the results, and then wrote its reply. Read more in [The Think-and-Act loop]({% link _Learning/LocalAI/AgenticChatbots.md %}#3-the-think-and-act-loop).

---

## Part 6: Improve Your Rules (Iterate When Things Go Wrong)

AI models follow `AGENTS.md` as instructions, not rigid computer code. On your first test run, one step may not work quite the way you wanted. Here is how to diagnose and fix the three most common issues:

| What went wrong in Test Bot | Why it happens | How to fix it in `AGENTS.md` |
| :--- | :--- | :--- |
| The bot replied nicely to Day 1, **but `diary.md` was not created** (no `write_user_file` in Tool Trace). | The rule sounded optional, or the model waited for an explicit "save this" request. | Make the trigger concrete: *"After EVERY daily entry, you MUST call `read_user_file("diary.md")` and then `write_user_file("diary.md", ...)` before replying."* |
| The bot asked **two or three follow-up questions** after a short entry. | Models tend to be overly helpful and ask multiple questions. | Tighten the limit: *"Ask AT MOST ONE question, in a single sentence. Wait for the reply before asking anything else."* |
| The bot answered "skipping Sunday" **without a citation** (`search_knowledge_base` did not run). | The model guessed from general knowledge instead of checking the protocol. | Add an explicit check: *"Never answer a question about study rules from memory. Always call `search_knowledge_base` first."* |

Whenever you edit `AGENTS.md`:
1. Click **Save AGENTS.md** and wait for `✓ AGENTS.md saved and agent reloaded!`.
2. Re-run the five-message test script in **Test Bot** (use **🗑️ Reset All Memory & Files** first if you want a clean slate).

---

## Part 7: Check Privacy, Then Share With Participants

Before inviting your 8 participants, make sure conversations are recorded and the bot is reachable.

1. Click **Edit Bot** in the top-right of **Test Bot** to return to the configuration page.
2. In **General Information**:
   - Toggle the privacy switch to **Public (Shared)** so any logged-in Data Foundry user can open the bot.
   - Toggle the transcript switch to **Save chat transcripts** so you can export conversations at the end of the study.
3. Click **Save Settings**.

You should now see: a **🌐 Public** badge and a **Share** button in the top-right header.

4. Right-click **Share** (or click it to open the public chat page) and copy the URL from your browser's address bar.
5. When you send the link to participants, include two short tips:
   - Log in with their Data Foundry account and use their participant code (like `P01`) instead of their real name.
   - Click **+ New Chat** in the top bar each day for a tidy new thread (their `diary.md` and profile carry over automatically). They can also click **🧠 Memory** at any time to see or clear what the bot saved about them.

{: .info}
**Going further: participants without Data Foundry accounts.** This tutorial uses Data Foundry accounts so participants need zero setup. If your study uses a **custom web interface** instead, your backend server can call `POST /api/v1/chatbots/:id/chat` with your Project API Key and pass `"user": "P01"` in the JSON body. Never put a Project API Key in browser JavaScript. Note that study **participation tokens** work with the API for plain chat, but persistent user memory is **not supported yet** for participation tokens. See the **[Chatbot API Reference]({% link _Reference/LocalAI/chatbotAPI.md %})**.

---

## Part 8: Monitor During the Two-Week Study

While the study is running, you can check participant progress without interrupting them:

1. Open your bot and click **Test Bot**.
2. At the top of the **🧠 Live User Memory & Notes** card, use the **Viewing User Memory:** dropdown to switch between users who have chatted with the bot.
3. Click `📄 diary.md` under **Saved Notes & Files** to read that participant's collected entries so far.
4. Click **Edit Bot** → **💬 Conversations** tab to see all recorded chat sessions.

{: .warning}
**Reminder on transparency:** Because you can read every participant's `diary.md` and saved transcripts, make sure your study protocol and consent form state this clearly before anyone starts.

---

## Part 9: Wrap Up and Clean Up After the Study

When the two weeks are over:

1. Open the **💬 Conversations** tab and click **Download** on each session to export the transcripts as JSON files for analysis.
2. To remove participant data after exporting:
   - Open **Test Bot**, select each participant in **Viewing User Memory:**, and click **🗑️ Reset All Memory & Files**.
   - Delete any saved conversation files you no longer need according to your data management plan.
3. Switch the bot back to **Private (Only me)** when data collection closes.

### Quick Ethics Checklist for Student Studies

Before running a real study with people:
- [ ] Check whether your study needs Ethical Review Board (ERB) approval and complete a [Project Review]({% link _Learning/Projects/ProjectReview.md %}) if applicable.
- [ ] Explain in your informed consent form that responses are processed by a local TU/e AI model and that the researcher can read saved notes and transcripts (see [Data Protection]({% link _Learning/DataFoundry/DataProtection.md %})).
- [ ] Instruct participants to use pseudonymous participant codes (`P01`) instead of real names or sensitive personal details.
- [ ] Keep memory rules minimal—store only what your research question needs.
- [ ] Delete participant memory, notes, and transcripts after exporting and anonymizing your dataset.

---

## Recap & Next Steps

You have designed, built, tested, and prepared a complete agentic research bot. Along the way you practiced:
- Planning memory, notes, search, and boundaries before writing prompts.
- Turning that plan into `AGENTS.md` rules and heading-structured knowledge documents.
- Verifying tool calls and citations with a repeatable test script, then iterating on rule wording.
- Managing multi-user privacy, monitoring, and cleanup.

Where to go next:
- **[AI Agents: How Agentic Chatbots Work]({% link _Learning/LocalAI/AgenticChatbots.md %})**: Full reference of concepts, tools, memory types, and limits.
- **[Designing Custom Chatbots]({% link _Guides/LocalAI/Chatbots.md %})**: Quick lookup of every setting and tab.
- **[Chatbot AI API]({% link _Reference/LocalAI/chatbotAPI.md %})**: Connect a custom web prototype to your bot.
- **[Scripting Conversational Experiences]({% link _Guides/LocalAI/convoscript/index.md %})**: If you ever need strict, word-for-word conversation flows instead of autonomous agent decisions.
