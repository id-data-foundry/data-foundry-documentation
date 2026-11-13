---
layout: default
title: Configuration Reference
parent: Configuration
nav_order: 6
---

# Configuration Key Reference

This page provides a complete key-by-key reference for `conf/application.conf` (and admin-relevant defaults from `conf/reference.conf`). For guided explanations and examples, see [Instance Configuration]({% link _Setup/Configuration/ConfiguringDF.md %}).

---

## Core Platform & Web Proxy

| Key | Type | Default / Example | Description |
| :--- | :--- | :--- | :--- |
| `df.base_url` | String | `"http://localhost:9000"` | Public base URL of the Data Foundry instance (including port if non-standard). Used for redirects, invitations, and link generation. |
| `df.upload_directory` | String | `"data/"` | Directory path for uploaded files and datasets (must end with a trailing slash `/`). |
| `df.web_proxy` | String | `""` (omitted) | Optional external web proxy base URL (e.g. `"https://sites.data-foundry.net"`) for serving dataset-hosted websites on an isolated origin. When omitted or empty, built-in sandboxed web delivery is used. |
| `df.max_active_projects` | Integer | `20` | Maximum number of active projects allowed per user. |
| `df.oocsi_server` | String | `""` | Hostname of the OOCSI server used for real-time data streaming and events. |
| `df.feedback_link` | String | `""` (optional) | Optional URL for an external feedback form displayed in the platform UI. |

---

## Branding & Institutional Links

| Key | Type | Default / Example | Description |
| :--- | :--- | :--- | :--- |
| `df.links.organization` | String | `"Example Organization"` | Display name of your institution or organization. |
| `df.links.about` | String | `"https://example.com/about"` | URL for the About page linked in the footer. |
| `df.links.contact` | String | `"https://example.com/contact"` | URL for the Contact page linked in the footer. |
| `df.links.privacy` | String | `"https://example.com/privacy"` | URL for the Privacy Policy linked in the footer. |
| `df.links.scientific_integrity` | String | `"https://example.com/integrity"` | URL for the Scientific Integrity policy. |
| `df.links.data_protection` | String | `""` | URL for the Data Protection notice. |
| `df.links.organization_logo` | String | `"https://example.com/org-logo"` | URL to the organization logo image. |
| `df.links.teams_community` | String | `""` | Optional URL to an MS Teams (or community) support channel. |

---

## Users & Roles

| Key | Type | Default / Example | Description |
| :--- | :--- | :--- | :--- |
| `df.users.admins` | List\<String\> | `["admin1@example.org"]` | Email addresses of instance administrators (full Admin Portal access). |
| `df.users.librarians` | List\<String\> | `["libr1@example.org"]` | Email addresses of librarians (dataset curation across the platform). |
| `df.users.moderators` | List\<String\> | `["mod1@example.org"]` | Email addresses of moderators. |
| `df.users.reviewers` | List\<String\> | `["reviewer1@example.org"]` | Email addresses of ethical/scientific reviewers. |

---

## Authentication & SSO

| Key | Type | Default / Example | Description |
| :--- | :--- | :--- | :--- |
| `df.sso.client` | String | `""` | OpenID Connect (OIDC) Client ID provided by your Identity Provider (IdP). |
| `df.sso.secret` | String | `""` | OIDC Client Secret provided by your IdP. |
| `df.sso.tenant` | String | `""` | Tenant ID (e.g. Microsoft Entra ID / Azure AD tenant). |
| `df.sso.discovery` | String | `""` | OIDC well-known discovery URL (`https://.../.well-known/openid-configuration`). |
| `df.auth.participationTokenMaxAgeDays` | Long | *(optional)* | Maximum validity period (in days) for participant invitation/access tokens. |

---

## API Keys & Tokens

| Key | Type | Default / Example | Description |
| :--- | :--- | :--- | :--- |
| `df.keys.registration` | List\<String\> | `[""]` | Valid registration codes required when signing up (if registration is restricted). |
| `df.keys.project` | String | `""` | Secret key used for project-level token operations. |
| `df.keys.api` | String | `""` | Master API key for general system access. |
| `df.keys.auth.api` | String | `""` | API key for the authentication service. |
| `df.keys.v2.multi.api` | List\<String\> | `[""]` | V2 multi-project API keys for trusted external services. |
| `df.keys.v2.user.api` | List\<String\> | `[""]` | V2 user-centric API keys (convention: service name in first 8 characters). |

---

## AI Processing, Models & Concurrency Lanes

| Key | Type | Default / Example | Description |
| :--- | :--- | :--- | :--- |
| `df.processing.python` | String | `"python3"` | Path or command name for the Python binary used in server-side processing. |
| `df.processing.ai.baseurl` | String | `"http://localhost:9191/v1"` | Base URL for the OpenAI-compatible AI API gateway. |
| `df.processing.ai.key` | String | `""` | API key sent in the `Authorization` header to the AI gateway. |
| `df.processing.ai.images.url` | String | `"http://localhost:8094/v1"` | Optional dedicated base URL for image generation/editing endpoints. |
| `df.processing.ai.stt.longform.url` | String | `"http://localhost:9191/v1"` | Base URL for longform batch Speech-to-Text and speaker diarization. |
| `df.processing.ai.stt.realtime.url` | String | `"ws://localhost:9191/v1/audio/stream"` | WebSocket (`ws://` or `wss://`) URL for real-time streaming STT. |
| `df.processing.ai.default_max_tokens` | Integer | `4096` | Default maximum output tokens for standard AI completions. |
| `df.processing.ai.agent_max_tokens` | Integer | `8192` | Maximum output tokens for agentic AI workflows. |
| `df.processing.ai.stream.idle_timeout` | Duration | `90s` | Fail a streamed AI response only if the backend is silent for this duration. |
| `df.processing.ai.stream.max_duration` | Duration | `30m` | Absolute maximum duration for a single streamed AI response. |
| `df.processing.ai.models.default` | String | `"hermes-2-pro-llama-3-8b"` | Default model identifier. |
| `df.processing.ai.models.chat` | String | `"hermes-2-pro-llama-3-8b"` | Model identifier for chat completions. |
| `df.processing.ai.models.vision` | String | `"llava-llama-3-8b-v1_1"` | Model identifier for vision/multimodal tasks. |
| `df.processing.ai.models.coding` | String | `"qwen/qwen3.6-27b"` | Model identifier for coding tasks. |
| `df.processing.ai.models.coding_subagent` | String | *(optional)* | Model identifier for coding subagents. |
| `df.processing.ai.models.text` | String | `"openai/gpt-oss-20b"` | Model identifier for general text generation. |
| `df.processing.ai.models.translate` | String | `"apertus-8b"` | Model identifier for translation tasks. |
| `df.processing.ai.models.image` | String | `"Flux-schnell"` | Model identifier for image generation. |
| `df.processing.ai.models.image_edit` | String | *(optional)* | Model identifier for image editing. |
| `df.processing.ai.models.stt` | String | *(optional)* | Model identifier for Speech-to-Text. |
| `df.processing.ai.models.tts` | String | *(optional)* | Model identifier for Text-to-Speech. |

### AI Concurrency Lanes

Lanes can be configured under `df.processing.ai.lanes.<lane>` (preferred) or `df.ai.lanes.<lane>` (fallback). Each lane supports `concurrency` (`0` = unlimited), `queue`, `timeout`, and optional `max_per_user` (defaults to `2` for `image`, `-1` unlimited for others).

| Lane | Default Concurrency | Default Queue | Default Timeout | Description |
| :--- | :--- | :--- | :--- | :--- |
| `llm` | `16` | `64` | `120s` | Chat, completions, and general LLM tasks. |
| `stt` | `1` | `32` | `1800s` | Batch audio transcription and diarization. |
| `stt_realtime` | `8` | `16` | `600s` | Real-time WebSocket streaming STT sessions. |
| `tts` | `1` | `32` | `60s` | Text-to-Speech synthesis. |
| `image` | `1` | `16` | `600s` | Image generation, editing, and variations (`max_per_user` defaults to `2`). |
| `embedding` | `1` | `32` | `60s` | Text embedding requests. |
| `models` | `0` | `0` | `5s` | Model listing requests (`0` = unlimited, served from cache). |

---

## Email & Messaging

| Key | Type | Default / Example | Description |
| :--- | :--- | :--- | :--- |
| `df.msgraph.from` | String | `""` | Sender email address for Microsoft Graph (O365) mail delivery. |
| `df.msgraph.client` | String | `""` | Azure App Registration Client ID for Microsoft Graph. |
| `df.msgraph.secret` | String | `""` | Client Secret for Microsoft Graph. |
| `df.msgraph.tenant` | String | `""` | Microsoft 365 Tenant ID. |
| `df.msgraph.discovery` | String | `""` | OIDC/OAuth discovery URL for Microsoft Graph. |
| `play.mailer.from` | String | `""` | Sender email address for SMTP fallback (`Java Mail`). |
| `play.mailer.host` | String | `""` | SMTP server hostname. |
| `play.mailer.username` | String | `""` | SMTP authentication username. |
| `play.mailer.password` | String | `""` | SMTP authentication password. |
| `df.telegram.bot_name` | String | `""` | Telegram bot username (e.g. `"my_df_bot"`). |
| `df.telegram.bot_token` | String | `""` | Telegram bot API token from `@BotFather`. |

---

## System Notifications & Alerts

| Key | Type | Default / Example | Description |
| :--- | :--- | :--- | :--- |
| `df.notifications.enabled` | Boolean | `true` | Master switch for all outgoing system notifications. |
| `df.notifications.channels.slack.enabled` | Boolean | `false` / `true` | Enable or disable Slack webhook notifications. |
| `df.notifications.channels.slack.url` | String | `""` | Full Slack incoming webhook URL. |
| `df.notifications.channels.slack.key` | String | `""` | Slack webhook path key (`T.../B.../XXX`), used if `url` is omitted. |
| `df.notifications.channels.ntfy.enabled` | Boolean | `false` | Enable or disable Ntfy push notifications. |
| `df.notifications.channels.ntfy.server` | String | `"https://ntfy.sh"` | Ntfy server base URL. |
| `df.notifications.channels.ntfy.topic` | String | `"datafoundry-alerts"` | Ntfy topic name. |
| `df.notifications.channels.ntfy.token` | String | `""` | Optional access token for protected Ntfy topics. |
| `df.notifications.channels.ntfy.priority` | Integer | `3` | Default Ntfy message priority (`1` min to `5` max/urgent). |
| `df.notifications.channels.pushover.enabled` | Boolean | `false` | Enable or disable Pushover notifications. |
| `df.notifications.channels.pushover.token` | String | `""` | Pushover Application API Token. |
| `df.notifications.channels.pushover.user` | String | `""` | Pushover User or Delivery Group Key. |
| `df.notifications.channels.pushover.device` | String | *(optional)* | Target a specific registered Pushover device name. |
| `df.notifications.channels.pushover.priority` | Integer | `0` | Default Pushover priority for `INFO` alerts (`-2` to `1`). |
| `df.notifications.channels.pushover.url` | String | `"https://api.pushover.net/1/messages.json"` | Optional Pushover API endpoint override. |
| `df.notifications.ai.alert_on_offline` | Boolean | `true` | Send an alert when the AI service becomes unreachable. |
| `df.notifications.ai.alert_on_recovery` | Boolean | `true` | Send an alert when the AI service recovers. |
| `df.notifications.ai.consecutive_failures_threshold` | Integer | `2` | Number of consecutive failed health checks before declaring AI offline. |
| `df.vendor.slack.channel` | String | `""` | Legacy Slack webhook URL fallback if `df.notifications.channels.slack` is not configured. |

---

## External Wearables

| Key | Type | Default / Example | Description |
| :--- | :--- | :--- | :--- |
| `df.vendor.fitbit.id` | String | `""` | Fitbit OAuth2 Client ID. |
| `df.vendor.fitbit.secret` | String | `""` | Fitbit OAuth2 Client Secret. |
| `df.vendor.googlefit.id` | String | `""` | Google Fit OAuth2 Client ID. |
| `df.vendor.googlefit.secret` | String | `""` | Google Fit OAuth2 Client Secret. |

---

## Database & Admin-Relevant Server Settings

| Key | Type | Default / Example | Description |
| :--- | :--- | :--- | :--- |
| `db.default.url` | String | `"jdbc:h2:mem:play;DB_CLOSE_DELAY=-1"` | JDBC connection URL (H2 in-memory/file for dev, PostgreSQL for production). |
| `production.mockDB` | Boolean | `false` / `true` | Populate a testing database for local production testing. |
| `play.http.secret.key` | String | *(required in prod)* | Secret key used by Play to sign session cookies and cryptographic tokens. |
| `play.http.session.secure` | Boolean | `false` | Set to `true` in production HTTPS deployments so session cookies are only sent over HTTPS. |
| `play.http.session.domain` | String | `"localhost"` | Cookie domain for sessions (set to your production hostname, or `null` for localhost). |
| `play.http.parser.maxDiskBuffer` | Size | `30MB` | Maximum disk buffer size for HTTP request bodies (`reference.conf`). |
| `parsers.anyContent.maxLength` | Size | `30MB` | Maximum allowed request body size for general uploads (`reference.conf`). |
| `parsers.MultipartFormData.maxLength` | Size | `30MB` | Maximum allowed multipart form upload size (`reference.conf`). |
| `df.securitytxt.contact` | String | `"mailto:security@data-foundry.net"` | Security contact URI served at `/.well-known/security.txt` (RFC 9116). |
| `df.securitytxt.expires` | String | `""` | Expiration timestamp for `security.txt`. |
| `df.securitytxt.preferred-languages` | String | `"en, nl"` | Preferred languages for security reports. |
| `df.securitytxt.policy` | String | `"https://github.com/id-data-foundry/data-foundry/blob/main/SECURITY.md"` | Security policy URL. |
| `df.securitytxt.acknowledgments` | String | `"https://github.com/id-data-foundry/data-foundry/blob/main/SECURITY.md#hall-of-fame"` | Security acknowledgments / Hall of Fame URL. |
