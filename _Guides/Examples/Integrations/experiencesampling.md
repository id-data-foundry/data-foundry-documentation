---
layout: default
title: Experience Sampling
parent: Example Projects
nav_order: 2
has_children: true
has_toc: false
---

# Use PIEL Experience Sampling with Data Foundry

Combining qualitative and quantitative data collection, to find comprehensive patterns and insights into the individual differences of movement behaviour.

## Context

Experience sampling is an intensive data collection technique, in which participants are asked to answer a questionnaire (with questions about, for example, mood and context) at several times a day, and usually for several days. By repeatedly measuring thoughts, emotions, perceptions, and behavior, as they occur, a more comprehensive and valid insight into individual differences and changes within the individual are gained. Moreover, associations with contextual variables can be discovered. Furthermore, Collected data can be combined using unified timestamp information, export for data mining or visualization.
EXAMPLE

Experience sampling is often used in the health domain to research our behaviour when looking at mental and physical aspects of the individual. An example of such a study can be a study of the effect of the increase of physical activity for patients suffering from depression. By prompting them to actively track their thoughts, emotions, perception, mood, context, etc. by means of a questionnaire they have to fill in multiple times per day, and relating this to the physical activity they gain during these through the measurement of Fitbit data, new relations and patterns can be found. Hereby, qualitative data collection techniques (such as Diary entries, forms and interviews) are combined with quantitative techniques (heart rate, calories, sleep etc) that are measured with a Fitbit. Later, the researcher can combine both datasets and by means of visualization, data mining and annotation make sense of the data.

![Data Flow]({% link _Guides/Examples/Integrations/images/usecase-experience-sampling.png %})

## What you need to get started

- Wearables for your participant such as a Fitbit or GoogleFit.
- A project created in Data Foundry, including a
    - A Fitbit or GoogleFit dataset (depending on your wearable)
    - Experience Sampling dataset
    - Annotation dataset
    - Optional: Form dataset
- Participants

## How to get started

Start with the basic setup (register or login, create a new project), then:

1. Add a Fitbit or Google Fit dataset
2. Add an Experience sampling dataset
3. Add your participants
4. Add the wearables to the project
5. Optional: Add a Form dataset

### Setup the Experience Sampling dataset

1. Click on the experience sampling dataset you just created
2. Upload your PIEL files by using the upload button in the dataset. Important is that you do not upload data that contains private information. Only upload and share data if you have the right to do so. If in doubt, please check with support.
3. Select the participant whom the data belongs to and provide a short description.

### Setup a Form dataset

1. Create a structure for the Form dataset by going to the dataset page and heading over to the form design section. You can use the functions provided on the bottom of this section to add different items to the firm: single and multi choice, a scale or numerical input, single and multi-line text and grids.
2. Save the dataset when you are happy with the result.
3. Use the token link to send this form to your participants by email.

### Use the Data Export tool: Export, annotate or visualize

1. Go to the Data Tool and select the IoT and Media dataset of this project, and the columns of that dataset that you want to visualize, or export. Click on proceed to continue.
2. Fill in the x and y axis
3. You have the options to filter the data or annotate it. Annotation might be helpful to discover new relations between your IoT dataset and another dataset. Click here for more information on how to annotate items of a media dataset.
4. Change the color of each data column to your own preference
5. Use sampling where needed
6. When you are happy with the result, export the dataset by clicking the export button, or save the visualization as an image by clicking on the button with 3 dots.

