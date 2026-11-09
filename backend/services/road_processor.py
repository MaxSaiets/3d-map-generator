# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Сервіс для обробки доріг з буферизацією та об'єднанням
Покращена версія з фізичною шириною доріг та підтримкою мостів
Використовує trimesh.creation.extrude_polygon для надійної тріангуляції"""

import ast
import os
import osmnx as ox
import json
import trimesh
import numpy as np
import warnings
import shapely as _shapely
from shapely.ops import unary_union, transform, snap
from shapely.geometry import Polygon, MultiPolygon, box, LineString, Point
from shapely.geometry import mapping, shape
from typing import Optional, List, Tuple
import geopandas as gpd
from services.terrain_provider import TerrainProvider
from services.global_center import GlobalCenter
from services.building_supports import union_mesh_collection
from services.detail_layer_utils import (
    MICRO_REGION_THRESHOLD_MM,
    MIN_ROAD_WIDTH_MODEL_MM,
    model_mm_to_world_m,
)
from services.geometry_context import (
    clean_geometry,
    looks_like_projected_meters,
    make_to_local_transformer,
    to_local_geometry_if_needed,
)
from services.mesh_triangulation import (
    extrude_polygon_grid,
    extrude_polygon_uniform,
    extrude_polygon_quality,
    refine_mesh_long_edges,
)
from services.mesh_quality import improve_mesh_for_3d_printing, validate_mesh_for_3d_printing
from services.processing_results import RoadProcessingResult
from scipy.spatial import cKDTree

NON_PRINTABLE_HIGHWAY_TYPES = None
PRINTABLE_HIGHWAY_PRIORITY = None
DRIVABLE_HIGHWAY_PRIORITY = None


def _extract_numeric_token(raw_value) -> float | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _resolve_osm_road_width_m(row, fallback_width_m: float) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def normalize_highway_tag(raw_highway):
    raise NotImplementedError("proprietary: removed from public showcase")


def normalize_drivable_highway_tag(raw_highway):
    raise NotImplementedError("proprietary: removed from public showcase")


def _write_debug_geometry_geojson(name: str, geometry) -> None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _rebuild_road_geometry(geometry):
    raise NotImplementedError("proprietary: removed from public showcase")


def _clip_mesh_to_road_footprint(
    mesh: Optional[trimesh.Trimesh], road_polygon
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _mesh_boundary_edge_count(mesh: Optional[trimesh.Trimesh]) -> int:
    raise NotImplementedError("proprietary: removed from public showcase")


def _cleanup_road_mesh(mesh: Optional[trimesh.Trimesh]) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _mesh_projection_geometry(
    mesh: Optional[trimesh.Trimesh], *, top_only: bool
) -> Optional[Polygon]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _road_mesh_candidate_score(mesh: Optional[trimesh.Trimesh], road_polygon=None) -> tuple:
    raise NotImplementedError("proprietary: removed from public showcase")


def _road_mesh_topology_only_score(mesh: Optional[trimesh.Trimesh]) -> tuple:
    raise NotImplementedError("proprietary: removed from public showcase")


def create_deep_road_prism(
    polygon: Polygon,
    terrain_provider: TerrainProvider,
    scale_factor: float = None,
    top_z_offset: float = None,
    min_height: float = None,
) -> Optional[trimesh.Trimesh]:
    """Створює блок дороги для вставки (Inlay).
    Дно розраховується локально: min(surface_z) - 1мм."""
    raise NotImplementedError("proprietary: removed from public showcase")


def create_road_surface_cap(
    polygon: Polygon,
    terrain_provider: TerrainProvider,
    *,
    scale_factor: float = None,
    top_z_offset: float = None,
    cap_thickness_m: Optional[float] = None,
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def create_bridge_supports(
    bridge_polygon: Polygon,
    bridge_height: float,
    terrain_provider: Optional[TerrainProvider],
    water_level: Optional[float],
    support_spacing: float = None,
    support_width: float = None,
    min_support_height: float = None,
) -> List[trimesh.Trimesh]:
    """Створює опори для моста, які йдуть від моста до землі/води.
    Це необхідно для стабільності при 3D друку."""
    raise NotImplementedError("proprietary: removed from public showcase")


def detect_bridges(
    G_roads,
    water_geometries: Optional[List] = None,
    bridge_tag: str = None,
    bridge_buffer_m: float = None,
    clip_polygon: Optional[object] = None,
) -> List[Tuple[object, object, float, bool, int]]:
    """Визначає мости: дороги, які перетинають воду або мають тег bridge=yes"""
    raise NotImplementedError("proprietary: removed from public showcase")


def densify_geometry(geom, max_segment_length=None):
    raise NotImplementedError("proprietary: removed from public showcase")


RAILWAY_MIN_WIDTH_FACTOR = None
RAILWAY_TARGET_MM = None


def build_railway_ladder(line, half_width_m: float, max_sleepers: int = None):
    """Залізниця = тонка нитка + ШПАЛИ ПОПЕРЕК (фідбек Роми 2026-08-10)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def build_railway_polygons(
    G_roads,
    *,
    scale_factor: Optional[float] = None,
    min_width_m: Optional[float] = None,
    clip_geom=None,
) -> Optional[object]:
    """Колії ОКРЕМОЮ геометрією — драбина (нитка + шпали) у світових метрах."""
    raise NotImplementedError("proprietary: removed from public showcase")


def build_road_polygons(
    G_roads,
    width_multiplier: float = None,
    min_width_m: Optional[float] = None,
    extra_buffer_m: float = None,
    scale_factor: Optional[float] = None,
    exclude_railway: bool = False,
) -> Optional[object]:
    """Builds merged road polygons (2D) from a roads graph/edges gdf.
    This is useful for terrain-first operations (flattening terrain under roads) and
    also allows reusing the merged geometry for mesh generation."""
    raise NotImplementedError("proprietary: removed from public showcase")


def merge_close_road_gaps(road_geom, min_gap_m: float) -> Optional[object]:
    """Об'єднує вузькі проміжки між дорогами (наприклад, між зустрічними смугами) у єдину дорогу.
    Проміжки менші за min_gap_m замінюються дорогою — щоб не створювати непрінтабельні шматки рельєфу."""
    raise NotImplementedError("proprietary: removed from public showcase")


def filter_non_printable_road_polygons(
    road_geom,
    *,
    min_feature_m: float,
    min_component_width_m: float = None,
    min_area_factor: float = None,
):
    raise NotImplementedError("proprietary: removed from public showcase")


def _fill_small_holes_in_polygon(
    poly: Polygon, *, min_feature_m: float, min_area_factor: float = None, preserve_geom=None
) -> Optional[Polygon]:
    raise NotImplementedError("proprietary: removed from public showcase")


def fill_small_road_voids(
    road_geom, *, min_feature_m: float, min_area_factor: float = None, preserve_geom=None
):
    raise NotImplementedError("proprietary: removed from public showcase")


def fill_narrow_orphan_road_holes(road_geom, *, max_hole_width_m: float, preserve_geom=None):
    raise NotImplementedError("proprietary: removed from public showcase")


def fill_narrow_boundary_road_gaps(
    road_geom, *, zone_polygon, max_gap_width_m: float, preserve_geom=None
):
    """Fill narrow terrain slivers between roads and the model boundary."""
    raise NotImplementedError("proprietary: removed from public showcase")


def merge_boundary_road_gaps_with_model_edge(
    road_geom, *, zone_polygon, max_gap_width_m: float, preserve_geom=None
):
    """Treat model edge as a virtual road side and close narrow open boundary gaps."""
    raise NotImplementedError("proprietary: removed from public showcase")


def fill_narrow_terrain_slivers_between_roads(
    road_geom, *, zone_polygon, max_gap_width_m: float, preserve_geom=None
):
    """Absorb sub-printable terrain slivers that sit between nearby roads."""
    raise NotImplementedError("proprietary: removed from public showcase")


def fill_narrow_terrain_channels_between_roads(
    road_geom, *, zone_polygon, max_gap_width_m: float, preserve_geom=None
):
    """Fill narrow terrain channels even when they are part of a larger open terrain polygon."""
    raise NotImplementedError("proprietary: removed from public showcase")


def fill_small_road_enclosed_terrain_islands(
    road_geom, *, zone_polygon, max_island_area_m2: float, preserve_geom=None
):
    """Fill small terrain islands that are fully enclosed by road boundaries."""
    raise NotImplementedError("proprietary: removed from public showcase")


def fill_compact_road_medians(road_geom, *, zone_polygon, channel_gap_width_m: float):
    """Fill compact median-like wedges left by near-parallel roads around junctions."""
    raise NotImplementedError("proprietary: removed from public showcase")


def fill_tiny_road_wedges(road_geom, *, gap_fill_m: float):
    """Conservatively fill only very small wedge-shaped additions that appear between
    neighboring road branches. This is intentionally stricter than a full closing
    delta, to avoid flooding intersections or widening roads too much."""
    raise NotImplementedError("proprietary: removed from public showcase")


def trim_narrow_attached_road_branches(road_geom, *, min_width_m: float, zone_polygon=None):
    """Trim dead-end road branches that remain thinner than the printable width."""
    raise NotImplementedError("proprietary: removed from public showcase")


def normalize_road_mask_for_print(
    road_geom,
    *,
    gap_fill_m: float = None,
    min_feature_m: float = None,
    trim_width_m: float = None,
    preserve_geom=None,
    zone_polygon=None,
    orphan_hole_width_m: float = None,
    scale_factor: float = None,
):
    """Normalize a 2D road mask for printing.
    Narrow voids between adjacent roads are filled into the road mask,
    and tiny leftover slivers/islands are removed before 3D extrusion."""
    raise NotImplementedError("proprietary: removed from public showcase")


def process_roads(
    G_roads,
    width_multiplier: float = None,
    terrain_provider: Optional[TerrainProvider] = None,
    floor_z: Optional[float] = None,
    clearance_mm: float = None,
    scale_factor: float = None,
    road_height: float = None,
    road_embed: float = None,
    road_elevation_mm: float = None,
    merged_roads: Optional[object] = None,
    water_geometries: Optional[List] = None,
    bridge_height_multiplier: float = None,
    global_center: Optional[GlobalCenter] = None,
    min_width_m: Optional[float] = None,
    tiny_feature_threshold_mm: float = MICRO_REGION_THRESHOLD_MM,
    merge_gap_mm: float = None,
    building_clearance_mm: float = None,
    clip_polygon: Optional[object] = None,
    city_cache_key: Optional[str] = None,
    building_polygons: Optional[object] = None,
    preserve_polygons: Optional[object] = None,
    return_result: bool = False,
) -> Optional[trimesh.Trimesh | RoadProcessingResult]:
    """Обробляє дорожню мережу, створюючи 3D меші з правильною шириною"""
    raise NotImplementedError("proprietary: removed from public showcase")
