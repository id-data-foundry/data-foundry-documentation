---
layout: default
title: IoT Dataset
parent: Datasets
nav_order: 1
has_children: true
---

# IoT Dataset
The IoT Dataset is one of the most common dataset in Data Foundry. It allows you to upload any type of time series data. For more information on the IoT dataset check out the [IoT Dataset documentation]({% link _Learning/Datasets/DatasetsOverview/iotdataset.md%}).

{: .info}
Before getting started with this guide, make sure you have followed [Tutorial 1]({% link _Tutorials/GettingStarted/MyFirstDataLogger.md%}), or are familiar with the basics of Data Foundry. You can also familiarize yourself by following the guide for [your specific client]({%link _Guides/Clients/index.md %}).

## Upload data to the IoT Dataset

### Requirements
> - **Dataset ID**
> - **Dataset Token**
> - **Device ID**
> - **Data Foundry Instance**

### Python:
To get started with uploading data to the IoT Dataset through Python, you can use the built-in `requests` and `json` libraries. This makes it to get started quickly without any additional dependencies. 

Before you get started, make sure you have created a dataset and obtained the `Dataset ID` and `Dataset Token`. Additionally you need to create a device and copy the `DeviceID` for the `SourceID`.

```python
# Import requests and json libraries
import requests
import json

# Your actual data
data = {
    "Temperature":45,
    "RoomName":"living room"
    # ... your data goes here ...
}

# Metadata, what device is uploading and when
jsondata = {
    "source_id": "DEVICE_ID",
    "activity": "ACTIVITY",
    "data": json.dumps(data)
}

# Post request 
response = requests.post("{{ site.external_base_urls.datafoundryurl }}/api/v1/datasets/ts/<DATASET-ID>/<DATASET-TOKEN>", json=jsondata)
print(response)
```

### Javascript:
The JavaScript example below shows how to upload data to the IoT Dataset using the `fetch` API. This is all built-in so you don't need any additional libraries. we also have a library 

Before you get started, make sure you have created a dataset and obtained the `Dataset ID` and `Dataset Token`. Additionally you need to create a device and copy the `DeviceID` for the `SourceID`.

```js
var data = { ... your data goes here ... }
var jsonBody = {
    activity: 'ACTIVITY',
    source_id: 'DEVICE_ID',
    data: JSON.stringify(data)
}

fetch('{{ site.external_base_urls.datafoundryurl }}/api/v1/datasets/ts/<DATASET-ID>/<DATASET-TOKEN>', {
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

### Java / Processing:
To upload data using Java / Processing, you can use the Data Foundry Java library. You can download this library though the processing library manager. 

{: .warning}
The Data Foundry library is part of the **OOCSI for processing** library. You will have to install this library before you can use it.

```java
// import the library
import nl.tue.id.datafoundry.*;
// fill in the Data Foundry server URL, just the domain (add port if needed)
DataFoundry df = new DataFoundry("{{ site.external_base_urls.datafoundrydomain }}");
// create dataset access
DFDataset iot = df.dataset(98, "<DATASET-TOKEN>=");
// log activity to IoT dataset
iot.device("<DEVICE_ID>").activity("ACTIVITY").log();
// example with DEVICE_ID = "d1234567890" and ACTIVITY = "indoor_climate"
iot.device("d1234567890").activity("indoor_climate").log();
// same example, but with additional data ("temperature" and "door")
iot.device("d1234567890").activity("indoor_climate").data("temperature", 34).data("door", "open").log();
// log new data, reuse the dataset access with device and activity set already:
iot.data("temperature", 32).data("door", "closed").log();
```

### Command Line:

```bash
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "source_id=<DEVICE_ID>&activity=ACTIVITY&data=DATA" {{ site.external_base_urls.datafoundryurl }}/api/v1/datasets/ts/<DATASET_ID>/<DATASET-TOKEN>
```

### Upload data in bulk to the IoT Dataset

```python
import csv
import requests

# Define the filename
csvfilename = "./mycsvfile.csv"
url = "{{ site.external_base_urls.datafoundryurl }}/api/v1/datasets/ts/<DATASET_ID>/<DATASET-TOKEN>
```datasets/ts/logFile/20435"

headers = {
    'Content-Type':'text/plain',
    "device_id": "DEVICE_ID",
    "api_token": "DATASET_TOKEN",
}

# Upload values to DF
print('*** Starting upload...')
with open(csvfilename, 'r') as csvfile:
    csv_content = csvfile.read()

response = requests.post(url, headers=headers, data=csv_content, timeout=30)

print('*** DATAFOUNDRY: Status code:', response.status_code)
print('*** DATAFOUNDRY: Response:', response.text)

# Only clear the file if upload was successful
if response.status_code in (200, 201, 202):
    # Remove values (except header) from CSV
    with open(csvfilename, "w") as resetfile:
        resetfile.write("ts,humidity,temperature\n")

    print('*** Upload successful - file cleared')
else:
    print('*** Upload failed with status code:', response.status_code)

```
