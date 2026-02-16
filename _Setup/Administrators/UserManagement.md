---
layout: default
title: User Management
parent: Administration
nav_order: 1
---
# User Management

Data Foundry has a robust role-based permission system. Administrators can manage these roles via the `application.conf` file or, for some actions, through the Admin Portal.

## User Roles

*   **User:** Standard user. Can create projects, datasets, and participate in studies.
*   **Librarian:** Can view and curate datasets across the platform to ensure data quality and FAIR principles.
*   **Moderator:** Can manage content and handle reported projects or users.
*   **Reviewer:** Can access projects requesting a scientific/ethical review.
*   **Admin:** Full system access.

## Managing Permissions

To assign special roles (Admin, Librarian, etc.), you currently need to edit the `df.users` section in `conf/application.conf` and restart the application.

```hocon
df {
    users {
        admins = ["admin@example.org"]
        librarians = ["lib@example.org"]
        # ...
    }
}
```

## User Actions

In the Admin Portal, you can:
*   **Search Users:** Find users by email or name.
*   **View Activity:** See recent projects and logins.
*   **Deactivate:** Temporarily disable a user account if necessary.
