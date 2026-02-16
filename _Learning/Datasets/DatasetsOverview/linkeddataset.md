---
layout: default
title: Linked Dataset
parent: Datasets
has_children: true
has_toc: false
---

# Linked Dataset

The Linked Dataset serves a simple but important organizational purpose: it acts as a bookmark to an external or internal resource. Unlike other datasets that store data directly within Data Foundry, this one holds just a single URL. This allows you to bring relevant external resources right into your project's dataset list, keeping everything you need in one place.

Think of this dataset type as a way to create a centralized dashboard for your project. You can use it to link to a wide variety of resources that are part of your research but live outside of Data Foundry. For example, you could link to a project blog, a survey hosted on an external platform like Qualtrics or Google Forms, a shared document in the cloud, or even a related scientific publication. By creating these links, you provide your team with a quick and easy way to access all facets of the project from a single interface.

Creating a Linked Dataset is straightforward. You simply provide a name for the link and the target URL. Once created, it will appear in your list of datasets alongside your data-heavy collections like the [IoT Dataset](./iotdataset.md) or [Form Dataset]({% link _Learning/Datasets/DatasetsOverview/formdataset.md %}). This helps in creating a holistic overview of your project's landscape, integrating both the data you collect and the context that surrounds it. It’s a small feature that can make a big difference in keeping your research organized and accessible.

## Configuring a Linked Dataset

The Linked Dataset is the simplest dataset type to configure because its only "configuration" is the URL it points to. This target URL is set when you create the dataset and can be changed by editing the dataset's properties. There are no complex settings for data ingestion, visualization, or processing because the Linked Dataset does not store any data itself.

The main page for a Linked Dataset is minimal. It prominently features a "Link" button that will take you directly to the target URL you have configured. Although the standard "Configuration" section with tabs for data downloads might be visible, these options are not applicable and will not have any function for this dataset type. The sole purpose of this dataset is to provide a quick and convenient bookmark within your project's list of datasets.
