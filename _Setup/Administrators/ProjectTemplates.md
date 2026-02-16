---
layout: default
title: Project Templates
parent: Administration
nav_order: 6
---

# Flexible Project Templates

Data Foundry supports a flexible, folder-based template system that allows you to quickly scaffold new projects with predefined datasets and files.

## How it Works

Templates are discovered from the `dist/templates/` directory in the project root. Each subdirectory within this folder represents a standalone project template.

### Directory Structure

To create a new template, follow this structure:

```text
dist/templates/
└── [TemplateName]/              <-- This becomes the template name in the UI
    ├── [DatasetNameA]/          <-- A "COMPLETE" dataset will be created with this name
    │   ├── data.csv             <-- Files to be pre-loaded into the dataset
    │   └── documentation.pdf
    └── [DatasetNameB]/          <-- Another "COMPLETE" dataset
        └── initial_config.json
```

### Dataset Creation
- **Dataset Type:** Every folder inside a template directory is automatically created as a **COMPLETE** dataset. 
- **Files:** All files located directly inside a dataset folder are copied into the newly created dataset in the Data Foundry project.
- **Database Records:** For every file copied, a corresponding record is added to the dataset's database table so they appear immediately in the file list.

## Usage Instructions

### 1. Prepare the Template (Admin)
1.  Access the Data Foundry server files.
2.  Create a new folder under `dist/templates/`.
3.  Create subfolders for the datasets you want to include.
4.  Add the desired files into those subfolders.

### 2. Create a Project (User)
1.  Log in to Data Foundry.
2.  Navigate to **Add New Project**.
3.  Open the **Advanced settings** section.
4.  Your new template will appear in the **Choose an optional project template** dropdown.
5.  Fill in the project name and introduction, select your template, and click **ADD**.

### 3. Outcome
*   Data Foundry will create the project.
*   It will automatically create all datasets defined in your template.
*   It will populate those datasets with the files you provided.
*   The project description will be set to: `Created from template: [TemplateName]`.

## Technical Notes

- The system still supports hardcoded templates (like `wearable` or `iot_devices`). If a template name exists both as a folder and a hardcoded case, the folder-based template takes precedence.
- If you are running in a development environment, ensure the `dist/templates` folder is reachable from the working directory.
