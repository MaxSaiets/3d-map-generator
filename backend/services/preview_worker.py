# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
import json
import os
import signal
import sys
import time
from pathlib import Path
from services.site_preview import PREVIEW_JOBS_DIR, build_preview_cache_from_worker_payload


class PreviewWorkerTimeout(TimeoutError):
    pass


def _install_timeout_guard() -> None:
    raise NotImplementedError("proprietary: removed from public showcase")


def main() -> int:
    raise NotImplementedError("proprietary: removed from public showcase")
