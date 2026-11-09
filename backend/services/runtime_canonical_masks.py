# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
import json
import os
from pathlib import Path
from typing import Optional
from shapely.geometry import Polygon, box, mapping
from shapely.geometry.base import BaseGeometry
from shapely.ops import unary_union
from services.canonical_mask_bundle import (
    CanonicalMaskBundle,
    _normalize_loaded_geometry,
    load_canonical_mask_bundle,
)
from services.detail_layer_utils import MIN_LAND_WIDTH_MODEL_MM

CANONICAL_PARTITION_MIN_FEATURE_MM = None
CANONICAL_AREA_CLUSTER_MERGE_MM = None
CANONICAL_PARK_ISOLATED_DETAIL_MIN_AREA_MM2 = None
CANONICAL_WATER_ISOLATED_DETAIL_MIN_AREA_MM2 = None
CANONICAL_ROAD_MIN_PART_AREA_MM2 = None
CANONICAL_TERRAIN_SLIVER_MAX_AREA_MM2 = None
CANONICAL_TERRAIN_SLIVER_MAX_WIDTH_MM = None
CANONICAL_ROAD_CORNER_ROUND_MM = None
CANONICAL_ROAD_CORNER_CLOSE_MM = None
CANONICAL_ROAD_CORNER_MAX_AREA_CHANGE_RATIO = None


def _iter_polygons(geometry: BaseGeometry | None) -> list[Polygon]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _polygon_equivalent_width(poly: Polygon) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _land_min_feature_m(scale_factor: float | None) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _model_mm_to_world_m(model_mm: float, scale_factor: float | None) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _clip_to_zone(
    geometry: BaseGeometry | None, zone_geometry: BaseGeometry | None
) -> BaseGeometry | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _drop_outlier_components(
    geometry: BaseGeometry | None, *, min_ratio_to_largest: float = None
) -> BaseGeometry | None:
    """Drop components whose area is a fraction of the largest component."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _drop_isolated_area_details(
    geometry: BaseGeometry | None, *, scale_factor: float | None, min_area_mm2: float
) -> BaseGeometry | None:
    """Remove printable but visually noisy isolated green/water specks."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _drop_small_road_components(
    geometry: BaseGeometry | None,
    *,
    min_feature_m: float,
    min_area_factor: float = None,
    min_ratio_to_largest: float = None,
) -> BaseGeometry | None:
    """Drop isolated road specks that are technically printable but meaningless."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _component_count(geometry: BaseGeometry | None) -> int:
    raise NotImplementedError("proprietary: removed from public showcase")


def _round_road_corners_for_print(
    geometry: BaseGeometry | None,
    *,
    scale_factor: float | None,
    radius_mm: float = CANONICAL_ROAD_CORNER_ROUND_MM,
    close_radius_mm: float = CANONICAL_ROAD_CORNER_CLOSE_MM,
    max_area_change_ratio: float = CANONICAL_ROAD_CORNER_MAX_AREA_CHANGE_RATIO,
) -> BaseGeometry | None:
    """Round acute road tips without running broad road gap-fill."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _apply_mask_difference(
    geometry: BaseGeometry | None, exclusion: BaseGeometry | None
) -> BaseGeometry | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _bounds_overlap(
    a: BaseGeometry | None, b: BaseGeometry | None, *, padding_m: float = None
) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _clip_conflict_to_building_window(
    conflict: BaseGeometry | None, building: BaseGeometry | None, *, padding_m: float
) -> BaseGeometry | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _polygon_min_dimension(poly: Polygon | None) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _overlap_spans_building(
    building: Polygon | None,
    overlap: BaseGeometry | None,
    *,
    span_ratio: float = None,
    min_area_ratio: float = None,
) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _build_road_groove_from_insert(
    roads_geom: BaseGeometry | None, *, groove_clearance_m: float, zone_geom: BaseGeometry | None
) -> BaseGeometry | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _semantic_support_length(
    roads_semantic_geom: BaseGeometry | None, region: BaseGeometry | None
) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _semantic_centerline_crosses_building(
    building: Polygon | None,
    roads_semantic_geom: BaseGeometry | None,
    *,
    groove_clearance_m: float,
    span_ratio: float = None,
    min_length_ratio: float = None,
) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _road_overlap_reaches_building_core(
    building: Polygon | None,
    overlap: BaseGeometry | None,
    *,
    groove_clearance_m: float,
    large_building_min_dim_m: float = None,
    core_margin_ratio: float = None,
    min_core_margin_m: float = None,
    max_core_margin_ratio: float = None,
) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _build_large_building_edge_clip_exclusion(
    *,
    building: Polygon | None,
    conflict: BaseGeometry | None,
    roads_geom: BaseGeometry | None,
    groove_clearance_m: float,
    large_building_min_dim_m: float = None,
    edge_depth_factor: float = None,
    min_edge_depth_m: float = None,
    max_edge_depth_ratio: float = None,
) -> BaseGeometry | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _buffer_building_for_road_cut(
    building: Polygon | None, *, groove_clearance_m: float
) -> BaseGeometry | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _build_local_road_cut_geometry(
    *, building: Polygon | None, road_overlap: BaseGeometry | None, groove_clearance_m: float
) -> BaseGeometry | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _road_cut_creates_subprintable_corridor(
    *,
    roads_geom: BaseGeometry | None,
    cut_geom: BaseGeometry | None,
    building: Polygon | None,
    min_feature_m: float,
    groove_clearance_m: float,
    loss_ratio_threshold: float = None,
) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _resolve_building_road_conflicts(
    *,
    roads_geom: BaseGeometry | None,
    buildings_geom: BaseGeometry | None,
    roads_semantic_geom: BaseGeometry | None,
    scale_factor: float | None,
    groove_clearance_m: float,
    zone_geom: BaseGeometry | None,
) -> tuple[BaseGeometry | None, BaseGeometry | None, BaseGeometry | None]:
    """Resolve building-vs-road conflicts before final canonical bundle freeze."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _filter_tiny_polygon_parts(
    geometry: BaseGeometry | None, *, min_feature_m: float
) -> BaseGeometry | None:
    """Drop polygons that fail the printability test used by the audit."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _fill_tiny_holes(geometry: BaseGeometry | None, *, min_feature_m: float) -> BaseGeometry | None:
    """Fill any interior ring that the audit would flag as an unprintable hole."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _survives_printable_erosion(geometry: BaseGeometry | None, *, min_feature_m: float) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _fill_unprintable_holes(
    geometry: BaseGeometry | None, *, min_feature_m: float, max_area_factor: float | None = None
) -> BaseGeometry | None:
    """Fill only conservative, audit-failing holes."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _fill_orphan_holes(
    geometry: BaseGeometry | None, *, backing_mask: BaseGeometry | None
) -> BaseGeometry | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _enforce_min_width(
    geometry: BaseGeometry | None, *, min_feature_m: float
) -> BaseGeometry | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _write_geojson(path: Path, geometry: BaseGeometry | None) -> Path:
    raise NotImplementedError("proprietary: removed from public showcase")


def _prepare_water_groove_mask(
    water_insert_mask: BaseGeometry | None,
    *,
    road_groove_mask: BaseGeometry | None,
    parks_groove_mask: BaseGeometry | None,
    building_polygons: BaseGeometry | None,
    groove_clearance_m: float,
) -> BaseGeometry | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _build_inlay_groove_from_insert(
    insert_mask: BaseGeometry | None,
    *,
    groove_clearance_m: float,
    zone_geom: BaseGeometry | None,
    hard_exclusions: list[BaseGeometry | None] | None = None,
) -> BaseGeometry | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _building_fit_exclusion_for_insert(
    *,
    buildings_geom: BaseGeometry | None,
    insert_geom: BaseGeometry | None,
    groove_clearance_m: float,
    min_overlap_ratio: float = None,
) -> BaseGeometry | None:
    """Expand only buildings that are actually embedded in an insert mask."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _close_unprintable_bays(
    geometry: BaseGeometry | None, *, min_feature_m: float
) -> BaseGeometry | None:
    """Fill concave bays/necks narrower than the printable floor."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _sanitize_nonroad_insert(
    geometry: BaseGeometry | None, *, min_feature_m: float, close_bays: bool = True
) -> BaseGeometry | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _fill_unbacked_insert_holes(
    geometry: BaseGeometry | None,
    *,
    backing_masks: list[BaseGeometry | None],
    min_overlap_ratio: float = None,
) -> BaseGeometry | None:
    """Fill insert holes that are not occupied by another final layer."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _is_unprintable_remainder(poly: Polygon | None, *, min_feature_m: float) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _is_visual_sliver_remainder(
    poly: Polygon | None, *, min_feature_m: float, scale_factor: float | None
) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _absorb_unprintable_remainders_into_inlays(
    *,
    zone_geom: BaseGeometry | None,
    roads_geom: BaseGeometry | None,
    road_groove_geom: BaseGeometry | None,
    parks_geom: BaseGeometry | None,
    water_geom: BaseGeometry | None,
    buildings_geom: BaseGeometry | None,
    min_feature_m: float,
    scale_factor: float | None = None,
) -> tuple[BaseGeometry | None, BaseGeometry | None]:
    """Assign tiny leftover terrain scraps to nearby park/water inlays."""
    raise NotImplementedError("proprietary: removed from public showcase")


def build_runtime_canonical_bundle(
    *,
    task_id: str,
    debug_generated_dir: Path,
    zone_polygon: BaseGeometry | None,
    roads_final: BaseGeometry | None,
    road_groove_mask: BaseGeometry | None,
    parks_final: BaseGeometry | None,
    parks_groove_mask: BaseGeometry | None,
    water_final: BaseGeometry | None,
    water_groove_mask: BaseGeometry | None,
    buildings_footprints: BaseGeometry | None,
    scale_factor: Optional[float],
    roads_semantic_preview: BaseGeometry | None = None,
    groove_clearance_mm: float = None,
) -> CanonicalMaskBundle:
    raise NotImplementedError("proprietary: removed from public showcase")
