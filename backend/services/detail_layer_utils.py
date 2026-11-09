# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Optional
import trimesh
import numpy as np
from geopandas import GeoDataFrame
from shapely.ops import transform as transform_geometry

MICRO_REGION_THRESHOLD_MM = None
MIN_ROAD_WIDTH_MODEL_MM = None
MIN_LAND_WIDTH_MODEL_MM = None


def model_mm_to_world_m(model_mm: float, scale_factor: Optional[float]) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def clamp_mesh_to_terrain_floor(
    mesh: Optional[trimesh.Trimesh], terrain_mesh: Optional[trimesh.Trimesh], *, label: str
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def prepare_green_areas_for_processing(
    gdf_green: Optional[GeoDataFrame], *, global_center: Any, zone_polygon_local: Any
) -> Optional[GeoDataFrame]:
    raise NotImplementedError("proprietary: removed from public showcase")


def filter_mesh_components_by_printability(
    mesh: Optional[trimesh.Trimesh],
    *,
    scale_factor: Optional[float],
    min_feature_mm: float = MICRO_REGION_THRESHOLD_MM,
    label: str = None,
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")
