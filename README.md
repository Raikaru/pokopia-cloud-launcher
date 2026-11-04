# Pokopia Cloud launcher

A standalone launcher and local TLS gateway for the Pokopia Cloud community server. It does not include or download an emulator, game files, keys, firmware or saves.

You must already have a compatible Eglantine build with the private-server integration, including `private_server_gateway_port`. **Current ordinary upstream releases do not have these features**; the launcher cannot add them. The compatible emulator source is [here](https://github.com/Raikaru/Eglantine/tree/6df23c2f4b). Building it requires its dependencies; no compatible prebuilt emulator is provided by this launcher.

1. Extract the launcher archive to a writable folder and run `PokopiaLauncher` (`PokopiaLauncher.exe` on Windows). Python is not required.
2. Select the executable from your existing compatible emulator. On macOS you can pass an `.app` using `play --emulator /path/to/eglantine.app`.
3. Create or sign into your account at https://pokopia.raikaru.com/ and approve the device after comparing its fingerprint with the launcher.
4. Approve the displayed network configuration changes. Your emulator's existing profile and saves are used; an existing configuration file is backed up before it is changed. The network changes persist after the launcher exits. Restore the backup when you want to undo them.
5. Select your own `.nup` file, or for loose files select `exefs/main`. Cancel to open the emulator
   and choose a game there. NUP loading also requires emulator support for NUP. Keep the launcher
   open while playing.

The Windows executable is unsigned; SmartScreen may warn. The macOS launcher is not notarized and Gatekeeper may block it. Linux x86_64 builds require glibc 2.35 or newer; the macOS build targets Apple Silicon.

## Privacy and compatibility

This is experimental. The server operator can see player IP addresses. The relay and signaling filter do not guarantee IP privacy; they have not been independently verified across separate networks. Compatibility with particular games, GPUs, operating systems and network setups is not guaranteed.

The emulator source and its GPL license are available at [commit `6df23c2f4b`](https://github.com/Raikaru/Eglantine/tree/6df23c2f4b). Launcher dependencies are listed in `requirements-launcher.txt`.

The launcher stores device private keys in its user directory; protect that directory. Run only builds from sources you trust.
