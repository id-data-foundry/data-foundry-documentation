---
layout: default
title: FitBit Dataset
parent: Datasets
has_children: true
has_toc: false
---

# FitBit Dataset

The FitBit Dataset provides a seamless and automated way to collect rich health and activity data from your participants' FitBit devices. This dataset connects directly to the FitBit API, allowing you to gather a wide range of physiological and behavioral data without requiring any manual data entry from you or your participants. It’s an ideal solution for studies interested in physical activity, sleep patterns, heart rate, and more, providing a continuous stream of objective data.

{: .info }
FitBit data is collected directly from the FitBit servers. When you set up participants and wearables in Data Foundry, the Data Foundry server will request authorization of the following scopes from the FitBit server. This happens only once, when participant sign-up their FitBit wearable to the Data Foundry.

Data in the different scopes will be collected either by minute or by day, see the following list:

**Recording by minute**
- Steps -- counting steps
- Distance -- counting moving distance (by - steps)
- Floors -- counting the climbed stairs
- Elevation -- counting the height of climbing (by floors)
- Calories -- counting the calories burned every minute
- Heart Rate -- recording heart rate every minute
- Sleep -- recording the status by minute during sleeping
- Activity (Summary) -- summary of all activities in a day

**Recording by day**
- Weight -- recording the weight
- Fat -- recording the fat
- BMI -- recording the BMI



Setting up a FitBit Dataset is straightforward. When you create the dataset, you'll be prompted to select the specific data `scopes` you are interested in, such as heart rate, steps, calories, distance, or sleep. This ensures you only collect the data you need for your research. We always request for all the scopes, but only the data for the scopes required by the FitBit dataset will be stored by the Data Foundry server. The data is collected from FitBit server once a day and ready for your use-case directly after. Not all the data of the scopes mentioned above can be obtained by the wearable directly, i.e., Weight, Fat, and BMI. Data for these scopes can only be provided by other smart devices, such as a smart scale or a smart phone app.

The next crucial step is for your participants to authorize Data Foundry to access their FitBit data. This is a one-time, secure process where they log in with their FitBit account and grant permission. Once authorized, Data Foundry will automatically fetch their data in the background.

The collected data is stored as a structured timeseries, linked to a specific `Wearable` resource in your project. The data schema is predefined to handle the various metrics provided by FitBit, including `heartrate`, `steps`, `calories`, `distance`, `sleep`, `weight`, `bmi`, and `fat`. The granularity of the data varies by metric; for instance, step count might be collected per minute, while sleep data is summarized per day. This automated collection process saves you an enormous amount of time and provides a high-fidelity record of your participants' daily lives.


## Configuring a FitBit Dataset

The most critical configuration for a FitBit Dataset happens once, at the moment of its creation. During setup, you must choose the specific data **scopes** (e.g., heart-rate, steps, sleep) your study requires. This choice is final and cannot be modified later.

Once the dataset is actively collecting data, the on-page "Configuration" options are focused on data export and integration:

*   **CSV/JSON Download:** This tab allows you to generate a public URL (with an access token) to download all the collected timeseries data in a structured CSV or JSON format, ready for analysis.
*   **Forward data to OOCSI:** Here, you can specify an OOCSI channel to stream the incoming FitBit data in real-time to an OOCSI network.

There are no settings to adjust the data collection itself; after the initial setup and participant consent, a process is fully automated.
