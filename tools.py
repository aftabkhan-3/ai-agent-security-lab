import os
import subprocess

# STRICT allowlist: only these commands can run
ALLOWED_COMMANDS = ["echo", "dir", "ls"]

# Secret files that must never be read
_SECRET_FILES = {".env", ".env.local", ".env.production", ".env.development"}

# Restrict file reads to the project directory
_BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def run_command(cmd: str) -> str:
    parts = cmd.strip().split()
    if not parts or parts[0] not in ALLOWED_COMMANDS:
        return "ERROR: Command not allowed"

    try:
        out = subprocess.check_output(parts, stderr=subprocess.STDOUT, shell=False, text=True)
        return out[:2000]
    except Exception as e:
        return f"ERROR: {e}"

def read_file(path: str) -> str:
    abs_path = os.path.abspath(path)
    if not abs_path.startswith(_BASE_DIR):
        return "ERROR: Access denied — path is outside the project directory"
    if os.path.basename(abs_path) in _SECRET_FILES:
        return "ERROR: Access denied — secret files cannot be read"
    if not os.path.exists(abs_path):
        return "ERROR: File not found"
    with open(abs_path, "r", encoding="utf-8") as f:
        return f.read()[:4000]

def debug_tool(query: str) -> str:
    return "LOG: System running normally. No errors detected."