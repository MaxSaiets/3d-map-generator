# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from shapely.geometry.base import BaseGeometry
from shapely.ops import unary_union
from services.detail_layer_utils import (
    MIN_LAND_WIDTH_MODEL_MM,
    MIN_ROAD_WIDTH_MODEL_MM,
    model_mm_to_world_m,
)

MIN_PRINTABLE_GAP_MM = None
DEFAULT_CLEARANCE_MM = None


@dataclass
class SlicerConfig:
    scale_factor: float
    min_width_mm: float = None
    gap_fill_mm: float = None
    corner_smooth_mm: float = None
    tiny_feature_mm: float = None


def _safe_buffer(geom: BaseGeometry, distance: float, **kwargs) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _clean(geom: Optional[BaseGeometry]) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def enforce_min_width(geom: Optional[BaseGeometry], min_width_m: float) -> Optional[BaseGeometry]:
    """Morphological open with half min_width, then dilate back to preserve edges."""
    raise NotImplementedError("proprietary: removed from public showcase")


def merge_close_gaps(geom: Optional[BaseGeometry], gap_m: float) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def smooth_corners(geom: Optional[BaseGeometry], radius_m: float) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def remove_tiny_features(
    geom: Optional[BaseGeometry], min_area_m2: float
) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def slice_mask(
    geom: Optional[BaseGeometry],
    *,
    config: SlicerConfig,
    subtract: Optional[BaseGeometry] = None,
    clearance_mm: float = None,
) -> Optional[BaseGeometry]:
    """Apply a full slicer-style cleanup pass to a 2D mask."""
    raise NotImplementedError("proprietary: removed from public showcase")


def slice_road_mask(
    roads: Optional[BaseGeometry],
    *,
    scale_factor: float,
    buildings: Optional[BaseGeometry] = None,
    building_clearance_mm: float = DEFAULT_CLEARANCE_MM,
) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def slice_land_mask(
    land: Optional[BaseGeometry],
    *,
    scale_factor: float,
    subtract: Optional[BaseGeometry] = None,
    clearance_mm: float = DEFAULT_CLEARANCE_MM,
) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")
