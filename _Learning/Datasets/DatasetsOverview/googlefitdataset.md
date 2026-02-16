---
layout: default
title: Google Fit Dataset
parent: Datasets
has_children: true
has_toc: false
---

# Google Fit Dataset

Similar to the FitBit dataset, the Google Fit Dataset enables automated collection of health and activity data, but this time from the Google Fit platform. This is an incredibly useful tool for studies involving participants in the Android ecosystem or for anyone who uses Google Fit to aggregate their health data. The data is fetched automatically from the Google Fit service, providing a continuous, objective stream of information without manual intervention. Data Foundry will request authorization for the following scopes from the GoogleFit servers. This happens when participants sign-up their GoogleFit wearables to the Data Foundry:

**Recording by minute**
- Activity -- activities by minute
- Calories -- calories burned by minute
- Speed -- moving speed by minute
- Heart rate -- recording the heart rate by minute
- Step count -- recording the steps by minute
- Distance -- counting the distance by minute

**Recording by day**
- Weight -- recording weight once a day

The data collected by and from Google Fit is similar to FitBit data. The main difference is the scope "Speed", which the GoogleFit API provides for recording moving behavior. We always request for all the scopes, but only the data for the scopes required by the Google Fit dataset will be stored by the Data Foundry server. The data is collected from Google Fit servers once a day and ready for your use-case directly after.

The setup process mirrors that of other wearable datasets. When creating the dataset, you, the researcher, select the specific data `scopes` you wish to collect. Participants must then authorize Data Foundry to access their Google Fit data through a secure, standard authentication process. A unique advantage of this dataset is its potential for cross-platform data collection; for example, it can be used with an Apple Watch if the participant has the Google Fit app installed and has granted it access to their Apple Health data, making it a surprisingly versatile choice.

All data collected is stored in a structured timeseries format, linked to a specific `Wearable` resource within your project. The schema is predefined to handle the various metrics available through the Google Fit API, including `activity`, `calories`, `speed`, `heart_rate`, `step_count`, `distance`, and `weight`. This automated and standardized data collection process ensures consistency and reliability in your dataset, allowing you to focus on the research rather than on data wrangling.

For participants with Apple Watch and iPhone: They can download the "Google Fit" app, and login, then they can set the permissions in Apple Health to share data with Google Fit app. To do so, these participants can use Apple Watch as their "Google" wearable and record data into the Google Fit dataset.

## Configuring a Google Fit Dataset

The most critical configuration for a Google Fit Dataset happens during its creation. At setup, you must choose the specific data **scopes** (e.g., activity, heart rate, step count) you want to collect. This selection is permanent and defines what permissions Data Foundry will request from your participants.

Once the dataset is active, the on-page "Configuration" options are focused on data export and integration:

*   **CSV/JSON Download:** This tab allows you to generate a public URL (with an access token) to download all the collected timeseries data in a structured CSV or JSON format.
*   **Forward data to OOCSI:** Here, you can specify an OOCSI channel to stream incoming Google Fit data in real-time to an OOCSI network.

The data collection process is fully automated based on the initial scope selection and participant consent, requiring no further configuration.
