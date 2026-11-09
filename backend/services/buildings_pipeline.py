# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
import os
from typing import Any, Optional
import pandas as pd
from geopandas import GeoDataFrame
from shapely.geometry.base import BaseGeometry
from shapely.ops import unary_union
from services.building_supports import (
    build_building_supports,
    concatenate_meshes,
    merge_building_and_support_meshes,
)
from services.building_processor import process_buildings
from services.detail_layer_utils import MICRO_REGION_THRESHOLD_MM, model_mm_to_world_m
from services.printable_3d_validator import validate_building_mesh
from services.processing_results import BuildingLayerResult


def _is_building_part_row(row: Any) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _clean_building_geometry(geometry: Optional[BaseGeometry]) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def split_building_parts_from_parent_footprints(
    buildings: GeoDataFrame,
    *,
    min_part_overlap_ratio: float = None,
    full_coverage_ratio: float = None,
    min_remainder_area_m2: float = None,
) -> GeoDataFrame:
    """Let OSM building:part geometry win over the parent building footprint."""
    raise NotImplementedError("proprietary: removed from public showcase")


def process_building_layer(
    *,
    task: Any,
    request: Any,
    scale_factor: Optional[float],
    terrain_provider: Any,
    global_center: Any,
    stl_extra_embed_m: float,
    gdf_buildings_local: Optional[GeoDataFrame],
    support_exclusion_polygons: Optional[BaseGeometry] = None,
    road_insert_mask: Optional[BaseGeometry] = None,
    road_groove_mask: Optional[BaseGeometry] = None,
    building_exclusion_polygons: Optional[BaseGeometry] = None,
) -> BuildingLayerResult:
    raise NotImplementedError("proprietary: removed from public showcase")
