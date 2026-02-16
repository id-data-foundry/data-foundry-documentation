---
layout: default
title: IoT Dataset
parent: Datasets
has_children: true
has_toc: false
---

# IoT Dataset

The IoT Dataset is the workhorse for collecting time-ordered data from a vast array of sources. It's designed to be a generic and highly flexible solution for logging data from sensors, connected products, interactive installations, or any data-streaming application. If you have a device or service that generates data over time, the IoT Dataset is almost certainly the right tool for the job. The IoT dataset type is useful for all kinds of data from sensors and connected products. The items in this dataset are ordered by time, so the first item to be stored is the first in the list, then the next until the most recent time that was stored. Think of a log book in which all items are listed one after each other.

One of its greatest strengths is the variety of ways you can send data to it. The dataset offers multiple ingestion methods to fit your specific needs: you can send a single JSON object via an HTTP POST request, batch upload an entire CSV file, or even use a simple web form for manual entries. For more advanced use cases, it can be configured to listen to [OOCSI](https://oocsi.com/) message streams, making it a powerful hub for multi-device ecosystems. This flexibility makes it suitable for everything from quick prototypes to large-scale, public-facing installations, as it can be configured to accept data from any source, not just pre-registered devices.

Despite its ability to accept flexible JSON payloads, the IoT Dataset brings structure to your data. Each record is stored with a `timestamp`, an optional `activity` label, and is associated with a `device_id`. The dataset intelligently inspects the keys within the incoming JSON data and dynamically builds a "projection," or schema. This allows you to export your entire dataset as a structured CSV file, where each key has its own column, even if different devices send slightly different data. To help you monitor your data streams, it also includes a live data visualization view and a tree view for exploring the raw data.

## Configuring an IoT Dataset

Configuring an IoT Dataset involves setting up the pathways for data ingestion and export. A key setting, **"Open participation,"** can be enabled when you create the dataset. If checked, the dataset will accept data from any source, which is ideal for public installations or projects where devices are not pre-registered.

Once created, the "Configuration" section provides a powerful set of tools:

*   **HTTP data upload:** This is an essential tab where you can generate, regenerate, or delete the **HTTP API Token** needed to authenticate devices sending data via HTTP POST.
*   **Data from OOCSI:** For real-time systems, this tab allows you to specify an **OOCSI Input Channel** for the dataset to subscribe to, enabling data ingestion from the OOCSI network.
*   **Forward data to OOCSI:** Conversely, this tab lets you specify an **OOCSI Output Channel** to broadcast all new data from the dataset to other OOCSI-enabled systems.
*   **CSV/JSON Download:** Here, you can generate a **Public CSV/JSON Access Token** to create a public URL for downloading the entire timeseries dataset, with all dynamically recognized data fields projected into their own columns.
