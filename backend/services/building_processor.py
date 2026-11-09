# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Сервіс для обробки будівель з екструзією та покращеними дахами
Покращено: додано посадку будівель на рельєф через TerrainProvider"""

import geopandas as gpd
import trimesh
import numpy as np
from shapely.geometry import Polygon, Point, MultiPolygon, box
from shapely.geometry.base import BaseGeometry
from shapely.ops import unary_union
from typing import List, Optional
from dataclasses import dataclass
from services.terrain_provider import TerrainProvider
from services.global_center import GlobalCenter
from services.geometry_context import to_local_geodataframe_if_needed
import mapbox_earcut
import re
import gc
import os

LANDMARK_RENDERING_ENABLED = None


@dataclass
class BuildingMeshRecord:
    mesh: trimesh.Trimesh
    footprint: Optional[BaseGeometry]
    base_z: float
    landmark: str = None


def process_buildings(
    gdf_buildings: gpd.GeoDataFrame,
    min_height: float = None,
    height_multiplier: float = None,
    terrain_provider: Optional[TerrainProvider] = None,
    foundation_depth: float = None,
    embed_depth: float = None,
    max_foundation_depth: Optional[float] = None,
    global_center: Optional[GlobalCenter] = None,
    coordinates_already_local: bool = False,
    return_records: bool = False,
    exclusion_polygons: Optional[BaseGeometry] = None,
    min_feature_m: float = None,
    scale_factor: Optional[float] = None,
    max_height: Optional[float] = None,
) -> List[trimesh.Trimesh] | List[BuildingMeshRecord]:
    """Обробляє будівлі, створюючи 3D меші з екструзією"""
    raise NotImplementedError("proprietary: removed from public showcase")


def get_building_height(row, min_height: float) -> float:
    """Визначає висоту будівлі з OSM тегів"""
    raise NotImplementedError("proprietary: removed from public showcase")


def extrude_building(polygon: Polygon, height: float) -> Optional[trimesh.Trimesh]:
    """Екструдує полігон будівлі на вказану висоту"""
    raise NotImplementedError("proprietary: removed from public showcase")
