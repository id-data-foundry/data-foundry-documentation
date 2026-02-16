---
layout: default
title: Connected Datalogger
parent: Getting Started
nav_order: 3
has_children: true
---

# Tutorial 3 - My First Connected Datalogger!

### Getting started with collecting data through an esp32 with Data Foundry
![Dataflow]({% link _Tutorials/GettingStarted/images/DF_Blocks_T3.jpg %}){:width="30%" style="float: right"}

As tutorial 2 already introduced you to the concept of dataloggers, we are stepping this up a notch, by turning a microcontroller into a datalogger. First we will setup an IoT dataset, then we will build a datalogger after which we will connect the two.

 We do this according to the following steps:

{:toc}
1. Gather Supplies
2. Datalogger Assembly
3. Prepare Laptop
4. Program microcontroller

## Gather supplies
Before we get started, you need to get all of the right supplies; Not every microcontroller will work properly hence we created a shopping list with proven components for you.
### Shopping List
- 1 x Waveshare ESP-32s3 pico (with headers)
- 1 x DHT11 temperature sensor
- 1 x Breadboard
- 3 x Jumper wires

{: .info }
Any other ESP-32 based boards would also work, however for the sake of the tutorials it will be easier to use this board.

## Datalogger Assembly
Once you have gotten your hands on all the components, you can start assembling the datalogger. We have created a small diagram as a reference of how you should connect everything together.

(image)

{: .warning }
The ESP32-s3 that we are using has the labeling of each pin underneath the pin itself. This can be very confusing so please take this in mind while assembling you datalogger

## Prepare Laptop
### Computer
Before we start, we have to make sure your computer is ready to follow the tutorial. To work with microcontrollers on Data Foundry, you will need to use a chromium webbrowser like; Brave, DuckDuckGo, Opera or Chrome. Additionally if you are running windows, [make sure to install the following drivers.](https://github.com/nodemcu/nodemcu-devkit/tree/master/Drivers)

### WiFi
You will also require wireless internet access. Because we are using an ESP microcontroller, you have to make sure your WiFi router has 2.4ghz enabled. For most routers this is enabled by default, but if this not the case this could be the reason your ESP32 can't connect to the internet later on.

{: .info }
 If you are working on campus check out, [IoTroam.](https://iotroam.org) Through IoTroam you can obtain device specific wifi credentials for your prototypes.

## Program microcontroller
### Tour link

{% include df-link.html text="Take the tour" path="/tour/making-sense-of-sensors" %}

### Additional video??
