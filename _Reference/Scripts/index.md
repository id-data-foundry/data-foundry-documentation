---
layout: default
title: Scripting reference
nav_order: 5
has_children: true
has_toc: false
---

# Scripting Function Reference

You can use the following functions in Data Foundry scripts to interact with datasets, participants, and external services.

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
These functions access the first active IoT dataset in the project if a specific dataset is not selected.

### .dataset()
Selects a specific dataset to write to.

```js
// Select dataset with ID 2, then log data to it
let data = { ... };
DF.dataset(2).log(devices[0].id, 'running', data);
```

### .get()
Retrieves event data from a device.

```js
// Get event data from device 42
let items = DF.eventData.get(42);

// Get the last 200 items
let items = DF.eventData.get(42, 200);

// Filter by start and end time
let items = DF.eventData.get(42, 200, start, end);
```

### .log()
Adds a data item to the dataset.

```js
// Log data for device 42, with an activity and data
var data = {one: 1.2, two: 'wow!'};
DF.eventData.log(42, 'cooking activity', data);
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

