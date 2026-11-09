# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
import os
from dataclasses import dataclass
from typing import Any, Optional
import osmnx as ox
from geopandas import GeoDataFrame
from shapely.geometry import box
from shapely.geometry.base import BaseGeometry
from shapely.ops import transform as transform_geometry, unary_union
from services.detail_layer_utils import MICRO_REGION_THRESHOLD_MM, model_mm_to_world_m
from services.road_processor import (
    build_road_polygons,
    build_railway_polygons,
    normalize_drivable_highway_tag,
    normalize_road_mask_for_print,
)
from services.geometry_context import looks_like_projected_meters

ROAD_MIN_WIDTH_WORLD_CAP_M = None
ROAD_GAP_FILL_WORLD_CAP_M = None
ROAD_ORPHAN_HOLE_WORLD_CAP_M = None
PRINT_SAFE_TERRAIN_WALL_MM = None
ROAD_THIN_WALL_FILL_WORLD_CAP_M = None


@dataclass
class RoadGeometryPreparationResult:
    merged_roads_geom: Optional[BaseGeometry]
    merged_roads_geom_local: Optional[BaseGeometry]
    merged_roads_geom_local_raw: Optional[BaseGeometry]
    semantic_centerlines_local: Optional[BaseGeometry] = None
    rails_geom_local: Optional[BaseGeometry] = None


def _build_local_road_edges_subset(
    *,
    G_roads: Any,
    global_center: Any,
    zone_polygon_local: Optional[BaseGeometry],
    zone_prefix: str,
) -> Optional[GeoDataFrame]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _fill_thin_terrain_walls_with_road(
    roads: Optional[BaseGeometry],
    zone_polygon_local: Optional[BaseGeometry],
    scale_factor: Optional[float],
    zone_prefix: str = None,
) -> Optional[BaseGeometry]:
    """Заповнює ДОРОГОЮ тонкі рельєфні стінки між/біля доріг (тонші за друкопридатне)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _drop_dense_service_clusters(
    gdf_local, *, cluster_gap_m=None, min_cluster_edges=None, zone_prefix=None
):
    """Прибирає service-смуги, що утворюють КЛАСТЕР (паркінг/дворовий лабіринт), лишаючи
    ПООДИНОКІ service-заїзди + УСІ residential та вищі (скелет вулиць). КОРІНЬ
    (верифіковано wf_3b3880fd + OSM-аналіз Вугледара: 153 service vs 19 residential у
    дворах): на масштабі друку (sf<~0.15) service-смуги <~5м одна від одної отримують
    min-width floor ~4.5м → перекриваються → суцільна чорна плита, яку НІЯКИЙ fill/"""
    raise NotImplementedError("proprietary: removed from public showcase")


def _fill_small_road_holes(
    geometry: Optional[BaseGeometry], *, max_hole_area_m2: float
) -> Optional[BaseGeometry]:
    """Fill small fully-ENCLOSED interior holes (terrain islands surrounded by road —
    e.g. a pocket between two close roads) below max_hole_area_m2. On THIS raw road
    polygon the islands are topological holes (the full-width road polygons close
    around them), unlike the narrower canonical insert mask where the same pocket
    reads as an open gap and the existing fill misses it. A hole is enclosed by
    definitio"""
    raise NotImplementedError("proprietary: removed from public showcase")


def prepare_road_geometry(
    *,
    G_roads: Any,
    scale_factor: Optional[float],
    road_width_multiplier_effective: float,
    min_printable_gap_mm: float,
    tiny_feature_threshold_mm: float = MICRO_REGION_THRESHOLD_MM,
    road_gap_fill_threshold_mm: float = None,
    enforce_printable_min_width: bool = False,
    min_gap_fill_floor_mm: float = None,
    global_center: Any,
    zone_polygon_local: Optional[BaseGeometry],
    zone_prefix: str = None,
) -> RoadGeometryPreparationResult:
    raise NotImplementedError("proprietary: removed from public showcase")
