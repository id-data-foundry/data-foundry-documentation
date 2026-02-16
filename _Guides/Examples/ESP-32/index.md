---
layout: default
title: ESP32 Examples
parent: Example Projects
nav_order: 2
has_children: true
has_toc: false
---

# ESP32 Examples
Data Foundry was made with connectivity and building smart prototypes in mind hence there are lots of ways to make your prototype or probe interact with Data Foundry. This section of the documentation contains various examples how to use Data Foundry to collect data from your microcontroller. We will show various ways from direct communication to communication over the oocsi protocol and even have an example in which we will upload small images. This section might be called ESP32 examples, but most of these examples will probably work on other internet enabled microcontrollers too, especially microcontrollers capable of running micropython. Is this not the case, please tell us so that we can make oocsi and data foundry compatible with your favorite prototyping boards.

## Micropython
After years of using the Arduino IDE, we decided to also start supporting micropython, If you are not familiar with micropython, we can help you get started and prepare your board.

{% link _Guides/Examples/ESP-32/ESP32micropython.md %}{: .btn}

## Camera Upload
In this example we will show you how you can upload pictures taken with an esp32 camera module and sent these to a media dataset

{% link _Guides/Examples/ESP-32/ESP32CameraUpload.md %}{: .btn}

## Asynchronous Communication
In this example we will show you how you can facilitate communication between multiple prototypes that might not be online at the same time.

{% link _Guides/Examples/ESP-32/Asynchronous.md %}{: .btn}
