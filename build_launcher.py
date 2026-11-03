#!/usr/bin/env python3
"""Build a launcher-only archive on the target OS; no emulator or game files are included."""
from __future__ import annotations

import hashlib
import os
import pathlib
import subprocess
import sys
import tarfile
import tempfile
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in {
        "windows-x86_64", "linux-x86_64", "macos-arm64"
    }:
        raise SystemExit("usage: build_launcher.py {windows-x86_64|linux-x86_64|macos-arm64}")
    platform = sys.argv[1]
    run(sys.executable, "-m", "PyInstaller", "--noconfirm", "--clean", "--onefile", "--console",
        "--name", "PokopiaLauncher", "--add-data", "portal.txt:.", "--add-data", "relay.txt:.",
        "launcher.py")
    binary = ROOT / "dist" / ("PokopiaLauncher.exe" if platform.startswith("windows") else "PokopiaLauncher")
    if not binary.is_file():
        raise SystemExit(f"Build did not produce {binary}")
    run(str(binary), "--help")
    with tempfile.TemporaryDirectory(prefix="pokopia-packaged-smoke-") as tmp:
        base = pathlib.Path(tmp)
        user = base / "user"
        user.mkdir()
        run(str(binary), "--home", str(base / "home"), "configure", "--user-dir", str(user),
            "--relay", "192.0.2.10:3478,49170-49233")
        config = (user / "config" / "qt-config.ini").read_text(encoding="utf-8")
        if "private_server_gateway_port=18443" not in config:
            raise SystemExit("Packaged launcher did not configure the gateway port")
    output = ROOT / "release"
    output.mkdir(exist_ok=True)
    name = f"PokopiaLauncher-{platform}"
    readme = ROOT / "README.md"
    if platform.startswith("linux"):
        archive = output / f"{name}.tar.gz"
        with tarfile.open(archive, "w:gz") as tar:
            tar.add(binary, arcname=binary.name)
            tar.add(readme, arcname=readme.name)
    else:
        archive = output / f"{name}.zip"
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as z:
            z.write(binary, arcname=binary.name)
            z.write(readme, arcname=readme.name)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (output / f"{archive.name}.sha256").write_text(f"{digest}  {archive.name}\n", encoding="ascii")
    print(f"Built and smoke tested {archive}; sha256={digest}")


if __name__ == "__main__":
    main()
