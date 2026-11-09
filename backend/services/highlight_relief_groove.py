# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Highlight-будинок на РЕЛЬЄФІ — паз ЯК У ДОРІГ (ЧИСТІ стінки) + будинок СТОЇТЬ."""

from __future__ import annotations
from typing import Optional, Tuple
import numpy as np
import trimesh
from shapely.geometry import Point
from shapely.geometry.base import BaseGeometry


def _contains_mask(poly: BaseGeometry, xy: np.ndarray) -> np.ndarray:
    """Векторизований point-in-polygon (shapely 2.x contains_xy) з prepared-fallback."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _vertex_set_fallback(terrain_mesh, groove, floor, zone_prefix):
    """Запасний паз опусканням вершин (стінки обривчасті — лише коли boolean недоступний)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def carve_highlight_groove(
    terrain_mesh: Optional[trimesh.Trimesh],
    footprint: Optional[BaseGeometry],
    building_top_m: float,
    building_bottom_m: float,
    *,
    scale_factor: float,
    clearance_mm: float = None,
    zone_prefix: str = None,
) -> Tuple[Optional[trimesh.Trimesh], Optional[trimesh.Trimesh]]:
    """ЧИСТА boolean-кишеня (паз) під будинок, що СТОЇТЬ + червоний будинок з пласким дном."""
    raise NotImplementedError("proprietary: removed from public showcase")
