---
layout: default
title: Developer Guide
nav_order: 7
has_children: false
has_toc: true
---

# Developer Guide

Welcome to the Data Foundry Developer Guide. This page serves as the central hub for developers, architects, and technical researchers, providing a comprehensive overview of the platform's capabilities and direct links to APIs, client SDKs, server-side scripting, local AI integration, web development, dataset structures, and development tools.

---

## Quick Navigation

| Area | What You Can Do | Key Documentation |
| :--- | :--- | :--- |
| **Connecting & APIs** | Ingest and retrieve data via REST, OpenAPI, and real-time WebSockets | [REST API](#rest--http-api) • [OOCSI Streaming](#oocsi-real-time-streaming) • [Clients & SDKs](#client-libraries--sdks) |
| **Server-Side Scripting** | Run custom JavaScript on Data Foundry triggered by events, timers, or messages | [Overview & Writing Scripts](#2-server-side-logic-scripting) |
| **Web Dev & Hosting** | Host web apps and interactive dashboards connected directly to live data | [Hosting & Participant Auth](#3-web-development--hosting) |
| **Local AI Integration** | Run LLM completions, Vision/OCR, Image generation, and Speech tools locally | [Modalities & APIs](#modality--task-apis) • [Structured Outputs](#advanced-ai-features) • [Chatbots & ConvoScript](#custom-chatbots--conversational-agents) |
| **Development Tools** | Analyze data in browser notebooks, flash microcontrollers, and plot charts | [Notebooks, ESP Tools & Visualizations](#5-development-tools--analysis) |
| **Datasets & Schemas** | Model IoT time-series, entity records, media files, and surveys | [Dataset Guides & Reference](#6-datasets--data-modeling) • [Dataset Types](#dataset-types) |
| **Project & Device Admin** | Manage devices, participant enrollment, study credentials, and API access | [Devices, Participants & API Settings](#7-project--device-administration) |
| **Quickstart Pathways** | End-to-end recipes for hardware logging, web dashboards, and AI bots | [Hardware to Cloud](#hardware-to-cloud-iot-pipeline) • [Web Dashboard](#full-stack-web-dashboard) • [AI Automation](#intelligent-ai-automation) |

---

## 1. Connecting & Data Exchange (APIs)

Data Foundry provides robust interfaces for synchronous logging, batch data retrieval, and bidirectional real-time data streaming.

### REST / HTTP API
Use standard HTTP requests for synchronous data operations. This is ideal for logging data from devices that wake up periodically, or for querying historical data for analysis.
*   **Authentication & API Keys**: Secure your requests using project-level API tokens. Learn how to generate and configure API keys in the [API Access Guide]({% link _Reference/DFapi.md %}#api-access) and review instance security in [Authentication Configuration]({% link _Setup/Configuration/ConfiguringAuth.md %}).
*   **Endpoints & Specifications**: Access endpoints for Datasets, Resources, and specific operations via the [Data Foundry Developer API]({% link _Reference/DFapi.md %}) and the [Participant API Reference]({% link _Reference/ParticipantAPI/index.md %}).
*   **Interactive Swagger / OpenAPI**: When running a Data Foundry instance, explore and test the interactive OpenAPI documentation directly at `/docs`.

### OOCSI (Real-Time Streaming)
For real-time applications, Data Foundry integrates with [OOCSI](https://oocsi.net), a high-performance, WebSocket-based messaging middleware.
*   **Real-time Streaming**: Stream sensor readings, device statuses, and UI events continuously between distributed clients and the server.
*   **Channels & Messages**: Publish data to specific topics and subscribe to receive immediate push updates without polling.
*   **Event-Driven Middleware**: Connect multiple physical and digital components simultaneously. See practical walkthroughs in:
    *   [Connected Data Logger Tutorial]({% link _Tutorials/GettingStarted/MyFirstConnectedDataLogger.md %}) — Connecting IoT devices to Data Foundry via OOCSI.
    *   [From Prototype to Website]({% link _Tutorials/GettingStarted/FromPrototypeToWebsite.md %}) — Bridging hardware prototypes to live web frontends.
    *   [Website Tracking Guide]({% link _Guides/Examples/Usecases/WebsiteTracking/index.md %}) — Real-time event streaming from browser interactions.
    *   [ESP32 Asynchronous Streaming]({% link _Guides/Examples/ESP-32/Asynchronous.md %}) — Non-blocking messaging on microcontrollers.

### Client Libraries & SDKs
Official libraries, SDKs, and code blueprints are available across creative coding, microcontroller, and data science ecosystems:
*   **[Clients Overview Hub]({% link _Guides/Clients/index.md %})**: Overview of supported platforms and installation patterns.
*   **[Python]({% link _Guides/Clients/Python.md %})**: Best for data science notebooks, backend logic, and Raspberry Pi prototypes. Send data via `requests` or stream via the `oocsi` Python library.
*   **[JavaScript]({% link _Guides/Clients/Javascript.md %})**: Integrate directly into web browsers and Node.js applications using `fetch` or `oocsi-web.js`.
*   **[Processing]({% link _Guides/Clients/Processing.md %})**: Native library for creative coding sketches. See also the [Processing Client Reference]({% link _Reference/Clients/processing.md %}).
*   **[ESP32 / Arduino (C++)]({% link _Guides/Examples/ESP-32/index.md %})**: Lightweight libraries for IoT microcontrollers, including [Camera Upload Examples]({% link _Guides/Examples/ESP-32/ESP32CameraUpload.md %}).
*   **[MicroPython]({% link _Guides/Examples/ESP-32/ESP32micropython.md %})**: Connect low-power microcontrollers running Python. See the [MicroPython Client Reference]({% link _Reference/Clients/micropython.md %}).
*   **[Unity 3D]({% link _Guides/Clients/Unity.md %})**: Integrate data collection and telemetry directly into 3D games, VR simulations, and spatial environments.
*   **[Max / MSP]({% link _Guides/Clients/Max.md %})**: Connect interactive sound, media, and audiovisual patches.
*   **[Raspberry Pi]({% link _Guides/Examples/RaspberryPi/index.md %})**: Set up single-board computers with sensor telemetry, such as the [Raspberry Pi DHT Sensor Guide]({% link _Guides/Examples/RaspberryPi/RPiDHTSensor.md %}).

---

## 2. Server-Side Logic (Scripting)

Data Foundry includes an internal sandboxed JavaScript execution engine that runs directly on the server, allowing you to implement logic that lives directly alongside your datasets.

*   **[Data Foundry Scripts Overview]({% link _Guides/Scripting/index.md %})**: Introduction to server-side automation and workflow capabilities.
*   **[Writing Scripts Guide]({% link _Guides/Scripting/writingScripts.md %})**: Step-by-step instructions on creating, testing, and debugging your first script.
*   **Event-Driven Logic & Inputs**: Automatically execute scripts on specific triggers, including incoming OOCSI messages, dataset modifications, or scheduled timers. Detailed in [Script Inputs]({% link _Guides/Scripting/scriptInputs.md %}).
*   **Resource & Dataset Access**: Programmatically read, transform, and write data across your project resources:
    *   [Access Project Resources]({% link _Guides/Scripting/AccessDatasets/AccessProjectResources.md %}) — Programmatically interact with Participants and Devices.
    *   [Access IoT Datasets]({% link _Guides/Scripting/AccessDatasets/AccessIoTData.md %}) — Query and append time-series sensor events.
    *   [Access Entity Datasets]({% link _Guides/Scripting/AccessDatasets/AccessEntityData.md %}) — Create, query, and update relational structured records.
    *   [Access Any Dataset]({% link _Guides/Scripting/AccessDatasets/AccessAnyDataset.md %}) — Generic dataset accessor patterns.
*   **Scripting Reference**:
    *   [Scripting Function Reference]({% link _Reference/Scripts/index.md %}) — Complete API specification (`DF.print`, `DF.dataset()`, `DF.eventData`, etc.).
    *   [AI APIs in Scripts]({% link _Reference/LocalAI/AIscripts.md %}) — Invoke LLMs and multimodal AI models directly inside server scripts.
*   **Conceptual Foundations**: Learn more about the scripting engine's role in [Scripts Concepts]({% link _Learning/Scripts/index.md %}).

---

## 3. Web Development & Hosting

Deploy full-stack web applications, participant questionnaires, and dynamic dashboards hosted directly inside your Data Foundry project.

*   **Project Website Hosting**: Host HTML, CSS, JavaScript, and asset bundles with built-in HTTPS. Learn how to launch your first hosted page in [Hosting a Simple Website on Data Foundry]({% link _Tutorials/GettingStarted/MyFirstDataFoundryWebsite.md %}).
*   **Connected Web Prototypes**: Connect frontends to live physical devices through OOCSI channels. Follow the complete guide in [From Prototype to Website]({% link _Tutorials/GettingStarted/FromPrototypeToWebsite.md %}).
*   **Frontend Integration & Tracking**:
    *   [Connecting JavaScript Guide]({% link _Guides/Clients/Javascript.md %}) — Fetching data, submitting forms, and handling authentication.
    *   [Website Tracking Guide]({% link _Guides/Examples/Usecases/WebsiteTracking/index.md %}) — Collecting user interactions, clicks, and journey telemetry.
    *   [Local AI JavaScript Library]({% link _Reference/LocalAI/JSAPI.md %}) — Embed local AI capabilities in client-side web applications using `local-ai.js`.
*   **Authentication & Access Control**:
    *   Secure your hosted study pages and manage participant sessions using the [Participant API Reference]({% link _Reference/ParticipantAPI/index.md %}) (stateless `X-Participant-Token` header auth; works in sandboxed frames and `sites.data-foundry.net`).
    *   Supports both **Anonymous Participation** (self-sign-up via `anonymousParticipation.js`) and **Registered Participation** (token-secured access via `#df_participant=` handoff and `participation.js`).
    *   For dataset-level storage/uploads from hosted prototypes, use Dataset `api_token` endpoints (see the [Files Dataset Guide]({% link _Guides/Datasets/Files/FilesData.md %})) rather than the retired `user.js` / `researcher.js` APIs. Keep write tokens in a private editor dataset rather than a public viewer dataset.

---

## 4. Local AI Integration

Data Foundry features deeply integrated, locally hosted AI models. Run inferencing with full data privacy on campus infrastructure without sending confidential study data to third-party cloud providers.

*   **[Local AI Guide Hub]({% link _Guides/LocalAI/index.md %})** & **[Local AI Reference Hub]({% link _Reference/LocalAI/index.md %})**: Overview of available capabilities and architecture.
*   **[Supported Models & Hardware Specs]({% link _Learning/LocalAI/Models.md %})**: Performance specifications, supported context windows, and model configurations.

### Modality & Task APIs
*   **Text-to-Text (LLMs)**: Chat completions, reasoning, and text transformations. See the [Chat Completion API Reference]({% link _Reference/LocalAI/AIAPI.md %}) and the [Prompt 101 Example]({% link _Guides/LocalAI/examples/1.Prompt101.md %}).
*   **Generative Media (Text-to-Image)**: Generate visual imagery from prompts using the [Text-to-Image API]({% link _Reference/LocalAI/text-to-image.md %}) and the [Text-to-Image Example]({% link _Guides/LocalAI/examples/6.Text-to-Image.md %}).
*   **Vision & OCR (Image-to-Text)**: Extract information, analyze diagrams, and transcribe text from images via the [Image-to-Text API]({% link _Reference/LocalAI/image-to-text.md %}) and the [Image-to-Text Example]({% link _Guides/LocalAI/examples/4.Image-to-Text.md %}).
*   **Speech-to-Text (Audio Transcription)**: Convert recorded audio and spoken responses to text via the [Speech-to-Text API]({% link _Reference/LocalAI/speech-to-text.md %}) and the [Speech-to-Text Example]({% link _Guides/LocalAI/examples/5.Speech-to-Text.md %}).
*   **Text-to-Speech (Voice Synthesis)**: Synthesize speech audio from text using the [Text-to-Speech API]({% link _Reference/LocalAI/text-to-speech.md %}) and the [Text-to-Speech Example]({% link _Guides/LocalAI/examples/7.Text-to-Speech.md %}).

### Advanced AI Features
*   **Structured Output & Tool Calling**: Enforce guaranteed JSON schemas and enable model function calling. Read the [Structured Output and Tools Reference]({% link _Reference/LocalAI/StructuredOutputAndTools.md %}) and try the [Structured Output Guide]({% link _Guides/LocalAI/examples/14.StructuredOutput.md %}) and [Tool Calls Guide]({% link _Guides/LocalAI/examples/15.ToolCalls.md %}).
*   **Streaming Responses**: Stream tokens in real-time for responsive interfaces. See the [Streaming Guide]({% link _Guides/LocalAI/examples/16.Streaming.md %}).
*   **Client & Script SDKs**:
    *   [AI APIs in Scripts]({% link _Reference/LocalAI/AIscripts.md %}) — Call AI models directly inside server-side scripts.
    *   [Local AI JavaScript Library]({% link _Reference/LocalAI/JSAPI.md %}) — Client-side web library (`local-ai.js`).

### Custom Chatbots & Conversational Agents
*   **[LLM Chatbots Guide]({% link _Guides/LocalAI/Chatbots.md %})**: Build custom chatbots with Retrieval-Augmented Generation (RAG) and custom knowledge bases.
*   **[Chatbot AI API Reference]({% link _Reference/LocalAI/chatbotAPI.md %})**: Programmatically invoke and manage custom chatbots.
*   **[Agentic Chatbot Tutorial]({% link _Tutorials/LocalAI/AgenticChatbot.md %})**: Build multi-step autonomous AI agents.
*   **ConvoScript Framework**: Declarative framework for authoring complex conversational interfaces:
    *   [Composing a ConvoScript Guide]({% link _Guides/LocalAI/convoscript/index.md %}) — Build interactive web chat applications.
    *   [ConvoScript Architecture & Learning]({% link _Learning/LocalAI/ConvoScript.md %}) — Deep dive into ConvoScript states and syntax.
*   **[Local AI Examples Suite]({% link _Guides/LocalAI/examples/index.md %})**: Explore 16 practical examples covering prompt engineering, benchmarking, token efficiency, translation, and chained pipelines.

---

## 5. Development Tools & Analysis

Data Foundry includes built-in web-based developer utilities for analysis, device flashing, and visualization without requiring local software installation.

*   **[Data Foundry Tools Hub]({% link _Guides/Tools/index.md %})**: Overview of integrated developer utilities.
*   **[Starboard Notebooks]({% link _Guides/Tools/Starboard/StarboardNotebook.md %})**: Interactive in-browser JavaScript and Python notebooks for rapid data manipulation and exploratory data analysis. See the hands-on [Starboard Notebooks 101 Tutorial]({% link _Tutorials/DataVisualisationTutorial.md %}).
*   **[ESP Tools & MicroPython Suite]({% link _Guides/Tools/ESPtools/MicropythonSuite.md %})**: Flash firmware, upload code, and manage ESP32 files directly from your web browser using WebSerial.
*   **[RawGraphs Data Visualization]({% link _Guides/Tools/Rawgraphs.md %})**: Transform dataset records into vector charts, sankey diagrams, and visual graphics.
*   **[Interviews Transcription Tool]({% link _Guides/Tools/Transcription.md %})**: Automated browser-based transcription for participant audio recordings.
*   **[Activity Logger Tool]({% link _Guides/Tools/ActivityLogger.md %})**: Interface for real-time human activity logging and annotation.

---

## 6. Datasets & Data Modeling

Data Foundry supports structured dataset types tailored to specific design research paradigms and physical-computing applications.

*   **[Datasets How-To Guides]({% link _Guides/Datasets/index.md %})**: Step-by-step guides for designing and populating datasets.
*   **[Dataset API Reference]({% link _Reference/Datasets/index.md %})**: Programmatic endpoints for querying, creating, and exporting datasets.
*   **[Datasets Overview & Concepts]({% link _Learning/Datasets/index.md %})**: Core concepts, schema design, and data modeling strategies.

### Dataset Types
*   **[IoT / Time Series Datasets]({% link _Guides/Datasets/TS/TimeSeriesDataset.md %})**: High-frequency, append-only sensor telemetry.
*   **[Entity Datasets]({% link _Guides/Datasets/Entity/EntityDataset.md %})**: Key-value and tabular entity state records with full update and query semantics.
*   **[Form Datasets]({% link _Guides/Datasets/Forms/FormsDataset.md %})**: Structured questionnaire submissions and user inputs.
*   **[Survey Datasets]({% link _Guides/Datasets/Survey/SurveyDataset.md %})**: Multi-step user surveys and psychometric instruments.
*   **[Media Datasets]({% link _Guides/Datasets/Media/MediaDataset.md %})**: Image, video, and binary asset storage with metadata.
*   **[Diary Datasets]({% link _Guides/Datasets/Diary/DiaryDataset.md %})**: Longitudinal diary studies and qualitative logs.
*   **[Annotation Datasets]({% link _Guides/Datasets/Annotation/AnnotationDataset.md %})**: Labels, bounding annotations, and metadata tagging.
*   **[Files Dataset]({% link _Guides/Datasets/Files/FilesData.md %})**: Upload, manage, and host files in Data Foundry.

---

## 7. Project & Device Administration

Configure your project environment, manage hardware access credentials, and coordinate multi-participant studies.

*   **[Devices & Hardware Credentials]({% link _Guides/ProjectManagement/AddDevice.md %})**: Register microcontrollers, generate individual device tokens, and configure streaming channels.
*   **[Participants & Study Management]({% link _Guides/ProjectManagement/AddParticipant.md %})**: Enroll participants, manage study cohorts, and configure access permissions.
*   **[Collaborators & Team Roles]({% link _Guides/ProjectManagement/AddGroupMembers.md %})**: Invite team members and configure reviewer or moderator privileges.
*   **[Project Clusters]({% link _Guides/ProjectManagement/Clusters.md %})**: Group related projects for collaborative analysis and shared infrastructure.
*   **[API Settings & Configuration]({% link _Setup/Administrators/APISettings.md %})**: Manage instance-level API policies, tokens, and quota limits. For self-hosted instances, review the [Instance Configuration Guide]({% link _Setup/Configuration/index.md %}).

---

## 8. Developer Quickstart Pathways

Depending on your project's architecture, follow one of these recommended end-to-end pathways:

### Hardware to Cloud (IoT Pipeline)
1. **Prepare Hardware**: Connect your ESP32 or microcontroller using the [Connected Data Logger Tutorial]({% link _Tutorials/GettingStarted/MyFirstConnectedDataLogger.md %}).
2. **Register Device**: Generate device credentials via [Add Device Guide]({% link _Guides/ProjectManagement/AddDevice.md %}).
3. **Stream Telemetry**: Send real-time data over [OOCSI]({% link _Tutorials/GettingStarted/FromPrototypeToWebsite.md %}) into an [IoT Dataset]({% link _Guides/Datasets/TS/TimeSeriesDataset.md %}).
4. **Trigger Server Actions**: Process incoming events with [Script Inputs & Triggers]({% link _Guides/Scripting/scriptInputs.md %}).

### Full-Stack Web Dashboard
1. **Scaffold Web Page**: Build a frontend and host it via [Data Foundry Website Hosting]({% link _Tutorials/GettingStarted/MyFirstDataFoundryWebsite.md %}).
2. **Integrate SDK**: Load the [JavaScript Client]({% link _Guides/Clients/Javascript.md %}) or [Local AI JS Library]({% link _Reference/LocalAI/JSAPI.md %}).
3. **Control Access**: Authenticate visitors using the [Participant API]({% link _Reference/ParticipantAPI/index.md %}).
4. **Visualize**: Render real-time charts using [RawGraphs]({% link _Guides/Tools/Rawgraphs.md %}) or custom D3/p5 visualizations.

### Intelligent AI Automation
1. **Select Model**: Review supported models in [Supported AI Models]({% link _Learning/LocalAI/Models.md %}).
2. **Build Agent / Bot**: Configure a conversational agent with [Custom Chatbots]({% link _Guides/LocalAI/Chatbots.md %}) or [ConvoScript]({% link _Guides/LocalAI/convoscript/index.md %}).
3. **Automate with Scripts**: Invoke AI completions programmatically with [AI in Scripts]({% link _Reference/LocalAI/AIscripts.md %}) and [Structured Outputs]({% link _Reference/LocalAI/StructuredOutputAndTools.md %}).
