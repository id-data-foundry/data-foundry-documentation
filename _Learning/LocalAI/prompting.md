---
layout: default
title: Model Categories
parent: Data Foundry AI
nav_order: 2
---

# Prompting

By taking this output object apart, we get the resulting text "Flowers for a global audience." (*Note that the output can differ when you try it.*), `finishReason` which gives you an idea about why GPT stopped generating tokens ("stop" is usually good, meaning that GPT's output was not cut off by a token limit), and the rough `cost` of the operation.

You can get just the text by using 

````Javascript
DF.print(result.text)
````

Another example is to generate text like an explanation:

````Javascript
let result = DF.api("localai", {
  "api_token": "<API-KEY>", 
  "task": "completion",
  "prompt": "Explain the difference between apples, oranges and pears for a primary school kid."
})
DF.print(result)
````

Result: 

````json
{"text":"\n\nApple, orange and pear are fruits. Apples are the most common type of fruit eaten whole. O oranges are the most common type of fruit eaten peeled and sectioned. Pears are the most common type of fruit eaten peeled and sectioned.","finishReason":"stop","cost":69}
````

Weird? Let's try again:

````json
{"text":"\n\nApples are red and have a crispy skin. Oranges are orange and have a juicy skin. Pears are green and have a squishy skin.","finishReason":"stop","cost":50}
````

We can change the prompt: "Explain the difference between apples, oranges and pears to a six year old child."

````json
{"text":"\n\nApples are round with a smooth skin and are bright red or green. Oranges are oval with a bumpy skin and are usually orange but can also be yellow or brown. Pears are also oval but are usually smooth, can be green or red and are a bit juicier than apples.","finishReason":"stop","cost":81}
````
