## Open WebUI Project
A Docker Compose setup for running a Web UI, Ollama, Python, SearxNG, and Fabric services with GPU support.

## Setup

1. Clone the project with Git `git clone https://github.com/aliuosio/open-webui.git`
2. Navigate into the project directory `cd open-webui`
3. Run `docker compose up -d` to create and start your environment.

## Usage

The Web UI is accessible at `http://localhost:3000`.

## Fabric Usage

    docker compose exec fabric bash
    source .bashrc

- **webui**: This is the Web UI component of the project. It is available on port 3000 of the host and depends on the Ollama service.
- **ollama**: This is the Ollama service, which is required by the webui.
- **python**: This is the Python service, which depends on the Ollama service. It is running in the `/usr/src` directory in the container.
- **searxng**: This is the SearxNG service, which is a search engine used by the Web UI for web search functionality. It is available on port 8080 of the host.
- **fabric**: This is the Fabric service, which depends on the Ollama service. It is used for managing Obsidian files and is configured to run indefinitely.

Please note that this service is configured for GPU acceleration and requires NVIDIA drivers working with docker
## NVIDIA GPU Setup on debian bassed Linux

To enable Docker to use NVIDIA drivers on a Linux system, follow these steps:

1. Install the NVIDIA Container Toolkit:

	https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html