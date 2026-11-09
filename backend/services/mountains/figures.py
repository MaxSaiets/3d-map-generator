# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Фігурки (люди, хатина) на рельєфі: бібліотека + посадка."""

from __future__ import annotations
import json
import os
from pathlib import Path
from typing import Optional
import numpy as np
from scipy.ndimage import gaussian_filter

ASSETS = None
_smooth = None


def library() -> list[dict]:
    raise NotImplementedError("proprietary: removed from public showcase")


def get(fid: str) -> Optional[dict]:
    raise NotImplementedError("proprietary: removed from public showcase")


def zat_on(Z, x, y, cell):
    raise NotImplementedError("proprietary: removed from public showcase")


def grade(Z, cell, cx, cy, r_flat, r_blend, clamp_deg, detail_k=None, pct=None):
    """Локальна площина (ухил ≤ clamp) у радіусі r_flat, перехід r_blend, дрібна фактура лишається.
    → (Zs, down_dir(2), slope_deg, max_change)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _rotz(deg):
    raise NotImplementedError("proprietary: removed from public showcase")


def _load(f: dict, height_mm: float):
    raise NotImplementedError("proprietary: removed from public showcase")


def place_standing(Zmm, cell, f, x, y, height_mm, log):
    raise NotImplementedError("proprietary: removed from public showcase")


def place_building(Zmm, cell, f, x, y, height_mm, log):
    raise NotImplementedError("proprietary: removed from public showcase")


def _steepest_near(Zmm, cell, x, y, radius):
    raise NotImplementedError("proprietary: removed from public showcase")


def place_climbing(Zmm, cell, f, x, y, height_mm, log):
    raise NotImplementedError("proprietary: removed from public showcase")


PLACERS = None


def place_all(
    Zmm: np.ndarray, cell: float, requests: list[dict], log=print
) -> tuple[np.ndarray, list[dict]]:
    """requests: [{"id","x_mm","y_mm","height_mm"}] у координатах РЕЛЬЄФУ (без ободка).
    → (Zmm після вирівнювань, [{"id","mesh","extra"(канат)}])."""
    raise NotImplementedError("proprietary: removed from public showcase")


def fuse_into(tile_mesh, parts: list, log=print):
    """Зрощує фігурки в плитку (manifold). Якщо не вдалося — повертає (плитка, окремі частини)."""
    raise NotImplementedError("proprietary: removed from public showcase")
