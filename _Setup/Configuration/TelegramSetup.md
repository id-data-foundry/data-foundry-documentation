---
layout: default
title: Telegram Bot Setup
parent: Configuration
nav_order: 4
---

# Setup Telegram Bot
To get started with the Data Foundry telegram bot functionality, youll first need to request a Data Foundry api token. To do so follow the steps below.

## Step 1. Download the telegram app
<br>
[Telegram Website](https://telegram.org/apps){: .btn}
It is preferable to do this on your phone as this makes it easier to create an account

## Step 2. Create a telegram account
To make a telegram account you need a phone number, follow the steps in the app

## Step 3. Start a chat with @botfather
Now to request a telegram Bot API token, follow the instructions below.
![Create chat]({% link _Setup/Configuration/assets/BotFather5.jpg %}){:width="30%"}
![Decline permissions]({% link _Setup/Configuration/assets/BotFather4.jpg %}){:width="30%"}
![Search for accounts]({% link _Setup/Configuration/assets/BotFather3.jpg %}){:width="30%"}
![Search and select Botfather]({% link _Setup/Configuration/assets/BotFather2.jpg %}){:width="30%"}
![Start Chat]({%link _Setup/Configuration/assets/BotFather1.jpg %}){:width="30%"}
![New bot]({% link _Setup/Configuration/assets/BotFather0.jpg %}){:width="30%"}
![Configure bot and copy token]({% link _Setup/Configuration/assets/BotFather6.jpg %}){:width="30%"}

## Step 5. Copy and Insert API Key
In `conf/application.conf`, configure your Telegram bot username and token under `df.telegram`:

```hocon
df {
    telegram {
        bot_name = "your_bot_username"
        bot_token = "1111111111:aaa_aaaaaaaaaaaaaaaaaa-aaaaaaaaaaa"
    }
}
```