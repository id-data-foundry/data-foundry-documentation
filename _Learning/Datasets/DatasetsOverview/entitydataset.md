---
layout: default
title: Entity Dataset
parent: Datasets
Datasets Overviewhas_children: true
has_toc: false
---

# Entity Dataset

The Entity Dataset is one of the most versatile and powerful datasets in Data Foundry, acting as a flexible key-value store for your project. It's designed to handle semi-structured data where each item, or "entity," is a JSON object identified by a unique `resource_id`. This dataset is perfect for scenarios where you need to store complex, evolving data that doesn't fit a rigid table structure. It fully supports CRUD (Create, Retrieve, Update, Delete) operations, primarily through a comprehensive [ReSTful API]({% link _Reference/DFapi.md %}), making it an ideal backend for custom applications, interactive installations, or dynamic data logging. Every item is identified by an ID and you can protect it with a token against unauthorized access. This way you could use this dataset to build a user account system in your digital prototype, or store visitor information in a museum exhibition. You can also use this dataset to temporarily store data that are shared between different prototypes.

One of the standout features of the Entity Dataset is its intelligent handling of JSON data. While you can store any valid JSON object as an entity, the dataset automatically creates a "projection" of all the keys used across your items. This projection is then used to generate a user-friendly flat table view within Data Foundry, complete with inline editing, which is incredibly handy for quick modifications. For more complex or nested JSON structures, a hierarchical tree view is also available, allowing you to inspect the full depth of your data. This dual-view system provides both a quick overview and a detailed inspection tool, right out of the box.

The Entity Dataset is built for developers and data managers. It maintains a complete history of changes for each item, and you can download this log to trace the evolution of your data. For security and access control, both individual items and the dataset itself can be protected with API tokens. To get you started quickly, the dataset can be pre-populated with existing project resources like participants, wearables, and devices. And to make development and debugging easier, a built-in API testing form lets you interact with your dataset's API directly from the web UI, without having to write any external code. When it's time for analysis, you can export either the latest state of all items or the complete historical log as a CSV file.

## Configuring an Entity Dataset

Configuring an Entity Dataset is centered around managing access and data flow through its powerful API. In the "Configuration" section, you'll find a tabbed interface to set up how other applications and services can interact with your key-value store:

*   **HTTP data upload:** This tab is critical for enabling external applications to create or update entities. You can generate, regenerate, or delete the **HTTP API Token** required to authenticate POST requests. Without a valid token, submissions will be rejected.
*   **Data from OOCSI:** This tab allows you to configure an **OOCSI Service Name**, enabling you to perform full CRUD (Create, Retrieve, Update, Delete) operations on the dataset via the OOCSI network for real-time, event-based integrations.
*   **Forward data to OOCSI:** Here, you can specify an **OOCSI Output Channel** to broadcast any new or updated data from the dataset, allowing other systems to react to changes in real-time.
*   **CSV/JSON Download:** This tab lets you generate a **Public CSV/JSON Access Token** to create a public URL for downloading your data. You can choose to export either the latest state of all items or the complete historical log.

For developers, the dataset page also features a "Test" button, which opens a form for sending test requests to the API, allowing for quick debugging and experimentation without leaving the UI.

## Open Participation

The "open participation" option has special semantics in the Entity Dataset type. Unlike other datasets where this flag might control the ability to contribute data, in an Entity Dataset, access is primarily governed by tokens and project-level settings:

*   **API Access & Tokens:** The "open participation" flag does not restrict data contribution via the HTTP API. Creating and updating items is controlled by the **Dataset API Token** and individual **Item Tokens**. As long as a valid token is provided, data operations are permitted.
*   **Public Listing (GET All Items):** Enabling "open participation" (often labeled as "Public" in the dataset settings) **is not sufficient** to allow external applications to retrieve the full list of items (via the `GET` API endpoint). To "open" the dataset for public indexing or browsing, the **Project** itself must be set to **Public** in the project settings. If the project is private, the API will reject requests to list all items with a `403 Forbidden` error, even if a valid API token is provided.

This means that to create a fully public backend where an external app can fetch all data, you must ensure your Project is Public.
