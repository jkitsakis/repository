FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN dpkg --add-architecture i386 && \
    apt update && \
    apt install -y software-properties-common && \
    add-apt-repository multiverse && \
    apt update && \
    apt install -y \
    wine64 wine32 winetricks \
    x11-apps pulseaudio rar unrar p7zip-full \
    joystick libsdl2-2.0-0 libsdl2-mixer-2.0-0 \
    libgl1-mesa-dri libgl1-mesa-glx \
    usbutils fuse zenity

# Add user
RUN useradd -m gamer

# Copy the script as root and set permissions BEFORE switching user
COPY entrypoint.sh /home/gamer/entrypoint.sh
RUN chmod +x /home/gamer/entrypoint.sh && chown gamer:gamer /home/gamer/entrypoint.sh

# Now switch to user and working directory
USER gamer
WORKDIR /home/gamer/game

ENTRYPOINT ["/home/gamer/entrypoint.sh"]
