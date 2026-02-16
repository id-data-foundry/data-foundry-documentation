---
layout: default
title: Script Inputs
parent: Scripting
nav_order: 1
has_children: true
has_toc: false
---
# Script inputs

Scripts are triggered and receive input data. The overview figure shows that different aspects of a project, but also data from IoT and Entity datasets is brought into the script context automatically. This means, you can make use of these data when running the script. See below for some examples.

Script inputs
### Scripts and Events

Scripts react on events--either from OOCSI channels or from Telegram. For OOCSI, that means, a script listens to events on a particular channel. You can set this in the scripting view. The data of the triggering event is available from data, something like this:

```js
// fresh event data
data = {
	item1: 10,
	item2: 12.345,
	item3: true,
	item4: 'string data'
}
```
If you would want to process this data in your script, you can refer to the data object and its properties directly:

```js
// print data item
DF.print("received " + data.item4);

// check some condition in the data
if(data.item3) {
	DF.print("prototype is working fine");
} else {
	DF.print("send maintenance crew");
}
```
### Script input from OOCSI channel

To get data from an OOCSI channel, you need to enable the script for a particular channel. There is a field to enter the OOCSI channel name on the script page. Press 'enable' to let the script be triggered by events from the channel. Use 'disable' to stop this.

Everytime the script is triggered from an event on the channel, the event data will be copied into the data object and is ready to be processed.

You have seen the DF.print() function in action. This function will print any text that you specify. Also, you can call it with an object and it will print the contents of the JavaScript object formatted as a JSON string:
```js
// print data item
DF.print("all my new event data:");
DF.print(data);

```
The object serialization only works if the object is the only parameter of DF.print().

### Script input from Telegram

Instead of receiving events from OOCSI, a script can also receive Telegram messages from researchers and participants in the same project. and the messages will become available in data.message. Reply to the message directly with DF.telegramReply('response').
```js
DF.print("message: " + data.message)

// respond to message with a particular word or expression
if(data.message.contains("happy")) {
	DF.telegramReply("Great, tell me more about why you are happy.")
}
// respond to a message with an arith. expression
else if(data.message.match("[0-9+*/-]+")) {
	DF.telegramReply(eval(data.message))
}
// catch all response
else {
	DF.telegramReply("No idea, continue.")
}
```
A script that receives message data from Telegram will receive these both from participants and researchers in the project. This allows to test the script first, then roll it out for participants. If you would to craft different responses for participants and researchers, you can use the data.participant or data.researcher properties to check:

```js
if(data.participant) {
	// participant_name contains the pseudonymous participant name
	DF.telegramReply("Hi, participant " + data.participant_name)
	// participant_id contains the id that can be used to retrieve data from an entity dataset
	//DF.telegramReply("Hi, participant " + data.participant_id)
}
else if(data.researcher) {
	// researcher_name contains the researcher's name
	DF.telegramReply("Hi, researcher " + data.researcher_name)
}
```

After checking, you can access the participant_id and researcher_id properties for more information.

Note that to enable Telegram registration for participants, you need to have a Diary dataset in your project, or a Media dataset with openParticipation. Only then, your participants will get the Telegram PIN number on their participant registration pages.

When a participant uploads media, e.g., a photo, video or audio message to the Telegram bot, these media files will be saved in a Media dataset (if available in the project). Also, if there is a script connected to Telegram, this script will receive a short message about this upload: PHOTO_UPLOAD, VIDEO_UPLOAD or AUDIO_UPLOAD. You can use these messages to track participant submissions in a multi-state submissions process. The file size limit for media files is 30MB.
