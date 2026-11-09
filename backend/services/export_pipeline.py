# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from dataclasses import dataclass
import json
import os
from pathlib import Path
import shutil
import subprocess
from typing import Any, Dict, Optional, Tuple, List
import zipfile
import numpy as np
import trimesh
from services.model_exporter import export_preview_parts_3mf, export_scene


@dataclass
class ExportPipelineResult:
    output_file_abs: Path
    primary_format: str
    stl_preview_abs: Optional[Path]
    parts_from_main: Optional[Dict[str, str]]


def _find_prusaslicer_console() -> Optional[Path]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _prepare_print_layout_inputs(
    *, output_dir: Path, task_id: str, parts_from_main: Optional[Dict[str, str]]
) -> List[str]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _create_print_layout_3mf_with_prusaslicer(
    *, output_dir: Path, task_id: str, parts_from_main: Optional[Dict[str, str]]
) -> Optional[Path]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _create_print_package(
    *,
    output_dir: Path,
    task_id: str,
    primary_format: str,
    output_file_abs: Path,
    stl_preview_abs: Optional[Path],
    parts_from_main: Optional[Dict[str, str]],
) -> Optional[Path]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _create_print_layout_3mf(
    *, output_dir: Path, task_id: str, parts_from_main: Optional[Dict[str, str]]
) -> Optional[Path]:
    raise NotImplementedError("proprietary: removed from public showcase")


def export_generation_outputs(
    *,
    task: Any,
    request: Any,
    task_id: str,
    output_dir: Path,
    terrain_mesh: Optional[trimesh.Trimesh],
    road_mesh: Optional[trimesh.Trimesh],
    building_meshes: Any,
    water_mesh: Optional[trimesh.Trimesh],
    parks_mesh: Optional[trimesh.Trimesh],
    reference_xy_m: Optional[float],
    preserve_z: bool = False,
    preserve_xy: bool = False,
    include_preview_parts: bool = True,
    include_parallel_stl: bool = True,
    include_print_package: bool = True,
    completion_message: str = None,
    file_basename: Optional[str] = None,
    extra_mesh_items: Optional[list[Tuple[str, trimesh.Trimesh]]] = None,
    repair_meshes: bool = True,
    merge_buildings_into_base: bool = False,
) -> ExportPipelineResult:
    raise NotImplementedError("proprietary: removed from public showcase")
