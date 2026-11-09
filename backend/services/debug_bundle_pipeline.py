# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Optional
from shapely.geometry import mapping
from shapely.ops import unary_union
from services.debug_renderers import render_geometry_png, render_mesh_top_png, render_overlay_png
from services.canonical_mask_bundle import CanonicalMaskBundle
from services.detail_layer_utils import prepare_green_areas_for_processing
from services.geometry_diagnostics import (
    concatenate_meshes,
    ensure_valid_geometry,
    geometry_stats,
    mesh_stats,
    overlap_report,
)


def _backend_root() -> Path:
    raise NotImplementedError("proprietary: removed from public showcase")


def _debug_run_root(task_id: str) -> Path:
    raise NotImplementedError("proprietary: removed from public showcase")


def _collect_gdf_geometry(gdf: Any) -> Any:
    raise NotImplementedError("proprietary: removed from public showcase")


def _write_geojson(path: Path, geometry: Any) -> Optional[Path]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _export_mesh(path: Path, mesh: Any) -> Optional[Path]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _safe_rel(path: Optional[Path], root: Path) -> Optional[str]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _safe_render(fn, *args, **kwargs) -> Optional[Path]:
    raise NotImplementedError("proprietary: removed from public showcase")


def create_debug_bundle(
    *,
    task_id: str,
    request: Any,
    output_dir: Path,
    zone: Any,
    source: Any,
    terrain_stage: Any,
    detail_layers: Any,
    postprocess_result: Any,
    clip_result: Any,
    merge_result: Any,
    export_result: Any,
    global_center: Any,
    canonical_mask_bundle: Optional[CanonicalMaskBundle] = None,
) -> Optional[Path]:
    raise NotImplementedError("proprietary: removed from public showcase")
