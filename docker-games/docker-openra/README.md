# OpenRA Arch Linux Docker Setup with Software Rendering and X11

## Requirements
- Podman or Docker
- X11 and PulseAudio running
- Your AppImage: OpenRA-Red-Alert-x86_64.AppImage

## Instructions

1. Place `OpenRA-Red-Alert-x86_64.AppImage` in this folder.

2. Allow X11 access (run on your **host**):
   ```bash
   xhost +local:root
   ```

3. Build and run the container:
   ```bash
   podman-compose build
   podman-compose up
   ```

4. You should see the Red Alert game window open (in windowed mode).

## Technical Notes

- Uses **Arch Linux base** for clean, modern Mesa/OpenGL stack.
- Forces software rendering via `LIBGL_ALWAYS_SOFTWARE=1` to avoid GPU driver mismatch issues.
- Mounts host X11 and PulseAudio devices for GUI and sound.

## Troubleshooting

If you don't see the GUI, run inside the container:
```bash
glxinfo | grep renderer
```

You should see:
```
OpenGL renderer string: llvmpipe (LLVM ...)
```

If not, something is wrong with Mesa or EGL.

Happy gaming!
