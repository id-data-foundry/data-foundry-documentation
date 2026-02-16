---
layout: default
title: MicroPython reference
parent: Client reference
nav_order: 2
---

# Data Foundry for MicroPython

To make it easier to interact with Data Foundry from a MicroPython device, we have developed a small Data Foundry library. This allows you to easily connect and upload your first data to Data Foundry.

## 1. Initialize Connection

### main.py
Before interacting with specific datasets, you must configure your connection to Data Foundry. The main.py file is ran automatically once your microcontroller is powered on, hence this will be the file we will work in. Place the following code in your `main.py` file:

```python
# Import relevant libraries
import DataFoundry as DF
import WifiTools as WT
import secrets

# Connect to the internet
wifi = network.WLAN(network.WLAN.IF_STA)
WT.connectWifi(secrets.wifi, wifi)

# Initialize DF connection
DataFoundry = DF.DataFoundry(secrets.instance, secrets.deviceid)
```
#### secrets.py (File to store credentials)
To make sure your data is safe and you do not accidentally leak your credentials, we recommend storing all your sensitive data in a separate secrets file. This prevents you from leaking credentials when sharing your main.py code. Don't share the contents of your secrets.py file. You can easily make a secrets.py file by making a new python file on your micro-python device.
```python
# Place to store your wifi credentials
wifi = {
    "<ssid>":"<wifi-password>",
    # "<ssid2>":"<wifi-password2>",
}

# The link to your Data Foundry server without https://
instance = "<data_foundry_url>"

# The ID generated for this device in the device section of your Data Foundry project
deviceid = "<data_foundry_device_id>"
```

## 2. Setup Datasets
<details markdown="1">
<summary><b>IoT Dataset</b></summary>

##### main.py
After having successfully set up the connection to your Data Foundry instance, the following code allows you to set up a data foundry connection to an IoT dataset
```python
# Configure dataset connection
dataset = DataFoundry.IoTDataset(dataset_id, secrets.iot_dataset_token)
```

##### secrets.py
And add the folowing information to your secrets.py
```python
# The iot dataset token can be generated on the data foundry webpage of your iot dataset
iot_dataset_token = "<your_iot_dataset_token>"
```
</details>

<details markdown="1">
<summary><b>Entity Dataset</b></summary>

##### main.py
After having successfully set up the connection to your Data Foundry instance, the following code allows you to set up a data foundry connection to an Entity dataset
```python
# Configure dataset connection
dataset = DataFoundry.EntityDataset(17362, secrets.entity_dataset_token)
```

##### secrets.py
And add the folowing information to your secrets.py
```python
# The iot dataset token can be generated on the data foundry webpage of your iot dataset
entity_dataset_token = "<your_entity_dataset_token>"
```
</details>

<details markdown="1">
<summary><b>Existing Dataset</b></summary>

##### main.py
After having successfully set up the connection to your Data Foundry instance, the following code allows you to set up a data foundry connection to an existing dataset
```python
```

##### secrets.py
And add the following information to your secrets.py
```python
```
</details>

<details markdown="1">
<summary><b>AI Tools</b></summary>

#### Large Language Models
To setup a connection to the Data Foundry AI tools you can initiate a LLM. You can do this by adding the following code to your main.py and secrets.py.

##### main.py
```python
# Setup a default LLM
llm = DataFoundry.AIFoundry(aitoken)

# Example of a specific LLM model and temperature
spicy_llm = DataFoundry.AIFoundry(api_token = aitoken, model = "phi-2-chat", temperature = 2)
```

##### secrets.py
```python
# You can get your Data Foundry AI token in your Data Foundry projects settings 
aitoken = "<data_foundry_project_ai_token>"
```

</details>

## #3 Interact with Datasets

<details markdown="1">
<summary><b>IoT Dataset</b></summary>

#### Example to send data to an IoT Dataset
```python
# This code belongs in your main code
# Datasend is a regular dictionary, you can as many key:value pairs as you want
datasend = {'temperature':random.randint(0,254), "door":random.choice(["Open","Closed"])}

# Dataset.send accepts dictionary's only
dataset.send(datasend)
```
</details>

<details markdown="1">
<summary><b>Entity Dataset</b></summary>

### 🆕 Add entry to entity dataset

##### main.py
```python
# Setup data for in the database
data = {'temperature':11, "door":"closed"}

# Create a new database entry, protected by a database secret
dataset.add("database-entry-name", data, secrets.database_entry_secret)
```

##### secret.py
```python
# The database secret is a simple secret you can generate yourself to protect database entries
database_entry_secret = "<somethingrandom123>"
```

### 🧺 Get entry from entity dataset

##### main.py
```python
# Get data from database
result = dataset.get("database-entry-name", secrets.database_entry_secret)
```

##### secret.py
```python
# The database secret is a simple secret you can generate yourself to protect database entries
database_entry_secret = "<somethingrandom123>"
```

### 🔧 Edit entry from entity dataset

##### main.py
```python
# Modify database entry
modified_data = {'temperature':12, "door":"closed"}
dataset.put("database-entry-name", modified_data, database_entry_secret)
```

##### secret.py
```python
# The database secret is a simple secret you can generate yourself to protect database entries
database_entry_secret = "<somethingrandom123>"
```

### 🗑️ remove entry from entity dataset

##### main.py
```python
# Get data from database
dataset.delete("database-entry-name", secrets.database_entry_secret)
```

##### secret.py
```python
# The database secret is a simple secret you can generate yourself to protect database entries
database_entry_secret = "<somethingrandom123>"
```
</details>
