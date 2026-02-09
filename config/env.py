"""
Minimal env loader with optional .env support.
Priority: explicit environment variables > .env values > defaults.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

_DOTENV_LOADED = False
_DOTENV_VARS: dict[str, str] = {}
_LOCAL_VARS: dict[str, str] = {}


def _parse_dotenv_line(line: str) -> Optional[tuple[str, str]]:
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    if "=" not in line:
        return None
    key, value = line.split("=", 1)
    key = key.strip()
    value = value.strip().strip("\"").strip("'")
    if not key:
        return None
    return key, value


def load_dotenv(dotenv_path: str | None = None) -> None:
    """
    Load .env into an internal cache. Does not mutate os.environ.
    """
    global _DOTENV_LOADED, _DOTENV_VARS
    if _DOTENV_LOADED:
        return

    path = Path(dotenv_path) if dotenv_path else Path(".env")
    if not path.exists():
        _DOTENV_LOADED = True
        return

    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            parsed = _parse_dotenv_line(line)
            if parsed:
                key, value = parsed
                _DOTENV_VARS[key] = value
    except Exception:
        # Fail silently; env vars will still work.
        pass
    _DOTENV_LOADED = True


def _load_local_overrides() -> None:
    global _LOCAL_VARS
    if _LOCAL_VARS:
        return
    try:
        from config import local  # type: ignore
        overrides = getattr(local, "ENV_OVERRIDES", {})
        if isinstance(overrides, dict):
            _LOCAL_VARS = {str(k): str(v) for k, v in overrides.items()}
    except Exception:
        _LOCAL_VARS = {}


def get_env(key: str, default: str = "") -> str:
    """
    Get a config value from environment or .env cache.
    """
    load_dotenv()
    _load_local_overrides()
    if key in os.environ:
        return os.environ[key]
    if key in _LOCAL_VARS:
        return _LOCAL_VARS[key]
    return _DOTENV_VARS.get(key, default)
