---
layout: default
title: Public Parameters
parent: Projects
nav_order: 1
---

# Public parameters

Public parameters are extra properties of participants, devices and wearables. These parameters can contain information about a participant, device or wearable that will exported. When working with multiple participants, wearables and devices, these parameters can be helpful in organizing your resources.

Let's go through a quick example with different participants in a study:

    Sign up or login into Data Foundry
    Create a new project or use an existing project and add a dataset and participants.
    When you have add a participant, you can define 3 parameters, these will be pp1, pp2 and pp3. Public parameters are part of participant-related datasets, so don't enter personally-identifiable information here. These parameters contain extra, valuable information. These parameters always contain the same type of information and won’t change their value (unless you change them).

In your study, you have a total of 18 participants that are split up in different ways. First, there is a control group (9 participants) and an experimental group (9 participants). Then, both groups are split by age into three sub groups: age_group_1, age_group_2 and age_group_3. We could continue here, but with 18 participants this will suffice. We can just use the third public parameter for the gender. Now, given the different segment we can assign public parameters to every participant depending on their age and whether they belong into control or experimental group. This could look like the following for just four participants:

Participant Alice

    - pp1: experiment_group
    - pp2: age_group_1
    - pp3: female

Participant Bob

    - pp1: control_group
    - pp2: age_group_1
    - pp3: male

Participant Alex

    - pp1: experiment_group
    - pp2: age_group_3
    - pp3: not given

Participant Vera

    - pp1: control_group
    - pp2: age_group_2
    - pp3: female

After you have collected data from your device on Data Foundry, you can download your dataset including these public parameters which now will be visible in the CSV file. With these parameters you can segment the dataset by age group or timeslot without revealing any personal information about the participants.

You might have noticed that what we call "public parameters" are basically independent variables of a study. Good! Extra points to you. We still like to call them public parameters, because "independent variable" carries more and different meaning than what we have built into Data Foundry.

We gave an example about participants above, but the same is possible for devices and wearables. So you could use public parameters to annotate the country and city location of devices, or age range and training level for wearables--all without releasing personal information into the dataset.