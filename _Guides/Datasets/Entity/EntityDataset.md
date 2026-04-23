---
layout: default
title: Entity Dataset
parent: Datasets
nav_order: 3
has_children: true
---

# Entity Dataset
The Entity Dataset allows you to store and retrieve structured data items associated with a resource identifier. For more information on the Entity dataset check out the [Entity Dataset documentation]({% link _Learning/Datasets/DatasetsOverview/entitydataset.md%}).
{: .info}
Before getting started with this guide, make sure you have followed [Tutorial 1]({% link _Tutorials/GettingStarted/MyFirstDataLogger.md%}), or are familiar with the basics of Data Foundry. You can also familiarize yourself by following the guide for [your specific client]({%link _Guides/Clients/index.md %}).

## Import libraries

You might need to install a library to make the Python code work. We need `requests` for retrieving the data and the easiest is to enter the following on the command line (where you also run Python):

```bash
pip install requests
```

## Requirements
- Dataset ID
- Dataset Token
- Resource ID
- Resource Token
- Data Foundry Instance

## Add a data item to the dataset

### Python:
```python
# Import requests library
import requests

# API endpoint
URL = "{{ site.external_base_urls.datafoundryurl }}/api/v1/datasets/entity/<DATASET-ID>"

# Use dict for headers to be sent to the API
HEADERS = {
    'api_token': '<DATASET-TOKEN>',
    'resource_id': '<RESOURCE-ID>',
    'token': '<RESOURCE-TOKEN>'
}

# Use dict for data items to be stored by the API 
PARAMS = {'data_item1': 'DATA 1', 'data_item2': 12.5} 

# Post request 
r = requests.post(url=URL, headers=HEADERS, json=PARAMS)
print(r)
```

### Javascript:
```js
// API endpoint
const URL = "{{ site.external_base_urls.datafoundryurl }}/api/v1/datasets/entity/<DATASET-ID>";

// Headers to be sent to the API
const HEADERS = {
    'api_token': '<DATASET-TOKEN>',
    'resource_id': '<RESOURCE-ID>',
    'token': '<RESOURCE-TOKEN>',
    'Content-Type': 'application/json'
};

// Data items to be stored by the API 
const PARAMS = {'data_item1': 'DATA 1', 'data_item2': 12.5}; 

// Post request 
fetch(URL, {
    method: 'POST',
    headers: HEADERS,
    body: JSON.stringify(PARAMS)
}).then(response => {
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    console.log('Data item added successfully');
});
```

## Get a data item from the dataset

### Python:
```python
# Import requests library
import requests

# API endpoint
URL = "{{ site.external_base_urls.datafoundryurl }}/api/v1/datasets/entity/<DATASET-ID>"

# Use dict for headers to be sent to the API
HEADERS = {
    'api_token': '<DATASET-TOKEN>',
    'resource_id': '<RESOURCE-ID>',
    'token': '<RESOURCE-TOKEN>'
}

# Get request 
r = requests.get(url=URL, headers=HEADERS, json={})
print(r.json())
```

### Javascript:
```js
// API endpoint
const URL = "{{ site.external_base_urls.datafoundryurl }}/api/v1/datasets/entity/<DATASET-ID>";

// Headers to be sent to the API
const HEADERS = {
    'api_token': '<DATASET-TOKEN>',
    'resource_id': '<RESOURCE-ID>',
    'token': '<RESOURCE-TOKEN>'
};

// Get request 
fetch(URL, {
    method: 'GET',
    headers: HEADERS
}).then(response => {
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
}).then(data => {
    console.log('Data item:', data);
});
```

## Update a data item in the dataset

### Python:
```python
# Import requests library
import requests

# API endpoint
URL = "{{ site.external_base_urls.datafoundryurl }}/api/v1/datasets/entity/<DATASET-ID>"

# Use dict for headers to be sent to the API
HEADERS = {
    'api_token': '<DATASET-TOKEN>',
    'resource_id': '<RESOURCE-ID>',
    'token': '<RESOURCE-TOKEN>'
}

# Use dict for data items to be stored by the API 
PARAMS = {'data_item1': 'DATA 1 v2', 'data_item3': True} 

# Put request 
r = requests.put(url=URL, headers=HEADERS, json=PARAMS)
print(r)
```

### Javascript:
```js
// API endpoint
const URL = "{{ site.external_base_urls.datafoundryurl }}/api/v1/datasets/entity/<DATASET-ID>";

// Headers to be sent to the API
const HEADERS = {
    'api_token': '<DATASET-TOKEN>',
    'resource_id': '<RESOURCE-ID>',
    'token': '<RESOURCE-TOKEN>',
    'Content-Type': 'application/json'
};

// Data items to be stored by the API 
const PARAMS = {'data_item1': 'DATA 1 v2', 'data_item3': true}; 

// Put request 
fetch(URL, {
    method: 'PUT',
    headers: HEADERS,
    body: JSON.stringify(PARAMS)
}).then(response => {
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    console.log('Data item updated successfully');
});
```

## Delete a data item from the dataset

### Python:
```python
# Import requests library
import requests

# API endpoint
URL = "{{ site.external_base_urls.datafoundryurl }}/api/v1/datasets/entity/<DATASET-ID>"

# Use dict for headers to be sent to the API
HEADERS = {
    'api_token': '<DATASET-TOKEN>',
    'resource_id': '<RESOURCE-ID>',
    'token': '<RESOURCE-TOKEN>'
}

// Delete request 
r = requests.delete(url=URL, headers=HEADERS, json={})
print(r)
```

### Javascript:
```js
// API endpoint
const URL = "{{ site.external_base_urls.datafoundryurl }}/api/v1/datasets/entity/<DATASET-ID>";

// Headers to be sent to the API
const HEADERS = {
    'api_token': '<DATASET-TOKEN>',
    'resource_id': '<RESOURCE-ID>',
    'token': '<RESOURCE-TOKEN>'
};

// Delete request 
fetch(URL, {
    method: 'DELETE',
    headers: HEADERS
}).then(response => {
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    console.log('Data item deleted successfully');
});
```
