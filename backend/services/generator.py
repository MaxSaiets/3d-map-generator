# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""3D Map Generation Pipeline — чистий, лінійний pipeline."""

from __future__ import annotations
import gc
import os
import concurrent.futures
import traceback
from dataclasses import dataclass, field
from typing import Optional, Callable, List
import numpy as np
import trimesh
import geopandas as gpd
from shapely.ops import unary_union, transform as shapely_transform
from shapely.geometry import box as shapely_box
from services.global_center import GlobalCenter, set_global_center
from services.crs_utils import bbox_latlon_to_utm
from services.data_loader import fetch_city_data
from services.extras_loader import fetch_extras
from services.terrain_generator import create_terrain_mesh
from services.road_processor import process_roads, build_road_polygons, merge_close_road_gaps
from services.building_processor import process_buildings
from services.water_processor import process_water_surface
from services.green_processor import process_green_areas
from services.terrain_cutter import (
    cut_roads_from_solid_terrain,
    extend_road_mesh_to_uniform_bottom,
    cut_parks_from_solid_terrain,
    extend_parks_mesh_to_uniform_bottom,
)
from services.model_exporter import export_scene

GROOVE_CLEARANCE_MM = None
MIN_PRINTABLE_GAP_MM = None


@dataclass
class GenerationParams:
    north: float
    south: float
    east: float
    west: float
    model_size_mm: float = None
    export_format: str = None
    terrain_resolution: int = None
    terrain_z_scale: float = None
    terrain_base_thickness_mm: float = None
    terrain_smoothing_sigma: float = None
    terrarium_zoom: int = None
    terrain_subdivide: bool = None
    terrain_subdivide_levels: int = None
    road_width_multiplier: float = None
    road_height_mm: float = None
    road_embed_mm: float = None
    building_min_height: float = None
    building_height_multiplier: float = None
    building_foundation_mm: float = None
    building_embed_mm: float = None
    building_max_foundation_mm: float = None
    include_parks: bool = None
    parks_height_mm: float = None
    parks_embed_mm: float = None
    water_depth_mm: float = None


def _to_local_transformer(global_center: GlobalCenter):
    """Повертає функцію для shapely_transform: UTM coords → local coords."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _convert_gdf_to_local(gdf: gpd.GeoDataFrame, to_local) -> gpd.GeoDataFrame:
    """Конвертує всі геометрії GDF у локальні координати."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _safe_unary_union(geoms) -> Optional[object]:
    """Безпечний unary_union, повертає None при помилці."""
    raise NotImplementedError("proprietary: removed from public showcase")


def generate_3d_map(
    params: GenerationParams,
    output_path: str,
    status_fn: Optional[Callable[[int, str], None]] = None,
) -> str:
    """Генерує 3D карту з пазами для доріг та парків."""
    raise NotImplementedError("proprietary: removed from public showcase")
