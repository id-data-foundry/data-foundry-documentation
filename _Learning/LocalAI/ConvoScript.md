---
layout: default
title: ConvoScript
nav_order: 2
parent: Data Foundry AI
has_toc: false
---
# How does ConvoScript work

Convoscript is library that makes it easier to compose a chatbot conversation website, by allowing you to script everything out beforehand. Not only does it allow you to create scripted chatbots, but it also has thorough integration with Data Foundry LocalAI, allowing you to leave some parts unscripted! This flexibility between going on and off script, combined with clever context saving, poses a powerful tool to script out structured chatbot interactions. It even has the ability to interact with OOCSI devices.

## ConvoScript components
A ConvoScript chat webpage consists of 3 main elements:
1. The body (usually a html webpage)
2. The mind (a javascript function initializing the ConvoScript library and setting up the AI connection)
3. a script (The script for your conversation flow)


### The body:
The body of a ConvoScript website is where the user interacts with your chatbot. This usually a simple HTML file containing all the basic building blocks, libraries and a css stylesheet to make everything look pretty. The html file should also contains the javascript that will run the brain. 

### The Brain:
The brain is where all the magic happens, which is were the ConvoScript library itself runs. This runs inside of the javascript section of the body and allows you to configure your chatbot.

### The Script
The script is where you define the conversation flow of your chatbot. Here you can script out what the chatbot responds on a message by message. 

#### Structure:
The scripts are store on a message by message in a [JSON structure](https://www.w3schools.com/whatis/whatis_json.asp). Every message has their own properties and is stored in a script block, this makes it easy to create an overview of all the messages. Convoscript automatically cycles between all steps and waits for user input when requested.

```js
let script = [
    { /*script block 1*/ },
    { /*script block 2*/ },
    { /*script block 3*/ }
]
```

#### Roles
Every script block can contain one of 3 types of messages, defined by the role property. These all have different functionalities
1. **Assistant responses**, these are scripted messages sent by the assistant, they contain 
```js
{
    role: "assistant",
    // Content allows you to script a message
    content: "Hi! I'm here to speak to you about your hobbies. Press the button to start chatting."
},
```
2. **User input**, by scripting these you can easily save the user responses as context. This means that later in the conversation you can refer to these messages as context. This creates a structured way of storing user replies, that is easy retrieve.
```js
{
    role: "user",
    // What kind of input will this user submit?
    input: "text",
    // How will this context be saved
    context: "hobby"
},
```
3. **Functions**, functions allow you to plan in functions during the conversation. This can be used to for example request responses from Large Language Models, for unscripted replies. By planning these functions out in the script, you can easily time when in the conversation these functions are executed
```js
{
    role: 'function',
    // What kind of function are you providing
    content: 'textToText',
    // How long should the message be
    max_tokens: 500,
    // What are you sending
    messages: [
        // Provide a system prompt here (this will not be shown)
        { role: "system", content: "You are a helpful agent with an interest in design research and ethnography. You provide great bulleted summaries."},
        // Provide a prompt
        { 
            role: 'user', 
            // This way of notating (content: (context) =>) means save the llm reply to this prompt into the context. This will make it show up as a reply
            // ${context.get("hobby")} allows you to embed earlier saved user responses into the prompt.
            content: (context) => `Summarize the story in less than 30 words: ${context.get("hobby")}`
        }
    ]
},
```

#### Load a script

After creating a script, you can easily start the script by loading it into the ConvoScript function like:
```js
    // run the script
    convoScript.run(script)
```
This also means you can make 1 ConvoScript function run multiple scripts,. For example by making certain responses trigger other scripts.

Now you know the structure of a ConvoScript, [click here to learn how you can compose your own ConvoScript.]({% link _Guides/LocalAI/convoscript/index.md %})
