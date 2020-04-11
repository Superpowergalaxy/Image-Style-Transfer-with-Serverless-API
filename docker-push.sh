#!/usr/bin/env bash
# This tags and uploads an image to Docker Hub
#!/bin/bash
# run this scrept after 'docker build --tag=app .''

dockerpath="superpowergalaxy/create_music"

# Authenticate & Tag
echo "Docker ID and Image: $dockerpath"
docker login &&\
    docker image tag create_music $dockerpath

# Push Image
docker image push $dockerpath 