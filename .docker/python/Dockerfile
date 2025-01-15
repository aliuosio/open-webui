ARG PY_VERSION
FROM python:${PY_VERSION:-3.9.21-bookworm}

LABEL maintainer="Osiozekhai Aliu"

RUN apt update && apt upgrade -y

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    musl-dev \
    python3-dev \
    libffi-dev \
    git \
    build-essential \
    bash \
    bash-completion \
    nano \
    curl \
    tcpdump

RUN rm -rf /var/lib/apt/lists/*

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

RUN pip install --upgrade pip