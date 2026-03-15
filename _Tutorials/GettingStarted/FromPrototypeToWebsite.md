---
layout: default
title: From Prototype to Website
parent: Getting Started
nav_order: 5
has_children: true
---

# Tutorial 5 - From Prototype to Website!

## Connecting your prototype to a website through OOCSI

This last tutorial builds forward on all of the prior tutorials, teaching you how you can combine multiple Data Foundry tools to create a connected prototype. We will build a small prototype with various sensors, and host a corresponding website. Then we will connect the prototype to the website through OOCSI.

## The Concept

We are going to bridge the physical world (your sensors) with the digital world (your website).
1.  **The Prototype (ESP32):** Reads sensor data and sends it to an OOCSI channel.
2.  **The Bridge (OOCSI):** A real-time messaging server that passes messages between devices.
3.  **The Website (HTML/JS):** Listens to that channel and updates the UI when new data arrives.

## Step 1: The OOCSI Channel

First, decide on a unique channel name. This is like a chat room name. If you use a common name like "test", you will receive everyone else's data.
Use a structure like: `YourName/ProjectName/SensorData`.

**My Channel:** `_______________________`

## Step 2: The Prototype (ESP32)

We will use the OOCSI library for ESP32. Ensure your board is set up as in Tutorial 2.

### Code Example (Arduino/C++)

```cpp
#include "OOCSI.h"

// ... WiFi and Sensor setup ...

OOCSI oocsi = OOCSI();

void setup() {
  // ... setup code ...
  oocsi.connect("MyESP32Client", "{{ site.external_base_urls.oocsi }}", "YourWiFi", "YourPassword");
}

void loop() {
  // Read sensor
  int sensorValue = analogRead(A0);

  // Send data to OOCSI
  oocsi.newMessage("YourName/ProjectName/SensorData");
  oocsi.addInt("value", sensorValue);
  oocsi.sendMessage();

  delay(1000); // Wait a second
}
```

Flash this code to your ESP32.

## Step 3: The Website

Now, let's create a simple HTML page that listens to this data. You can host this on Data Foundry (see Tutorial 4).

### Code Example (HTML/JS)

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Connected Prototype</title>
    <!-- Import OOCSI Library -->
    <script src="https://{{ site.external_base_urls.oocsi}}/assets/js/oocsi-web.min.js"></script>
</head>
<body>
    <h1>Sensor Value: <span id="valueDisplay">Waiting...</span></h1>

    <script>
        // Connect to OOCSI
        OOCSI.connect("wss://{{ site.external_base_urls.oocsi }}/ws");

        // Subscribe to your channel
        OOCSI.subscribe("YourName/ProjectName/SensorData", function(msg) {
            // This function runs every time a message arrives
            console.log("Received:", msg);
            
            // Update the HTML element
            document.getElementById("valueDisplay").innerText = msg.data.value;
        });
    </script>
</body>
</html>
```

## Step 4: Test it!

1.  Power up your ESP32.
2.  Open your website in a browser.
3.  Watch the value change in real-time as you interact with the sensor!

Congratulations! You have built a full IoT system.
