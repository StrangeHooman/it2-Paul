import platform
import shlex
import subprocess
import sys
from pathlib import Path

script = Path(__file__).resolve().with_name("test.py")
folder = str(script.parent)

if platform.system() == "Windows":
    command = subprocess.list2cmdline([sys.executable, str(script)])
    subprocess.Popen(
        ["cmd", "/c", command],
        cwd = folder,
        creationflags = subprocess.CREATE_NEW_CONSOLE
    )

elif platform.system() == "Darwin":
    command = (
        f"cd {shlex.quote(folder)} && "
        f"{shlex.join([sys.executable, str(script)])};"
    )

    command = command.replace("\\", "\\\\").replace('"', '\\"')
    subprocess.Popen([
        "osascript", "-e",
        f'tell application "terminal" to do script "{command}"'
    ])

else:
    raise RuntimeError(f"Unsupported operating system: {platform.system()}")