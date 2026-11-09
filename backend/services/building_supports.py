# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
import os
import shutil
import subprocess
import uuid
from typing import Iterable, List, Optional
import trimesh
from shapely.geometry import MultiPolygon, Polygon
from shapely.geometry.base import BaseGeometry
from services.building_processor import BuildingMeshRecord
from services.detail_layer_utils import MICRO_REGION_THRESHOLD_MM, model_mm_to_world_m


def _polygon_min_dimension(poly: Polygon) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _normalize_support_footprint(
    footprint: Optional[BaseGeometry],
    *,
    inset_m: float = None,
    simplify_m: float = None,
    exclusion_geom: Optional[BaseGeometry] = None,
    min_feature_m: float = None,
) -> list[Polygon]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _cleanup_support_mesh(
    mesh: Optional[trimesh.Trimesh], *, min_feature_m: float = None
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def build_building_supports(
    building_records: Iterable[BuildingMeshRecord] | None,
    *,
    support_bottom_z: float | None,
    top_overlap_m: float = None,
    footprint_inset_m: float = None,
    exclusion_polygons: Optional[BaseGeometry] = None,
    min_feature_m: float = None,
) -> List[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def merge_building_and_support_meshes(
    building_meshes: Iterable[trimesh.Trimesh] | None,
    support_meshes: Iterable[trimesh.Trimesh] | None,
) -> List[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _find_blender() -> Optional[str]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _run_blender_union(meshes: list[trimesh.Trimesh], *, label: str) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def union_building_layer_meshes(
    building_meshes: Iterable[trimesh.Trimesh] | None,
    support_meshes: Iterable[trimesh.Trimesh] | None,
    *,
    label: str = None,
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def union_mesh_collection(
    meshes: Iterable[trimesh.Trimesh] | None, *, label: str = None
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def concatenate_meshes(meshes: Iterable[trimesh.Trimesh] | None) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")
