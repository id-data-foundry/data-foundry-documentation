---
layout: default
title: Media Dataset
parent: Datasets
has_children: true
has_toc: false
---

# Media Dataset

The Media Dataset is specifically designed for storing, displaying, and annotating media files. It's the ideal choice when your research involves collecting visual or auditory data, such as photos or audio recordings from participants, media from a field study, or any other standard media format like PNG, JPG, GIF, MP3, WAV, M4A, OGG, or MP4. This dataset provides a centralized and organized home for all your project's media materials. The media dataset stores images, audio, and video files. If you have an **Annotation Dataset** in your project, you can annotate the media files as well when you go to the dataset page (right side of media entry). You can also show the media files in the data tool to visualize, annotate, or export them.

When uploading media files, you have the option to associate each file with a specific `Participant` registered in your project. This is a crucial feature for keeping your data organized and ensuring that you can easily track the source of each file. The dataset is more than just a file repository; it includes a built-in media server that handles on-the-fly thumbnail generation and scaling for images. This optimizes performance significantly, ensuring that your web browser doesn't get bogged down when you're browsing through hundreds or thousands of high-resolution images. Audio and video files are streamed directly.

A key feature of the Media Dataset is its deep integration with the [Annotation Dataset](./annotationdataset.md). The user interface provides tools to directly add annotations to your media files, allowing you to capture notes, observations, and codes right alongside the data. This creates a powerful link between your qualitative insights and the media they relate to. To suit different workflows, the dataset offers both a traditional table-like list view and a more visual tile view for browsing your collection.

## Configuring a Media Dataset

While the primary way to interact with a Media Dataset is by uploading media files through the user interface, its configuration options are focused on enabling programmatic access and data export. In the "Configuration" section, you will find tabs to manage how data flows in and out of the dataset:

*   **HTTP data upload:** This tab is essential for uploading media files from an external application or script. Here, you can generate or delete the **HTTP API Token** that must be included in HTTP POST requests for authentication.
*   **CSV/JSON Download:** This tab allows you to generate a **Public CSV/JSON Access Token** to create a public URL for downloading a structured file with metadata about all your media files, including participant associations and descriptions.
*   **Forward data to OOCSI:** This tab can be configured to specify an **OOCSI Output Channel** that sends a message every time a new media file is uploaded, enabling real-time integrations.
