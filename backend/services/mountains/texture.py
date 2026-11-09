# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Текстури й превʼю для режиму «Гори»."""

from __future__ import annotations
import io
import math
import os
import time
from pathlib import Path
from typing import Optional
import numpy as np
import requests

CACHE = None
ESRI = None
UA = None


def _get(url: str, key: str) -> Optional[bytes]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _gpx(lat, lon, z):
    raise NotImplementedError("proprietary: removed from public showcase")


def satellite_texture(
    lat: float, lon: float, area_m: float, tex: int = None, epsg: Optional[int] = None
) -> Optional[np.ndarray]:
    """→ uint8 (tex×tex×3), рядок 0 = ПІВДЕНЬ (як сітка моделі). None, якщо тайли недоступні."""
    raise NotImplementedError("proprietary: removed from public showcase")


def hillshade_rgb(
    Z: np.ndarray, step_m: float, az: float = None, alt: float = None, cmap: str = None
) -> np.ndarray:
    """Тіньова карта (рядок 0 = південь) → uint8 RGB."""
    raise NotImplementedError("proprietary: removed from public showcase")


def hillshade_png(
    Z: np.ndarray, step_m: float, size_px: int = None, texture: Optional[np.ndarray] = None
) -> bytes:
    """PNG «північ угорі»: hillshade (за бажанням змішаний із знімком)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def paint_texture(Z: np.ndarray, step_m: float, sat: np.ndarray) -> np.ndarray:
    """Знімок без тіней: оцінюємо сонце знімка (перебір азимут/висота за кореляцією), ділимо
    на модель освітлення, у глибоких тінях підставляємо колір околу."""
    raise NotImplementedError("proprietary: removed from public showcase")


def compose_plate_texture(
    inner: np.ndarray, size_mm: float, fw: float, tex: int = None, frame_rgb=None, wall_rgb=None
) -> np.ndarray:
    """Текстура на всю плиту (для UV = xy/size): усередині — знімок/розпис, по краю — ободок."""
    raise NotImplementedError("proprietary: removed from public showcase")
