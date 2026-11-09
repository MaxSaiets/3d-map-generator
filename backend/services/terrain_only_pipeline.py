# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional
import trimesh
from services.export_pipeline import ExportPipelineResult, export_generation_outputs
from services.terrain_pipeline_utils import (
    compute_water_depth_m,
    compute_water_surface_thickness_m,
    resolve_generation_source_crs,
)
from services.terrain_generator import create_terrain_mesh
from services.water_processor import process_water_surface


@dataclass
class TerrainOnlyPipelineResult:
    terrain_mesh: Optional[trimesh.Trimesh]
    terrain_provider: Any
    water_mesh: Optional[trimesh.Trimesh]
    export_result: ExportPipelineResult


def run_terrain_only_pipeline(
    *,
    task: Any,
    request: Any,
    task_id: str,
    output_dir: Path,
    bbox_meters: Any,
    latlon_bbox: Any,
    scale_factor: Optional[float],
    gdf_buildings: Any,
    G_roads: Any,
    gdf_water: Any,
    global_center: Any,
    reference_xy_m: Optional[float],
) -> TerrainOnlyPipelineResult:
    raise NotImplementedError("proprietary: removed from public showcase")
