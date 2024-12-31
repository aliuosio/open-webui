ARG PY_VERSION
FROM python:${PY_VERSION:-3.9-alpine3.21}

LABEL maintainer="Osiozekhai Aliu"

RUN apk update && apk upgrade

RUN apk add --no-cache \
    gcc \
    g++ \
    musl-dev \
    python3-dev \
    libffi-dev \
    git \
    build-base \
    bash \
    bash-completion \
    nano