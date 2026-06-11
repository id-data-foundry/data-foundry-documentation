---
layout: default
title: Instance configuration
parent: Configuration
nav_order: 0
---

# Configuring your Data Foundry instance

The core configuration of Data Foundry is handled via the `conf/application.conf` file. This file allows you to customize the environment, branding, and connected services of your instance.

## Basic Configuration

### Base URL
Ensure the `df.base_url` matches the URL where your instance will be accessible.

```hocon
df {
    base_url = "https://data.your-university.edu"
}
```

### Upload Directory
Specify where uploaded files (images, datasets) should be stored.

```hocon
df {
    # specify upload directory with trailing slash
    upload_directory = "data/"
}
```

## Branding & Links

You can customize the footer links and organization name to match your institution.

```hocon
df {
    links {
        organization = "Your Organization Name"
        about = "https://your-org.edu/about"
        privacy = "https://your-org.edu/privacy"    
        scientific_integrity = "https://your-org.edu/integrity"
        organization_logo = "https://your-org.edu/logo.png"
    }
}
```

## Python Processing

Data Foundry uses Python for certain data processing tasks (e.g., generating exports). Ensure the python executable path is correct for your environment.

```hocon
df {
    processing.python = "python3" # or /usr/bin/python3
}
```

## AI Processing

Data Foundry supports AI-powered features that can be connected to either a local model instance (e.g., LocalAI) or an OpenAI-compatible API.

```hocon
df {
    processing.ai {
        # Base URL for the AI API (local or remote)
        baseurl = "http://localhost:9191/v1"
        # API key if required by the provider
        key = ""
    }
}
```

## OOCSI Server

Data Foundry relies on OOCSI for real-time data streaming. You should point this to your OOCSI server instance.

```hocon
df {
    oocsi_server = "oocsi.your-org.edu"
}
```