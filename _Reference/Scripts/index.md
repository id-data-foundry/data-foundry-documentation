---
layout: default
title: Scripting reference
nav_order: 5
has_children: true
has_toc: false
---

# Scripting Function Reference

You can use the following functions in Data Foundry scripts to interact with datasets, participants, and external services.

<details markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## General Functions

### DF.print()
Prints text to the console or an object as JSON.

```js
// Print text
DF.print("Some text to print out on the console");

// Print an object as JSON
var data = {one: 1.2, two: 'wow!'};
DF.print(data);
```

## IoT Datasets

{: .warning }
These functions access the first active IoT dataset in the project if a specific dataset is not selected. Replace `.eventData` for `.dataset(<Dataset-ID>)` if you want to work with a specific dataset.

### .dataset()
Selects a specific dataset to write to.

```js
// Select dataset with ID 2, then log data to it
let data = { ... };
DF.dataset(2).log(devices[0].id, 'running', data);

// Or retrieve data from dataset.
DF.dataset(2).get(42, 200);
```

### .get()
Retrieves event data from a device. When using DF.eventData, it will automatically select the first IoT dataset in the project.

#### Get data from any device
```js
// Get event data from any device by providing an empty device ID string
let items = DF.eventData.get('');
// Get event data collected by any device from dataset 2
let items = DF.dataset(2).get('');
```

#### Get data from specific device
If you want to collect data from a specific Data Logger you can do so by putting the DeviceID in the request.
```js
// Get event data from device 42
let items = DF.eventData.get(42);
// Get event data collected by device 42 from dataset 2
let items = DF.dataset(2).get(42);
```

#### Get the last 200 items collected by specific device
If you want to only get the last 200 items collected by a device, you can add a second parameter specifying how many entries you want.
```js
// Get the last 200 items collected by device 42 from the first IoT dataset in your project
let items = DF.eventData.get(42, 200);
// Get the last 200 items collected by device 42 from dataset 2
let items = DF.dataset(2).get(42, 200);
```

#### Get 200 items collected by any device
If you want to only get the last 200 items collected by any device, you can also add a second parameter specifying how many entries you want.
```js
// Get the last 200 items from the first IoT dataset in your project
let items = DF.eventData.get('', 200);
// Get the last 200 items from dataset 2
let items = DF.dataset(2).get('', 200);
```

#### Get 200 items collected by device between start and end-time
If you only want to collect data collected within a certain timeframe, you can add a start and end date

```js
// Get the last 200 items collected by device 42, filtered by start and end time
// The start and end date should be submitted in unix epoch (milliseconds) format

// one minute (= 60 000 milliseconds) ago
let start = Date.now() - 60 * 1000;
// one day ago
// let start = Date.now() - 24 * 60 * 60 * 1000;
// right now
let end = Date.now();

let items = DF.eventData.get(42, 200, start, end);
// Get the last 200 items collected by device 42 from dataset 2, filtered by start and end time
let items = DF.dataset(2).get(42, 200, start, end);
```

### .log()
Adds a data item to the dataset.

```js
// Log data for device 42, with an activity and data to the first dataset in your project
var data = {one: 1.2, two: 'wow!'};
DF.eventData.log(42, 'cooking activity', data);

// Log to a specific dataset, with 2 as dataset ID
DF.dataset(2).log(42, 'cooking activity', data);
```

## Entity Datasets

{: .warning }
These functions access the first active entity dataset in the project if a specific dataset is not selected.

### .getAll()
Retrieves all items from an entity dataset.

```js
let items = DF.entity.getAll();
```

### .get()
Retrieves a specific entity dataset item.

```js
// Get item with resource ID 'user1'
let item = DF.entity.get('user1');
```

### .add()
Adds an item to an entity dataset.

```js
var data = {one: 1.2, two: 'wow!'};
DF.entity.add('user1', data);
```

### .update()
Updates an existing entity dataset item.

```js
var data = {one: 1.2, two: 'wow!'};
DF.entity.update('user1', data);
```

### .delete()
Deletes an item from an entity dataset.

```js
DF.entity.delete('user1');
```

## Advanced Data Retrieval

You can access any dataset by ID and filter results.

```js
// Get last 200 items from dataset 100 within a timeframe
// The start and end date should be submitted in unix epoch (milliseconds) format
let items = DF.eventData.from(100).get('', 200, start, end);

// Filter by device ID
let items = DF.eventData.from(100).get(42, 200, start, end);
```

## Statistics and Filtering

### .stats()
Calculates simple statistics over one or more columns.

```js
// Stats for a single column
let st = DF.dataset(15).stats('value1');

// Stats for multiple columns
let st = DF.dataset(15).stats(['value1', 'value2']);
```

### .filter()
Filters data before calculating statistics.

```js
// Filter for specific device and limit to last 40 items
let st = DF.dataset(15).filter('d1234567', 40).stats('value1');
```

## Project Resources

### .getParticipant()
Retrieves a participant by ID.
```js
let p = DF.getParticipant('u12345678abcdef');
```

### .getDevice()
Retrieves a device by ID.
```js
let d = DF.getDevice('d123456abcdef');
```

### .getWearable()
Retrieves a wearable by ID.
```js
let w = DF.getWearable('w123456abcdef');
```

## External Services

### OOCSI
Sends a message to an OOCSI channel.
```js
var data = {one: 1.2, two: 'wow!'};
DF.oocsi('channelName', data);
```

### Telegram
Sends messages to researchers or participants via Telegram.

```js
// Notify researchers
DF.telegramResearchers('Someone completed a survey');

// Message a specific participant
DF.telegramParticipant('u12345678abcdef', 'Thanks for the data!');

// Reply to an incoming message
DF.telegramReply('Message received, thank you.');
```
