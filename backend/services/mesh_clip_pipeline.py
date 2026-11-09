# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional
import trimesh
from services.mesh_clipper import clip_mesh_to_bbox, clip_mesh_to_polygon


@dataclass
class MeshClipPipelineResult:
    terrain_mesh: Optional[trimesh.Trimesh]
    road_mesh: Optional[trimesh.Trimesh]
    building_meshes: Any
    water_mesh: Optional[trimesh.Trimesh]
    parks_mesh: Optional[trimesh.Trimesh]


def clip_generated_meshes(
    *,
    terrain_mesh: Optional[trimesh.Trimesh],
    road_mesh: Optional[trimesh.Trimesh],
    building_meshes: Any,
    water_mesh: Optional[trimesh.Trimesh],
    parks_mesh: Optional[trimesh.Trimesh],
    bbox_meters: Any,
    zone_polygon_coords: Any,
    global_center: Any,
    preclipped_to_zone: bool,
    clip_tolerance: float = None,
) -> MeshClipPipelineResult:
    raise NotImplementedError("proprietary: removed from public showcase")
