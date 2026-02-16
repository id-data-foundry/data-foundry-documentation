---
layout: default
title: Access any Dataset
parent: Scripting
nav_order: 4
has_children: true
has_toc: false
---

# Reading data from ANY dataset

Data Foundry also supports reading from any dataset in a project, regardless of its type. This can be handy in looking up data, processing data from multiple datasets in a script and structuring datasets in such a way that not all information needs to be kept in a single dataset.

Ok, how to do that? The first step is to select the dataset to read from:

```js
// select dataset with dataset ID, here the dataset has the ID 2
DF.eventData.from(2)
```

Based on this selection, we use get to retrieve items from the dataset. The get method can take four arguments: device ID, limit, start, end. The first one allows to filter the data by a specific participant, device or wearable. So, this ID relates to the type of dataset: for example, IoT datasets can be filtered by devices, Diary and Media datasets can be filtered by participants, and Fitbit and GoogleFit datasets can be filtered by wearables. In the following example, we use an IoT dataset and filter by a device:

```js
// device ID can be from the devices in the project
// here first device in project
DF.eventData.from(2).get(devices[0].id)

// device ID can be an empty string
DF.eventData.from(2).get('')

// by the way, this is how you print the results to check:
var items = DF.eventData.from(2).get('')
DF.print(items)

// or like this:
DF.print(DF.eventData.from(2).get(''))
```

The second argument for get gives the maximum number of records returned. So, we can safely return the last n items in a larger dataset.

```js
// limit the number of items to max. 4 (can be less)
DF.eventData.from(2).get('', 4)
```
The final two arguments for get allow for filtering the dataset by time. The third argument start is the start time of the filtering and the second end the end time. The results between start and end will be returned.

```js
// retrieve max. 20 items without filtering for device or time
DF.eventData.from(2).get('', 20)

// filter results for the timeframe February 15 - March 15, 2021
var start = new Date('2021-02-15').getTime()
var end = new Date('2021-03-15').getTime()
DF.eventData.from(2).get('', 20, start, end)
```
You can also leave start or end open to return all results before or after a time. The default value for the time filter is -1.

```js
// -1 is the default value for the time filtering
DF.eventData.from(2).get('', 20, -1, -1)

// filter results for the time before February 15
DF.eventData.from(2).get('', 20, -1, start)

// filter results for the time after March 15
DF.eventData.from(2).get('', 20, end)

// or:
DF.eventData.from(2).get('', 20, end, -1)
```
