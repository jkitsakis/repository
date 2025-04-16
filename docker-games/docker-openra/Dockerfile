FROM docker.io/library/archlinux:latest

# Update and install necessary packages
RUN pacman -Syu --noconfirm \
  mesa \
  mesa-demos \
  libglvnd \
  gtk3 \
  xorg-xhost \
  xorg-xclock \
  pulseaudio \
  libxrender \
  libxext \
  libsm \
  wget \
  unzip \
  ca-certificates \
  && pacman -Scc --noconfirm

WORKDIR /opt/openra

# Copy and extract the AppImage
COPY OpenRA-Red-Alert-x86_64.AppImage ./OpenRA.AppImage

RUN chmod +x OpenRA.AppImage && \
    ./OpenRA.AppImage --appimage-extract && \
    mv squashfs-root/* . && rm -rf squashfs-root OpenRA.AppImage

# Set windowed mode for OpenRA
RUN mkdir -p /root/.openra && \
    echo -e "Video:\n  WindowMode: Windowed \n  Resolution: 1024x768" > /root/.openra/settings.yaml

CMD ["bash", "-c", "LIBGL_ALWAYS_SOFTWARE=1 ./AppRun Game.Mod=ra"]
