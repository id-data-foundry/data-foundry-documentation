---
layout: default
title: Connecting Javascript
parent: Clients
nav_order: 3
---

# Connecting JavaScript

## Send data to Data Foundry via `fetch` requests

### Step 1. Project

Create or Open a DF project

### Step 2. Create an IoT Dataset

Before we can send data to Data Foundry, you first have to create or open a dataset to which you want to send the data. To do so open or create a dataset that you want to use.

### Step 3. Create device ID

To get your dataset to work you will need to create a new device ID. You get the device ID by opening the project page your dataset resides in. On the project page open the sources tab from the top bar and press the `ADD DEVICE`button to create a new Data Foundry Device. Here fill in the name of your device and continue by pressing the green ADD button. This will open the Device page on which you can find the `Reference ID` at the top of the device info section. Copy and paste this into your code, you will need this later.

### Step 4. Configure the IoT Dataset

Open the new IoT dataset and scroll down to the configuration examples. Click on the javascript example or insert the code from the example code below.

### Code Example

```javascript
var data = { ... your data goes here ... }
var jsonBody = {
	activity: 'ACTIVITY',
	source_id: 'DEVICE_ID',
	data: JSON.stringify(data)
}
fetch('https://<YOUR-DF-INSTANCE>/api/v1/datasets/ts/13000/TOKEN', {
    method: 'POST',
    mode: 'cors',
    cache: 'no-cache',
    headers: {
            'Content-Type': 'application/json'
    },
    redirect: 'follow',
    referrerPolicy: 'no-referrer',
    body: JSON.stringify(jsonBody)
});
```

### Step 5. Test

To check if everything is working try sending data to the OOCSI channel and check if the dataset table has a new data point

---

## Send data to Data Foundry through OOCSI

You can send data to Data Foundry using [OOCSI](https://oocsi.net). The websocket implementation of OOCSI is the easiest to use and can be added to any simple HTML site. 
There are two ways to use the OOCSI library, depending on your project you can decide which of the two suits you best.

### Step 1. Import OOCSI

To import the OOCSI library, you have again two choices:

#### Option 1: Use library on Data Foundry

Direct link to the library, from within the instance (this is great if you use an existing dataset for your website).
Note that this works only if the page is hosted on Data Foundry.

```html
<script src="/assets/javascripts/oocsi-web.min.js"></script>
```

#### Option 2: Use the library that is hosted externally

To import OOCSI on a website hosted anywhere else you can import it from any public data foundry instance. You can use the following code snippet but make sure to insert the URL of your Data Foundry instance.

```html
<script src="https://<LINK-TO-YOUR-DATAFOUNDRY-INSTANCE>/assets/javascripts/oocsi-web.min.js"></script>
```

#### Option 3: Use `node.js`

If you are working on a more advanced web project, you can also import the library via [NPM](https://www.npmjs.com). You can install OOCSI for node.js through NPM by running the following command in your console.

```bash
npm install oocsi
```


### Step 2. Setup IoT dataset

Before we can send data to Data Foundry, you first have to create or open a dataset to which you want to send the data. To do so open or create a dataset that you want to use. Navigate to the configuration section and select the first OOCSI stream button. Here in the text field, create an unique channel name like
`YourName/ProjectName/Channel` and press save. Now, any new data on this channel will be stored in the dataset.

### Step 3. Create device ID

To upload data to Data Foundry you will need to create a new device ID. You get the device ID by opening the project page your dataset resides in. On the project page open the sources tab from the top bar and press the `ADD DEVICE`button to create a new Data Foundry Device. Here fill in the name of your device and continue by pressing the green ADD button. This will open the Device page on which you can find the `Reference ID` at the top of the device info section. Copy and paste this into your code, you will need this later.

### Step 4.  Code Example

Then use the following code snippit to start sending data to Data Foundry. But before you do make sure to replace the OOCSI channel and the device ID for your own.

```javascript
OOCSI.connect('wss://oocsi.id.tue.nl/ws');
// send data in JSON format
// replace CHANNEL by the channel that you provided above
OOCSI.send("<YOUR-OOCSI-CHANNEL>",
	// replace DEVICE by the refId of any device in this project
	{"device_id": "<YOUR-DEVICE-ID>",
	// optional activity marker
	"activity": "EVENT or ACTIVITY",
	// provide actual data to be stored in the dataset
	"airquality": 0.67, 
	"doorclosed": false
});
```

### Step 5. Test

To check if everything is working try sending data to the OOCSI channel and check if the dataset table has a new data point
