# Open-webui webinterface for ollama

**This project uses Docker Compose to set up a multi-container environment with the following services:**
- `ollama`: A service for the Ollama API.
- `open-webui`: A web UI service that depends on the `ollama` service.
- `python`: A Python environment for running scripts.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone the repository:

        git clone git@github.com:aliuosio/open-webui.git
        cd open-webui

## Usage

1. Build and start the services:

       docker-compose up -d

2. Open open-webui

    http://localhost:3000

3. include new modes

        docker exec -it ai_ollama ollama pull <model>

