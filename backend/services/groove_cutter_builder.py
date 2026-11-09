# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import numpy as np
import trimesh
from shapely.geometry.base import BaseGeometry
from shapely.ops import unary_union

MIN_POCKET_FLOOR_MM = None


@dataclass
class UnifiedGrooveCutterBuildResult:
    cutter_mesh: Optional[trimesh.Trimesh]
    cut_bottom_z: Optional[float]
    cut_top_z: Optional[float]


def build_unified_groove_cutter(
    *,
    terrain_mesh: trimesh.Trimesh,
    road_polygons: Optional[BaseGeometry] = None,
    road_clearance_m: float = None,
    parks_polygons: Optional[BaseGeometry] = None,
    parks_clearance_m: float = None,
    parks_mesh: Optional[trimesh.Trimesh] = None,
    water_polygons: Optional[BaseGeometry] = None,
    water_clearance_m: float = None,
    water_mesh: Optional[trimesh.Trimesh] = None,
    road_mesh: Optional[trimesh.Trimesh] = None,
    groove_depth_m: Optional[float] = None,
    scale_factor: Optional[float] = None,
) -> UnifiedGrooveCutterBuildResult:
    raise NotImplementedError("proprietary: removed from public showcase")
