---
layout: default
title: System Notifications & Alerts
parent: Configuration
nav_order: 5
---

# System Notifications & Alerts

Data Foundry includes a notification service for system alerts and operational health monitoring. When errors occur or when connected services (such as the local AI backend) become unreachable, Data Foundry can send alerts to one or more external notification channels.

Administrators can configure three notification channels in `conf/application.conf`:
- **Slack**: Posts messages to a Slack channel using incoming webhooks.
- **Ntfy**: Sends push alerts to desktop and mobile devices using a public or self-hosted [ntfy](https://ntfy.sh) server.
- **Pushover**: Sends private push notifications to iOS, Android, and desktop devices using the [Pushover](https://pushover.net) service.

---

## Global Switch

You can enable or disable all notifications using the master switch under the `df.notifications` block:

```hocon
df {
    notifications {
        # Master switch for all system notifications (true/false)
        enabled = true
    }
}
```

If `enabled = false`, no messages are sent through any channel, but recent notifications are still recorded in the admin log.

---

## Notification Channels

You can enable multiple channels at the same time. Each enabled channel receives every outgoing notification.

### 1. Slack

To send notifications to a Slack channel, create an incoming webhook in your Slack workspace and add either the full webhook URL or the webhook key.

```hocon
df {
    notifications {
        channels {
            slack {
                enabled = true

                # Full webhook URL
                url = "https://hooks.slack.com/services/T00/B00/XXXX"

                # Alternatively, you can specify only the webhook key:
                # key = "T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
            }
        }
    }
}
```

*Note: For backward compatibility, Data Foundry also falls back to `df.vendor.slack.channel` if no new Slack channel configuration is present.*

---

### 2. Ntfy

[ntfy](https://ntfy.sh) is a simple HTTP-based pub-sub notification service. You can use the free public service at `https://ntfy.sh` or run your own self-hosted ntfy server.

```hocon
df {
    notifications {
        channels {
            ntfy {
                enabled = true

                # Ntfy server URL (default: https://ntfy.sh)
                server = "https://ntfy.sh"

                # Topic name to publish alerts to (choose a secret or unique name)
                topic = "your-unique-df-alerts-topic"

                # Optional access token (required only for protected topics)
                token = ""

                # Default priority for INFO messages: 1 (min) to 5 (max/urgent)
                priority = 3
            }
        }
    }
}
```

Because public ntfy topics can be accessed by anyone who knows the topic name, choose an unguessable topic name or use a self-hosted server with an access token. Server hostnames are omitted from ntfy messages for privacy.

---

### 3. Pushover

[Pushover](https://pushover.net) delivers private push notifications to phones, tablets, and desktops. Because Pushover messages are private to your user account, Data Foundry automatically includes the server's hostname in the notification title (e.g. `df-server-01: 🚨 [CRITICAL] AI Service Offline`) so you know which instance sent the alert.

To set up Pushover:
1. Create an account at [pushover.net](https://pushover.net) and copy your **User Key**.
2. Register an application in Pushover (e.g. "Data Foundry Alerts") and copy the generated **API Token**.
3. Add the credentials to `conf/application.conf`:

```hocon
df {
    notifications {
        channels {
            pushover {
                enabled = true

                # Your Pushover Application API Token (30 characters)
                token = "your-application-api-token"

                # Your Pushover User Key or Delivery Group Key (30 characters)
                user = "your-user-key"

                # Optional: send only to a specific registered device name
                # device = "my-phone"

                # Default priority for INFO alerts: -2 (lowest), -1 (low), 0 (normal), 1 (high)
                priority = 0
            }
        }
    }
}
```

#### Priority Mapping in Pushover
Data Foundry maps internal message levels to Pushover priorities automatically:
- **CRITICAL / ERROR**: Priority `1` (High priority: displays in red, sounds an alert, bypasses quiet hours).
- **WARNING**: Priority `0` (Normal priority).
- **INFO**: Configured `priority` (default `0`).
- **DEBUG / TRACE**: Priority `-1` (Quiet: generates a notification without sound or vibration).

---

## Local AI Health Monitoring

Data Foundry can monitor the health of your connected AI service (such as LocalAI or an OpenAI-compatible endpoint). If the AI service fails consecutive health checks or becomes unreachable, Data Foundry triggers an alert. When the service is reachable again, a recovery alert is sent.

```hocon
df {
    notifications {
        ai {
            # Send an alert when the AI service becomes unreachable
            alert_on_offline = true

            # Send an alert when the AI service comes back online
            alert_on_recovery = true

            # Number of consecutive failures before declaring the service offline
            consecutive_failures_threshold = 2
        }
    }
}
```

---

## Viewing Notifications in the Admin Portal

Instance administrators can view recent notification history directly in the Data Foundry web interface:

1. Sign in as an administrator.
2. Open the **Admin Portal** (`/admin`).
3. Click **Configuration** in the menu.
4. Scroll to the **Recent System Notifications & Alerts** table.

The portal displays an in-memory buffer of the last 50 notifications, including their timestamp, severity level, message text, targeted delivery channels, and delivery status.
