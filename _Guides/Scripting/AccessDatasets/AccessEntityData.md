---
layout: default
title: Access Entity Dataset
parent: Scripting
nav_order: 3
has_children: true
has_toc: false
---

# Access Entity dataset from script

Entity datasets are useful to store participant or device-related meta data. For instance, we could store a participant profile that is updated on all their interactions with a prototype.

```js
// get entry in device profile from entity dataset 
// (`DF.entity` selects the first entity dataset in your df project, if you want to use a specific dataset then replace this for `DF.dataset(dataset_id)`)
var profile = DF.entity.get(devices[0].id)

// print out if necessary
//DF.print(profile)

// check incoming event data for activity
if(data.x > 100 && data.y > 100) {
	profile.activity = Math.min(data.x, data.y);
} else {
	profile.activity = 0;
}

// update device profile in entity dataset
var profile = DF.entity.update(devices[0].id, profile)
```

You can test this script with the following data:

```js
var data = {
	x: 123,
	y: 148
};
```

The access functions for Entity datasets are very straight-forward: all require an id as the first argument. Retrieve an existing entry with df.entity.get(), add new entries with df.entity.add(), update existing entries with df.entity.update() and delete existing entries with df.entity.delete().

You can get all items in the Entity datasets in one go and works with them (updating them one-by-one, or deleting too old ones) by using the DF.entity.getAll() function:

```js
// get all items from first entity dataset in project
var allItems = DF.entity.getAll()
// get all items from specific entity dataset, where 2 is the dataset ID
// var allItems = DF.dataset(2).getAll()

// print array of all items
DF.print(allItems)
```
You can use the DF.entity.getAllMatching(id) function to retrieve items with a resource_id that starts with the given id:

```js
// filter by code
var code = "item_";

// get all items
var allMatchingItems = DF.entity.getAllMatching(code)

// print array of all items
DF.print(allMatchingItems)
```

Similar to the IoT dataset access, the read and write access to Entity datasets only works if your Project contains at least one Entity dataset that is currently active.
