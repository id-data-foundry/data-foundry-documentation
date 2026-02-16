---
layout: default
title: Access IoT Dataset
parent: Scripting
nav_order: 2
has_children: true
has_toc: false
---

# Access IoT dataset from script

Although we can store data automatically from an OOCSI channel with IoT datasets, we can use scripts to process the data before inserting into a dataset. We can also compute extra values (mean, standard deviation, etc.). Let's see how this works:

```js
// use the event and add more data
data.roundedXValue = Math.round(data.x)
data.roundedYValue = Math.round(data.y)

// log an event with new data
DF.eventData.log(devices[0].id, '', data)

// in addition: change activity based on values (if greater 100)
if(data.X > 100 && data.y > 100) {
	DF.eventData.log(devices[0].id, 'running', data)
} else {
	DF.eventData.log(devices[0].id, 'walking', data)
}
```
Storing data into an IoT dataset always follows the pattern: id, activity, data, see above.

Note that scripting access for IoT datasets only works if there is at least one IoT dataset available and active in your project. 'Active' means that the dataset has a start date before today and an end date in the future.

## How to retrieve event data from IoT dataset?
Use the function DF.eventData.get() to retrieve most recent events for an IoT dataset.

```js
// retrieve up to 20 (default) most recent events
var iot = DF.eventData.get('')
DF.print(iot.length)

// retrieve up to 20 (default) most recent events for the first device
var iot1 = DF.eventData.get(devices[0].id)
DF.print(iot1.length)

// retrieve up to 2 most recent events for the first device
var iot2 = DF.eventData.get(devices[0].id, 2)
DF.print(iot2.length)
```

With this access to event data, we could, for instance, compute the mean over the last 10 events and use this somehow.

```js
// retrieve up to 10 most recent events for the first device
var iot = DF.eventData.get(devices[0].id, 10)

// loop through items and compute mean
var result = 0;
for(var i = 0; i < iot.length; i++) {
	// incrementally compute the mean by summing values divided
	// by the total number
	result += iot[i].value1/iot.length;
}
DF.print("mean: " + result);
```
Note that at this moment, only the first active IoT dataset can be accessed in scripts

{: .todo }
Add section on how to specify dataset