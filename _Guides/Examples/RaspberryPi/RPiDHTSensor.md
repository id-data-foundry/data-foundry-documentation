---
layout: default
title: Raspberry Pi DHT Sensor
parent: Raspberry Pi Examples
nav_order: 2
has_children: true
has_toc: false
---

https://github.com/edenchiang/PlayWithDataFoundry/tree/master/examples/DHT11_in_Pi

### Description

In this example, we will collect humidity and temperature data through an DHT sensor. This data will be collected every minute, of which the mean value will be calculated every 10 minutes and then be sent via OOCSI into an IoT dataset. After which the project researchers will receive notification every hour from the Data Foundry by the script through the TelegramBot of the Data Foundry.


## Raspberry Pi Setup

To start off it is important to set up your raspberry and make sure whether the GPIO pins are enabled. [Check this tutorial to learn how to set up your Pi.](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)

### Enable GPIO

When you are sure the GPIO pins are enabled properly, you can start attaching your sensor to the board. You do this with the following pin-out: GPIO4(pin 7) for data transferring, pin 4 for 5V power supply, and pin 6 for grounding
![]({% link _Guides/Examples/RaspberryPi/images/usecase-device-DHT11-in-Pi.jpg %})


{: .info }
This fritzing diagram is for a loose DHT11 or DHT22 sensor without module like on the picture
![]({% link _Guides/Examples/RaspberryPi/images/sketchDHTpi.png %})


### Setup Code

Now your circuit is complete and the GPIO pins are enabled, you can set up your python script. [Take this example](https://github.com/edenchiang/PlayWithDataFoundry/blob/master/examples/DHT11_in_Pi/DHT11-in-Pi.py) 

{: .warning}
Make sure to change the OOCSI channel you will be sending data to in line 43 of the code example to something like `YourName/ProjectName/DeviceName`.

### Data Foundry setting

Set the same OOCSI channel name for the IoT dataset you want the data to flow to.
* IoT dataset setting for uploading OOCSI: Channel name
![]({% link _Guides/Examples/RaspberryPi/images/usecase-project-DHT11-in-Pi.jpg %})

And create a new script to send a telegram message to the researchers by pasting the following code into a new script. Before you can receive however, you need to [register your telegram account at the telegram bot of your instance.]()

```javascript
DF.print("test message data: " + data.sendMsg + ", humidity: " + data.humidity)
if (data.sendMsg == true) {
  DF.telegramResearchers("Humidity:" + data.humidity + ", temperature:" + data.temperature)  
}
```

{%comment%}

### TelegramBot settings

* Install [Telegram app](https://telegram.org/)
* Add the Telegram Bot of the Data Foundry, search id: DataFoundryBot
* Log into the DATAFOUNDRYTELEGRAMBOT as a researcher, reference: [Login as a researcher]({% link _Guides/Examples/Integrations/telegram.md %})

TODO DIEDE -- remove data.id.tue.nl references, replace with generic instance info? perhaps also avoid "DatafoundryBot" which is _our_ bot and cannot be the bot of another instance. We actually have a replace for this in the HomeController, I believe. Pls check. "NOTE: could we replace this for the actual bot name?"

{%endcomment%}
