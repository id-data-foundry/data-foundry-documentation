---
layout: default
title: Diary Dataset
parent: Datasets
has_children: true
has_toc: false
---

# Diary Dataset

The Diary Dataset is your go-to solution for collecting rich, qualitative textual data—diary entries—from or about the participants in your study. It serves as a structured journal where day-to-day experiences, reflections, and observations can be recorded. This dataset is invaluable for studies where understanding the personal context and subjective experiences of participants is key. Whether you, as a researcher, are making observational notes or participants are sharing their own stories, the Diary Dataset keeps it all organized.

The diary dataset allows to capture qualitative data in a simple textual form from participants about participants of a study. Participants can submit own "diary entries" directly as part of their study participation.

Each entry in the dataset is more than just a piece of text. It's a structured record containing a `title`, the `text` of the entry, and a `timestamp`. Crucially, every entry is linked to a specific participant via their `participant_id`. To make data analysis easier, each entry also captures the participant's three public parameters (`pp1`, `pp2`, `pp3`), which are configurable labels you can assign to your participants (for instance, a group name or a pseudonym). This ensures that every piece of qualitative data is neatly contextualized.

Data Foundry offers flexible ways to contribute to a Diary Dataset. Researchers can add entries directly through the web interface. For participants, you can configure a template for the diary entry form to provide prompts or structure, guiding them on what to write about. The platform is also designed for integration with external tools; for example, participants could submit their diary entries through a chat application like Telegram, making the process feel natural and accessible. All entries can be viewed within Data Foundry, and for deeper analysis, the entire dataset can be exported as a CSV file. You can even filter the export to include entries only from a specific **Cluster** of participants, helping you to focus your analysis.

## Configuring a Diary Dataset

When you set up a Diary Dataset, you have several configuration options to guide participants and manage data flow.

A unique feature is the **Diary template**. In the main configuration panel, you can write a default text that will appear in the diary entry form for participants. You can use this to pose a question, provide instructions, or simply offer a gentle prompt to help them start writing.

In the "Configuration" section, you'll also find tabs for data export and integration:

*   **CSV/JSON Download:** This tab lets you generate a public URL (using an access token) to download all the diary entries into a single file, which is ideal for detailed qualitative analysis in other software.
*   **Forward data to OOCSI:** This tab allows you to specify an OOCSI channel to stream diary entries to an OOCSI network, enabling real-time monitoring or integration with other connected devices and applications.

## Example

We are using the Diary dataset in the **Object Ethnography** use-case.
