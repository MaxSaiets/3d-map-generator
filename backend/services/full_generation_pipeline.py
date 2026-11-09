# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
import gc
import json
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional
import trimesh
from shapely.geometry import box
from services.canonical_2d_pipeline import prepare_canonical_2d_stage
from services.bridge_water_pipeline import prepare_bridge_water_geometries
from services.building_supports import union_mesh_collection
from services.canonical_mask_bundle import load_canonical_mask_bundle
from services.data_fetch_pipeline import fetch_generation_data
from services import overpass_health
from services.debug_bundle_pipeline import create_debug_bundle
from services.detail_layer_pipeline import process_detail_layers
from services.export_pipeline import export_generation_outputs
from services.flat_plate_pipeline import run_flat_plate_pipeline
from services.detail_layer_utils import MICRO_REGION_THRESHOLD_MM
from services.firebase_publish_pipeline import publish_outputs_to_firebase
from services.mesh_clip_pipeline import clip_generated_meshes
from services.mesh_postprocess_pipeline import postprocess_generated_meshes
from services.processing_results import SourceDataResult, TerrainStageResult, ZonePreparationResult
from services.road_groove_validation import print_road_groove_validation_report
from services.runtime_canonical_masks import build_runtime_canonical_bundle
from services.terrain_only_pipeline import TerrainOnlyPipelineResult, run_terrain_only_pipeline
from services.zone_context_pipeline import build_zone_context
from services.zone_geometry_pipeline import prepare_zone_geometry
from services.building_geometry_pipeline import prepare_building_geometry
from services.generation_pipeline import process_generation_stage
from services.geometry_preclip_pipeline import prepare_preclipped_geometry
from services.inlay_fit import InlayFitConfig
from services.print_acceptance import (
    summarize_export_print_failures,
    write_export_print_acceptance_report,
)
from services.printer_profile import get_printer_profile_for_request
from services.road_geometry_pipeline import prepare_road_geometry
from services.terrain_pipeline_utils import compute_water_depth_m, resolve_generation_source_crs
from services.terrain_building_merge_pipeline import merge_terrain_and_buildings
from services.stage_snapshot_pipeline import create_stage_snapshot_collector
from services.model_exporter import (
    _filter_mesh_components_for_export,
    _normalize_part_for_print_export,
    repair_base_export_mesh_aggressive,
    repair_road_export_mesh,
    export_stl_safe,
)


@dataclass
class FullGenerationPipelineResult:
    output_file_abs: Path
    primary_format: str
    terrain_only_result: Optional[TerrainOnlyPipelineResult] = None


def _geometry_area(geom: Any) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _symdiff_area(lhs: Any, rhs: Any) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _validate_canonical_mask_handoff(
    *, canonical_mask_bundle: Any, terrain_stage: Any, detail_layers: Any, zone_prefix: str
) -> None:
    """Hard-check that 3D stages consume canonical 2D masks without drift."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _is_printable_water_export_mesh(mesh: Any, *, min_face_count: int = None) -> bool:
    """Validate a water mesh would survive slicing."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _repair_print_part_file(*, part_name: str, path: Path, report: dict[str, Any]) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _attempt_print_recovery(
    *,
    task_id: str,
    output_dir: Path,
    task: Any,
    parts_for_print: dict[str, str],
    expected_parts: dict[str, bool],
    printer_profile: Any,
    initial_report: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, str], dict[str, bool]]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _collect_print_part_paths(task: Any, export_result: Any) -> dict[str, str]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _compute_stl_extra_embed(scale_factor: Optional[float], export_format: str) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _validate_groove_stage(*, detail_layers: Any, task: Any, zone_prefix: str) -> None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _validate_groove_result(*, detail_layers: Any, task: Any, zone_prefix: str) -> None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _prepare_zone_stage(
    *,
    request: Any,
    global_center: Any,
    zone_polygon_coords: Optional[list],
    grid_bbox_latlon: Any,
    zone_row: Any,
    zone_col: Any,
    hex_size_m: Any,
    zone_prefix: str,
) -> ZonePreparationResult:
    raise NotImplementedError("proprietary: removed from public showcase")


def _fetch_source_stage(
    *, task: Any, request: Any, global_center: Any, zone_prefix: str
) -> SourceDataResult:
    raise NotImplementedError("proprietary: removed from public showcase")


def _validate_source_stage(
    *, source: SourceDataResult, zone_prefix: str, request: Any = None
) -> None:
    raise NotImplementedError("proprietary: removed from public showcase")


def cut_relief_connector_notch(terrain_mesh, *, zone, request, sf_c, zone_prefix=None):
    """Ріже конектор-паз (ластівчин хвіст) у ДНІ рельєф-мешу + повертає ключ-метелик.
    ВИКЛИКАТИ на ГЕРМЕТИЧНОМУ (ДО-грувовому) рельєфі → manifold ріже чисто (drift≈0).
    Паз — у дні, груви — на версі → не конфліктують. Раніше різали ПІСЛЯ грувів на
    негерметичному мешеві → boolean руйнував/відкидав («рельєф: нема зʼєднання»).
    Повертає (terrain_mesh, connector_key_mesh, carved)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _run_terrain_stage(
    *,
    task: Any,
    request: Any,
    latlon_bbox: Any,
    global_center: Any,
    zone_prefix: str,
    zone: ZonePreparationResult,
    source: SourceDataResult,
    min_printable_gap_mm: float,
    groove_clearance_mm: float,
    canonical_mask_bundle: Any = None,
) -> TerrainStageResult:
    raise NotImplementedError("proprietary: removed from public showcase")


def _flush_raised_content_at_tile_edge(
    meshes,
    *,
    terrain_provider,
    zone_polygon_local,
    scale_factor,
    edge_mm: float = None,
    zone_prefix: str = None,
):
    """СЕРІЯ: підняте покриття (дороги/вода/парки) сидить на ~0.6–1.3мм ВИЩЕ рельєфу.
    Коли його ріже по краю плитки — торець зрізу стирчить угору над рельєфом = «стінки/
    зубці» на шві (річка — найгірша). Тут ОПУСКАЄМО верх контенту до поверхні рельєфу
    у тонкому кільці (~edge_mm) біля межі зони: контент ДОХОДИТЬ до краю, але ВРІВЕНЬ
    (без торців-стінок). Внутрішня (піднята) частина не чіпається. Не критичн"""
    raise NotImplementedError("proprietary: removed from public showcase")


def run_full_generation_pipeline(
    *,
    task: Any,
    request: Any,
    task_id: str,
    output_dir: Path,
    global_center: Any,
    latlon_bbox: Any,
    zone_polygon_coords: Optional[list],
    grid_bbox_latlon: Any,
    zone_row: Any,
    zone_col: Any,
    hex_size_m: Any,
    zone_prefix: str = None,
    min_printable_gap_mm: float = None,
    groove_clearance_mm: float = None,
    file_basename: Optional[str] = None,
) -> FullGenerationPipelineResult:
    raise NotImplementedError("proprietary: removed from public showcase")
