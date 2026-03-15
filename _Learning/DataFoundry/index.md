---
layout: default
title: About Data Foundry
nav_order: 1
has_toc: false
---

# About Data Foundry

When designing intelligent interactive products, when researching user behavior and choices, when investigating the interplay of design and the everyday, we are in need of data. Traditionally, data in design has been scarce. It was collected either in highly qualitative forms or the means to scale were lacking. Data, if it is collected at all, is silo-ed, meaning it is stored and processed in proprietary ways that are not open to other designers and a community of design students, educators, and researchers (Funk, Chiang, & van der Born, 2019).

With Data Foundry, we aim to change this. We want to scale up data collection and processing, make it extremely easy to connect to various data sources, and combine all data into a common format that encourages new forms of design research, mashing up, and creative inquiry beyond low-scale qualitative methods.

## Platform Origin

The platform originated from the Department of Industrial Design at the Eindhoven University of Technology in The Netherlands. A survey among staff, students, and alumni in late 2018 revealed a diversity of data-related research projects, a variety of commonly used tools, and explicit difficulties in basic data collection, processing, and storage tasks. In addition, new regulations on ethics and data management increased the burden on staff and students to perform design research.

We envisioned a designing infrastructure that simplifies both the Data Design process and the Research Data Management process, allowing students and staff to focus more on design and research. This vision is built upon five core philosophies:

1.  **Versatility:** Enable data collection from diverse sources.
2.  **Unification:** Collect data in a unified, accessible structure.
3.  **Compliance:** Provide data access that is strictly compliant with GDPR and ethical standards.
4.  **Empowerment:** Provide intuitive tools to connect, curate, and share data.
5.  **Education:** Promote the understanding, reuse, and creative application of data.

We recognized that successful infrastructure must address two critical aspects often neglected in purely technical solutions: **embedding the infrastructure in a learning context** and **navigating the legal/ethical landscape**.

## Who is this for?

Data Foundry is designed to serve a diverse community of users:

*   **For Students & Researchers:** A platform to quickly build data-enabled prototypes, conduct field studies, and gather insights without needing deep technical expertise or managing complex server infrastructure.
*   **For Educators:** A comprehensive tool to teach data literacy, IoT, and creative coding in a controlled, safe, and accessible environment.
*   **For Developers & Administrators:** An open-source, extensible platform that can be self-hosted, customized, and integrated into existing institutional ecosystems.

## Platform Capabilities

Data Foundry has evolved into a robust ecosystem for data-enabled design.

### Unified Data Collection
We provide a structured way to handle heterogeneous research data through various **Dataset types**:
*   **IoT & Entity:** For sensor data and object states.
*   **Media:** For images, audio, and video collection.
*   **Forms & Diaries:** For qualitative user feedback and longitudinal studies.
*   **Wearables:** Direct integration with FitBit and other health devices.

### Seamless Prototyping & Connectivity
Data Foundry is built to connect.
*   **Client Libraries:** Ready-to-use libraries for Python, Processing, JavaScript, Unity, and Max/MSP make it easy to integrate data into creative projects.
*   **microcontroller Support:** First-class support for ESP32 (MicroPython) and Raspberry Pi allows for rapid physical prototyping.
*   **OOCSI Integration:** The platform is tightly integrated with OOCSI, providing a real-time messaging backbone that connects prototypes, websites, and the server instantly.
*   **Static Web Hosting:** Host your project's frontend or digital prototype directly on Data Foundry for a fully integrated experience.

### Powerful In-Browser Tools
Analyze and manage your data without leaving the browser.
*   **Starboard Notebooks:** An integrated, Jupyter-like environment for in-browser data analysis using Python and JavaScript.
*   **Data Visualization:** Built-in visualization tools powered by RawGraphs for immediate data inspection.
*   **ESP Tools:** A suite of web-based tools including a firmware flasher and file manager to lower the barrier to physical computing.

### Integrated AI Services
Harness the power of AI directly within your projects.
*   **AI API:** Access locally-hosted models through a unified API.
*   **Creative Intelligence:** Utilize Text-to-Speech, Speech-to-Text (Whisper), and Large Language Models (LLMs) for creative and analytical tasks.

### Server-Side Scripting
Run custom logic on the server. Users can write **JavaScript code** to process data streams, trigger events (e.g., sending Telegram messages), or perform complex logic without managing their own backend infrastructure.

### Robust Research & Project Management
Designed for the realities of academic research.
*   **Participant & Device Management:** Tools to manage study participants and deployed devices.
*   **GDPR Compliance:** Built-in features to ensure data handling meets strict privacy standards.
*   **Project Templates:** Get started quickly with pre-configured setups.
*   **Clustering:** Organize resources and filter data effectively for large-scale projects.

## Implementation

The Data Foundry infrastructure is a mature, containerized system designed for scalability and maintainability.

*   **Architecture:** Built on the **Play Framework** (Java/Scala), the system utilizes a modular structure that separates core logic from project-specific implementations.
*   **Deployment:** The platform is fully containerized using **Docker**, ensuring consistent environments for development and production.
*   **Real-time Core:** An **OOCSI** server acts as the central nervous system, handling real-time communication between devices and the platform.
*   **Database:** A robust database layer handles administration, while a decoupled layer manages the massive influx of collected data.

![Data Foundry Overview]({% link _Learning/DataFoundry/images/data-foundry.png %})

## Open Source & Community

After years of development and internal use at TU/e, Data Foundry is now **open source**. We believe in a community-driven approach to design education and research tools.

*   **Community Driven:** We invite other universities, design institutions, and developers to host their own instances, contribute code, and help shape the future of the platform.
*   **Adoption:** TU Delft adopted the platform in 2025, enabling their students to experience the ease of data collection. We encourage other institutions to join this growing network.
*   **Contribute:** The codebase is available for contribution. Whether you are fixing a bug, adding a feature, or improving documentation, your help is welcome.

## Publications

Funk, M., Chiang, I., & van der Born, E. J. (2019). Data Foundry: A Data Infrastructure for Design Research (p. 1). Retrieved from https://www.tue.nl/en/research/research-areas/data-science/data-science-summit-2019/
