# Warcraft III Docker (Ubuntu + Wine) - Native GUI Mode

## Requirements
- Podman or Docker
- PulseAudio + X11 running on your host
- Your AppImage: Warcraft3.rar (renamed from Warcraft.III.Complete.Edition.MULTi6.rar.part)

## Instructions

1. Rename your archive:
   ```bash
   mv Warcraft.III.Complete.Edition.MULTi6.rar.part Warcraft3.rar
   ```

2. Place it in the same folder as this Dockerfile.

3. Allow X11 access from containers:
   ```bash
   xhost +local:root
   ```

4. Build and run the container:
   ```bash
   podman-compose build
   podman-compose up
   ```

## Notes

- This setup will extract the archive and run `War3.exe` using Wine.
- You may need to adjust the `CMD` in `Dockerfile` if the game is in a subfolder after extraction.
- Audio (PulseAudio) and GUI (X11) are pre-configured.

## Troubleshooting

To test GUI and audio inside the container:
```bash
xclock
paplay /usr/share/sounds/alsa/Front_Center.wav
```

Enjoy classic Warcraft III!
