---
layout: default
title: Files Dataset
parent: Datasets
redirect_from:
  - /Guides/Datasets/Existing/ExistingData.html
  - /Guides/Datasets/Files/FilesDataset.html
  - /Guides/Datasets/Files/filesDataset.html
nav_order: 3
has_children: true
---

# Files Dataset

The Files Dataset allows you to upload, store, download, and host arbitrary files (such as JSON, CSV, text documents, images, HTML, CSS, and JavaScript) within your project. For a conceptual overview of how the Files Dataset works, check out the [Files Dataset Overview]({% link _Learning/Datasets/DatasetsOverview/filesdataset.md %}).

{: .info}
Before getting started with this guide, make sure you have followed [Tutorial 4 - My First Data Foundry Website]({% link _Tutorials/GettingStarted/MyFirstDataFoundryWebsite.md %}), or are familiar with the basics of Data Foundry. You can also check the guide for [your specific client]({% link _Guides/Clients/index.md %}).

## Upload files to the Files Dataset

### Requirements
- Dataset ID
- Dataset API Token (generated under **Configuration &rarr; HTTP data upload**)
- Data Foundry Instance

### Python:
You can upload one or more files to a Files Dataset using Python's `requests` library by sending a `multipart/form-data` `POST` request with the field name `files`:

```python
import requests

url = "{{ site.external_base_urls.datafoundryurl }}/api/v1/datasets/files/<DATASET-ID>"
headers = {
    'api_token': '<DATASET-TOKEN>'
}

with open("path/to/your/file.json", "rb") as f:
    files = {'files': (f.name, f)}
    data = {'description': 'Uploaded via Python'}

    response = requests.post(url, headers=headers, files=files, data=data)
    if response.ok:
        print("Upload successful:", response.json())
    else:
        print(f"Upload failed with status {response.status_code}")
```

### Javascript:
The JavaScript example below shows how to upload files from a browser form or `File` / `Blob` object using the built-in `fetch` API:

```js
const uploadFile = async (datasetId, apiToken, file) => {
  const formData = new FormData();
  formData.append('files', file);
  formData.append('description', 'Uploaded via JavaScript');

  const response = await fetch(`{{ site.external_base_urls.datafoundryurl }}/api/v1/datasets/files/${datasetId}`, {
    method: 'POST',
    headers: {
      'api_token': apiToken
      // Note: Do not set Content-Type manually when sending FormData
    },
    body: formData
  });

  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }

  const result = await response.json();
  console.log('Upload successful:', result);
};
```

## Download files from the Files Dataset

### 1. Public Download (with Public Access Token)
If you have generated a token under **Configuration &rarr; CSV/JSON Download**, you can download any file in the dataset publicly without a user session:

#### Python:
```python
import requests

url = "{{ site.external_base_urls.datafoundryurl }}/datasets/files/filePublic/<FILENAME>/<PUBLIC-ACCESS-TOKEN>"
response = requests.get(url)

if response.ok:
    with open("downloaded_file.json", "wb") as f:
        f.write(response.content)
    print("Download successful")
else:
    print(f"HTTP error! status: {response.status_code}")
```

#### Javascript:
```js
const response = await fetch('{{ site.external_base_urls.datafoundryurl }}/datasets/files/filePublic/<FILENAME>/<PUBLIC-ACCESS-TOKEN>');
if (!response.ok) {
  throw new Error(`HTTP error! status: ${response.status}`);
}
const data = await response.text();
console.log('Downloaded file content:', data);
```

### 2. Authenticated Download (Logged-In Session)
When accessing files from an authenticated browser session, you can fetch the latest version of a file directly by dataset ID and filename:

```js
const fileUrl = '{{ site.external_base_urls.datafoundryurl }}/datasets/files/downloadLatest/<DATASET-ID>/<FILENAME>';
```

## Hosting a Static Website or Prototype

A Files Dataset can also serve HTML, CSS, JavaScript, and Markdown files as a live website:
1. Upload an `index.html` file (and any supporting `.css`, `.js`, or media files) to your Files Dataset.
2. Open **Configuration &rarr; Web access** on the dataset page and click **Activate web access**.
3. Optionally choose the entry-point file (defaults to `index.html`) and open or share the generated public web link.
