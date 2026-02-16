---
layout: default
title: Movement Dataset
parent: Datasets
has_children: true
has_toc: false
---

# Movement Dataset

The Movement Dataset is a specialized tool for handling GPS location data. It is designed to import, parse, and store movement tracks from standard file formats, making it easy to analyze and visualize the spatial behavior of participants or the paths of tracked objects. If your research involves understanding where and how people or things move, this dataset is an essential tool. The movement dataset accepts GPX or XML files, which you can obtain, for example, from wearable GPS trackers.

The primary way to get data into the dataset is by uploading files in GPX or XML format, which are common export formats for many GPS tracking devices and applications. Once a file is uploaded, Data Foundry automatically parses it, extracting the individual track points—each containing longitude, latitude, elevation, and a timestamp. This parsed data is then stored in a clean, structured IoT dataset, ready for analysis or export. For archival and validation purposes, the dataset also retains a copy of the original uploaded file.

In addition to file uploads, the dataset offers an alternative method for logging location data. A dedicated function (`addMovement`) allows for single location points to be logged one at a time. This method is particularly useful for real-time tracking applications and is used by integrations such as the Data Foundry Telegram bot, which allows participants to log their current location with a simple command. At any time, the complete, parsed timeseries of all GPS points from all sources can be exported as a single CSV file.

## Configuring a Movement Dataset

The Movement Dataset is designed for easy data ingestion and requires very little configuration. The main interaction is the "Upload files" button, which allows you to import GPS data in GPX or XML format.

The formal "Configuration" options are located at the bottom of the page and are focused on data export:

*   **CSV/JSON Download:** This tab allows you to generate a public URL (with an access token) to download a single, aggregated file of all the parsed GPS track points from all uploaded files, making it easy to perform spatial analysis in other software.
*   **Forward data to OOCSI:** This tab can be used to specify an OOCSI channel to stream the parsed location data to an OOCSI network, enabling real-time visualizations or integrations.
