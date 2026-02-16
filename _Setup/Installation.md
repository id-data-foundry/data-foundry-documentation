---
layout: default
title: Installation
nav_order: 1
has_children: true
has_toc: false
---

# Setting up Your Own Data Foundry Instance

This guide will walk you through the process of setting up a local or server-based instance of Data Foundry.

## Requirements

Almost any modern computer can run a Data Foundry instance. For example, the instance at TU/e runs on a virtual private server (VPS) with 4 cores and 8GB of RAM. We recommend at least 100GB of storage for a medium-sized instance (approx. 200 monthly users).

To run Data Foundry, your system must support virtualization and be capable of running Docker.

## Preparation Steps

### 1. Install Docker

Docker is the primary way to deploy Data Foundry. 

- **Windows/macOS**: We recommend [Docker Desktop](https://www.docker.com/products/docker-desktop/).
- **Linux**: Install Docker Engine and Docker Compose. Refer to the [official Docker installation guide](https://docs.docker.com/engine/install/).

### 2. Clone the Repository

Clone the Data Foundry repository to your local machine:

```bash
git clone https://github.com/data-foundry-id/data-foundry.git
```

Then to set up the documentation, open the folder you just cloned and run the following commands
```bash
# Initialize and update submodules
git submodule init
git submodule update
```

This will install all the required files to get started with the configuration process

### Step 3 (optional): Configuring Configuration file
configuring `configuration/application.conf` > needs a special page

### Step 4 (optional): Configuring Docker Compose file
This repository contains 2 docker compose files, one for the development environment and one for the production environment. In here you can enable additional services like a reverse proxy, FAIRLY or OOCSI. 

### Step 5: Running Data Foundry
You can deploy data foundry both in development and production mode. Both will use a separate database keeping you production environment clean. Development mode allows you to interact with the container itself, even being able to change stuff about it. Additionally it allows generates a testing database, this can be easily accessed with a simple email and password. Production mode is only intended for actual deployments with working authentication. This should be configured in the application.conf file.

{: .warning}
Make sure to run the terminal commands in the folder where you downloaded Data Foundry.

##### For the development container:
```bash
docker build --tag datafoundrydocker:development -f .devcontainer/Dockerfile.dev . && docker compose -f DF-development.yaml up
```
##### For the production container:
```bash
docker build --tag datafoundrydocker:production --target production . && docker compose -f DF-production.yaml up
```

### Step 6: Reverse Proxy
> collect RP info from Mathias