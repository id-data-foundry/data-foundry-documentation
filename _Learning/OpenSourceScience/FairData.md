---
layout: default
title: Fair Principles
parent: Open Source and Science
has_children: true
has_toc: true
---

# FAIR Practices

## Description and Names

Every dataset needs a name and a description. Try to write something sensible, especially if you want to make the project public. A good description and name helps to make the contents of your project clearer and accessible to others. This way we can do design research collaboratively and push it to the next frontier! Learn more here about [Open Science]({% link _Learning/OpenSourceScience/index.md %})

Next, datasets have a start and end date. This allows to open and close the dataset for new data. For example, when you want to schedule an experiment, you can use the start and end dates to ensure that data can be added only in the given time period. If you don't specify start and end dates, then the dataset starts right away and ends in three months.
Public parameters

## Public Parameters

Data Foundry datasets have an important feature: public parameters. These are three attributes that are present in almost all datasets in Data Foundry, which are derived from the resources that the items are connected to. Ok, that was a bit abstract. Let's go step by step: every project in Data Foundry can have participants, devices and wearables. These are called resources and they can have their own meta-data. For example, if you collect survey data from different participants of a study, you might want to label or tag the participants "experiment" or "control" according to they belong to the experimental group or control group. The two labels, "experiment" and "control", can be captured in a public parameter for every participant. When you collect data from the participant, these data will then be tagged as well with "experiment" or "control", depending on the participant who entered the data.

You can have up to three of these public parameters. for every participant, device, or wearable in your project. If you don't use them, they will just be empty. Why do we do this? We want to avoid accidentally exporting privacy-sensitive participant information with a dataset. Makes sense, right?

## Project Metadata
If you want to publish or share your datasets, you might want to fill in more of the project metadata, to make it easier to trace back where it comes from. For example if you create a dataset for a paper, you can add the link to the paper or the DOI of the paper to related section that can be found in the project settings. Here you can also fill in what your organization or institution is. 

## Upload to Zenodo
If you think your dataset might be valuable for future research, or it is essential to your research as is, you can think about uploading your dataset to Zenodo. Zenodo is a free repository that allows you to publish more than just papers, and is generally used to share datasets and other data based artifacts. Data Foundry is able to publish datasets directly to Zenodo through our fairly integration. This means that is super easy to share and publish your data. For this you do need to [register an Orcid ID however.](https://orcid.org/). You can start the upload process by opening your Data Foundry project and clicking the publish button. Here you can select the option "Publish Dataset", but before you do make sure to first fill in the author information and metadata!

---
