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
from services.detail_layer_utils import (
    MICRO_REGION_THRESHOLD_MM,
    MIN_ROAD_WIDTH_MODEL_MM,
    filter_mesh_components_by_printability,
    model_mm_to_world_m,
)


@dataclass
class ValidatorConfig:
    scale_factor: float
    min_feature_mm: float = None
    min_wall_mm: float = None
    fill_holes: bool = None
    repair_normals: bool = None


def _footprint_extents(mesh: trimesh.Trimesh) -> tuple[float, float]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _reject_thin_walled_components(
    mesh: Optional[trimesh.Trimesh], *, min_wall_m: float, min_feature_m: float, label: str
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _repair_mesh(
    mesh: Optional[trimesh.Trimesh], *, fill_holes: bool, repair_normals: bool, label: str
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def validate_mesh(
    mesh: Optional[trimesh.Trimesh], *, config: ValidatorConfig, label: str = None
) -> Optional[trimesh.Trimesh]:
    """Slicer-style validation: drop unprintable components, repair, fill holes."""
    raise NotImplementedError("proprietary: removed from public showcase")


def validate_road_mesh(
    mesh: Optional[trimesh.Trimesh], *, scale_factor: float
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def validate_building_mesh(
    mesh: Optional[trimesh.Trimesh], *, scale_factor: float
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")
