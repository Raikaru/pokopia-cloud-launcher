# Pokopia Cloud launcher

A launcher and local TLS gateway for the Pokopia Cloud community server. Players supply their own game files, keys and firmware. No game content or credentials are included.

The launcher links a device to an account using a passkey and a device certificate. The compatible Eglantine build uses the private-server integration and restricts guest networking to the gateway and configured relay. Account creation: https://pokopia.raikaru.com/.

## Privacy and compatibility

This is experimental. The server operator can see player IP addresses. The relay and signaling filter do not guarantee IP privacy; they have not been independently verified across separate networks. Compatibility with particular games, GPUs, operating systems and network setups is not guaranteed.

The emulator source and its GPL license are available at https://github.com/Raikaru/Eglantine/tree/pokopia-release. Launcher dependencies are listed in `requirements-launcher.txt`.

The launcher stores device private keys in its user directory; protect that directory. Run only builds from sources you trust.
