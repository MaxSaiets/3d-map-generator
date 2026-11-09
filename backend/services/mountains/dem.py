# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Джерела висот для режиму «Гори»."""

from __future__ import annotations
import math
import os
import threading
import time
from pathlib import Path
from typing import Optional
import numpy as np
import requests

CACHE_ROOT = None
COP_URL = None
SWISS_STAC = None
UA = None


def utm_epsg(lat: float, lon: float) -> int:
    raise NotImplementedError("proprietary: removed from public showcase")


def make_grid(lat: float, lon: float, area_m: float, grid: int):
    """Квадратна UTM-сітка grid×grid зі стороною area_m навколо (lat, lon).
    → (lons, lats) плоскі масиви, step_m, epsg, (cx, cy)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _cop_name(lat_floor: int, lon_floor: int) -> str:
    raise NotImplementedError("proprietary: removed from public showcase")


_dl_locks: dict[str, threading.Lock] = None
_dl_guard = None


def _download(url: str, dest: Path, timeout: float = None, attempts: int = None) -> bool:
    """Один тайл качає лише один потік (превʼю і генерація йшли одночасно → «.part → tif» падав
    у другого з ENOENT). Лок на шлях + унікальний tmp; після чекання просто перевіряємо файл."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _download_locked(url: str, dest: Path, timeout: float, attempts: int) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def sample_copernicus(lats: np.ndarray, lons: np.ndarray) -> Optional[np.ndarray]:
    """Білінійна вибірка Copernicus GLO-30. NaN там, де тайла немає (океан)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _swiss_items(bbox_ll):
    raise NotImplementedError("proprietary: removed from public showcase")


def sample_swissalti(
    lats: np.ndarray, lons: np.ndarray, target_step_m: float, max_tiles: int = None
) -> Optional[np.ndarray]:
    """→ висоти (NaN поза швейцарськими даними) або None, якщо область не в Швейцарії."""
    raise NotImplementedError("proprietary: removed from public showcase")


def sample_terrarium(lats: np.ndarray, lons: np.ndarray, zoom: int = None) -> Optional[np.ndarray]:
    raise NotImplementedError("proprietary: removed from public showcase")


def fetch_dem(
    lat: float, lon: float, area_m: float, grid: int, blend_m: float = None, progress=None
) -> dict:
    """→ {"Z": (grid×grid) м, рядок 0 = південь; "step_m"; "sources": [..]; "coverage": {..};
    "epsg"; "center_utm"; "elev_min"; "elev_max"; "lat"; "lon"; "area_m"}"""
    raise NotImplementedError("proprietary: removed from public showcase")
