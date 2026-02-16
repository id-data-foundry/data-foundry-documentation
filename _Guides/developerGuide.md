---
layout: default
title: Developer Guide
nav_order: 7
has_children: false
has_toc: true
---

# Developer Guide

Welcome to the Data Foundry Developer Guide. This page serves as a central hub for developers, providing an overview of the technical capabilities of the platform and linking to specific documentation for APIs, SDKs, scripting, and tools.

## 1. Connecting & Data Exchange (APIs)

Data Foundry provides robust interfaces for logging, retrieving, and streaming data.

### REST/HTTP API
Use standard HTTP requests for synchronous data operations. This is ideal for logging data from devices that wake up periodically or for retrieving historical data for analysis.
*   **Authentication**: Secure your requests using API tokens generated in your project settings.
*   **Endpoints**: Access standard endpoints for Datasets, Resources, and specific data operations.

### OOCSI (Real-time)
For real-time applications, Data Foundry integrates with [OOCSI](https://oocsi.net), a WebSocket-based protocol.
*   **Real-time Streaming**: Stream data continuously between devices and the server.
*   **Channels & Messages**: Publish data to specific channels and subscribe to receive immediate updates.
*   **Middleware**: Unlike direct HTTP calls, OOCSI acts as a middleware layer facilitating event-driven architectures.

### Client Libraries
We provide SDKs and examples for popular platforms to get you started quickly:
*   **[Python]({% link _Guides/Clients/Python.md %})**: Perfect for backend logic, data analysis, and Raspberry Pi implementations.
*   **[JavaScript]({% link _Guides/Clients/Javascript.md %})**: Integrate directly into web browsers for frontend applications.
*   **[Processing]({% link _Guides/Clients/Processing.md %})**: Built for creative coding and visual arts projects.
*   **[ESP32/Arduino]({% link _Guides/Examples/ESP-32/index.md %})**: Connect low-power IoT microcontrollers.

## 2. Server-Side Logic (Scripting)

Data Foundry includes an internal JavaScript environment that runs on the server, allowing you to implement logic that lives with your data.

*   **[Data Foundry Scripts]({% link _Guides/Scripting/index.md %})**: Write and deploy JavaScript code that runs continuously on the server.
*   **Event-Driven Logic**: Trigger scripts automatically based on incoming OOCSI messages or specific dataset updates.
*   **Resource Access**: Programmatically access and modify project resources such as Participants, Devices, and Datasets directly from your server-side code.

## 3. Web Development & Hosting

You can host and deploy full web applications directly within your Data Foundry project.

*   **Project Website Hosting**: Host static HTML, CSS, and JavaScript files.
*   **Frontend Integration**: Use the JavaScript client to build interactive dashboards, control panels, or visualizations that consume live data.
*   **Authentication**: Implement access control for your hosted pages to manage participant logins securely.

## 4. Local AI Integration

Leverage powerful AI models running locally on the Data Foundry infrastructure to enhance your applications.

*   **[AI Service APIs]({% link _Guides/LocalAI/index.md %})**: Access a variety of local models:
    *   **Text-to-Text**: Interact with Large Language Models (LLMs).
    *   **Generative Media**: Use Text-to-Image and Image-to-Text capabilities.
    *   **Audio**: Implement Speech-to-Text (Transcription) and Text-to-Speech features.
*   **[Custom Chatbots]({% link _Guides/LocalAI/Chatbots.md %})**: Build RAG-enabled chatbots with custom knowledge bases.
*   **Convoscript**: Script complex conversational flows and interactions.

## 5. Development Tools & Analysis

Data Foundry provides a suite of browser-based tools to streamline your development and analysis workflow.

*   **[Starboard Notebooks]({% link _Guides/Tools/Starboard/StarboardNotebook.md %})**: Run JavaScript and Python notebooks directly in your browser for immediate data cleaning and analysis, with no local setup required.
*   **[ESP Tools]({% link _Guides/Tools/ESPtools/MicropythonSuite.md %})**: Flash firmware and manage files on your ESP32 devices via the web interface.
*   **[Visualization]({% link _Guides/Tools/Rawgraphs.md %})**: Create insightful visualizations using integrated tools like RawGraphs or build custom views with libraries like D3.js or p5.js.
