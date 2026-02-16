---
layout: default
title: Survey Dataset
parent: Datasets
has_children: true
has_toc: false
---

# Survey Dataset

The Survey Dataset is designed for creating and distributing surveys specifically to the registered `Participants` within your project. While it uses the same powerful form-building engine as the [Form Dataset]({% link _Learning/Datasets/DatasetsOverview/formdataset.md %}), its key distinction is that every submission is automatically and reliably linked to a known participant. This makes it the perfect tool for collecting structured data from your study's cohort.

Just like the Form Dataset, you create your survey using an intuitive Markdown-based editor that provides a live preview as you build. You have access to the full range of question types, including multiple choice, numerical scales, text fields, and grids. This allows you to build rich, interactive surveys tailored to your research questions. The creation process is designed to be fast and flexible, enabling you to get your survey up and running in minutes.

The critical difference lies in distribution. Instead of a single anonymous link, the Survey Dataset allows you to generate unique, tokenized survey URLs for each individual participant. You can then distribute these personal links via email or any other communication channel. When a participant uses their unique link to complete the survey, their submission is automatically tagged with their `participant_id`. This eliminates any ambiguity about who the response came from. The dataset provides the same great built-in visualization tools and powerful CSV export options as the Form Dataset, giving you everything you need to analyze your participant-specific data.

## Configuring a Survey Dataset

Configuring a Survey Dataset is a process of two halves: designing the survey content and managing its distribution to your participants.

First, you build your survey in the interactive editor on the dataset's main page. Using a flexible Markdown syntax, you can add various question types, with a live preview showing you what participants will see. Once saved, the same page becomes your distribution center. A dropdown menu lists all registered project participants, allowing you to generate a unique, tokenized URL for each person.

Second, the "Configuration" section at the bottom of the page provides standard data export options:

*   **CSV/JSON Download:** This tab allows you to generate a public URL (with an access token) for downloading the collected survey responses.
*   **Forward data to OOCSI:** Here, you can specify an OOCSI channel to forward all new survey submissions to, enabling real-time integrations.
