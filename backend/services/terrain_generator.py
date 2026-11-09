# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Оптимізований генератор рельєфу та основи.
Фокус: максимальна якість mesh, відсутність багів, правильні трикутники."""

import os
import numpy as np
import trimesh
import time
import math
from typing import Tuple, Optional, List
from shapely.geometry.base import BaseGeometry
from shapely.geometry import Polygon as ShapelyPolygon
import networkx as nx
from services.global_center import GlobalCenter, get_or_create_global_center
from services.crs_utils import bbox_latlon_to_utm
from services.heightmap import (
    get_elevation_data,
    flatten_heightfield_under_buildings,
    flatten_heightfield_under_polygons,
    depress_heightfield_under_polygons,
)
from services.solidifier_robust import create_solid_terrain_robust as create_solid_terrain
from services.solidifier_robust import _sample_polygon_boundary
from services.terrain_provider import TerrainProvider
from services.mesh_clipper import clip_mesh_to_polygon_planes


def _snap_and_extract_boundary_from_clipped(
    mesh: trimesh.Trimesh, polygon: ShapelyPolygon, tolerance: float = None
) -> Tuple[trimesh.Trimesh, Optional[np.ndarray]]:
    """Вирівнює boundary обрізаного mesh по прямим лініям між вершинами полігона
    ТА одразу повертає впорядкований набір boundary вершин."""
    raise NotImplementedError("proprietary: removed from public showcase")


def create_grid_faces(rows: int, cols: int) -> np.ndarray:
    """Створює оптимізовану сітку трикутників для регулярної grid."""
    raise NotImplementedError("proprietary: removed from public showcase")


def lift_relief_to_target(Z, target_relief_m, max_amp=None):
    """Адаптивне підсилення рельєфу для рівнинних міст."""
    raise NotImplementedError("proprietary: removed from public showcase")


def create_terrain_mesh(
    bbox_meters: Tuple[float, float, float, float],
    z_scale: float = None,
    resolution: int = None,
    latlon_bbox: Optional[Tuple[float, float, float, float]] = None,
    source_crs: Optional[object] = None,
    terrarium_zoom: int = None,
    elevation_ref_m: Optional[float] = None,
    baseline_offset_m: float = None,
    base_thickness: float = None,
    flatten_buildings: bool = True,
    building_geometries: Optional[List[BaseGeometry]] = None,
    flatten_roads: bool = False,
    road_geometries: Optional[BaseGeometry] = None,
    smoothing_sigma: float = None,
    water_geometries: Optional[List[BaseGeometry]] = None,
    water_depth_m: float = None,
    global_center: Optional[GlobalCenter] = None,
    bbox_is_local: bool = False,
    subdivide: bool = False,
    subdivide_levels: int = None,
    zone_polygon: Optional[BaseGeometry] = None,
    grid_step_m: Optional[float] = None,
    road_polygons_for_cutting: Optional[BaseGeometry] = None,
    max_relief_m: Optional[float] = None,
    target_relief_m: Optional[float] = None,
    relief_gain: Optional[float] = None,
) -> Tuple[Optional[trimesh.Trimesh], Optional[TerrainProvider]]:
    raise NotImplementedError("proprietary: removed from public showcase")
