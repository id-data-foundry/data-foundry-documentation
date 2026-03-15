---
layout: default
title: Connecting Processing
parent: Clients
nav_order: 2
---

# Connecting Processing

## Send direct HTTP requests

{: .info}
You will need the OOCSI library to send data to Data Foundry directly, even when not using OOCSI

### Step 1. install the OOCSI library

To install the OOCSI library open the processing library manage. You can find this at the top bar under `sketch > Import Library.. > Manage Libraries..` Then search for `oocsi` and install the `OOCSI for Processing` package published by Mathias Funk.

### Step 2. Import Data Foundry library

After having imported the OOCSI library you can import Data Foundry by adding the following line of code at the top of your processing code.

```java
import nl.tue.id.datafoundry.*;
```

### Step 3. Create/Setup IoT dataset

Before we can send data to Data Foundry, you first have to create a dataset to which you want to send the data. After creating or opening a dataset Copy the `Token` as set in the HTTP-POST configuration section. Additionally copy the `Dataset ID` which can be found above the token or in the info block on the top right. Paste both values into your code so that you can retrieve them in step 5.

### Step 4. Create device ID

Other than the Dataset ID and Token, you will also need to create a new device ID. You get the device ID by opening the project page your dataset resides in. On the project page open the sources tab from the top bar and press the `ADD DEVICE`button to create a new Data Foundry Device. Here fill in the name of your device and continue by pressing the green ADD button. This will open the Device page on which you can find the `Reference ID` at the top of the device info section. Copy and paste this into your code, you will need this later.

### Step 5. Setup Code

After having imported the Data Foundry library, we can set up the code to send new data to data foundry. Use the following example code, and make sure to replace the Dataset ID, Token and Device ID.

```java
// fill in the Data Foundry server URL, just the domain (add port if needed)
DataFoundry df = new DataFoundry("{{ site.external_base_urls.datafoundry }}");
// create dataset access
DFDataset iot = df.dataset("<Dataset ID>", "<Token>");
// log activity to IoT dataset
iot.device("<Device ID>").activity("ACTIVITY").log();
// same example, but with additional data ("temperature" and "door")
iot.device("d1234567890").activity("indoor_climate").data("temperature", 34).data("door", "open").log();

```

---

## Use OOCSI for Processing

### Step 1. Install the OOCSI library

To install the OOCSI library open the processing library manage. You can find this at the top bar under `sketch > Import Library.. > Manage Libraries..` Then search for `oocsi` and install the `OOCSI for Processing` package published by Mathias Funk.

### Step 2. Import Data Foundry library

After having imported the OOCSI library you can import Data Foundry by adding the following line of code at the top of your processing code.

```java
import nl.tue.id.datafoundry.*;
```

### Step 3. Setup IoT dataset

Before we can send data to Data Foundry, you first have to create or open a dataset to which you want to send the data. To do so open or create a dataset that you want to use. Navigate to the configuration section and select the second OOCSI stream button. Here in the text field, create an unique channel name like
`YourName/ProjectName/Channel` and press save. Now when new data enters this dataset, the data will be streamed to this OOCSI channel!

### Step 4. Create device ID

Other than the Dataset ID and Token, you will also need to create a new device ID. You get the device ID by opening the project page your dataset resides in. On the project page open the sources tab from the top bar and press the `ADD DEVICE`button to create a new Data Foundry Device. Here fill in the name of your device and continue by pressing the green ADD button. This will open the Device page on which you can find the `Reference ID` at the top of the device info section. Copy and paste this into your code, you will need this later.

### Step 5. Setup Code

Now, you can just use OOCSI in Processing to send messages to Data Foundry and store data in a dataset.

```java
// replace CLIENT_HANDLE by a unique name for your prototype or IoT device
OOCSI oocsi = new OOCSI(this, "CLIENT_HANDLE", "{{ site.external_base_urls.oocsi }}");
// replace CHANNEL by the channel that you provided above
oocsi.channel("<YourName/ProjectName/DeviceName>")
	// replace DEVICE by the refId of any device in this project
	.data("device_id", "<YOUR-DEVICE-ID>")
	// optional activity marker
	.data("activity", "EVENT or ACTIVITY")
	// provide actual data to be stored in the dataset
	.data("airquality", 0.67)
	.data("doorclosed", false)
	// don't forget to send
	.send();
```

## More examples

https://github.com/edenchiang/PlayWithDataFoundry/tree/master/examples/Processing_with_OOCSI
