# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
import os
from typing import Any, Callable, Optional
import trimesh
from services.building_supports import union_mesh_collection
from services.processing_results import TerrainBuildingMergeResult
from services.terrain_cutter import extend_buildings_mesh_to_uniform_bottom


def _component_count(mesh: Optional[trimesh.Trimesh]) -> int:
    raise NotImplementedError("proprietary: removed from public showcase")


def merge_terrain_and_buildings(
    *,
    terrain_mesh: Optional[trimesh.Trimesh],
    building_meshes: Any,
    merged_building_mesh: Optional[trimesh.Trimesh] = None,
    merged_building_mesh_factory: Optional[Callable[[], Optional[trimesh.Trimesh]]] = None,
    support_meshes: Any = None,
    bottom_clearance_m: float = None,
) -> TerrainBuildingMergeResult:
    raise NotImplementedError("proprietary: removed from public showcase")
