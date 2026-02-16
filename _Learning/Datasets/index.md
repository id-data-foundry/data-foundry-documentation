---
layout: default
title: Datasets
redirect_from:
  - /dataset-active
nav_order: 2
has_children: true
has_toc: false
---

# Datasets

Data Foundry offers a wide array of datasets you can use throughout your designing and research processes. But not all of these are as straight forward to get started with. Hence this part of the documentation explains the purpose of each of the datasets in more detail. Hopefully clearing up their purposes and allowing you to know what dataset to use for your project. This part will also explain some of the more generalized features used through out all the datasets, such as Public Parameters, limits and fair practices

For more details on how to implement these datasets please refer to the [How-to Guides]({% link _Guides/index.md %}) section of this documentation, as this section will go into more depth about working with the datasets.


## Dataset Limits

You can add multiple datasets to your projects. Every project can store at least 10 datasets. Note that you can collect data from different devices in a single dataset (e.g., an IoT dataset). You do not need to create a separate dataset for every individual sensor or device.

To prevent data tsunami's, Each dataset only accept 2 events per seconds. But this should be plenty for most research. If you want to capture more, think about averaging out your data through for example [OOCSI's rolling average feature!]()<TODO MATHIAS>

## Overview

![dataset flow chart]({% link _Learning/Datasets/images/dataset-choice-flow.png %})


### Main Datasets

- **[IoT Dataset]({% link _Learning/Datasets/DatasetsOverview/iotdataset.md %})**: Store live data generated through HTML, OOCSI, or manual import.
- **[Entity Dataset]({% link _Learning/Datasets/DatasetsOverview/entitydataset.md %})**: Store and manage structured state variables.

### Text-based Datasets

>[**Form Dataset**]({% link _Learning/Datasets/DatasetsOverview/formdataset.md %})
Generate forms of which the results will automatically be collected in a dataset

>[**Survey Dataset**]({% link _Learning/Datasets/DatasetsOverview/surveydataset.md %})
Generate surveys for participants of which the results will automatically be collected in a dataset

>[**Diary Dataset**]({% link _Learning/Datasets/DatasetsOverview/diarydataset.md %})
Collect diary study information through our online environment or telegram integration. the results will be put into a dataset

>[**Annotation Dataset**]({% link _Learning/Datasets/DatasetsOverview/annotationdataset.md %}) Annotate other datasets through the annotation dataset.


### Wearable Datasets

- **[Fitbit Dataset]({% link _Learning/Datasets/DatasetsOverview/fitbitdataset.md %})**: Collect health and vitality data from FitBit devices.
- **[Google Fit Dataset]({% link _Learning/Datasets/DatasetsOverview/googlefitdataset.md %})**: (Deprecated) Formerly used for Google Fit data.

### File-based Datasets

- **[Existing Dataset]({% link _Learning/Datasets/DatasetsOverview/existingdataset.md %})**: Upload, store, and host any file type.
- **[Media Dataset]({% link _Learning/Datasets/DatasetsOverview/mediadataset.md %})**: Specifically designed for uploading and storing images.
- **[Movement Dataset]({% link _Learning/Datasets/DatasetsOverview/movementdataset.md %})**: Store movement data via GPX and XML files.

### Experience Sampling

- **[Experience Sampling Dataset]({% link _Learning/Datasets/DatasetsOverview/experiencesamplingdataset.md %})**: Probe participants using the PIEL survey app and aggregate survey results.

## Dataset Metadata

Beyond the basic identity of your dataset, Data Foundry allows you to add rich metadata. This is not just "admin work"; it is crucial for making your data **Findable, Accessible, Interoperable, and Reusable (FAIR)**. Good metadata ensures that others (and your future self!) can understand the context, origin, and legal terms of your research data.

You can edit these details by clicking the **Edit** button on the dataset overview page. Here are some key fields to consider:

*   **Dataset Introduction**: This is more than just a description for you. It is often displayed to participants during the consent process or when browsing public datasets, so write it with a clear, non-technical voice that explains the purpose and value of the data.
*   **License**: Choosing a license (such as MIT or Creative Commons) is essential if you plan to share your data. It clearly defines how others can legally use your work.
*   **Organization & Relation**: These fields provide context. Use **Organization** to credit your lab or funding body, and **Relation** to link to related publications or other datasets (e.g., "Supplementary data for [Publication Title]").
*   **DOI (Digital Object Identifier)**: If your dataset supports a publication, entering the DOI here creates a permanent link to the official record, making your work easier to cite.

Taking the time to complete this information significantly increases the long-term value of your research.

## Dataset Limits

You can add all types of datasets to your projects. Note that you can collect data from different devices in a single dataset (IoT dataset, see below). The same holds for participants and wearables. So, you don't need to create a dataset for every sensor or device. However, it is often a good idea to just create a new dataset if you make a change to your probe or study setup.

When sending data to datasets via OOCSI, note that each dataset is throttled to only accept 2 events per seconds. This is usually enough for most research. If you want to capture more, talk to the administrator of your Data Foundry instance.


## Dataset Structure

Data Foundry datasets are designed with a consistent core structure to facilitate data integration and analysis across various types. Every data record within a dataset typically includes the following fundamental fields:

*   **`id`**: A unique identifier assigned to each individual record, ensuring traceability and distinctness.
*   **`ts` (Timestamp)**: Records the exact time when a data entry was created or last modified, crucial for time-series analysis and understanding data chronology.
*   **`pp1`, `pp2`, `pp3` (Public Parameters)**: These are flexible, user-definable string fields. They act as generic metadata slots that can be customized to add context, categorize data, or store additional relevant information without altering the core dataset schema. For instance, you might use `pp1` for a participant group, `pp2` for an experimental condition, or `pp3` for a specific device model. Their generic nature allows for powerful filtering and grouping operations across different datasets.

This common structure, especially the presence of timestamps and public parameters, is key to "mashing up" data from disparate sources. It enables you to combine and analyze data from, for example, a FitBit dataset, a Diary dataset, and an IoT dataset, all within a unified framework.

Beyond these core fields, each dataset type (e.g., IoT, Entity, Media) includes additional fields specific to its purpose. Many also contain a `data` field, often storing content in JSON format, which holds the primary information pertinent to that dataset type.

For more details on how to export and work with the structured data, please refer to the relevant sections in the [How-to Guides]({% link _Guides/index.md %}).


## Open Participation

"Open Participation" is a key feature that dictates how data can be submitted to a dataset. When a dataset is configured for open participation (controlled by the `openParticipation` setting), it allows external entities — such as devices, scripts, or unregistered users — to submit data records without needing to be pre-registered as participants or devices within your Data Foundry project.

In such cases, data submission is authorized through a unique API token associated with that specific dataset. This API token acts as a key, granting permission for data to be appended to the dataset. This mechanism is particularly useful for:

*   **Public data collection**: Gathering data from a wide range of external sources where individual registration might be impractical.
*   **Integration with third-party systems**: Allowing external applications or services to push data into your Data Foundry project seamlessly.
*   **Flexible data streams**: Setting up dynamic data pipelines where the origin of each individual data point isn't tied to a specific pre-defined entity.

While many datasets leverage open participation, the **Entity Dataset** has special semantics related to it, as it manages mutable state and may involve more intricate token-based authorization and resource identification. This ensures that even in an open context, data integrity and controlled access to specific resources are maintained.


## Dataset-specific License

While your overall Data Foundry project may operate under a general license, each individual dataset can be assigned its own distinct license. This granular control is managed through the `license` field associated directly with each dataset.

Assigning a dataset-specific license is crucial for adhering to **FAIR (Findable, Accessible, Interoperable, Reusable) data principles**, especially when:

*   **Sharing data**: If you plan to make a particular dataset publicly available or share it with collaborators, defining a clear license (e.g., Creative Commons, MIT, ODC-By) explicitly states the terms under which others can use, modify, and distribute that specific data.
*   **Mixed licensing**: Your project might contain datasets with different origins or sensitivities, requiring varied usage terms. For example, some datasets might be open access, while others require more restrictive conditions due to privacy concerns or intellectual property.
*   **Legal clarity**: A clearly stated license helps prevent ambiguities regarding data ownership and usage rights, fostering trust and enabling ethical data governance.

By leveraging dataset-specific licenses, Data Foundry empowers you to manage the legal and ethical dimensions of your research data with precision, ensuring that each dataset's usage aligns with its specific context and sharing intentions.


## Dataset Active State

A dataset's "active" state determines whether it can currently accept new data submissions. This is primarily controlled by the start and end dates you configure for the dataset. For more information on how these dates fit into the broader project schedule, refer to the [Project Timeline]({% link _Learning/Projects/index.md %}#timeline) section.

Generally, a dataset is considered **active** if the current date falls between its start date (inclusive) and a specific "terminal" date. The main purpose of this state is to control data ingestion; only active datasets can have new data appended to them.

The calculation of the terminal date includes a grace period to accommodate delays in data synchronization:

*   **Fitbit and Google Fit Datasets**: These remain active for **two days** after their configured end date. This ensures that all data from the participants' devices, which might sync late, is successfully collected.
*   **All Other Datasets**: These have a grace period of **one day** after their end date.

For a dataset to be active, the current date must be on or after the start date and before this terminal date.

### Special Cases

Some internal dataset types are always considered active, regardless of their start and end dates. This includes special-purpose datasets such as those for **Study Management** or **Saved Exports**.
