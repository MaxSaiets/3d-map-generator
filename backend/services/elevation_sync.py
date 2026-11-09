# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Сервіс для синхронізації висот між зонами гексагональної сітки.
Забезпечує, що всі зони використовують один глобальний elevation_ref_m та baseline_offset_m."""

import numpy as np
from typing import List, Tuple, Optional, Dict
from services.elevation_api import get_elevation_abs_meters_from_api
from services.crs_utils import bbox_latlon_to_utm
import os
import math


def _terrarium_minmax_elevation_in_bbox(
    bbox_latlon: Tuple[float, float, float, float], terrarium_zoom: Optional[int] = None
) -> Tuple[Optional[float], Optional[float]]:
    """Robust global (min, max) for Terrarium: scan *all* tiles intersecting bbox and take
    the min/max pixel elevation (via low/high quantiles to reject outlier spikes).
    The robust MIN avoids negative Z / seams; the robust MAX gives the true global relief
    range so a SERIES of tiles can share ONE vertical-exaggeration gain (continuous relief
    across seams — no per-tile "висоти перепадають")."""
    raise NotImplementedError("proprietary: removed from public showcase")


def calculate_global_elevation_reference(
    zones: List[Dict],
    source_crs: Optional[object] = None,
    terrarium_zoom: Optional[int] = None,
    z_scale: float = None,
    sample_points_per_zone: int = None,
    global_center: Optional[object] = None,
    explicit_bbox: Optional[Tuple[float, float, float, float]] = None,
) -> Tuple[Optional[float], float, Optional[float]]:
    """Обчислює глобальний elevation_ref_m для всієї сітки зон.
    Це забезпечує, що всі зони використовують одну базову висоту для нормалізації."""
    raise NotImplementedError("proprietary: removed from public showcase")


def calculate_optimal_base_thickness(
    elevation_ref_m: Optional[float],
    zones: List[Dict],
    model_size_mm: float = None,
    min_base_thickness_mm: float = None,
    max_base_thickness_mm: float = None,
) -> float:
    """Обчислює оптимальну товщину підложки (base) для всіх зон.
    Мінімізує товщину, але забезпечує стабільність моделей та ідеальне стикування зон."""
    raise NotImplementedError("proprietary: removed from public showcase")
