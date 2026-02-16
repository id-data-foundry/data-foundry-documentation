---
layout: default
title: Access Project Resources
parent: Scripting
nav_order: 5
has_children: true
has_toc: false
---
# Accessing Project resources

All scripts are part of a project and you have read-access to all participants and devices in the project directly from the script. You can get the IDs, names, and configuration of participants, devices and wearables directly from two variables.


## Participants
```js
// list of participants in the project
participants = [
	{
		id: '1',
		participant_id: 'u123456789',
		name: 'P1',
		pp1: 'experiment',
		pp2: '',
		pp3: '',
		devices: [2],
		wearables: [3]
	},
	...
]
```

## Devices
```js
// list of devices in the project
devices = [
	{
		id: '2',
		device_id: 'd123456789',
		name: 'device1',
		pp1: 'experiment',
		pp2: '',
		pp3: '',
		participants: [1]
	},
	...
]
```
## Wearables
```js
// list of wearables in the project
wearables = [
	{
		id: '3',
		wearable_id: 'w123456789',
		name: 'heartrate_tracker1',
		pp1: 'experiment',
		pp2: '',
		pp3: '',
		participants: [1]
	},
	...
]
```

What can you use these for? You need the IDs when saving data ("logging") into an IoT dataset (device IDs), or a diary dataset (participant IDs). Or for sending messages, see Accessing IoT Dataset or .

In Data Foundry, participants, devices and wearables are sometimes grouped together ("all lamps of participant Bob, all gardening tools of participant Alex"). This clustering is also available from the project:

```js
// list of devices in the project
clusters = [
	{
		name: 'P1 lamps',
		participants: [1],
		devices: [2],
		wearables: [3]
	},
	...
]
```

How can you use this in a script? As a start, you can print out the ids or names of your resources. Read on to see how to log data with the id of a device.

```js
// print out id of first device in project
DF.print(devices[0].id);

// print name of first cluster in project
DF.print(clusters[0].name)

// print all participant names (using a for loop)
for(var i = 0; i < participants.length; i++) {
	DF.print(participants[i].name);
}
```
So, after this you have basically all the tools to start experimenting with resources such as participant, devices and wearables in a project.