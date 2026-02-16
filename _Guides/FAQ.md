---
layout: default
title: FAQ
redirect_from:
  - /faq
nav_order: 8
has_toc: false
---

# Frequently asked questions (FAQs)

## About Data Foundry

### General

Q: What is the access code?

A: You don't need an access code, if your Data Foundry instance is using Single-Sign-On for authentication, that means, that you log in with your organization's username and password on a different website (usually for students or staff).

---

Q: The project page and dataset pages are not visible to guests, how come?

A: Please check that the project is public (--> project edit, bottom of form).

---

Q: How can I delete projects or datasets?

A: We believe that open science needs openness about methods and how we achieve results. So, Data Foundry does not allow for deleting projects or datasets. However, you can archive projects to de-clutter your list of active projects. Try to finish the meta-data for the project before archiving, so others can learn from you and your way of working.

---

Q: Can I host a project website on the Data Foundry?

A: Yes, see the reference here.

---

Q: How can I find the participation page?

A: On project page
→ click [MANAGE RESOURCES]
→ find and click the target participant from the list inside "PARTICIPANTS" tab
→ the invitation link is the URL of participation page, click [OPEN LINK] to open the page with a new tab. \

Only the participants in suspend / accept status have participation page like this:

participation page

---

### IoT & OOCSI

Q: My dataset cannot receive information, what can I do?

A: Always check that the dataset is active and (for some dataset types such as IoT datasets) you had checked the option openParticipation on its edit page. This setting allows any device to send data to the dataset, not only devices which are registered in your project.

---

Q: My IoT dataset does not store data, something is broken?

A: Always check that the dataset is active, that means, the start date of the project is before today and the end data is after today. The next thing to check is that the device id that you use in the sending of data corresponds to a registered device in the project. Alternatively, you can allow any device to post data: ensure that the dataset is switched to openParticipation. This setting allows for any device to send data to the dataset, not just devices that are registered in your project.

---

Q: My devices seems to have stopped logging data, what should I do to check?

A: If you are using OOCSI to stream, check whether the device can connect to an OOCSI server (Internet connection? Did your device use a unique handle to connect to OOCSI? Do you have "deep sleep" issues with the device?) and can send data properly. You can check this also by running a Processing client that subscribes to the channel that you are sending device data on. If all fails, email us (see address above).

---

Q: How many events can I stream via OOCSI (per second)?

A: about 2

---

Q: How to use an OOCSI channel on the Data Foundry for uploading data?

A: Please find the CONFIGURATION block on the dataset page, and check the OOCSI STREAM tab with a cloud icon, which has an upward arrow inside it. Enter the channel name you want to use for the channel and save it!

---

#### OOCSI channel upload setting

Q: Can I forward the incoming data to another OOCSI channel? How?

A: Yes, all you need to do is set the channel name for the OOCSI service inside the tab "OOCSI STREAM" (with downward arrow). As data are added in the dataset (via both http-token and OOCSI), new events will be generated and sent to the OOCSI channel.

---

#### Forwarding incoming data to OOCSI channel

Q: How can I check my data sending to OOCSI channel?

A: You can check your data sending to OOCSI channel by subscribing to the OOCSI channel on OOCSI UI client page

---

#### Check your data sending to OOCSI channel

Q: I can't find the tab for uploading data via the OOCSI in the CONFIGURATION block on my dataset page, why?

A: If you can't find the tab for uploading data in the CONFIGURATION block on the dataset page, this means that the dataset cannot receive data from OOCSI. Currently, only IoT and Entity datasets support receiving and storing data with OOCSI service.

---

Q: Can I only fetch one record of the data in my IoT dataset?

A: No, IoT dataset doesn't support getting or editing data by a specific record. Only Entity dataset provide the functionalities for fetching and editing data for a specific record.

---

Q. Can I access Entity data with data from IoT device?

A: Yes, that's possible, but you will need an additional Script dataset for accessing the incoming data from OOCSI channel.
Reference here: Script for passing IoT data to Entity dataset

---

### Fitbit / GoogleFit

Q: I've just connected my Fitbit / GoogleFit wearable, and it's automatically synced all the day, why did my Fitbit / GoogleFit dataset not get any data?

A: The Fitbit / GoogleFit data will be fetched by the Data Foundry server at some time during the day, but not all the time. So, the data will be fetched once per day and it's normal that you don't have your data right after connecting your Fitbit / Googlefit (wearable) device. Please check again one day after your Fitbit / GoogleFit wearable is connected.

---

Q: What will happen if I forget to sync my wearable device?

A: The wearable data will be fetched automatically once you synced if you forget to sync your wearable device. For example, last time you synced is on Monday and which means the Data Foundry server fetched data until Sunday, then four days after, you synced your wearable device on Friday, then the Data Foundry server would fetch data from Monday to Thursday. And due to the limitation amount of requests and also the buffer of the wearables, it's better not more than 7 days between two synchronizations. If it's more than 7 days between two synchronizations, then it might take more than one day to fetch your data. Why not Friday? See next question.

---

Q: Can I see my data of the day I synchronized my wearable device?

A: No, because the data of the day you do the synchronization is not complete, so the Data Foundry server is always fetching data from earlier days.

---


### Telegram bot

Q: Something wrong with the DataFoundry Telegram bot, what can I do?

A: Enter "/stop" and "/start" over again.

---

Q: Your participants cannot submit photos to the Telegram bot?

A: Please check whether you have a MEDIA dataset in your project and whether this dataset has the option "open participation" switched ON.

---

## Other Issues

### ESP32 usage

Q. Why is ESP32 not uploading automatically after clicking the upload button of Arduino IDE?

A. You can try to press the BOOT button on the ESP32 board when the “Connecting…” message is showing up in the console window of Arduino IDE as uploading sketch to ESP32.

---

Q. Why is some sensors (pins) will not work as the Wi-Fi module is working?

A. This is because the design of ESP32 model, when the Wi-Fi module is working, only ADC2 pins are available, which means ADC1 will be occupied by Wi-Fi module; otherwise, ADC1 pins will work. Check the official document.
