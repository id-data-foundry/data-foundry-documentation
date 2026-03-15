---
layout: default
title: ConvoScript
parent: Local AI
nav_order: 2
has_children: true
has_toc: true
---

# Composing a Convoscript
In this guide we will show you how to compose your own convoscript. Before you get started it helps to know how convoscript works, [click here to learn more about the convoscript structure.]({% link _Learning/LocalAI/ConvoScript.md %}) Additionally you will need some experience with knowing how a basic html site works, and some javascript familiarity, [Learn more about HTML here](https://developer.mozilla.org/en-US/docs/Web/HTML).

## Step 0. Create the HTML file
Create a new HTML file (e.g., `index.html`) using your text editor of choice (VS Code, Notepad, Brackets, etc.). 

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- // Here we will import relevant files -->
    </head>
<body class="container">
    <!-- // Here we will build the body of your chatbot website -->

    <script>
        document.addEventListener('DOMContentLoaded', async () => {
        // And here we will configure and initiate ConvoScript
        });
    </script>
</body>
</html> 
```

## Step 1. Importing Libraries and Stylesheets

Convoscript runs on JavaScript, this means the convoscript.js file can be easily imported into any HTML file by including the following snippet into our basic HTML file. We can put this under the `<meta>` tags between the **`<head></head>`** tags.
```html
    <!-- ConvoScript Library -->
    <script src="https://{{ site.external_base_urls.datafoundry }}/assets/js/convoscript/latest"></script>
    <!-- AI Foundry Library required to interact with large language models-->
    <script src="https://{{ site.external_base_urls.datafoundry }}/assets/javascripts/local-ai/latest/local-ai.js"></script>
```
Additionally, we want to add a nice stylesheet to make everything look pretty by posting this underneath.
```html
    <!-- PicoCSS stylesheet -->
    <link rel="stylesheet" href="https://{{ site.external_base_urls.datafoundry }}/assets/stylesheets/picoCSS/pico.min.css" />
    <link rel="stylesheet" href="https://{{ site.external_base_urls.datafoundry }}/assets/stylesheets/picoCSS/pico.colors.min.css" />
    <!-- ConvoScript specific styling (create this file to add custom styles) -->
    <link rel="stylesheet" href="convoscript.css" />
```
If you want to learn how to edit CSS files and personalise these yourself, [you can find more information here.](https://www.w3schools.com/html/html_css.asp)

## Step 2. Building the body
Now we have all libraries and stylesheets in place, we can build the body of your chatbot website. For this we will scaffold a simple interface containing the most important blocks to interact with the chatbot. We do that with the following code:

```html
<!-- this is the main chat interface -->
  <main>
    <!-- chat messages go in this section here -->
    <section id="chat" class="container">
    </section>
    <!-- assistant typing indicator which shows when the bot is typing-->
    <section class="container">
      <!-- <progress hidden id="load"></progress> -->
      <div id="load" hidden class="typing-indicator">
        <span class="dot"></span>
        <span class="dot"></span>
        <span class="dot"></span>
      </div>
    </section>
    <!-- user input section, which allows the user to interact with the bot -->
    <section id="userResponse">
      <div role="group">
        <!-- The userInput text box where messages are being typed -->
        <input id="userInput" hidden type="text" placeholder="start typing here" />
        <!-- The userInput send button -->
        <button id="btn-send" hidden class="pico-background-pumpkin-350" >
          send
        </button>
      </div>
    </section>
```

This code snippet should go in between the `<body>` tags and above the `<script>` tags.

## Step 3. Setting up your convoscript runner
Within the `<script>` tags we will set up our convoscript. To get started we will first define your AI API key, if you've done the tutorial already you know where to find this. If you haven't, then you should head to the edit settings of your Data Foundry project and generate an API key there (you can also do this later after following the tutorial). Then insert the following snippet underneath the `document.addEventListener`. 

{: .info }
The document.addEventListener function will make sure that your script only starts after everything has been loaded properly.
```js
// DEFINE API token, replace <your_api_key> with your actual api key
const api_token = "<your_api_key>";

```
After having set up the AI API keys, we can set up ConvoScript itself. We do this by creating the following convoscript constant. In this constant we define the AI API server, and what elements of the body convoscript should interact with. This should be inserted after the api key.
```js
// create ConvoScript
const convoScript = new ConvoScript({
    // SETUP CONNECTION TO DF LLM
    api_token: api_token, //your data foundry api token
    server: 'https://{{ site.external_base_urls.datafoundry }}', // optional: server (ex. "https://<data-foundry.net>")

    // CONVOSCRIPT SETTINGS
    delayTime: 500, //A delay after every message that can help distinguish incoming messages

    // SETUP CONNECTION TO THE UI/BODY
    resultElementSelector: '#chat', //the HTML element where the conversation will be placed. Should be a <section></section> element
    loadingElementSelector: '#load', //the HTML element that shows a loading icon when waiting for AI requests.
    acceptButtonElementSelector: '#btn-send', //the HTML button that is used to send user messages. Should be a <button></button> element
    inputElementSelector: '#userInput', //the HTML input element that is used by the user to give input. Should be an <input type="text"/> element
})
```

## Step 4. Writing your Convoscript
Now that all the technical details are in place, we can get started with actually writing your script. To get started, we can open a convoscript array underneath the convoscript runner like:
```js 
let script = [
// Here we will put in script blocks
];
```
In between the two square brackets is where we will be writing our script. We will do this by placing one of three conversation blocks. Let's get started by scripting our bot to give us a welcome message. To do so put the following code block between the script brackets. Here you can modify the content variable to your liking.

``` js
{
    role: "assistant", // Assistant here means that the bot will respond this
    content: "Hi! I'm here to speak to you about your hobbies. What is your favorite thing to do?"
},
```

Then after having written an opening message we should insert another block that takes into account what the user replies. We're starting off with a multiple choice question defined by the array inside the input variable. By defining a context name, we can easily store the users choice in our context file named "hobby". Here you can define the context name yourself. This code should be placed between the brackets underneath the previous block.

``` js
{
    role: "user",
    input: ["food stuff", "sport stuff", "just stuff"],
    context: "hobby"
},
```
Now if we want our chatbot to reply to the user's choice, we can embed this choice by embedding the context into the next message, such as in the following example.
``` js
{
    role: "assistant",
    content: (context) => `oh wow, I'm also into ${context.hobby()}. what specifically do you like about ${context.hobby()}?`
},
```
By changing the input to "text" we can also have the user submit text messages into the chat. Additionally we can deepen the hobby context into a more detailed context like in the following.
``` js
{
    role: "user",
    input: "text",
    context: "hobby.details",
},
```
At last, we can reply to this last message through a Large Language Model (LLM). For this we need a function role block. These function blocks can be used for various JavaScript functions, but for now we will show you how to send a message with an LLM.
```js
{
    // Define a function block
    role: 'function',
    // Select the AI type you want to make use of
    content: 'textToText',
    // Limit the amount of tokens for the response
    max_tokens: 500,
    // Query the prompt and send this
    messages: [
        { 
            role: 'user', 
            // By prompting like this, your message will appear as a response
            content: (context) => `Write a short, but raving food blog about delicious ${context.hobby.details()}. No longer than 120 words.`
        }
    ],
    // Save the message to the story context
    context: 'story'
},
```

## Step 5. Trigger the Convoscript
Starting a convoscript is quite easy; all you have to do is to post the following line after the script (outside of the brackets). You can also trigger the convoscript run in function blocks of another convoscript, making you able to daisy-chain interactions or use different branches for different answers.

```
    // run the script
    convoScript.run(script)
```

## Step 6. (Optional) Run in DataFoundry
To learn how to run your newly generated convoscript in Data Foundry, you can follow the following tutorial on your Data Foundry instance of choice! But in that case you can use your newly created file instead of the example file

{% include df-link.html text="Take the Interactive Tour" path="/tour/ai-tour" %}
