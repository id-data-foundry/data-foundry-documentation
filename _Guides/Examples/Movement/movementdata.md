---
layout: default
title: Tracking Movement Data
parent: Example Projects
nav_order: 2
has_children: true
---
# Working with movement data

![Data Flow]({% link _Guides/Examples/Movement/images/usecase-movement-patterns.png %})
## WHAT YOU NEED

- Wearables for your participant that tracks GPS such as a Fitbit.
- Smart home devices/IoT prototypes that senses movement in the home
- A project created in Data Foundry, including a
    - Movement dataset
    - IoT dataset (2x)
- Participants
- Option using OOCSI
    - OOCSI connection implemented in the Java/Arduino/Python code of your IoT prototype
- Python/Processing script that uses an API from open source weather data platform, to store data via OOCSI in one of the IoT datasets

## HOW TO USE THIS
### Complete basic setup

 1. Register or login
 2. Create a new project
 3. Add a Movement dataset
 4. Add an IoT dataset
 5. Add a Linked dataset
 6. Add your participants
 7. Add the wearables to the project
 8. Add your smart home devices/IoT prototypes to the project

Collect and log sensor data in the home

Use the OOCSI network to add, retrieve, update and delete data items for the Entity dataset. This is option is available from a wide variety of platforms and technologies. A list with possible options is provided under the tab OOCSI API.

1. Connect to the OOCSI API by setting up channel namer: go to the second tab in the configuration screen
2. To create a channel, you need to provide the service name. Enter a unique channel name and click on save.
3. Copy paste the example code into your existing ESP/Arduino code and add, retrieve, update or delete a data item in the dataset. You can also do this with other platforms. Simply click on the example code of each different platform. Here is the example used for Arduino/ESP.

Change the following things in the example code to your own preferences. Based upon Arduino/ESP, these include:

```c++
// connect to OOCSI network
oocsi.connect(...);
// Replace CHANNEL by the channel that you provided above
oocsi.newMessage("CHANNEL");
// Copy paste your device id (head over to manage resources devices → and copy paste it into ‘DEVICE’)
oocsi.addString("device_id", "DEVICE");
// Optional server marker
oocsi.addString("activity", "EVENT or ACTIVITY");
// Here you can provide actual data to be stored in the dataset
oocsi.addFloat("airquality", 0.67);
oocsi.addBool("doorclosed", false);
// Send the data
oocsi.sendMessage();
```

Repeat this step for every code that is part of one the prototypes.

If all participants have given their consent for the study through the invitation email, the participants in the resources screen will turn green and be active.
Use the Movement dataset to upload GPX data

Get GPX file from your participants that recorded GPS data and upload it to Data Foundry by using the upload button in the Movement dataset.

1. Select the participants who corresponds to the data
2. Provide a description
3. Repeat this for every GPX dataset from every participant

Use a Python script with weather API to store data in IoT dataset

Use the OOCSI network to add, retrieve, update and delete data items for the Entity dataset. This option is available from a wide variety of platforms and technologies. A list with possible options is provided under the tab OOCSI API.

This use case uses an API and therefore it is important to install the request module. You can easily install the request module by inserting the following in the command line

```python
pip install request
```

Connect to the OOCSI API by setting up channel namer: go to the second tab in the configuration screen To create a channel, you need to provide the service name. Enter a unique channel name and click on save. Copy paste the example code into your existing Python code and add, retrieve, update or delete a data item in the dataset. You can also do this with other platforms. Simply click on the example code of each different platform. Here is the example used for Python

Change the following things in the example code to your own preferences. Based upon Python, these include:

Next to your other dependencies, you have to import the request model in your script. Paste the following at the top of your script

```python
import request
```

Get your data from the weather API; a possible way to do this is:

```python
request = requests.get('INSERT API TOKEN HERE')
```

Select which data you want to use for Data Foundry

Depending on how the weather data is formatted, you can parse the data, e.g. JSON data into an object in Python, which you can later use to send to Data Foundry. For on how to import JSON data via an API key in Python see: https://www.pluralsight.com/guides/importing-data-from-json-resource-with-python

Further steps for this include:

1. Setup OOCSI
2. Replace CHANNEL by the channel that you provided above
3. Include the object you just created for your weather data into the oocsi.send call.

Use the Data Export tool: Export, annotate or visualize

Go to the Data Tool and select the IoT and Media dataset of this project , and the columns of that dataset that you want to visualize, or export. Click on proceed to continue. Fill in the x and y axis You have the options to filter the data or annotate on it. Annotation might be helpful to discover new relations between for example your IoT and weather dataset. Change the color of each data column to your own preference Use sampling where needed When you are happy with the result, export the dataset by the export button, or save the visualization as an image by clicking on button with 3 dots.

For more information on the data export tool, click here.