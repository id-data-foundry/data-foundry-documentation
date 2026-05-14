---
layout: default
title: Structured Output and Tools
parent: Local AI Reference
nav_order: 1
---

# Structured Output and Tool Calling

When you want the AI to do more than just "chat", you can use **Structured Output** and **Tool Calling**. These features allow you to get data in a specific format (like JSON) or give the AI the ability to "interact" with your code.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## 1. Structured Output (`responseFormat`)

Sometimes you need the AI to return data that your program can easily understand, like a list of items, a configuration, or a specific set of values. Instead of just asking the AI to "output JSON" in the prompt (which it might sometimes fail to do correctly), you can enforce a **JSON Schema**.

### What is a JSON Schema?

A JSON Schema (sometimes called a "JS Schema" or simply a "Blueprint") is a way to describe the structure of data. It tells the AI exactly:
1. What **keys** (property names) should be in the JSON (e.g., `brightness`, `color`).
2. What **type** of data each key should hold (e.g., a number, a string, a boolean).
3. Which keys are **required** and cannot be missing.

#### Beginner Example
If you want the AI to pick a random color and give you its name and Hex code, your "blueprint" (schema) would describe an object with two strings.

### Using it in JavaScript
In the `local-ai.js` library, you pass this schema inside the `responseFormat` parameter.

```javascript
const response = await foundry.textToTextWithUsage({
  api_token: "YOUR_API_KEY",
  prompt: "Pick a random warm color.",
  // Use responseFormat to force the AI to follow your blueprint
  responseFormat: {
    type: "json_schema", 
    json_schema: {
      name: "color_picker",
      strict: true, // Forces the AI to strictly follow the schema
      schema: {
        type: "object",
        properties: {
          name: { type: "string", description: "The name of the color" },
          hex: { type: "string", description: "The hex code, e.g. #FF5733" }
        },
        required: ["name", "hex"],
        additionalProperties: false // Don't allow the AI to add extra keys
      }
    }
  }
});

// The result in response.text will be a valid JSON string
const data = JSON.parse(response.text);
console.log("Color Name:", data.name);
console.log("Hex Code:", data.hex);
```

---

## 2. Tool Calling (`tools`)

Tool calling (also known as "Function Calling") allows you to give the AI "powers" or "capabilities". You describe your own JavaScript functions to the AI, and the AI can decide to "call" them when it needs to perform a specific action.

### How it Works
1. **Define the Tools**: You provide a list of functions, explaining what they do and what parameters they need (using the same JSON Schema format).
2. **AI Decides**: The AI looks at the user's request. If it thinks one of your tools can help, it returns a **tool call** instead of a normal text message.
3. **You Execute**: Your code detects the tool call, runs your actual JavaScript function with the arguments provided by the AI, and then uses the result.

### Example: A Lighting Assistant
Suppose you have a function that sends commands to smart lights. You can tell the AI about it:

```javascript
// 1. Define the tool(s)
const myTools = [
  {
    type: "function",
    function: {
      name: "setLightLevel",
      description: "Sets the brightness of the room lights",
      parameters: {
        type: "object",
        properties: {
          level: { type: "number", description: "Brightness from 0 to 100" }
        },
        required: ["level"]
      }
    }
  }
];

// 2. Send the request
const response = await foundry.textToTextWithUsage({
  api_token: "YOUR_API_KEY",
  messages: [
    { role: "system", content: "You are a room lighting assistant." },
    { role: "user", content: "It's a bit too dark in here." }
  ],
  tools: myTools,
  toolChoice: "auto"
});

// 3. Handle the tool call
if (response.toolCalls && response.toolCalls.length > 0) {
  const call = response.toolCalls[0];
  if (call.function.name === "setLightLevel") {
    const args = JSON.parse(call.function.arguments);
    console.log("Setting lights to:", args.level); // The AI might pick 70 or 80
    // Actually call your light-setting code here!
  }
}
```

---

## Which one should I use?

| Use **Structured Output** when... | Use **Tool Calling** when... |
| :--- | :--- |
| You want the *final answer* to be data (e.g., a JSON object). | You want the AI to *do something* (e.g., send a message, search a database). |
| You are building a data processing tool. | You are building an interactive assistant or a "smart" prototype. |
| You want to guarantee the response is JSON. | You want the AI to decide *if* and *when* to use a specific capability. |

---

## See it in Action
- [Example 14: Structured Output]({% link _Guides/LocalAI/examples/example14.html %})
- [Example 15: Tool Calls]({% link _Guides/LocalAI/examples/example15.html %})
