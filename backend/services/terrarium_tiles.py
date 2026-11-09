# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Terrarium elevation tiles loader (no API key)."""

from __future__ import annotations
import math
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Tuple, Optional
import numpy as np
import requests


@dataclass(frozen=True)
class TileKey:
    z: int
    x: int
    y: int


def _latlon_to_global_pixel(lon: float, lat: float, z: int) -> Tuple[float, float]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _global_pixel_to_tile(x: float, y: float) -> Tuple[int, int, float, float]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _bilinear_sample(img: np.ndarray, px: float, py: float) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _decode_terrarium_png(png_bytes: bytes) -> np.ndarray:
    raise NotImplementedError("proprietary: removed from public showcase")


class TerrariumTileProvider:
    def __init__(self, base_url: str = None, cache_dir: str = None, timeout: float = None):
        raise NotImplementedError("proprietary: removed from public showcase")

    def _tile_path(self, key: TileKey) -> Path:
        raise NotImplementedError("proprietary: removed from public showcase")

    def _fetch_tile_png(self, key: TileKey) -> Optional[bytes]:
        raise NotImplementedError("proprietary: removed from public showcase")

    def get_tile(self, key: TileKey, _depth: int = None) -> Optional[np.ndarray]:
        raise NotImplementedError("proprietary: removed from public showcase")

    def prefetch(self, keys: "list[TileKey]", workers: int = None) -> None:
        """Паралельно тягне відсутні тайли (диск/памʼять — миттєво)."""
        raise NotImplementedError("proprietary: removed from public showcase")

    def sample_points(self, lats: np.ndarray, lons: np.ndarray, z: int) -> Optional[np.ndarray]:
        """Білінійна вибірка висот для масиву точок."""
        raise NotImplementedError("proprietary: removed from public showcase")
