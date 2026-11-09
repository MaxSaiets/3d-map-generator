# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional
import trimesh
from services.detail_layer_utils import (
    MICRO_REGION_THRESHOLD_MM,
    MIN_ROAD_WIDTH_MODEL_MM,
    MIN_LAND_WIDTH_MODEL_MM,
    filter_mesh_components_by_printability,
)
from services.mesh_quality import improve_mesh_for_3d_printing, validate_mesh_for_3d_printing


@dataclass
class MeshPostprocessResult:
    terrain_mesh: Optional[trimesh.Trimesh]
    road_mesh: Optional[trimesh.Trimesh]
    building_meshes: Any
    water_mesh: Optional[trimesh.Trimesh]
    parks_mesh: Optional[trimesh.Trimesh]


def _remove_tiny_detached_faces(
    mesh: Optional[trimesh.Trimesh], *, label: str, max_faces: int = None, max_vertices: int = None
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _sanitize_mesh_topology_no_drift(
    mesh: Optional[trimesh.Trimesh], *, label: str
) -> Optional[trimesh.Trimesh]:
    """Remove degenerate/duplicate topology without moving vertices."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _keep_dominant_component_if_fragmented(
    mesh: Optional[trimesh.Trimesh],
    *,
    label: str,
    min_dominant_face_ratio: float = None,
    min_fragment_count: int = None,
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def postprocess_generated_meshes(
    *,
    task: Any,
    request: Any,
    scale_factor: Optional[float],
    terrain_mesh: Optional[trimesh.Trimesh],
    road_mesh: Optional[trimesh.Trimesh],
    building_meshes: Any,
    water_mesh: Optional[trimesh.Trimesh],
    parks_mesh: Optional[trimesh.Trimesh],
) -> MeshPostprocessResult:
    raise NotImplementedError("proprietary: removed from public showcase")
