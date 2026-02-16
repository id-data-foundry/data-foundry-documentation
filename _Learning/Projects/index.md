---
layout: default
title: Projects
nav_order: 1
has_children: true
has_toc: false
---

# Projects

Projects are the central organizational unit in Data Foundry. A project bundles datasets, scripts, participants, and devices, and allows you to manage the entire lifecycle of your design research data.

When you open a project, you are presented with several perspectives (tabs) to manage different aspects of your work.

## General (Home)

The **General** tab acts as the landing page and dashboard for your project. Here, you define the core identity of your research. You can view and edit the project's name, introduction, and keywords, which help you and others identify the project later. This section also allows you to leave **Remarks**, which are internal notes useful for keeping your team aligned on the project's goals or current status.

This page is also your primary monitor for the **Project Status**. Data Foundry enforces a strict data life-cycle to ensure privacy and compliance. You will see visual indicators (like progress bars and colored alerts) regarding the project's duration. Crucially, this is where you will be notified if your project is **Approaching De-identification** (where personal data is stripped) or **Approaching Freeze** (where data is archived and removed from the active database).

Finally, the General view is the hub for **Team Management** and **Resources**. You can manage the people involved in your project by assigning different roles, which determine their level of access and control. It also lists all the **Datasets** and **Scripts** associated with the project, giving you quick access to the actual data and logic driving your research.

### Project Metadata

Beyond the basic identity of your project, Data Foundry allows you to add rich metadata. This is not just "admin work"; it is crucial for making your data **Findable, Accessible, Interoperable, and Reusable (FAIR)**. Good metadata ensures that others (and your future self!) can understand the context, origin, and legal terms of your research data.

You can edit these details by clicking the **Edit** button on the General tab. Here are some key fields to consider:

*   **Project Introduction**: This is more than just a description for you. It is often displayed to participants during the consent process, so write it with a clear, non-technical voice that explains the purpose and value of the study.
*   **License**: Choosing a license (such as MIT or Creative Commons) is essential if you plan to [share your data]({% link _Learning/Datasets/index.md %}). It clearly defines how others can legally use your work.
*   **Organization & Relation**: These fields provide context. Use **Organization** to credit your lab or funding body, and **Relation** to link to related publications or other datasets (e.g., "Supplementary data for [Publication Title]").
*   **DOI (Digital Object Identifier)**: If your dataset supports a publication, entering the DOI here creates a permanent link to the official record, making your work easier to cite.

Taking the time to complete this information significantly increases the long-term value of your research.

### Team Roles and Permissions

Managing a research project often requires a team with varying levels of responsibility. Data Foundry facilitates this through a structured permission system based on three roles: **Owners**, **Collaborators**, and **Subscribers**. Each role is designed to support a specific level of engagement with the project, from total administrative control to simple observation.

The **Project Owner** is typically the designer or design researcher who initiated the project. This role carries the highest level of responsibility. Owners can modify any aspect of the project, including its core metadata, datasets, and scripts. Most importantly, Owners are the "gatekeepers" of the project; they are the only users with the power to manage the research team by inviting new **Collaborators** or removing existing ones. They also handle critical lifecycle actions, such as archiving or reopening a project.

**Collaborators** represent the active research team. When a user is added as a collaborator, they gain full access to all the technical and administrative tabs of the project, such as Sources, Study Setup, and Timeline. They can create and edit datasets, write and execute scripts, and manage participant information. This role is ideal for co-researchers, student assistants, or technical partners who need to perform the day-to-day tasks of data collection and analysis but do not need administrative control over the team membership itself.

Finally, the **Subscriber** role is intended for stakeholders who need to stay informed about the project without directly participating in the research. Subscribers can view the project’s home page and its general description even if the project is set to "Private." This is particularly useful for supervisors or project partners who want to follow progress. Subscribing often involves a formal step of accepting the project's license, ensuring that even passive observers are aware of the data usage terms. Unlike collaborators, subscribers cannot see research-sensitive data like individual participant details or technical configurations.

## Sources

The **Sources** tab is the bridge between your digital project and the physical world. It manages the "inputs" and "actors" that generate data. This includes **Devices** (such as OOCSI-enabled prototypes), **Participants** (the human subjects of your study), and **Wearables** (integration with services like FitBit or Google Fit).

In this view, you can manage the inventory of devices connected to your project and, more importantly, manage your **Participants**. You can add participants individually to track specific metadata or use the bulk addition tools to onboard groups quickly. This is also where you establish links between specific participants and the devices or wearables they are using, enabling you to attribute data streams to specific individuals.

For a deep dive into connecting devices and managing participants, see the [Sources guide]({% link _Learning/Projects/Sources.md %}).

## Study Setup

The **Study Setup** perspective is dedicated to the logistical, ethical, and administrative aspects of running a user study. Unlike the technical data management tabs, this section focuses on the human element. It allows you to configure how participants interact with your system, specifically regarding the sign-up process and their legal rights.

A key feature here is the management of **Informed Consent**. You can upload and configure consent forms that participants must agree to before joining the study. This ensures your research complies with ethical standards and regulations (like GDPR). You can also organize and distribute **Study Materials**, such as instruction PDFs or other documents that participants need to access during their participation.

You can also control the **Activation** of various study features. Not every project is a full-blown user study; some might just be technical tests. This section lets you toggle features on and off, keeping your interface clean and focused on the tools you actually need for your current phase of work.

## Timeline

The **Timeline** view provides a visual Gantt-chart representation of your project's life-cycle. It maps out the "Project Phase" (when the project is active), the period after data collection stops, and the scheduled dates for automatic **Deidentification** and **Project Freeze**. This visualization helps you plan your research activities and ensures you aren't caught off guard by automatic data policies.

Below the main project timeline, you can see the individual durations for all your **Datasets** and **Participants**. Since different parts of a study might run for different periods, this view helps you verify that all your data collection buckets are active exactly when they need to be.

Crucially, this is where you handle **Extensions**. Research often encounters delays. If you need more time for data collection, the Timeline view allows you to extend the duration of the project and all its operational datasets. You can typically extend the project by 1, 2, or 3 months with a single action, updating all associated expiration dates in sync.

## Narrative Surveys

**Narrative Surveys** are a specialized feature for creating interactive, branching stories that function as data collection tools. Unlike traditional linear surveys, narrative surveys allow participants to make choices that influence the story's outcome. These choices are recorded as data, allowing you to analyze decision-making processes and perspective-taking.

In this tab, you can access the **Authoring Tool** to write your stories, upload images to embed within them, and manage the deployment of these surveys to your participants. Once data starts coming in, you can access specific **Data Analysis** views to visualize the paths participants took through your narrative.

For more details on creating and analyzing these stories, refer to the [Narrative Surveys guide]({% link _Learning/Projects/NarrativeSurveys.md %}).
