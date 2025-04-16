#!/bin/bash

# Allow container GUI access
xhost +local: > /dev/null

# Optional ROM to auto-start
ROMNAME=$1

# Define image name
IMAGE_NAME=mame-ubuntu

# Build image if not already built
podman build -t $IMAGE_NAME .

# Run container with mounts and config
podman run --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v $(pwd)/roms:/roms \
  -v $(pwd)/config:/config \
  -v $(pwd)/shaders:/usr/share/mame/shaders \
  --device /dev/snd \
  --device /dev/input \
  $IMAGE_NAME \
  ${ROMNAME:+$ROMNAME}
