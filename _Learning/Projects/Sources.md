---
layout: default
title: Sources
parent: Projects
nav_order: 0
---

# Sources

In Data Foundry, **Sources** are the entities that generate or provide data for your project. This includes the physical devices you build, the participants who join your study, the wearable technology they might use, and even the direct communication channels you establish with them.

The **Sources** tab in your project view is your command center for managing all these inputs. It provides a comprehensive overview of every connected entity and allows you to configure, monitor, and interact with them directly.

## Devices

Devices in Data Foundry typically represent the IoT prototypes, sensor kits, or data loggers you deploy in the field. Whether it's a custom-built sensor station based on an ESP32, a Raspberry Pi gateway, or a connected artifact, you register it here as a device.

When you add a device, Data Foundry generates unique identifiers and keys that allow your hardware to securely authenticate and send data to the platform. You can manage these credentials directly from the list, ensuring that if a device is compromised or lost, you can revoke access for that specific unit without affecting the rest of your deployment.

For technical details on connecting your hardware, check out the [Data Foundry Clients]({% link _Reference/Clients/index.md %}) section or the [API Reference]({% link _Reference/DFapi.md %}).

## Participants

Participants are the heart of user-centered research. In this section, you can manage the people taking part in your study. Data Foundry allows you to create profiles for each participant, which then serve as the central hub for all data collected about or by that person—be it through surveys, wearable data, or manual annotations.

You can add participants individually if you are running a small, qualitative study, or use the "Many people" bulk-import feature to add a large cohort via email addresses. Once registered, participants can be linked to specific devices or wearables, allowing you to trace data back to its human source easily.

## Wearables

If your research involves physiological data or activity tracking, the Wearables section allows you to integrate commercial platforms like FitBit or Google Fit directly into your project.

By connecting a participant's wearable account, Data Foundry can automatically sync their activity data (like steps, heart rate, or sleep) into your project's datasets. This requires prior configuration of the platform (usually by your server administrator), but once set up, it provides a seamless flow of health data alongside your custom IoT metrics.

## Communication

Keeping in touch with your participants is crucial for longitudinal studies. Data Foundry supports integration with messaging platforms like Telegram, allowing for two-way communication directly from the project interface.

You can view a log of all messages exchanged with a participant, which is helpful for gaining context during analysis. Furthermore, you can send messages to individual participants—perhaps to troubleshoot an issue or ask a follow-up question—or broadcast a message to your entire study cohort to send reminders or updates.

## Clusters

As your project grows, managing dozens of participants and devices individually can become overwhelming. This is where **Clusters** come in. Clusters allow you to group related resources together—for example, grouping a family's devices and participants into a "Household A" cluster, or grouping a specific cohort of participants together.

### Organizing with Clusters
You can create clusters to reflect the logical structure of your deployment. A cluster might contain:
*   **Participants**: The specific people belonging to a group.
*   **Devices**: The hardware deployed to that group.
*   **Wearables**: The trackers worn by those participants.

This grouping isn't just for organization; it's a powerful tool for data management. When you view a cluster, you get a filtered view of the data, allowing you to monitor the activity of that specific group in isolation.

### Data filtering and Annotation
One of the most powerful features of clusters is data filtering. Instead of downloading a massive dataset containing everyone's data and filtering it manually, you can download datasets specifically for a cluster. This is incredibly useful for case-by-case analysis.

Additionally, clusters support **Annotations**. You can record qualitative observations or notes at the cluster level. If you are conducting a field deployment where you visit households, you can use cluster annotations to keep a field log specific to that household.

For a step-by-step guide on setting this up, please refer to the [Clusters Guide]({% link _Guides/ProjectManagement/Clusters.md %}).
