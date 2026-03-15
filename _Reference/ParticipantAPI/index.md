---
layout: default
title: Participant API reference
nav_order: 4
has_children: true
has_toc: false
---

# Participant API Reference

The Participant API provides a way to read and log data specific to a participant. The API is only accessible to participants who have agreed to participate in a study and have logged into their participant landing page. They are authenticated using a participant cookie.

You can find information on how to practically use the Participant API in the remote study use-case guides.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Participation Modes

There are two primary ways to access the API:

1. **Anonymous Participation**: Allows unregistered visitors to interact with the system.
2. **Registered Participation**: Restricted to pre-registered participants.

### Anonymous Participation

If you prefer anonymous participation with an uncontrolled number of participants, you need to use the following HTML blueprint to embed the API script code. Note that this requires you to specify the project ID, in which the participants should be registered: replace the <PROJECT-ID> with the numerical project ID. A second thing you need to do is you need to set the project to allow for self-sign-up of participants. You can do this on the project page under "study management". First activate study management, then tick the box "New participants can sign-up to this project".

```html
<!DOCTYPE html>
<html>
<head>
    <!-- This script loads the Participant API -->
    <script src="/api/v1/<PROJECT-ID>/anonymousParticipation.js" type="text/javascript"></script>
</head>
<body>
    <!-- The HTML body -->
    <script type="text/javascript">
        // Access the Participant API here
    </script>
</body>
</html>
```

If successful, you will always have a participant present in your HTML page, because previously unregistered visitors will be automatically assigned an anonymous participant profile with their own participant ID.

## Registered participation

If you are running a study with a limited number of (pre-registered) participants, it is better to use the following API embedding. This ensures that you can check in your custom JavaScript code whether a registered participant is visiting the site or not. Only in the first case, the full API will be available. If the visitor is not a registered participant, accessing the API methods will result in an error.

```html
<!DOCTYPE html>
<html>
<head>
    <!-- This script loads the Participant API -->
    <script src="/api/v1/participation.js" type="text/javascript"></script>
</head>
<body>
    <!-- The HTML body -->
    <script type="text/javascript">
        // Access the Participant API here
    </script>
</body>
</html>
```

## Participant-Specific API Functions

All Participant API methods can only access (i.e., read and write) data that is specific to the single participant currently browsing the page. This API cannot change or retrieve any other data. The Participant API first contains the participant ID:

```js
// the internal id of the participant (long value)
DF.participant.id
```

## Logging diary entries

The participant API first contains a flag whether it is possible to add diary entries in a Diary dataset in the project (only if the Diary dataset exists). Then you can use the diaryEntry function to store a diary entry for the current participant.

```js
// check whether there is an active Diary dataset
// and entries can be added (true, false)
DF.participant.canAddDiaryEntry

// store a diary entry with title and entry text
// (you might need to get both from a text field or text prompt)
DF.participant.diaryEntry("this is the title", "this is the diary entry itself...")

Accessing user profiles

Then, the API allows to read and write participant profiles into an Entity dataset in the project (only if the Entity dataset exists).

// store data in an Entity dataset in the project
// in an item identified by the participant id
var data = {
    // example data
    xPosition: 100,
    yPosition: 120,
    color: "blue",
    active: true
}
DF.participant.setProfile(data)

// retrieve profile data for this participant from an Entity dataset
DF.participant.getProfile(function(data) {
    // extract profile data from data (example based on data in previous example)
    // do something with the data...
    if(data.active) {
        console.log(data.color)
    }
})
```
## Accessing participant data

You can retrieve participant-related data from any dataset in the project. This means, only from datasets that can be filtered on participant ID (or a device ID that is associated to the participant).
```js
// set start and end time for filtering on time
var start = new Date('2021-02-15').getTime()
var end = new Date('2021-03-15').getTime()

// retrieve participant data from the dataset with ID 2, filtered by start and end time in CSV format
DF.participant.getDataCSV(2, start, end, function(data) {
    console.log(data);
})

// retrieve participant data from the dataset with ID 2, filtered by start and end time in Json format
DF.participant.getDataJson(2, start, end, function(data) {
    console.log(data);
})

// retrieve data without filtering either by using -1 for the time values
DF.participant.getDataCSV(2, -1, -1, function(data) { ... })

// or by taking the time filtering out of the function call
DF.participant.getDataCSV(2, function(data) { ... })
```
## Device-specific API functions

There are two functions of the API that are more related to the web page they are currently visiting than themselves. Therefore these two functions are sorted under DF.device.
Logging data

Since a participant might be in the same cluster as a device, this API also allows to log data on behalf of this one device that is directly linked to a participant. If there is no device linked to a participant ("in the same cluster as participant"), then this functionality will not be available for that participant.

```js
// check whether there is an active IoT dataset
// and data items can be logged (true, false)
DF.device.canLogData

// log data for this participant's associated device,
// that is, a single device in the same cluster as the participant
var data = {
    xPosition: 450,
    yPosition: 540,
    color: 'blue',
    active: true
}
DF.device.logData(data, 'some activity')

// or in one line:
DF.device.logData({xPosition: 450, yPosition: 540, color: 'blue', active: true}, 'some activity')
```
## Uploading images

You can upload canvas graphics as images for participants. You need to provide the canvas image data as a "Blob" to the uploadImage function and the image will be rendered and stored as a .png file.

```js
// check whether there is an active Media dataset
// and data images can be uploaded (true, false)
DF.device.canUploadImage

// let's assume you have a <canvas> element in the HTML somewhere with id="mycanvas"
const canvas = document.getElementById('mycanvas');

// render canvas as a blob and upload it to media dataset
canvas.toBlob(function(blob) {
    DF.device.uploadImage(blob);
});
```

You can find a full example with the anonymous participation option below. Don't forget to replace <PROJECT-ID> with the correct project ID.

```html
<!DOCTYPE html>
<html>
    <head>
        <!-- this script loads the anonymous Participant API -->
        <script src="/api/v1/<PROJECT-ID>/anonymousParticipation.js" type="text/javascript"></script>
    </head>
    <body>
        <!-- the HTML body -->
        <canvas id="mycanvas"></canvas>

        <!-- scripting -->
        <script type="text/javascript">
        // create a canvas with a green rectangle
        const canvas = document.getElementById('mycanvas');
        const ctx = canvas.getContext('2d');
        ctx.fillStyle = 'green';
        ctx.fillRect(10, 10, 150, 100);

        // check if the participant can upload images
        // this is checking whether there is a media dataset and it can be accessed
        if(DF.device.canUploadImage) {
            // render canvas as a blob and upload it to media dataset
            canvas.toBlob(function(blob) {
                DF.device.uploadImage(blob);
            });
        }
        </script>
    </body>
</html>

```
