# Docker Compose Project

**This project uses Docker Compose to set up a multi-container environment with the following services:**
- `ollama`: A service for the Ollama API.
- `open-webui`: A web UI service that depends on the `ollama` service.
- `python`: A Python environment for running scripts.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone the repository:

        git clone https://github.com/aliuosioopen-webui.git
        cd open-webui

## Usage

1. Build and start the services:

       docker-compose up -d

2. Open open-webui

    http://localhost:3000