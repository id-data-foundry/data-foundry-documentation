---
layout: default
title: Scripts
nav_order: 1
has_children: true
has_toc: false
---

# What are Data Foundry Scripts?
Data Foundry scripts are a powerful tool to tie all your datasets together and make it easier to automate your research. Scripts are based on Javascript and allow you to interact with all of your projects datasets. Data Foundry scripts can be triggered through both oocsi and telegram. Allowing you to respond to incoming messages as they pour in. Data Foundry scripts can be added to any Data Foundry project, just like datasets, and open a small code editor in which you can write and edit your scripts. Here you can also assign an oocsi channel which the script will tap into. Scripts have access to all of your datasets by default, this makes it easy to create complex workflows. Additionally scripts can make use of the Data Foundry AI api, allowing you to instantly transcribe, moderate or rephrase incoming data.

## Triggering events
Scripts can also be used to trigger events based on incoming data. Maybe you want to send out a telegram message when the airquality drops below a certain threshold. Or as a research you might want to receive a notification when your participants fill out a survey or complete a task. More complex usecases can for example be an oocsi powered chatbot That has access to all the recently submitted data of a participant, without sharing access to the entire dataset. 

## Labeling Data
As scripts do not just have access to all incoming data but is also able to create new datapoints itself. You can use scripts to identify and label data based on certain criteria. For example you could insert qualitative data labels in real-time when you spot a certain data pattern. For example in the use-case of tracking phone charging data, this allows you to add an extra datapoint to indicate your phone started charging when the chargers voltage changes from 0 to 5 volt. This makes your data easier to interpret and analyze manually, and can give you an advantage in data interviews.

## Data Transformation
Scripts can also be used to transform data in real-time. For example you could use a script to convert temperature data from Celsius to Fahrenheit. Or you could use a script to calculate the average of a set of data points. This makes it easy to create complex workflows that can be triggered by incoming data. Additionally scripts can make use of the Data Foundry AI api, allowing you to instantly transcribe, moderate or rephrase incoming data. As scripts can also save data to datasets, this makes it possible to use the scripts as an intemediary step between the devices generating the data and the dataset storing the data.
