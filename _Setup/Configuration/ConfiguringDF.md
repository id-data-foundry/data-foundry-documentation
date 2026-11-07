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

## AI Processing & Voice Services

Data Foundry supports AI-powered features connected to local model engines or OpenAI-compatible APIs, including dual Speech-to-Text backends for longform batch transcription and real-time streaming recognition.

```hocon
df {
    processing.ai {
        # Base URL for the text/vision AI API (local or remote)
        baseurl = "http://localhost:9191/v1"
        # API key if required by the provider
        key = ""

        # Speech-to-Text Services
        stt {
            # Longform batch audio file transcription (Parakeet TDT / Whisper)
            longform.url = "http://localhost:8092"
            # Real-time low-latency streaming STT over WebSocket (Sherpa-ONNX)
            realtime.url = "http://localhost:8093"
        }

        # Concurrency & queue lanes for AI requests
        lanes {
            text {
                concurrency = 4
                queue = 8
                timeout = 120s
            }
            vision {
                concurrency = 2
                queue = 4
                timeout = 180s
            }
            stt {
                concurrency = 2
                queue = 4
                timeout = 300s
            }
            stt_realtime {
                concurrency = 8
                queue = 16
                timeout = 600s
            }
            tts {
                concurrency = 2
                queue = 4
                timeout = 120s
            }
            embedding {
                concurrency = 4
                queue = 8
                timeout = 60s
            }
        }
    }
}
```

## External Vendors & Academic Integrations

Data Foundry can integrate with academic discovery platforms like Semantic Scholar:

```hocon
idp {
    vendors {
        semanticscholar {
            # Optional Semantic Scholar API key for paper and author lookups
            api_key = ""
        }
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

## System Notifications & Alerts

Data Foundry can send system error alerts and AI service health notifications to Slack, Ntfy, and Pushover.

```hocon
df {
    notifications {
        enabled = true
        channels {
            slack {
                enabled = true
                webhook_url = "https://hooks.slack.com/services/..."
            }
            ntfy {
                enabled = false
                topic = "datafoundry-alerts"
                server = "https://ntfy.sh"
            }
            pushover {
                enabled = false
                user = ""
                token = ""
            }
        }
    }
}
```

For full setup instructions and channel options, see the **[System Notifications & Alerts Guide]({% link _Setup/Configuration/Notifications.md %})**.