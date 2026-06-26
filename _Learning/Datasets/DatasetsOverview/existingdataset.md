---
layout: default
title: Existing Dataset
parent: Datasets
has_children: true
has_toc: false
---

# Existing Dataset (File Repository)

The Existing Dataset is a flexible and powerful file repository, designed to store any collection of files related to your project. Think of it as a dedicated hard drive for your study, where you can upload, organize, and manage a wide variety of documents, data files, images, and source code. Its primary purpose is to serve as a general-purpose storage solution that can also function as a self-contained website. Files in this dataset are accessible to the project owner, collaborators and subscribers. If the project is a public project, then the files will also be accessible to guests.

The dataset provides a user-friendly interface for managing your files. You can upload individual files, entire folders, or even create new, empty text files directly within the browser. For each file, a set of contextual actions is available, such as downloading, deleting, and, for text-based files, editing them with a built-in code editor. A particularly powerful feature is its ability to serve its contents as a static website. If you upload HTML, CSS, and JavaScript files, you can configure the dataset to make them publicly accessible as a fully functional website.

## Configuring an Existing Dataset

Configuring an Existing Dataset is primarily about managing its function as a file repository and web host. The "Configuration" section on the dataset page provides the following options:

*   **Web Access:** In this tab, you can activate or disable public web access to the dataset. Activating it generates a unique, tokenized public URL, effectively turning your file collection into a browse-able website.
*   **Web Access Entry Point:** When web access is active, this setting allows you to designate a specific uploaded file (e.g., an `index.html` page) as the landing page or entry point for your website.
*   **CSV/JSON Download:** This tab allows you to generate a public URL (with an access token) to download a CSV or JSON file containing a list of metadata about all the files uploaded to the dataset.
*   **Forward data to OOCSI:** Here, you can specify an OOCSI channel to forward metadata about newly uploaded files, allowing other systems to be notified of changes.

## Use Cases for Web Hosting

The ability to serve a collection of files as a website opens up many possibilities for presenting your project and data. Here are a few examples:

*   **Project Website or Portfolio:** You can create a simple and effective website to showcase your project's goals, team members, and outcomes. Upload your HTML, CSS, and image files, set an `index.html` as the entry point, and you have a public-facing site.

*   **Interactive Data Visualizations:** If your project involves data analysis, you can use libraries like [p5.js](https://p5js.org), [D3.js](https://d3js.org), or [Observable Plot](https://observablehq.com/plot/) to create rich, interactive visualizations. Upload your visualization code along with the necessary data files (e.g., CSV, JSON), and your audience can explore the data directly in their browser.

*   **Sharing Interactive Prototypes:** For design and engineering projects, you can share functional web-based prototypes. This allows stakeholders to experience and interact with your work in a realistic environment, providing more effective feedback than static images.

*   **Flexible Content Presentation:** The "entry point" does not have to be a traditional `index.html` file. You could set a Markdown file (`.md`) as the entry point to present a formatted document, or even a specific image or video file if that's the primary content you want to share. This flexibility allows you to tailor the presentation to your specific needs. You can even switch the entry point between different files to, for example, show different versions of a prototype.

## Project website

You can use the existing dataset also to host a project website for your project. How to do this? Just name the dataset "www" and upload your HTML, JS, CSS and image files into the dataset. If you go back to the project page, you will see a link "Project website" next to the project title. Click this link to see the project website. Note that the project needs to be public to show the project website.

## File Upload/Download API

The Existing Dataset provides a programmatic API for uploading and downloading files.

### 1. Generating an API Token
Before using the API, you must generate a token. Open the dataset configuration in the Data Foundry GUI, navigate to the **HTTP data upload** tab, and click **Generate** next to the token field.

### 2. HTTP POST File Upload
You can upload one or more files to the dataset by sending a `POST` request to the following API endpoint:

`POST /api/v1/datasets/existing/<DATASET_ID>`

#### Headers
*   `api_token`: Your generated API token.

#### Body (Multipart Form Data)
*   `files`: The file or files to be uploaded.
*   `description`: (Optional) A description to associate with the uploaded files.

#### Examples

##### Javascript
```javascript
const uploadFile = async (datasetId, apiToken, file) => {
  const formData = new FormData();
  formData.append('files', file);
  formData.append('description', 'Uploaded via API');

  const response = await fetch(`https://your-datafoundry-url/api/v1/datasets/existing/${datasetId}`, {
    method: 'POST',
    headers: {
      'api_token': apiToken
    },
    body: formData
  });

  if (response.ok) {
    const result = await response.json();
    console.log("Success:", result);
  }
};
```

##### cURL
```bash
curl -X POST \
  -H "api_token: YOUR_API_TOKEN" \
  -F "files=@/path/to/local/file.json" \
  -F "description=Uploaded via cURL" \
  "https://your-datafoundry-url/api/v1/datasets/existing/DATASET_ID"
```

##### Python
```python
import requests

url = "https://your-datafoundry-url/api/v1/datasets/existing/DATASET_ID"
headers = {
    'api_token': 'YOUR_API_TOKEN'
}
files = {'files': open('file.json', 'rb')}
data = {'description': 'Uploaded via Python'}

response = requests.post(url, headers=headers, files=files, data=data)
if response.status_code == 200:
    print("Success:", response.json())
```

### 3. File Download
There are two ways to download files programmatically:

#### A. Public Download (No Authentication)
If your dataset has public web access enabled, you can download files publicly using the tokenized file download route. In this route, the dataset ID is **not** included in the URL because it is derived directly from the token:

`GET /datasets/existing/filePublic/<FILENAME>/<PUBLIC_ACCESS_TOKEN>`

##### Example (cURL)
```bash
curl -O -J \
  "https://your-datafoundry-url/datasets/existing/filePublic/file.json/YOUR_PUBLIC_ACCESS_TOKEN"
```

#### B. Direct Download (Requires User Session/Cookie)
If you are running in a browser environment where the user is logged in, you can download the latest version of a file directly using the dataset ID:

`GET /datasets/existing/downloadLatest/<DATASET_ID>/<FILENAME>`

##### Example (cURL with Session Cookie)
```bash
curl -O -J \
  -b cookies.txt \
  "https://your-datafoundry-url/datasets/existing/downloadLatest/DATASET_ID/file.json"
```

