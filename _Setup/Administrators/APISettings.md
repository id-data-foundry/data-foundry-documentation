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

*   **`registration`**: List of valid registration codes required to sign up when registration is restricted.
*   **`project`**: Secret key used for project-level token operations.
*   **`api`**: The master API key for general system access (use with caution).
*   **`auth.api`**: Key for the authentication service.
*   **`v2.multi.api`**: List of V2 multi-project API keys for trusted external services.
*   **`v2.user.api`**: List of specialized V2 keys for user-centric API operations (convention: service name in the first 8 characters).

```hocon
df {
    keys {
        registration = ["secret-signup-code"]
        project = ""
        api = ""
        auth.api = ""

        v2 {
            multi.api = [""]
            user.api = [""]
        }
    }
}
```

## Project API Keys

Users can generate their own API keys for specific projects.
1.  Go to the **Project Settings** page.
2.  Scroll to **API Access**.
3.  Click **Generate Key**.

This key allows scripts and prototypes to interact *only* with that specific project's datasets.

## Rate Limiting

To protect the system, API endpoints may be rate-limited. If you encounter `429 Too Many Requests` errors, consider optimizing your application to batch requests or reduce polling frequency.
