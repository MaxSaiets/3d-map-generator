# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Пайплайн «Гори»: spec → DEM → поле висот (масштаб, ободок, боки, фігурки) → файли."""

from __future__ import annotations
import gc
import io
import json
import os
import time
import zipfile
from pathlib import Path
import numpy as np
from . import figures as FIG
from .agent import normalize_spec
from .dem import fetch_dem
from .mesh import (
    apply_slope_band,
    frame_solid,
    preview_glb,
    split_tiles,
    tile_cuts,
    write_3mf,
    write_3mf_multi,
)
from .texture import compose_plate_texture, hillshade_png, paint_texture, satellite_texture

MAX_GRID = None
DEFAULT_AREA_KM = None


def _grid_for(inner_mm: float) -> int:
    raise NotImplementedError("proprietary: removed from public showcase")


def _summit(Zmm, core_mask):
    raise NotImplementedError("proprietary: removed from public showcase")


def _figure_xy(
    where: str,
    f: dict,
    Zmm: np.ndarray,
    cell: float,
    core_mask,
    inner: float,
    band: float,
    taken: list,
):
    """→ (x_mm, y_mm) у координатах рельєфу."""
    raise NotImplementedError("proprietary: removed from public showcase")


def quick_preview(
    lat: float,
    lon: float,
    area_km: float,
    size_mm: float = None,
    height_mm: float | None = None,
    with_sat: bool = True,
) -> dict:
    """Миттєве превʼю для мапи: hillshade (+знімок) 384 px + цифри масштабу. Грубa сітка 181."""
    raise NotImplementedError("proprietary: removed from public showcase")


def run(spec_in: dict, out_dir: Path, basename: str, progress=None, log=print) -> dict:
    raise NotImplementedError("proprietary: removed from public showcase")
