---
layout: default
parent: Admin Settings
title: API Settings
nav_order: 1
---
# API Settings

Data Foundry provides several APIs for programmatic access to data and services.

## Global API Keys

System-wide API keys are configured in `conf/application.conf` under `df.keys`.

*   **`api`**: The master API key for general system access (use with caution).
*   **`auth.api`**: Key for the authentication service.
*   **`v2.user.api`**: Specialized keys for user-centric API operations.

## Project API Keys

Users can generate their own API keys for specific projects.
1.  Go to the **Project Settings** page.
2.  Scroll to **API Access**.
3.  Click **Generate Key**.

This key allows scripts and prototypes to interact *only* with that specific project's datasets.

## Rate Limiting

To protect the system, API endpoints may be rate-limited. If you encounter `429 Too Many Requests` errors, consider optimizing your application to batch requests or reduce polling frequency.
