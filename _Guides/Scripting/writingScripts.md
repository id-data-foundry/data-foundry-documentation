---
layout: default
title: Get Started with Scripts
parent: Scripting
nav_order: 0
has_children: true
has_toc: false
---
# Writing your own scripts
Writing scripts might be quite intimidating at first as it adds yet another abstraction layer on top of Data Foundry. However, with a bit of practice and patience, you'll find that it's actually quite easy to write scripts for Data Foundry, which will take your project to the next level. Let's get started with your introduction to Data Foundry scripting. 

## Step 1: Creating your first script:
To create your first script, you'll first need to have a Data Foundry project to work in. After having opened or created a Data Foundry project, it will be hard to miss the create new script button on the main page, which is located right under the create new dataset button. Click on it to create your first script! This will take you to the script editor, where you can start writing your first script. 

## Step 2: Interacting with incoming data
Because Data Foundry Scripts are always triggered by either an oocsi or telegram message every script is triggered with a message object. This message object includes access to the incoming data, which can be accessed using the `data` property. For example, if you want to access the `temperature` property sent with the incoming data, you can use `data.temperature`. This allows you to easily interact with the incoming data. 

you can preview this data through the testing tab, which is located to the right of the script editor below the information pane. Here you can test your script by emulating the incoming data. You can configure this yourself by changing up the data in the testing pane. To send the data, all you have to do is press the green test button.

to see what data arrives, you can add this function to your script:
```javascript
DF.print(data)
```
This will print out all `data` values underneath the test button, like:
![testing pane]({% link _Guides/Scripting/images/TestingPane.png %})

## Step 3. Sending LLM requests
After having received data, you can process this with a large language model directly from Data Foundry. This can be done with the DF.api functionality. After collecting an API token in the project settings, you can use the following code to do a small text2text request to our local-ai:

```javascript
// Create an empty message context
let context = [];

// Add a system prompt to the context, including the the username and message provided by oocsi
context.push({
  role: 'system',  // Change to 'role' and make it 'user' to ask the question
  content: `You are DFBot a short and concise chatbot. Respond with a chat message to the following message: ${data.message} by ${data.username}`
});

// Send the request to the local-ai, replace <api-key>, with the api-key generated in the project settings
let result = DF.api("localai", {
  "api_token": "<api-key>", 
  "task": "chat",
  "messages": context
});

// Preview the request text
df.print(result.content)
```

## Step 4: Logging data into Data Foundry
To send data back to Data Foundry, you can use the `DF.eventData.log` function. This function takes three arguments: the device ID, the event name, and the event data. For example, if you want to log a temperature alert for a device with ID, you can use the following code:

**Here the:**
1. **data.device_id** is used to tie this to a logging device
2. **'temperature_alert'** is the activity name
3. **The last value** is a JSON object containing the values you want to add to a dataset.

```javascript
DF.eventData.log(data.device_id, 'temperature_alert', {temperature: data.temperature});
```

This will upload the data to the first dataset in your project. If you want to upload the data to a specific dataset, you will have to replace eventData with `.dataset(<dataset_id>)`. This will allow you to set the id of the dataset you want the data to be uploaded. This would look like
```javascript
DF.dataset(dataset_id).log(devices[0].id, 'running', data);
```

If you dont want to use a device ID you can also insert an empty string in there like this. This will upload the data without any device ID, but for this to work the dataset must have Open Participation enabled.
```javascript
DF.eventData.log('', 'temperature_alert', {temperature: data.temperature});
```

## Step 5: Sending data back through oocsi
Sometimes you want to send data back through oocsi. For example to use the LLM reply in your user interface or on your other prototypes. This is quite easy as all you have to do for this is to call the `DF.oocsi()` function. This function takes two arguments: the channel name and the message. For example, if you want to send a message to the chatbot channel, you can use the following code:
```javascript
DF.oocsi("chatbot", reply);
```

This is all that is needed to get started with Data Foundry Scripts. You now know how to receive data from oocsi, modify this with an LLM, log it to Data Foundry and send it back through oocsi! You can now start building your own scripts and automating your data processing.
