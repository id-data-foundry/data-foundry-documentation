---
layout: default
title: Dataset API reference
nav_order: 3
has_children: true
has_toc: false
---

# Dataset Reference

This page provides technical reference information for the Data Foundry dataset structures, specifically the CSV and JSON export formats for each dataset type.

## Entity Dataset

Used for storing generic JSON objects linked to a resource ID.

### CSV Export
*   **Standard Columns:** `id`, `resource_id`, `ts`, `pp1`, `pp2`, `pp3`, `data` (contains the full JSON object).
*   **Projected Export:** `id`, `resource_id`, `ts`, `pp1`, `pp2`, `pp3`, followed by columns defined in the dataset projection. The `data` column is parsed, and keys matching the projection are extracted as separate columns.

### JSON Structure
*   **Fields:** `id`, `resource_id`, `ts`, `pp1`, `pp2`, `pp3`.
*   **Data Handling:** The contents of the stored JSON object are merged into the root object.

## IoT Dataset

Optimized for time-series data from devices, including activity labels.

### CSV Export
*   **Standard Columns:** `id`, `device_id`, `ts`, `activity`, `pp1`, `pp2`, `pp3`, `data` (contains the full JSON object).
*   **Projected Export:** `id`, `device_id`, `ts`, `activity`, `pp1`, `pp2`, `pp3`, followed by columns defined in the dataset projection.

### JSON Structure
*   **Fields:** `id`, `device_id`, `ts`, `activity`, `pp1`, `pp2`, `pp3`.
*   **Data Handling:** The contents of the stored JSON object are merged into the root object.

## Existing Dataset

Used for managing collections of files (e.g., images, documents) with metadata.

### CSV Export
*   **Columns:** `id`, `dataset_id`, `ts`, `link` (URL to the file), `description`.

### JSON Structure
*   **Fields:** `id`, `ts`, `file_name`, `description`.

## Form Dataset

Stores responses from simple forms.

### CSV Export
*   **Standard Columns:** `id`, `ts`, `data` (verbatim).
*   **Projected Export:** `id`, `ts`, followed by columns defined in the dataset projection.

### JSON Structure
*   **Fields:** `id`, `ts`.
*   **Data Handling:** The contents of the stored JSON object are merged into the root object.

## Survey Dataset

Stores responses from surveys, linked to specific participants.

### CSV Export
*   **Standard Columns:** `id`, `participant_id`, `ts`, `data` (verbatim).
*   **Projected Export:** `id`, `participant_id`, `ts`, followed by columns defined in the dataset projection.

### JSON Structure
*   **Fields:** `id`, `participant_id`, `ts`.
*   **Data Handling:** The contents of the stored JSON object are merged into the root object.

## Media Dataset

Manages media files uploaded by participants.

### CSV Export
*   **Columns:** `id`, `participant_id`, `ts`, `link`, `mediatype`, `description`, `pp1`, `pp2`, `pp3`.

### JSON Structure
*   **Fields:** `id`, `participant_id`, `ts`, `link`, `mediatype`, `description`, `pp1`, `pp2`, `pp3`.

## Movement Dataset

Stores geolocation and movement data (GPX tracks).

### CSV Export
*   **Columns:** `id`, `participant_id`, `ts`, `lng` (longitude), `lat` (latitude), `ele` (elevation), `track`, `pp1`, `pp2`, `pp3`, `atemp`, `hr`, `cad`.
*   **Note:** `lng`, `lat`, `ele` correspond to `x`, `y`, `z` internally. `atemp`, `hr`, `cad` are extracted from the `data` field.

### JSON Structure
*   **Fields:** `id`, `participant_id`, `ts`, `x`, `y`, `z`, `track`, `pp1`, `pp2`, `pp3`.
*   **Data Handling:** The contents of the stored JSON object are merged into the root object.

## Annotation Dataset

Stores text annotations linked to clusters of data.

### CSV Export
*   **Columns:** `id`, `cluster_id`, `ts`, `title`, `text`.

### JSON Structure
*   **Fields:** `id`, `cluster_id`, `ts`, `title`, `text`.

## Diary Dataset

Stores diary entries or textual logs linked to participants.

### CSV Export
*   **Columns:** `id`, `participant_id`, `ts`, `pp1`, `pp2`, `pp3`, `title`, `entry`.

### JSON Structure
*   **Fields:** `id`, `participant_id`, `ts`, `pp1`, `pp2`, `pp3`, `title`, `text`.

## Fitbit Dataset

Stores data synchronized from Fitbit wearable devices.

### CSV Export
*   **Columns:** `id`, `wearable_id`, `user_id`, `ts`, `pp1`, `pp2`, `pp3`, `data_date`, `heartrate`, `activity`, `calories`, `steps`, `distance`, `floors`, `elevation`, `sleep`, `weight`, `bmi`, `fat`.

### JSON Structure
*   **Fields:** `id`, `wearable_id`, `ts`, `activity`, `calories`, `heart_rate`, `step_count`, `distance`, `floors`, `elevation`, `weight`, `bmi`, `fat`, `sleep`, `pp1`, `pp2`, `pp3`.

## Google Fit Dataset

Stores data synchronized from Google Fit accounts.

### CSV Export
*   **Columns:** `id`, `wearable_id`, `user_id`, `ts`, `pp1`, `pp2`, `pp3`, `data_date`, `activity`, `calories`, `speed`, `heart_rate`, `step_count`, `distance`, `weight`, `sleep`.

### JSON Structure
*   **Fields:** `id`, `wearable_id`, `ts`, `activity`, `calories`, `speed`, `heart_rate`, `step_count`, `distance`, `weight`, `sleep`, `pp1`, `pp2`, `pp3`.


