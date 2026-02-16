---
layout: default
title: ESP32 Tools
parent: Tools
nav_order: 3
has_children: true
---

# ESP Tools

For projects using ESP32 microcontrollers, Data Foundry provides a suite of web-based tools to simplify the workflow, especially for MicroPython users.

## Web Flasher

The Web Flasher allows you to install MicroPython firmware directly from your browser (Chrome/Edge required for WebSerial support) without installing any local software like `esptool`.

1.  Connect your ESP32 via USB.
2.  Go to **Tools > ESP Tools**.
3.  Click **Connect**.
4.  Select the serial port of your device.
5.  Choose the firmware version and click **Flash**.

## File Manager

Once MicroPython is installed, you can use the File Manager to upload your python scripts (`main.py`, `boot.py`) to the device.

*   **Upload:** Drag and drop `.py` files onto the device view.
*   **Edit:** Click on a file to edit it directly on the device.
*   **Run:** Soft-reboot the device to run your updated code.

This tool is perfect for quick prototyping and classrooms where installing drivers and IDEs on every student laptop is difficult.