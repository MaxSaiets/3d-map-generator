# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
import os
from pathlib import Path


def candidate_pbf_paths() -> list[Path]:
    raise NotImplementedError("proprietary: removed from public showcase")


def resolve_osm_source() -> str:
    raise NotImplementedError("proprietary: removed from public showcase")


def resolve_pbf_path() -> Path | None:
    raise NotImplementedError("proprietary: removed from public showcase")
