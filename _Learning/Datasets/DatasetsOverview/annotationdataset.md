---
layout: default
title: Annotation Dataset
parent: Datasets
has_children: true
has_toc: false
---

# Annotation Dataset

The Annotation Dataset is a powerful tool for researchers to capture qualitative insights and observations about their data. Think of it as a dedicated digital notebook for your project, allowing you to jot down thoughts, interpretations, and notes about specific groups of data resources. These annotations are an essential part of the research process, helping you to build a narrative around your data and to collaborate with your team. Keeping your notes alongside your data ensures that valuable context is never lost.

Annotations are textual bits of data from the researcher's perspective, and annotations refer to clusters in your project. The annotation dataset allows to capture annotations in various forms of groupings of such project resources. Every annotation contains a title and text, as well as a timestamp. The first step to annotations is to create an annotation dataset and then either use one of three options to create annotations:

1. Go to the annotation dataset page and use the annotation button
2. Go to the "manage resources" page and annotate any cluster that is shown there
3. Use the data tool together with a media dataset

At its core, an Annotation Dataset stores textual annotations, each with a title, the main text content, and a timestamp. What makes this dataset type particularly useful is its direct link to **Clusters**. A Cluster is a flexible grouping of resources, such as participants, devices, or even specific data points. By linking annotations to clusters, you can create a structured log of your analysis. For example, you might create a cluster of participants who showed a particular behavior and then use an annotation to describe your observations about that group. You can learn more about how to manage project resources in our [Guides section]({% link _Guides/ProjectManagement/index.md %}).

Creating annotations is designed to be seamless and intuitive, fitting right into your research workflow. You can add annotations directly from the dataset's main page, from the management page of a specific Cluster, or even while you are exploring visual data in a [Media Dataset]({% link _Learning/Datasets/DatasetsOverview/mediadataset.md %}). Data Foundry is smart about it, too: if you try to add an annotation but haven't created an Annotation Dataset yet, it will automatically create one for you. This means you can focus on your research without interruption. When you're ready to analyze or share your notes, the entire collection of annotations can be easily exported as a CSV file.

## Configuring an Annotation Dataset

Configuring an Annotation Dataset is focused on how you access and export the data you've collected. From the dataset's page, you will find a "Configuration" section with several tabs for managing data pathways:

*   **CSV/JSON Download:** This tab is your primary tool for exporting your research notes. You can generate a public URL (using an access token) to download all annotations in either CSV or JSON format. This is perfect for offline analysis, sharing with collaborators, or importing into other software.
*   **Forward data to OOCSI:** This tab lets you specify an OOCSI channel to stream your annotations to in real-time for integration with other reactive systems or visualizations.
