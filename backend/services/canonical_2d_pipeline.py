# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional
from shapely.geometry import MultiPolygon, Polygon
from shapely.ops import unary_union
from services.building_geometry_pipeline import prepare_building_geometry
from services.canonical_mask_bundle import CanonicalMaskBundle, load_canonical_mask_bundle
from services.detail_layer_pipeline import _build_canonical_road_masks
from services.detail_layer_utils import (
    MICRO_REGION_THRESHOLD_MM,
    MIN_LAND_WIDTH_MODEL_MM,
    model_mm_to_world_m,
    prepare_green_areas_for_processing,
)
from services.green_processor import process_green_areas
from services.geometry_preclip_pipeline import prepare_preclipped_geometry
from services.groove_pipeline import _prepare_parks_groove_mask
from services.print_acceptance import (
    build_mask_printability_report,
    summarize_mask_printability_failures,
    write_mask_printability_report,
)
from services.printer_profile import PrinterProfile, get_printer_profile_for_request
from services.road_geometry_pipeline import RoadGeometryPreparationResult, prepare_road_geometry
from services.runtime_canonical_masks import build_runtime_canonical_bundle
from services.water_layer_pipeline import _prepare_water_polygons


@dataclass
class Canonical2DStageResult:
    canonical_mask_bundle: CanonicalMaskBundle
    printer_profile: PrinterProfile
    printability_report: dict[str, Any]
    source_bundle_dir: Path
    bundle_origin: str
    road_geometry: Optional[RoadGeometryPreparationResult] = None
    building_geometry: Any = None
    preclip_result: Any = None


def _has_blocking_mask_failures(report: dict[str, Any] | None) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _is_road_only_debt(report: dict[str, Any] | None) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _fill_orphan_holes(geometry: Any, *, backing_mask: Any) -> Any:
    raise NotImplementedError("proprietary: removed from public showcase")


def _fill_small_enclosed_holes(geometry: Any, *, max_hole_area_m2: float) -> Any:
    """Fill tiny fully-enclosed interior holes (road-surrounded terrain pads, the
    "white diamonds" at junctions) below max_hole_area_m2 — merge them into the
    mask. A hole is enclosed by the mask by definition, so this NEVER absorbs
    edge terrain or large courtyards (those exceed the cap or are not holes).
    Topology-only: keeps the exterior + the large holes, drops the small ones."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _smooth_sharp_corners(
    geometry: Any, *, scale_factor: Optional[float], radius_mm: float = None
) -> Any:
    """Round convex and concave corners sharper than the printer can resolve."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _collapse_acute_corners(
    geometry: Any, *, scale_factor: Optional[float], collapse_mm: float
) -> Any:
    """Erode+dilate (morphological opening) to drop acute spikes and necks."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _prune_tiny_fragments(
    geometry: Any,
    *,
    scale_factor: Optional[float],
    min_feature_mm: float = MICRO_REGION_THRESHOLD_MM,
    min_area_mm2: float = None,
) -> Any:
    """Drop tiny islands that survived boolean ops but won't print cleanly."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _subtract_masks(geometry: Any, *masks: Any) -> Any:
    raise NotImplementedError("proprietary: removed from public showcase")


def _expand_building_mask_for_roads(
    buildings: Any, *, scale_factor: float | None, clearance_mm: float
) -> Any:
    raise NotImplementedError("proprietary: removed from public showcase")


def _audit_bundle_or_none(
    bundle_dir: Path, *, printer_profile: PrinterProfile
) -> dict[str, Any] | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _bundle_matches_zone(*, bundle: CanonicalMaskBundle, zone_polygon_local: Any) -> bool:
    """Return True only if external canonical bundle belongs to current zone."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _attempt_runtime_overlap_self_heal(
    *,
    task_id: str,
    debug_generated_dir: Path,
    zone_polygon_local: Any,
    scale_factor: float | None,
    groove_side_clearance_mm: float,
    runtime_bundle: CanonicalMaskBundle,
    failing_overlaps: list[str],
    zone_prefix: str = None,
) -> CanonicalMaskBundle | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _attempt_drop_water_overlap_fallback(
    *,
    task_id: str,
    debug_generated_dir: Path,
    zone_polygon_local: Any,
    scale_factor: float | None,
    groove_side_clearance_mm: float,
    runtime_bundle: CanonicalMaskBundle,
    zone_prefix: str = None,
) -> CanonicalMaskBundle | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _attempt_runtime_road_hole_self_heal(
    *,
    task_id: str,
    debug_generated_dir: Path,
    zone_polygon_local: Any,
    scale_factor: float | None,
    groove_side_clearance_mm: float,
    runtime_bundle: CanonicalMaskBundle,
    zone_prefix: str = None,
) -> CanonicalMaskBundle | None:
    """Patch orphan holes in road masks and rebuild runtime bundle once."""
    raise NotImplementedError("proprietary: removed from public showcase")


def prepare_canonical_2d_stage(
    *,
    task_id: str,
    request: Any,
    source: Any,
    zone: Any,
    global_center: Any,
    debug_generated_dir: Path,
    zone_prefix: str = None,
) -> Canonical2DStageResult:
    raise NotImplementedError("proprietary: removed from public showcase")
