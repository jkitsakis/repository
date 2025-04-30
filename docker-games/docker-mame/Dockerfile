FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install Flatpak + runtime deps
RUN apt update && apt install -y \
    flatpak \
    xterm \
    wget \
    pulseaudio \
    dbus-x11 \
    libgl1-mesa-glx \
    && apt clean

# Setup dbus
RUN mkdir -p /run/dbus

# Add Flathub + install RetroArch
RUN flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo && \
    flatpak install -y flathub org.libretro.RetroArch

# Create roms mount point
RUN mkdir -p /roms
