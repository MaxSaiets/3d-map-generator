# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Green areas (parks/forests/grass) processor."""

from __future__ import annotations
import os
from typing import Optional
import geopandas as gpd
import numpy as np
import trimesh
from shapely.geometry import Polygon, MultiPolygon, box, Point
from shapely.ops import transform, unary_union
from services.terrain_provider import TerrainProvider
from services.global_center import GlobalCenter
from services.geometry_context import (
    clean_geometry,
    clip_geometry,
    to_local_geodataframe_if_needed,
    to_local_geometry_if_needed,
)
from services.detail_layer_utils import MICRO_REGION_THRESHOLD_MM, model_mm_to_world_m
from services.mesh_triangulation import (
    extrude_polygon_uniform,
    extrude_polygon_grid,
    extrude_polygon_quality,
)
from services.processing_results import GreenAreaProcessingResult


def _polygon_min_dimension(poly: Polygon) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _polygon_meets_micro_threshold(poly: Polygon, min_feature_m: float) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _recover_park_geometry(*, original_geom, current_geom, blocker_geom, min_feature_m: float):
    raise NotImplementedError("proprietary: removed from public showcase")


def _iter_polygon_parts(geom) -> list[Polygon]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _safe_distance(lhs, rhs) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _absorb_tiny_zone_remainder_into_target(
    *,
    target_geom,
    zone_polygon_local,
    road_polygons=None,
    water_polygons=None,
    building_polygons=None,
    min_feature_m: float,
):
    raise NotImplementedError("proprietary: removed from public showcase")


def _polygon_equivalent_width(poly: Polygon) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _polygon_meets_land_threshold(poly: Polygon, min_feature_m: float) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _fill_tiny_park_voids(park_geom, *, min_feature_m: float, preserve_geom=None):
    raise NotImplementedError("proprietary: removed from public showcase")


def _opened_geometry(geom, radius_m: float):
    raise NotImplementedError("proprietary: removed from public showcase")


def _normalize_land_partition(
    *, parks_geom, legal_land, zone_polygon_local, park_intent_geom=None, min_feature_m: float
):
    raise NotImplementedError("proprietary: removed from public showcase")


def _apply_fit_inset_to_green_mask(geometry, *, fit_clearance_m: float, min_feature_m: float):
    raise NotImplementedError("proprietary: removed from public showcase")


def _finalize_land_masks(
    *,
    parks_geom,
    park_intent_geom=None,
    zone_polygon_local,
    road_polygons=None,
    water_polygons=None,
    building_polygons=None,
    min_feature_m: float,
):
    raise NotImplementedError("proprietary: removed from public showcase")


def _create_high_res_mesh(
    poly: Polygon, height_m: float, target_edge_len_m: float
) -> Optional[trimesh.Trimesh]:
    """Створює меш з UNIFORM тріангуляцією (remeshed) використовуючи Steiner points.
    Виправляє проблему діагональних смуг, створюючи рівномірні трикутники."""
    raise NotImplementedError("proprietary: removed from public showcase")


def process_green_areas(
    gdf_green: gpd.GeoDataFrame,
    height_m: float,
    embed_m: float,
    terrain_provider: Optional[TerrainProvider] = None,
    global_center: Optional[GlobalCenter] = None,
    scale_factor: Optional[float] = None,
    zone_polygon_local: Optional[object] = None,
    min_feature_mm: float = MICRO_REGION_THRESHOLD_MM,
    simplify_mm: float = None,
    fit_clearance_mm: float = None,
    road_polygons: Optional[object] = None,
    water_polygons: Optional[object] = None,
    building_polygons: Optional[object] = None,
    return_result: bool = False,
) -> Optional[trimesh.Trimesh | GreenAreaProcessingResult]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _add_strong_faceted_texture(
    mesh: trimesh.Trimesh,
    height_m: float,
    scale_factor: Optional[float] = None,
    original_polygon: Optional[Polygon] = None,
    global_center: Optional[GlobalCenter] = None,
    relative_heights: Optional[np.ndarray] = None,
) -> trimesh.Trimesh:
    """Adds a seam-stable faceted park texture using world-anchored coordinates.
    Only top vertices are modified and boundary fade keeps insert fit stable."""
    raise NotImplementedError("proprietary: removed from public showcase")
