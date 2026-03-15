---
layout: default
title: Wearables
parent: Integration Examples
nav_order: 2
has_children: true
has_toc: false
---

# Wearable Examples

Data Foundry supports collecting data from consumer wearable devices to track health, movement, and activity metrics. These examples guide you through connecting these devices to your project.

## Supported Devices

*   **Fitbit:** Connect Fitbit accounts to access steps, heart rate, sleep, and activity data.
*   **Google Fit:** (Note: Legacy support, verify API availability) Connect Android phones and WearOS watches.
*   **Apple Watch:** Connect via third-party bridges or custom iOS apps.

# What you need for this how-to guide

Users must have a wearable dataset (e.g, Fitbit or Google Fit dataset) and there is at least one participant in the project.

## Preparation steps:

1. Wearables of Data Foundry need to be added to target project:
    - Add a new wearable directly with the hyperlink `"ADD WEARABLE"` inside the tab `"WEARABLES"` on the `"MANAGE RESOURCES"` page of your project.
    - Make sure the wearable and the participant, which are going to link to each other, are added into the same cluster before starting to link. And there must be only one participant in the cluster, then Data foundry will group them together and the participant can see the wearable on participation page.
2. Connect Data Foundry wearables to physical ones:
    - Click the `"MANAGE RESOURCES"` button on the project page and click on `"PARTICIPANTS"` tab in the right side column of `"MANAGE PROJECT RESOURCES"` page.
    - By clicking on a participant on the screen will be redirected to a participant page. Users can use the `"SEND LINK TO PARTICIPANT" `button to invite the participant via email.
    - Participants can link wearables on the participation page by clicking the wearables with yellow background. The background of the wearable will turn to green after finishing linking up the Data Foundry wearalbe and physical wearable.
3. What is important for this linking to work, is that participants should synchronize their data manually everyday. This might be a lot to ask, thus there is a way to this quick and easy: (For Fitbit wearable only)

## Fitbit settings

Fitbit wearables require one more step for syncing easily:

1. Go to your Fitbit app/dashboard
2. Get into your account
3. Choose your wearable device
4. Scroll down and find "All-Day Sync", and turn it on
5. Keep the Fitbit app open in the background

## Points for Google Fit wearables and Apple Watch devices

1. Data Foundry always fetches the data of yesterday in the evening of the day, which means data of yesterday will be fetched around 11:00 P.M. today.
2. Try to sync your data every day. But if you forget or have no time for few days to do so, it is totally no problem because Data Foundry will sync your data from last time you synced your data til yesterday. For example, I forgot to sync my data for three days, from this Monday to Wednesday, and I synced my data on Thursday (before the fetching time of Data Foundry of course), Data Foundry will fetch the data of this Monday to Wednesday (yesterday) in the evening of Thursday (today).
3. How to sync data?
    - Google Fit wearables - Just open the Google Fit app and wait.
    - Apple Watch - Check here

https://github.com/edenchiang/PlayWithDataFoundry/tree/master/examples/Apple_to_GoogleFit
