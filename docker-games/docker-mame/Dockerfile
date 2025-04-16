FROM docker.io/library/archlinux:latest


RUN pacman -Syu --noconfirm && \
    pacman -S --noconfirm mame libgl alsa-lib joystick xorg-xhost && \
    pacman -Scc --noconfirm

WORKDIR /roms

CMD ["mame", "-rompath", "/roms", "-cfg_directory", "/config"]
