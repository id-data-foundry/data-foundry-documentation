---
layout: default
title: Authentication
parent: Configuration
nav_order: 2
has_children: true
has_toc: false
---

# Configuring Authentication

Data Foundry supports multiple ways to manage user access and authentication. This guide covers how to configure administrators, set up Single Sign-On (SSO), and manage registration access.

## Administrator Access

Administrators are super-users who can manage the Data Foundry instance, including user management, project oversight, and system settings.

To configure administrators, edit the `conf/application.conf` file in your Data Foundry installation. Locate the `df.users` block:

```hocon
df {
    users {
        # list of admin user email addresses
        admins = ["admin@example.org"]
        
        # list of librarians user email addresses (can curate datasets)
        librarians = ["librarian@example.org"]
        
        # list of moderator user email addresses
        moderators = ["mod@example.org"]
        
        # list of reviewers' email addresses (for project reviews)
        reviewers = ["reviewer@example.org"]
    }
}
```

Add the email addresses of the users you wish to grant admin privileges to the `admins` list. These users must log in to the platform to access the Admin Portal.

## Single Sign-On (SSO)

Data Foundry supports OpenID Connect (OIDC) for Single Sign-On. This allows users to log in using their existing institutional or organizational credentials (e.g., Microsoft Entra ID / Azure AD).

To configure SSO, update the `df.sso` block in `conf/application.conf`:

```hocon
df {
    sso {
        # The Client ID provided by your Identity Provider (IdP)
        client = "YOUR_CLIENT_ID"
        
        # The Client Secret provided by your IdP
        secret = "YOUR_CLIENT_SECRET"
        
        # The Tenant ID (common for Microsoft/Azure setups)
        tenant = "YOUR_TENANT_ID"
        
        # The Discovery URL (well-known endpoint) for your IdP
        # e.g., https://login.microsoftonline.com/{tenant_id}/v2.0/.well-known/openid-configuration
        discovery = "https://login.microsoftonline.com/YOUR_TENANT_ID/v2.0/.well-known/openid-configuration"
    }
}
```

Once configured, a "Sign in with SSO" option will appear on the login page.

## Registration Keys

If you want to restrict registration to specific users (e.g., for a private instance or internal testing), you can configure registration keys. Users will need to provide a valid key to sign up.

Configure this in the `df.keys` block:

```hocon
df {
    keys {
        # List of valid registration codes
        registration = ["secret-code-1", "class-2026-signup"]
    }
}
```

Leave this list empty or remove it if you want to allow open registration (depending on your instance's specific custom logic, usually registration is open by default or restricted to SSO domains).