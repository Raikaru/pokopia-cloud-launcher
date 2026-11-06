# Pokopia Cloud launcher

A standalone launcher and local TLS gateway for the Pokopia Cloud community server. It does not include game files, keys, firmware or saves.

You need an Eglantine build with private-server support. If you do not already have one, the launcher offers to download the newest release from [notsapinho/Eglantine](https://github.com/notsapinho/Eglantine/releases), verifies its download and checks the executable for the required features. Ordinary Djihads80/Eglantine releases do not include that integration. The launcher cannot add it to an incompatible build.

1. Extract the launcher archive to a writable folder and run `PokopiaLauncher` (`PokopiaLauncher.exe` on Windows). Python is not required.
2. Select your existing compatible emulator, or agree to download one. On macOS you can pass a compatible `.app` using `play --emulator /path/to/eglantine.app`; upstream does not currently publish a macOS package.
3. Create or sign into your account at https://pokopia.raikaru.com/ and approve the device after comparing its fingerprint with the launcher.
4. Approve the displayed network configuration changes. Your emulator's existing profile and saves are used; an existing configuration file is backed up before it is changed. If a downloaded replacement needs an existing portable profile, the launcher links it without copying; it stops rather than switching profiles if the system refuses the link. The network changes persist after the launcher exits. Restore the backup when you want to undo them.

   For a non-portable Eglantine build, the launcher uses `%APPDATA%\eglantine` on Windows, or the `eglantine` directories under `XDG_DATA_HOME` and `XDG_CONFIG_HOME` on Linux. An existing portable `user` directory takes priority.

5. Select your own `.nup` file, or for loose files select `exefs/main`. Cancel to open the emulator
   and choose a game there. NUP loading also requires emulator support for NUP. Keep the launcher
   open while playing.

The Windows executable is unsigned; SmartScreen may warn. The macOS launcher is not notarized and Gatekeeper may block it. Linux x86_64 builds require glibc 2.35 or newer; the macOS build targets Apple Silicon.

## Privacy and compatibility

This is experimental. The server operator can see player IP addresses. The relay and signaling filter do not guarantee IP privacy; they have not been independently verified across separate networks. Compatibility with particular games, GPUs, operating systems and network setups is not guaranteed.

The downloaded emulator's corresponding source and GPL license are available from [notsapinho/Eglantine](https://github.com/notsapinho/Eglantine). Launcher dependencies are listed in `requirements-launcher.txt`.

The launcher stores device private keys in its user directory; protect that directory. Run only builds from sources you trust.
