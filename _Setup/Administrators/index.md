---
layout: default
title: Administration
nav_order: 4
has_children: true
has_toc: true
---

# Administration Guide

To make hosting a large Data Foundry instance easier, we built several administration and management tools into the platform. These tools allow administrators to manage users, archive projects, manage AI API access, and backup the database.

## Configuring Administrators

Admin users are configured in the `application.conf` file. By default, no user is assigned as an admin. To configure a new administrator, open the `conf/application.conf` file and locate the `users` section:

```hocon
users {
        # List of admin user email addresses
        admins = ["admin@example.org"]

        # List of librarians email addresses
        librarians = ["librarian@example.org"]

        # List of moderator email addresses
        moderators = ["moderator@example.org"]

        # List of reviewers email addresses
        reviewers = ["reviewer@example.org"]
}
```

Add the email addresses of the desired administrators to the `admins` list. After adding the emails, restart the Data Foundry container for the changes to take effect.

## Accessing the Admin Portal

To access the admin portal, authenticated administrators simply append `/admin` to the Data Foundry instance URL:

`{{ site.external_base_urls.datafoundryurl }}/admin`

{% include df-link.html text="Go to the Admin Portal" path="/admin" %}

## Admin Portal Dashboards

The Admin Portal consists of several dashboards for specialized tasks:

- **[Instance Overview]({% link _Setup/Administrators/Overview.md %})**: General system status and statistics.
- **[User Management]({% link _Setup/Administrators/UserManagement.md %})**: Manage user roles and access.
- **[Project Archival]({% link _Setup/Administrators/ProjectsArchival.md %})**: Handle end-of-life projects.
- **[API Settings]({% link _Setup/Administrators/APISettings.md %})**: Manage AI API keys and token distribution.
- **[Project Templates]({% link _Setup/Administrators/ProjectTemplates.md %})**: Configure global project templates.
