---
layout: default
title: Media Dataset
parent: Datasets
nav_order: 2
has_children: true
---

# Media Dataset
The Media Dataset allows you to upload and download images. For more information on the Media dataset check out the [Media Dataset documentation]({% link _Learning/Datasets/DatasetsOverview/mediadataset.md%}).
{: .info}
Before getting started with this guide, make sure you have followed [Tutorial 1]({% link _Tutorials/GettingStarted/MyFirstDataLogger.md%}), or are familiar with the basics of Data Foundry. You can also familiarize yourself by following the guide for [your specific client]({%link _Guides/Clients/index.md %}).

## Upload images to the Media Dataset

### Requirements
- Dataset ID
- Dataset Token
- Participant ID (optional), depends on if you enabled open participation or not.
- Data Foundry Instance

### Python:
To get started with uploading images to the Media Dataset through Python, you can use the built-in `requests` library. This makes it easy to get started quickly without any additional dependencies. 

Before you get started, make sure you have created a dataset and obtained the `Dataset ID` and `Dataset Token`.

```python
# Import requests library
import requests

# Your actual file path
file_path = "path/to/your/image.jpg"

# Open file in binary mode
with open(file_path, 'rb') as f:
    files = {'file': (f.name, f)}
    
    # Post request 
    response = requests.post(
        "https://{{ site.external_base_urls.datafoundry }}/api/v1/datasets/media/<DATASET-ID>",
        headers={
            'api_token': '<DATASET-TOKEN>',
            'participant_id': 'PARTICIPANT_ID'  # optional
        },
        files=files
    )
    print(response)
```

### Javascript:
The JavaScript example below shows how to upload images to the Media Dataset using the `fetch` API. This is all built-in so you don't need any additional libraries.

Before you get started, make sure you have created a dataset and obtained the `Dataset ID` and `Dataset Token`.

```js
// Get form element
const myform = document.querySelector('#myform');
const formData = new FormData(myform);

fetch('https://{{ site.external_base_urls.datafoundry }}/api/v1/datasets/media/<DATASET-ID>', {
    method: 'POST',
    headers: {
        'api_token': '<DATASET-TOKEN>',
        'participant_id': 'PARTICIPANT_ID'  // optional
    },
    body: formData
}).then(response => {
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    console.log('Upload successful');
});
```

## Download images from the Media Dataset

### Requirements
- Dataset ID
- Dataset Token
- Participant ID (optional)
- Filename
- Data Foundry Instance

### Python:
To download an image from the Media Dataset through Python, you can use the built-in `requests` library.

```python
# Import requests library
import requests

# Download request
response = requests.get(
    "https://{{ site.external_base_urls.datafoundry }}/api/v1/datasets/media/<DATASET-ID>/<FILENAME>",
    headers={
        'api_token': '<DATASET-TOKEN>',
        'participant_id': 'PARTICIPANT_ID'  # optional
    }
)

if response.ok:
    # Save image to file
    with open('downloaded_image.jpg', 'wb') as f:
        f.write(response.content)
    print('Download successful')
else:
    print(f"HTTP error! status: {response.status}")
```

### Javascript:
The JavaScript example below shows how to download images from the Media Dataset using the `fetch` API.

```js
// Download function
const downloadFile = (id, imageElementId) => {
  const response = fetch('https://{{ site.external_base_urls.datafoundry }}/api/v1/datasets/media/<DATASET-ID>/<FILENAME>', {
    headers: {
      'api_token': '<DATASET-TOKEN>',
      'participant_id': id
    }
  });

  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }

  const imageBlob = await response.blob();
  const imageObjectURL = URL.createObjectURL(imageBlob);

  const imgElement = document.getElementById(imgElementId);
  imgElement.src = imageObjectURL;
};

// Use it
const participantId = 'PARTICIPANT_ID'; // looks like: u1234567890abcdef
downloadFile(participantId, '#imageElement');
```
