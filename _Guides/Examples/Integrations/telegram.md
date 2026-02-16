---
layout: default
title: Telegram Bot
parent: Example Projects
nav_order: 2
has_children: true
has_toc: false
---

# Use telegram with Data Foundry
## Using the Telegram bot

This use-case is about using the Telegram messenger to collect diary, photos and possibly location data from participants in your study. Data Foundry has its own Telegram bot that can collect this data interactively.

CONTEXT

You want to collect diary entries, photos and/or location information from participants in a study. You might also want to get in touch with the participants of your study. With Telegram, you can do all this directly from Data Foundry. This also allows to communicate safely without leaking personal data in the process. All collected items from your participants, so diaries, photos or images, and location information, can be used in the flow of your study. You can export them and combine them with each other.

![Data Flow]({% link _Guides/Examples/Integrations/images/usecase-telegram.png %})

In short, what you can you as the researcher to with the Data Foundry Telegram bot:

1. collect diary entries from participants (-> diary dataset)
2. collect photos or images from participants (-> media dataset)
3. collect location data from participants (-> movement dataset)
4. receive messages from participants directly from your own Telegram client (mobile or desktop)
5. send messages to individual or all participants directly from Telegram client (mobile or desktop)

## What you need to get started

1. A project created in Data Foundry, and depending on your needs one or more
    - Diary dataset (activate "open participation" option)
    - Media dataset (activate "open participation" option)
    - Movement dataset (activate "open participation" option)
2. Multiple participants registered in your project
3. Optional: install Telegram client on mobile or desktop for yourself

## How to get started

### 1. Start with the basic setup (register or login, create a new project), then:

1. Add participants
2. Add diary, media and movement datasets as you need them (can be one, two or all three) and don't forget to activate the "open participation" option in the dataset settings
3. Email the sign-up links to your participants and ask them to sign up (consent form and accept)

![Step 1]({% link _Guides/Examples/Integrations/images/usecase-telegram-step1.png %})

### 2. Setup Telegram from participant view

Your participants can use Telegram from a participant perspective to collect data and to receive messages from you or send you messages. The procedure is quite straight-forward for participants that have signed-up:

1. Start Telegram (mobile version is best)
2. Open a new conversation with the Data Foundry bot: DATAFOUNDRYBOTNAME
3.  Type /start or click on the start button
4. Following the questions "participant" -> email address -> PIN number. The PIN number is available from the participant sign-up page that have used to accept the study. This is essentially the link that you sent to them.

![participant pin]({% link _Guides/Examples/Integrations/images/usecase-telegram-participant-pin.png %})

### 3. participant telegram pin

After the initial sign-up is completed, the participants can collect data: either they can send diary entries with /diary directly into the diary dataset, or take pictures and upload them with /photo (note: it's one picture or photo at a time, not multiples). Finally, they can also send their current location with /location, which is collected in a movement dataset (if you have added that to your project). If the photo or diary entry submission fails, always check if you have activated the "open participation" option in the dataset settings.

Participants can also send you a message with /message. This message will be available from the "manage resources" page of your project. If you have installed and signed up for Telegram as a researcher in the project (see below), you will receive the message as well via Telegram.
Setup Telegram from researcher view

You can use Telegram from a researcher perspective to receive messages from your participants or send them messages. The procedure is quite similar to what participants have to do:

1. Start Telegram (mobile or desktop version)
2. Open a new conversation with the Data Foundry bot: DATAFOUNDRYBOTNAME
3. Type /start or click on the start button
4. Following the questions "researcher" -> your email address -> PIN number. The PIN number is available from your profile page.

After this initial sign-up, you can use Telegram to select the active project: type /project or directly /project 1 for the first project. The number indicates the project number. Once you are "inside" a project, you can either message individual participants (type /message for a list; or directly /message 1 for the first participant) or all participants at the same time with /messageAll.

Quick recap: if you want to message just participant 3 of your second project, you would first enter the second project with /project 2, then start the message with /message 3. The list of participants in a project is available from the "manage resources" page.

This functionality is available for both project owners and collaborators, so you take turns in messaging. Also, the "manage resources" page contains a view of all Telegram conversations separated by participant. Good luck!

##### Based on:
https://data.id.tue.nl/documentation/usecase-telegram
