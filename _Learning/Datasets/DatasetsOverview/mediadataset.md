---
layout: default
title: Media Dataset
parent: Datasets
has_children: true
has_toc: false
---

# Media Dataset

The Media Dataset is specifically designed for storing, displaying, and annotating image files. It's the ideal choice when your research involves collecting visual data, such as photos from participants, images from a field study, or any other standard image format like PNG, JPG, or GIF. This dataset provides a centralized and organized home for all your project's visual materials. The media dataset stores image files (no video or audio files at this moment). If you have an **Annotation Dataset** in your project, you can annotate the images as well when you go to the dataset page (right side of image entry). You can also show the images in the data tool to visualize, annotate, or export them.

When uploading images, you have the option to associate each file with a specific `Participant` registered in your project. This is a crucial feature for keeping your data organized and ensuring that you can easily track the source of each image. The dataset is more than just a file repository; it includes a built-in image server that handles on-the-fly thumbnail generation and image scaling. This optimizes performance significantly, ensuring that your web browser doesn't get bogged down when you're browsing through hundreds or thousands of high-resolution images.

A key feature of the Media Dataset is its deep integration with the [Annotation Dataset](./annotationdataset.md). The user interface provides tools to directly add annotations to your images, allowing you to capture notes, observations, and codes right alongside the visual data. This creates a powerful link between your qualitative insights and the media they relate to. To suit different workflows, the dataset offers both a traditional table-like list view and a more visual tile view for browsing your collection of images.

## Configuring a Media Dataset

While the primary way to interact with a Media Dataset is by uploading images through the user interface, its configuration options are focused on enabling programmatic access and data export. In the "Configuration" section, you will find tabs to manage how data flows in and out of the dataset:

*   **HTTP data upload:** This tab is essential for uploading images from an external application or script. Here, you can generate or delete the **HTTP API Token** that must be included in HTTP POST requests for authentication.
*   **CSV/JSON Download:** This tab allows you to generate a **Public CSV/JSON Access Token** to create a public URL for downloading a structured file with metadata about all your media files, including participant associations and descriptions.
*   **Forward data to OOCSI:** This tab can be configured to specify an **OOCSI Output Channel** that sends a message every time a new media file is uploaded, enabling real-time integrations.
