---
layout: default
title: Processing reference
parent: Client reference
nav_order: 1
---

# Data Foundry for Processing and Java

This library allows you to interact with Data Foundry from Processing or any Java-based environment.

## General Setup

### Importing Relevant Libraries
```java
// import the library
import nl.tue.id.datafoundry.*;
import java.util.Map;
```

### Connect to Data Foundry Instance
```java
// fill in the Data Foundry server URL, just the domain (add port if needed)
DataFoundry df = new DataFoundry("server.url.com");
```

## IoT Dataset

### Connect to an IoT Dataset
```java
// create dataset access
DFDataset iot = df.dataset(2, "tokentokentokentokentoken1234567890+++");
```

### Add Data to an IoT Dataset
```java
// log to IoT dataset
iot.device("d123456789").activity("indoor_measurement").data("temperature", 34).data("door", "open").log();
```

## Entity Dataset

### Connect to Dataset (Entity)
```java
// create dataset access
DFDataset entity = df.dataset(15, "tokentokentokentokentoken1234567890+++");
```

### Access Item from an Entity Dataset
```java
// access specific item
DFDataset item = df.dataset(15, "tokentokentokentokentoken1234567890+++").id("userX").token("nosecrets");
```

### Add Item to Entity Dataset
```java
// add an item
item.data("temperature", 34).data("door", "open").add();
```

### Retrieve Item from Entity Dataset
```java
// get an item
Map<String, Object> itemData = item.get();
```

### Retrieve Nested Item from Entity Dataset
```java
Map<String, Object> nestedItem = (Map<String, Object>) itemData.get("key/value");
```

### Update an Item in Entity Dataset
```java
// update an item
item.data("temperature", 32).update();
```

### Remove Item from Entity Dataset
```java
// delete an item
item.delete(); 
```