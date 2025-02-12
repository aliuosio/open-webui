ARG GO_IMAGE_VERSION
FROM golang:${GO_IMAGE_VERSION:-1.23.6-alpine3.21}

RUN apk update
RUN apk add --no-cache bash

RUN go install github.com/danielmiessler/fabric@latest

COPY .bashrc /root/.bashrc