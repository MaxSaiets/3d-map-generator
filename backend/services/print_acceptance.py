# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
import json
import subprocess
from pathlib import Path
from typing import Any, Mapping, Optional
import trimesh
from shapely.geometry import Polygon, shape
from shapely.geometry.base import BaseGeometry
from shapely.ops import unary_union
from shapely.prepared import prep
from services.printer_profile import PrinterProfile


def _load_geojson_geometry(path: Path | None) -> BaseGeometry | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _iter_polygons(geometry: BaseGeometry | None) -> list[Polygon]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _polygon_equivalent_width(poly: Polygon) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _survives_printable_erosion(geometry: BaseGeometry | None, *, min_feature_m: float) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _component_stats(geometry: BaseGeometry | None, *, min_feature_m: float) -> dict[str, Any]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _orphan_hole_count(geometry: BaseGeometry | None, *, backing_mask: BaseGeometry | None) -> int:
    raise NotImplementedError("proprietary: removed from public showcase")


def _overlap_area(lhs: BaseGeometry | None, rhs: BaseGeometry | None) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _resolve_world_threshold_m(
    bundle_dir: Path, min_feature_mm: float, *, scale_factor_override: float | None = None
) -> tuple[float, float | None]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _overlap_failure_threshold_m2(scale_factor: float | None) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def build_mask_printability_report(
    bundle_dir: Path,
    *,
    min_feature_mm: float,
    scale_factor_override: float | None = None,
    check_road_holes: bool = True,
    check_layer_overlaps: bool = True,
) -> dict[str, Any]:
    raise NotImplementedError("proprietary: removed from public showcase")


def write_mask_printability_report(
    bundle_dir: Path,
    *,
    printer_profile: PrinterProfile,
    scale_factor_override: float | None = None,
    check_road_holes: bool = True,
    check_layer_overlaps: bool = True,
    report: Mapping[str, Any] | None = None,
) -> Path:
    raise NotImplementedError("proprietary: removed from public showcase")


def summarize_mask_printability_failures(report: Mapping[str, Any]) -> str:
    raise NotImplementedError("proprietary: removed from public showcase")


def find_prusaslicer_cli() -> Path | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _write_slicer_config(
    path: Path, *, printer_profile: PrinterProfile, support_material: bool = False
) -> Path:
    raise NotImplementedError("proprietary: removed from public showcase")


def _boundary_edge_count(mesh: trimesh.Trimesh) -> int:
    raise NotImplementedError("proprietary: removed from public showcase")


def _mesh_part_report(
    mesh_path: Path, *, part_name: str, printer_profile: PrinterProfile
) -> dict[str, Any]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _run_slicer_slice(
    slicer: Path,
    config_path: Path,
    input_path: Path,
    output_path: Path,
    *,
    rotate_x_deg: int = None,
) -> dict[str, Any]:
    raise NotImplementedError("proprietary: removed from public showcase")


def write_export_print_acceptance_report(
    *,
    task_id: str,
    output_dir: Path,
    parts_for_print: Mapping[str, str] | None,
    expected_parts: Mapping[str, bool] | None = None,
    printer_profile: PrinterProfile,
    require_slicer_validation: bool = True,
    fail_on_slicer_warnings: bool = True,
    rotate_x_deg: int = None,
) -> Path:
    raise NotImplementedError("proprietary: removed from public showcase")


def summarize_export_print_failures(report: Mapping[str, Any]) -> str:
    raise NotImplementedError("proprietary: removed from public showcase")
