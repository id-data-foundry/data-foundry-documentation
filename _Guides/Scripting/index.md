---
layout: default
title: Scripting
nav_order: 3
has_children: true
---

# Data Foundry Scripts

Data Foundry provides an always-on scripting environment that allows for small programs to process data from OOCSI channels, update databases or user profiles, and trigger state changes in physical products or services. While OOCSI handles the messaging and Data Foundry provides the storage, scripting connects these two with higher-level logic.

## What Are Scripts?

Scripts are written in JavaScript and run directly on the Data Foundry server. Every script can listen to events on OOCSI channels and process that data alongside information from its project.

Scripts have access to several project resources:
- **Participants and Devices**: Manage project members and connected hardware.
- **IoT Datasets**: Store and retrieve time-series data.
- **Entity Datasets**: Serve as a database for structured data like user profiles, decision trees, and content.

## Script Management

Every script in Data Foundry belongs to a project. To create a script, navigate to the scripting tool within your project. Currently, each user can create up to five scripts across their projects.

- **[Accessing Datasets]({% link _Guides/Scripting/AccessDatasets/AccessAnyDataset.md %})**: How to read and write data from scripts.
- **[Script Inputs]({% link _Guides/Scripting/scriptInputs.md %})**: Working with script parameters and inputs.
