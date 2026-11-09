# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
import concurrent.futures
import hashlib
import json
import math
import os
import subprocess
import sys
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Optional
import geopandas as gpd
import osmnx as ox
import pandas as pd
from shapely.geometry import LineString, MultiLineString, MultiPolygon, Polygon, box, mapping, shape
from shapely.geometry.base import BaseGeometry
from shapely.ops import transform as transform_geometry
from shapely.ops import unary_union
from services.building_geometry_pipeline import prepare_building_geometry
from services.building_processor import get_building_height
from services.canonical_2d_pipeline import _expand_building_mask_for_roads, _subtract_masks
from services.detail_layer_pipeline import _build_canonical_road_masks
from services.detail_layer_utils import MIN_LAND_WIDTH_MODEL_MM, prepare_green_areas_for_processing
from services.data_loader import fetch_city_data
from services.extras_loader import fetch_extras
from services.full_generation_pipeline import (
    _prepare_zone_stage,
    run_canonical_preview_pipeline,
    run_full_generation_pipeline,
)
from services.generation_runtime_context import prepare_generation_runtime_context
from services.generation_task import GenerationTask
from services.geometry_preclip_pipeline import prepare_preclipped_geometry
from services.global_center import GlobalCenter
from services.green_processor import process_green_areas
from services.printer_profile import get_printer_profile_for_request
from services.processing_results import SourceDataResult, ZonePreparationResult
from services.road_geometry_pipeline import prepare_road_geometry
from services.road_processor import normalize_drivable_highway_tag
from services.terrain_generator import create_terrain_mesh
from services.terrain_pipeline_utils import resolve_generation_source_crs
from services.water_layer_pipeline import _prepare_water_polygons
from services.zone_context_pipeline import build_zone_context
from services.zone_geometry_pipeline import prepare_zone_geometry

PREVIEW_CACHE_DIR = None
PREVIEW_CANONICAL_DIR = None
PREVIEW_JOBS_DIR = None
PREVIEW_OUTPUT_DIR = None
PREVIEW_WORKER_TIMEOUT_SECONDS = None
PREVIEW_MAX_ACTIVE_WORKERS = None
PREVIEW_FAILED_RETRY_DELAY_SECONDS = None
MAX_FEATURES = None
ROAD_WIDTH_MAP_M = None


def _cache_key(payload: dict[str, Any]) -> str:
    raise NotImplementedError("proprietary: removed from public showcase")


def _empty_collection() -> dict[str, Any]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _bbox_from_bounds(bounds: dict[str, float]) -> Polygon:
    raise NotImplementedError("proprietary: removed from public showcase")


def _selection_geometry(
    bounds: dict[str, float], polygon_geojson: Optional[dict[str, Any]]
) -> BaseGeometry:
    raise NotImplementedError("proprietary: removed from public showcase")


def _features_from_bbox(bounds: dict[str, float], tags: dict[str, Any]) -> gpd.GeoDataFrame:
    raise NotImplementedError("proprietary: removed from public showcase")


def _filter_by_tag(gdf: gpd.GeoDataFrame, tag: str, values: Any = True) -> gpd.GeoDataFrame:
    raise NotImplementedError("proprietary: removed from public showcase")


def _merge_frames(*frames: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    raise NotImplementedError("proprietary: removed from public showcase")


def _clip_to_selection(
    gdf: gpd.GeoDataFrame, bounds: dict[str, float], polygon_geojson: Optional[dict[str, Any]]
) -> gpd.GeoDataFrame:
    raise NotImplementedError("proprietary: removed from public showcase")


def _numeric_width(value: Any) -> Optional[float]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _road_buffer_radius_m(row: Any, road_width_multiplier: float = None) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _build_preview_road_mask(
    roads: gpd.GeoDataFrame,
    bounds: dict[str, float],
    polygon_geojson: Optional[dict[str, Any]],
    road_width_multiplier: float,
) -> gpd.GeoDataFrame:
    raise NotImplementedError("proprietary: removed from public showcase")


def _subtract_buildings_from_roads(
    roads: gpd.GeoDataFrame, buildings: gpd.GeoDataFrame
) -> gpd.GeoDataFrame:
    raise NotImplementedError("proprietary: removed from public showcase")


def _height_from_row(
    row: Any, building_min_height: float = None, building_height_multiplier: float = None
) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _feature_collection(
    gdf: gpd.GeoDataFrame,
    limit: int,
    simplify: float,
    layer: str,
    *,
    building_min_height: float = None,
    building_height_multiplier: float = None,
    scale_factor_mm_per_m: float = None,
) -> dict[str, Any]:
    raise NotImplementedError("proprietary: removed from public showcase")


class _PreviewTask:
    def update_status(self, *_args: Any, **_kwargs: Any) -> None:
        raise NotImplementedError("proprietary: removed from public showcase")


def _request_namespace(
    *,
    bounds: dict[str, float],
    road_width_multiplier: float,
    building_min_height: float,
    building_height_multiplier: float,
    model_size_mm: float,
    terrain_z_scale: float,
    terrain_resolution: int,
    terrain_base_thickness_mm: float,
    road_height_mm: float,
    road_embed_mm: float,
    building_foundation_mm: float,
    building_embed_mm: float,
    water_depth: float,
    parks_height_mm: float,
    parks_embed_mm: float,
) -> SimpleNamespace:
    raise NotImplementedError("proprietary: removed from public showcase")


def _zone_polygon_coords_from_geojson(polygon_geojson: Optional[dict[str, Any]]) -> Optional[list]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _local_to_wgs84_transformer(global_center: GlobalCenter):
    raise NotImplementedError("proprietary: removed from public showcase")


def _geometry_feature_collection(
    geometry: BaseGeometry | None,
    *,
    limit: int,
    layer: str,
    global_center: GlobalCenter,
    props: Optional[dict[str, Any]] = None,
) -> dict[str, Any]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _clip_mask_to_zone(
    geometry: BaseGeometry | None, zone_polygon: BaseGeometry | None
) -> BaseGeometry | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _canonical_building_collection(
    *,
    gdf_buildings_local: Optional[gpd.GeoDataFrame],
    building_mask: BaseGeometry | None,
    global_center: GlobalCenter,
    scale_factor_mm_per_m: float,
    height_scale_factor: float,
    limit: int,
) -> dict[str, Any]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _build_preview_canonical_masks(
    *,
    request_ns: SimpleNamespace,
    source: SourceDataResult,
    zone: ZonePreparationResult,
    global_center: GlobalCenter,
    zone_prefix: str,
) -> SimpleNamespace:
    """Build the same canonical 2D source masks as full generation, without print/export audit."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _fetch_preview_source_data(
    *, request_ns: SimpleNamespace, global_center: GlobalCenter, zone_prefix: str
) -> SourceDataResult:
    raise NotImplementedError("proprietary: removed from public showcase")


def _terrain_heightfield_layer(
    *,
    request_ns: SimpleNamespace,
    latlon_bbox: tuple[float, float, float, float],
    source: SourceDataResult,
    zone: ZonePreparationResult,
    global_center: GlobalCenter,
    building_geometries_for_flatten: Any,
    road_groove_mask: Optional[BaseGeometry],
    zone_prefix: str,
) -> dict[str, Any]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _build_canonical_preview(
    *,
    preview_id: str,
    bounds: dict[str, float],
    polygon_geojson: Optional[dict[str, Any]],
    include_terrain: bool,
    include_roads: bool,
    include_buildings: bool,
    include_water: bool,
    include_parks: bool,
    model_logic: dict[str, Any],
    request_ns: SimpleNamespace,
    started: float,
) -> dict[str, Any]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _pending_preview_response(
    *,
    preview_id: str,
    bounds: dict[str, float],
    polygon_geojson: Optional[dict[str, Any]],
    model_logic: dict[str, Any],
    status: str = None,
    message: str = None,
) -> dict[str, Any]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _read_preview_job_status(preview_id: str) -> dict[str, Any] | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _pid_is_running(pid: Any) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _active_preview_worker_count(now: float) -> int:
    raise NotImplementedError("proprietary: removed from public showcase")


def _start_preview_worker_if_needed(
    *, preview_id: str, worker_payload: dict[str, Any]
) -> dict[str, Any]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _static_file_url(path_str: str | None) -> str | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _build_full_pipeline_preview(
    *,
    preview_id: str,
    bounds: dict[str, float],
    polygon_geojson: Optional[dict[str, Any]],
    include_terrain: bool,
    include_roads: bool,
    include_buildings: bool,
    include_water: bool,
    include_parks: bool,
    model_logic: dict[str, Any],
    request_ns: SimpleNamespace,
    started: float,
) -> dict[str, Any]:
    raise NotImplementedError("proprietary: removed from public showcase")


def build_preview_cache_from_worker_payload(payload: dict[str, Any]) -> dict[str, Any]:
    raise NotImplementedError("proprietary: removed from public showcase")


def build_fast_preview(
    *,
    bounds: dict[str, float],
    polygon_geojson: Optional[dict[str, Any]] = None,
    include_terrain: bool = True,
    include_roads: bool = True,
    include_buildings: bool = True,
    include_water: bool = True,
    include_parks: bool = True,
    road_width_multiplier: float = None,
    building_min_height: float = None,
    building_height_multiplier: float = None,
    model_size_mm: float = None,
    terrain_z_scale: float = None,
    terrain_resolution: int = None,
    road_height_mm: float = None,
    road_embed_mm: float = None,
    building_foundation_mm: float = None,
    building_embed_mm: float = None,
    water_depth: float = None,
    parks_height_mm: float = None,
    parks_embed_mm: float = None,
) -> dict[str, Any]:
    raise NotImplementedError("proprietary: removed from public showcase")
