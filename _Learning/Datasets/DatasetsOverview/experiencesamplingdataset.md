---
layout: default
# title: Experience Sampling Dataset
title: 404
parent: Datasets
nav_exclude: true
has_children: true
has_toc: false
---

# Experience Sampling Dataset

The Experience Sampling Method (ESM) is a popular research technique for capturing in-the-moment thoughts, feelings, and behaviors. Data Foundry directly supports this with the Experience Sampling Dataset, which is specifically designed to work with data from the popular [PIEL Survey app](https://pielsurvey.org/). This dataset streamlines the process of getting ESM data from your participants' phones into a structured and analyzable format within your project.

Getting data into the system is a simple, two-step process. First, participants use the PIEL app to respond to surveys on their mobile devices. Then, they export their data as a CSV file, which they send to you. As the researcher, you simply upload this CSV file into the Experience Sampling Dataset and associate it with the correct participant in your project. This manual but clear process ensures that all data is correctly attributed from the start.

Once a CSV file is uploaded, Data Foundry's backend does the heavy lifting. The system automatically parses the file, intelligently skipping the header rows and extracting the core data: timestamps and survey responses. This raw data is then transformed into a clean, structured timeseries format. The dataset cleverly keeps both the original uploaded CSV file for archival purposes and the newly parsed, structured data. For analysis, you can either download the original files or, more conveniently, export a single, aggregated CSV file containing all the parsed data from every participant, ready for statistical analysis.

## Configuring an Experience Sampling Dataset

The Experience Sampling Dataset requires minimal configuration, as its main function is to process and store data files uploaded by the researcher. The primary interface is focused on uploading the CSV files exported from the PIEL survey app.

The "Configuration" section at the bottom of the page provides a tabbed interface for managing data exports:

*   **CSV/JSON Download:** This is the most important configuration tab. It allows you to generate a public URL (with an access token) to download a single, aggregated CSV or JSON file containing all the parsed timeseries data from every uploaded file. This is the main export you will use for analysis.
*   **Forward data to OOCSI:** This tab allows you to specify an OOCSI channel to stream the parsed survey responses to an OOCSI network for real-time applications.
