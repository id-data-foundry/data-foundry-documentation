---
layout: default
title: Connecting Python
parent: Clients
nav_order: 1
---

# Connecting Python

With Python we have two options to send data to Data Foundry and one option to download it (we will also show you how to work it). Let's check this out.

## Use Python to *send* data

### Step 1. Create/Setup IoT dataset

Before we can send data to Data Foundry, you first have to create a dataset to which you want to send the data. After creating or opening a dataset Copy the `Token` as set in the HTTP-POST configuration section. Additionally copy the `Dataset ID` which can be found above the token or in the info block on the top right. Paste both values into your code so that you can retrieve them in step 5.

### Step 2. Create device ID

Other than the Dataset ID and Token, you will also need to create a new device ID. You get the device ID by opening the project page your dataset resides in. On the project page open the sources tab from the top bar and press the `ADD DEVICE` button to create a new Data Foundry Device. Here fill in the name of your device and continue by pressing the green ADD button. This will open the Device page on which you can find the `Reference ID` at the top of the device info section. Copy and paste this into your code, you will need this later.

### Step 3. Send data

Open the new IoT dataset and scroll down to the configuration examples. Click on the Python example or insert the code from the example code below.

### Example code

```python
# import requests library
import requests
# API endpoint
URL = "https://<YOUR-DF-INSTANCE>/api/v1/datasets/ts/<dataset_id>/<dataset_token>"
# use dict for parameters to be sent to the API
DATACONTENT = {'source_id':'DEVICE_ID', 'activity': '<ACTIVITY>', '<data_name>': '<DATA>', '<data_name_2>': '<DATA_2>'}
# post request
r = requests.post(url = URL, params = DATACONTENT)
```

---

## Use Python to *download* data

### Configuring IoT Dataset for download
Open the IoT dataset and scroll down to the configuration examples. Press the third tab labelled CSV/JSON export, and look at the Python examples.

### Import Python libraries

You might need to install a few libraries to make the Python code work. We need requests for retrieving the data, and pandas and matpotlib for working with the data in Python.

```python
## import libraries: requests, pandas as pd, matplotlib as plt
# https://pandas.pydata.org/
# https://matplotlib.org/
import requests, pandas as pd, matplotlib as plt
```

### Download csv file from the dataset

```python
## Replace URL with the TOKEN LINK that you generate in the dataset. Replace FILENAME as the name you want.
## Get and save as csv file
# API endpoint
URL = "TOKEN LINK generated in the dataset"
FILENAME = "file_name.csv"
# fetch file
r = requests.get(URL, verify=False)
# save result as a csv in current folder
open(FILENAME, 'wb').write(r.content)
```

### Visualize the data from a csv file with a bar chart

```python
# read csv file
# if there are too many rows (>50) in the file, use head(rows) to control the rows of data to be read
# ex. for reading first 10 rows, df = pd.read_csv('file_name.csv').head(10)
df = pd.read_csv('file_name.csv')
# draw the bar chart
df.plot(kind='bar')
```

### Get some statistics data by a specific column

```python
# read data with first 25 rows
df = pd.read_csv('file_name.csv').head(25)
# get column names of the csv file
df.columns
# show the first 5 rows
df.head()
# group the data by the value of 'column_name'
allocation_display = df.groupby('column_name')
# summary statistics for all numeric columns by column_name
allocation_display.describe()
```

---

## Use OOCSI for Python to *send* data

Other than being able to send data to Data Foundry directly, you can also choose to use our middleware OOCSI. This middleware has plenty of different clients. Let's look at the Python client.

### Step 1. Install OOCSI

To install the OOCSI library you first have to install OOCSI for Python. You can do this by running the following command.

```bash
pip install oocsi
```

## Stream Data Foundry data to an OOCSI channel!

Sometimes its easiest to get an OOCSI message with new data right as it gets uploaded to Data Foundry, for example when a telegram message is received. In this case you can make sure that all new dataset data is streamed into an OOCSI channel.

### Step 2. Project

Open or Create a project

### Step 3. Setup Dataset

Open or create a dataset that you want to use. Navigate to the configuration section and select the second OOCSI stream button. Here in the text field, create an unique channel name like `YourName/ProjectName/Channel` and press save. Now when new data enters this dataset, the data will be streamed to this OOCSI channel!

### Step 4. Receive Data from OOCSI

## Use OOCSI for Python to send data to Data Foundry!

Another way to send data to data foundry is through OOCSI, this is handy if yoou also want to send the data to another OOCSI client at the same time.

### Step 2.

Open or Create a project

### Step 3. Setup Dataset

Open or Create a dataset that you want to use. Navigate to the configuration section and select the first OOCSI stream button. Here in the text field, create an unique channel name like `YourName/ProjectName/Channel` and press save. Now all OOCSI messages in this channel will be saved to the dataset!

### Step 4. Setup Code

Now to send the data to the `YourName/ProjectName/Channel` channel we have to set up the OOCSI Python client. to set up OOCSI:

```python
# Import the OOCSI library
from oocsi import OOCSI

# Setup your OOCSI device name and point it towards an OOCSI server only has to happen once
oocsi = OOCSI('YourName/ProjectName/DeviceName', 'oocsi.example.com')
```

After having OOCSI set up you can then use the following command to send data to an OOCSI channel:

```python
# Use this snippit to send data to an OOCSI channel
oocsi.send('<YourName/ProjectName/Channel>', {'data': 120, 'data2':'test'})
```
