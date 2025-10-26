"""Docassemble logging helpers for the MA1A rebuild."""

from __future__ import annotations

from typing import Any

from docassemble.base.util import log

PACKAGE_PREFIX = "[ma1a]"

def log_event(message: str, level: str = "info", **context: Any) -> None:
    """Emit a namespaced interview log entry with optional context."""
    suffix = "".join(f" {key}={value!r}" for key, value in context.items() if value is not None)
    log(f"{PACKAGE_PREFIX} {message}{suffix}", level)
