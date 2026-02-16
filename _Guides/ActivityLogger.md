---
layout: default
title: Activity Logger Guide
nav_order: 7
parent: How-To Guides Overview
---

# Activity Logger Guide

## Introduction

The Activity Logger is a tool within DataFoundry that allows users to log various activities, both instantaneous ("direct event activities") and continuous ("state activities"), to a dataset. This guide will walk you through setting up and using the Activity Logger.

## Setup
1.  **Navigate to the Setup Page:**
    *   Log in to DataFoundry.
    *   Go to `/tools/actilogger` in your browser.
2.  **Select a Project and Dataset:**
    *   On the setup page, use the dropdown menus to select an existing project and a dataset within that project.
    *   Ensure the selected dataset is active and has an API token configured.
    *   (Optional) Select a participant from the dropdown if you want to generate a logger link for a specific participant.
3.  **Define Activities:**
    *   **Direct Event Activities:** Enter the names of activities that you want to log as single, instantaneous events (e.g., "Drinking Water", "Button Press") into the "New direct activity name" field and click "Add".
    *   **State Activities:** Enter the names of activities that have a start and end time (e.g., "Reading", "Working", "Sleeping") into the "New state activity name" field and click "Add".
    *   Activities are saved automatically to the dataset configuration when added or removed (by clicking the 'x' button).

## Using the Activity Logger
1.  **Access the Logger Interface:**
    *   After selecting a dataset, a "Start Activity Logger" button and a QR code will appear. Click the button or scan the QR code to open the logger interface.
    *   Alternatively, you can navigate directly to the logger interface using the URL format: `/tools/actilogger/logger/<projectId>/<datasetId>/<datasetToken>/<participantId>`. Replace the placeholders with your actual project ID, dataset ID, dataset API token, and a participant ID (e.g., "NO_PARTICIPANT" if you are using an "open participation" dataset and haven't selected a specific participant).
2.  **Logging Direct Events:**
    *   On the logger interface, simply click the button corresponding to a "direct event activity". A brief visual cue will confirm that the event has been logged.
3.  **Logging State Activities:**
    *   Click a "state activity" button once to start the activity. The button will change visually (e.g., to a green background with a pulsating effect) to indicate it's "on". This logs `<activity_name>:on`.
    *   Click the same button again to end the activity. The button will revert to its default state, logging `<activity_name>:off`.

## Data Visualization
On the setup page, after selecting a dataset, an "Activity Timeline Visualization" section will display a timeline chart of previously logged activities (fetching data for the last 7 days) using Vega-Lite. This provides immediate feedback on the collected data, showing both discrete events and duration-based state activities. 

Note: In the visualization, if a state activity is ended within 60 seconds of starting, it is typically visualized as a direct event point rather than a bar.
