FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Update and install all needed packages
RUN apt update && apt install -y \
    retroarch \
    supervisor \
    xfce4 \
    x11vnc \
    xvfb \
    websockify \
    wget \
    net-tools \
    xterm \
    dbus-x11 \
    pulseaudio \
    python3 \
    python3-websockify \
    git \
    && apt clean

# Install noVNC manually
RUN git clone https://github.com/novnc/noVNC.git /opt/novnc && \
    ln -s /opt/novnc/utils/novnc_proxy /usr/bin/novnc_proxy

# Set up x11vnc password
RUN mkdir -p /root/.vnc && x11vnc -storepasswd 1234 /root/.vnc/passwd

# Copy supervisor configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Make a folder for ROMs
RUN mkdir -p /roms

# Set working directory
WORKDIR /root

EXPOSE 8080

# Run everything via supervisord
CMD ["/usr/bin/supervisord"]
