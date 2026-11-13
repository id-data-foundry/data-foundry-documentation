---
layout: default
title: Instance configuration
parent: Configuration
nav_order: 0
---

# Configuring your Data Foundry instance

The core configuration of Data Foundry is handled via the `conf/application.conf` file (which inherits defaults from `conf/reference.conf`). This guide walks through the main configuration blocks. For a complete key-by-key lookup table, see the **[Configuration Key Reference]({% link _Setup/Configuration/ConfigurationReference.md %})**.

---

## Basic Configuration

### Base URL
Ensure `df.base_url` matches the public URL where your instance is accessible (including port if non-standard). It is used for redirects, invitations, and link generation.

```hocon
df {
    base_url = "https://data.your-university.edu"
}
```

### Upload Directory
Specify where uploaded files (images, datasets) should be stored. Always include a trailing slash.

```hocon
df {
    # specify upload directory with trailing slash
    upload_directory = "data/"
}
```

### Project Limits & Feedback Link
You can limit the number of active projects per user and optionally expose a feedback form link in the UI:

```hocon
df {
    max_active_projects = 20
    # feedback_link = "https://your-org.edu/feedback"
}
```

### Dataset Web Delivery & External Web Proxy (`df.web_proxy`)
Data Foundry allows projects to host static websites (HTML, Markdown, and supporting assets) directly inside datasets. Because user-authored HTML and JavaScript can run in a visitor's browser, Data Foundry isolates that content from the main platform session:

* **Built-in sandboxed delivery (default):** If `df.web_proxy` is omitted or left empty (`""`), Data Foundry serves dataset-hosted pages via its own `/web/<token>/...` routes in a sandboxed frame.
* **External web proxy (recommended for production):** When `df.web_proxy` is set to a separate origin (domain), Data Foundry strips any trailing slashes and routes dataset web URLs to `<proxyBase>/<requestHost>/<token>/<fileName>`. Serving user-hosted pages from a dedicated domain (such as `https://sites.data-foundry.net`) isolates browser origin and session cookies from your main Data Foundry domain without relying on restrictive iframe `sandbox` attributes.

```hocon
df {
    # External web proxy for dataset-hosted websites (e.g. https://sites.data-foundry.net)
    # If omitted or empty, Data Foundry uses built-in sandboxed web delivery
    web_proxy = "https://sites.data-foundry.net"
}
```

> Note: If you enable `df.web_proxy`, you must deploy and configure the external proxy service separately to forward `<proxyBase>/<host>/<token>/...` requests back to your Data Foundry instance's `/web/...` endpoint.

---

## Branding & Links

You can customize the footer links, support links, and organization branding to match your institution:

```hocon
df {
    links {
        organization = "Your Organization Name"
        about = "https://your-org.edu/about"
        contact = "https://your-org.edu/contact"
        privacy = "https://your-org.edu/privacy"
        scientific_integrity = "https://your-org.edu/integrity"
        data_protection = "https://your-org.edu/data-protection"
        organization_logo = "https://your-org.edu/logo.png"
        teams_community = ""
    }
}
```

---

## Python Processing

Data Foundry uses Python for certain data processing tasks (e.g., generating exports). Ensure the Python executable path is correct for your environment.

```hocon
df {
    processing.python = "python3" # or /usr/bin/python3
}
```

---

## AI Processing & Voice Services

Data Foundry supports AI-powered features connected to local model engines or OpenAI-compatible APIs, including dual Speech-to-Text backends for longform batch transcription and real-time streaming recognition.

```hocon
df {
    processing.ai {
        # Base URL for the OpenAI-compatible AI API (local or remote)
        baseurl = "http://localhost:9191/v1"
        # API key if required by the provider
        key = ""

        # Optional dedicated image generation endpoint
        # images.url = "http://localhost:8094/v1"

        # Token limits
        default_max_tokens = 4096
        agent_max_tokens = 8192

        # Streaming timeouts
        stream {
            # Fail the stream only if the backend goes silent this long
            idle_timeout = 90s
            # Absolute backstop for one streamed response
            max_duration = 30m
        }

        # Speech-to-Text Services
        stt {
            # Longform batch audio file transcription and diarization
            longform.url = "http://localhost:9191/v1"
            # Real-time low-latency streaming STT over WebSocket
            realtime.url = "ws://localhost:9191/v1/audio/stream"
        }

        # Default model identifiers per capability
        models {
            default = "hermes-2-pro-llama-3-8b"
            chat = "hermes-2-pro-llama-3-8b"
            vision = "llava-llama-3-8b-v1_1"
            coding = "qwen/qwen3.6-27b"
            # coding_subagent = "qwen/qwen3.6-27b"
            text = "openai/gpt-oss-20b"
            translate = "apertus-8b"
            image = "Flux-schnell"
            # image_edit = "Flux-fill"
            # stt = ""
            # tts = ""
        }

        # Per-category AI concurrency & queue lanes
        # (Also supports fallback under df.ai.lanes.*)
        lanes {
            llm          { concurrency = 16, queue = 64, timeout = 120s  }
            stt          { concurrency = 1,  queue = 32, timeout = 1800s }
            stt_realtime { concurrency = 8,  queue = 16, timeout = 600s  }
            tts          { concurrency = 1,  queue = 32, timeout = 60s   }
            image        { concurrency = 1,  queue = 16, timeout = 600s  } # max_per_user defaults to 2
            embedding    { concurrency = 1,  queue = 32, timeout = 60s   }
            models       { concurrency = 0,  queue = 0,  timeout = 5s    } # 0 = unlimited, cached
        }
    }
}
```

Each lane also accepts an optional `max_per_user` limit (which defaults to `2` for `image` and unlimited `-1` for all other lanes).

---

## Email & Microsoft Graph

Data Foundry can send transactional emails via Microsoft Graph (Office 365) or fall back to standard SMTP (`play.mailer`).

```hocon
df {
    msgraph {
        from = ""
        client = ""
        secret = ""
        tenant = ""
        # discovery = "https://login.microsoftonline.com/YOUR_TENANT_ID/v2.0/.well-known/openid-configuration"
    }
}

# Optional SMTP fallback
play.mailer {
    from = ""
    host = ""
    username = ""
    password = ""
}
```

---

## OOCSI Server

Data Foundry relies on OOCSI for real-time data streaming. Point this to your OOCSI server instance:

```hocon
df {
    oocsi_server = "oocsi.your-org.edu"
}
```

---

## System Notifications & Alerts

Data Foundry can send system error alerts and AI service health notifications to Slack, Ntfy, and Pushover.

```hocon
df {
    notifications {
        enabled = true
        channels {
            slack {
                enabled = true
                # Full webhook URL (or specify only `key = "T00/B00/XXX"`)
                url = "https://hooks.slack.com/services/..."
            }
            ntfy {
                enabled = false
                server = "https://ntfy.sh"
                topic = "datafoundry-alerts"
                token = ""
                priority = 3
            }
            pushover {
                enabled = false
                token = ""
                user = ""
                priority = 0
            }
        }
    }
}
```

For full setup instructions and AI health monitoring policies, see the **[System Notifications & Alerts Guide]({% link _Setup/Configuration/Notifications.md %})**.

---

## Admin-Relevant Server & Security Settings

When deploying Data Foundry to production, administrators should also review these Play Framework and security settings:

```hocon
# Required in production: unique, secret 64+ character string for signing session cookies
play.http.secret.key = "replace-with-a-long-random-secret-key"

# Session cookie security (set secure = true and your domain in HTTPS production)
play.http.session {
    secure = true
    domain = "data.your-university.edu"
}

# Upload size limits (defaults from reference.conf)
play.http.parser.maxDiskBuffer = 30MB
parsers.anyContent.maxLength = 30MB
parsers.MultipartFormData.maxLength = 30MB

# /.well-known/security.txt (RFC 9116)
df.securitytxt {
    contact = "mailto:security@your-org.edu"
    expires = ""
    preferred-languages = "en, nl"
    policy = "https://your-org.edu/security-policy"
    acknowledgments = ""
}
```
