# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Сервіс для обробки водних об'єктів з булевим відніманням"""

import os
import geopandas as gpd
import trimesh
import numpy as np
from shapely.geometry import Polygon, box, Point
from shapely.ops import transform
from typing import Optional
from services.terrain_provider import TerrainProvider
from services.global_center import GlobalCenter
from services.detail_layer_utils import model_mm_to_world_m
from services.mesh_triangulation import (
    extrude_polygon_uniform,
    extrude_polygon_grid,
    extrude_polygon_quality,
)


def process_water(
    gdf_water: gpd.GeoDataFrame,
    depth_mm: float = None,
    depth_meters: Optional[float] = None,
    terrain_provider: Optional[TerrainProvider] = None,
    depth: Optional[float] = None,
) -> Optional[trimesh.Trimesh]:
    """Створює меш для води (западини для булевого віднімання)"""
    raise NotImplementedError("proprietary: removed from public showcase")


def process_water_surface(
    gdf_water: gpd.GeoDataFrame,
    thickness_m: float,
    depth_meters: float,
    terrain_provider: Optional[TerrainProvider] = None,
    global_center: Optional[GlobalCenter] = None,
    coordinates_already_local: bool = False,
    surface_offset_m: float = None,
    scale_factor: Optional[float] = None,
) -> Optional[trimesh.Trimesh]:
    """Creates a thin "water surface" mesh for preview / multi-color printing."""
    raise NotImplementedError("proprietary: removed from public showcase")


def create_water_depression(
    polygon: Polygon, depth: float, terrain_provider: Optional[TerrainProvider] = None
) -> Optional[trimesh.Trimesh]:
    """Створює западину для води (для булевого віднімання з бази)"""
    raise NotImplementedError("proprietary: removed from public showcase")
