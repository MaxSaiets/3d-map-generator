# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Terrain Cutter — вирізання пазів (grooves) у рельєфі для вставки мешів (дороги, парки, вода)."""

import time
import trimesh
import shutil
import numpy as np
import os
import uuid
import subprocess
from typing import Optional, Tuple, List
from shapely.geometry.base import BaseGeometry
from shapely.geometry import MultiPoint, Polygon as ShapelyPolygon
from shapely.ops import unary_union


def manifold_repair_subtract(terrain_mesh, cutter_mesh):
    """РОБАСТНИЙ виріз: пропускає НЕгерметичний терен через manifold3d-конструктор
    (топологічний РЕМОНТ у валідний том — чого fill_holes/blender НЕ вміли), тоді
    boolean-різниця. Доведено на щільній юзер-зоні: 290138 граней wt=False →
    manifold3d → wt=True → виріз → wt=True (паз врізано чисто, без нівечення).
    Повертає trimesh.Trimesh або None. Це ГОЛОВНИЙ шлях різу конектор-паза —
    працює навіть коли trimes"""
    raise NotImplementedError("proprietary: removed from public showcase")


def _find_blender() -> Optional[str]:
    """Знаходить шлях до Blender."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _run_blender_boolean(
    terrain_mesh: trimesh.Trimesh,
    cutter_mesh: trimesh.Trimesh,
    label: str = None,
    clearance_m: float = None,
    pre_seal: bool = False,
) -> Optional[trimesh.Trimesh]:
    """Запускає Blender Boolean DIFFERENCE: terrain - cutter."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _mesh_component_count(mesh: Optional[trimesh.Trimesh]) -> int:
    raise NotImplementedError("proprietary: removed from public showcase")


def _boundary_edge_count(mesh: Optional[trimesh.Trimesh]) -> int:
    raise NotImplementedError("proprietary: removed from public showcase")


def _xy_bounds_delta(lhs: Optional[trimesh.Trimesh], rhs: Optional[trimesh.Trimesh]) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _z_bounds_delta(lhs: Optional[trimesh.Trimesh], rhs: Optional[trimesh.Trimesh]) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _z_span_ratio(lhs: Optional[trimesh.Trimesh], rhs: Optional[trimesh.Trimesh]) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _dominant_component(mesh: Optional[trimesh.Trimesh]) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _boolean_candidate_score(mesh: Optional[trimesh.Trimesh]) -> tuple:
    raise NotImplementedError("proprietary: removed from public showcase")


def _cleanup_boolean_candidate(mesh: Optional[trimesh.Trimesh]) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _accept_boolean_stage_result(
    *, previous_mesh: trimesh.Trimesh, candidate_mesh: Optional[trimesh.Trimesh], label: str
) -> trimesh.Trimesh:
    raise NotImplementedError("proprietary: removed from public showcase")


def _extract_2d_footprint(mesh: trimesh.Trimesh) -> Optional[ShapelyPolygon]:
    """Витягує 2D footprint (проекцію на XY) з 3D мешу."""
    raise NotImplementedError("proprietary: removed from public showcase")


def extend_road_mesh_to_uniform_bottom(road_mesh: "trimesh.Trimesh") -> None:
    """Продовжує дно доріг вниз до найнижчої точки мешу.
    Усі пази мають однакову висоту (плоске дно на road_min_z).
    Вершини нижніх граней опускаються до road_min_z."""
    raise NotImplementedError("proprietary: removed from public showcase")


def extend_buildings_mesh_to_uniform_bottom(
    building_meshes: Optional[List["trimesh.Trimesh"]], target_z: float
) -> None:
    """Опускає нижні грані КОЖНОЇ будівлі до спільного `target_z`."""
    raise NotImplementedError("proprietary: removed from public showcase")


def flatten_inlay_to_terrain_decal(
    inlay_mesh: Optional["trimesh.Trimesh"], terrain_provider, offset_m: float = None
) -> Optional["trimesh.Trimesh"]:
    """Convert a 3D inlay (road/park/water) into a thin coloured decal hugging
    the terrain surface — for the FAST PREVIEW path."""
    raise NotImplementedError("proprietary: removed from public showcase")


def build_terrain_decal_from_2d_mask(
    mask_geometry,
    terrain_provider,
    offset_m: float = None,
    target_edge_len_m: float = None,
    simplify_tolerance_m: float = None,
) -> Optional["trimesh.Trimesh"]:
    """Build a preview-only surface decal from a canonical 2D mask."""
    raise NotImplementedError("proprietary: removed from public showcase")


def extend_parks_mesh_to_uniform_bottom(parks_mesh: "trimesh.Trimesh") -> None:
    """Продовжує дно парків вниз до найнижчої точки мешу."""
    raise NotImplementedError("proprietary: removed from public showcase")


def cut_parks_from_solid_terrain(
    terrain_mesh: trimesh.Trimesh,
    parks_polygons: Optional[BaseGeometry] = None,
    clearance_m: float = None,
    scale_factor: float = None,
    parks_mesh: Optional[trimesh.Trimesh] = None,
) -> Optional[trimesh.Trimesh]:
    """Вирізає ПАЗИ (Grooves) для парків у рельєфі."""
    raise NotImplementedError("proprietary: removed from public showcase")


def cut_mesh_from_terrain(
    terrain_mesh: "trimesh.Trimesh",
    cutter_mesh: "trimesh.Trimesh",
    clearance_m: float = None,
    scale_factor: float = None,
    label: str = None,
) -> Optional["trimesh.Trimesh"]:
    """Вирізає ПАЗ (Groove) у рельєфі для вставки мешу (вода, парки тощо)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def cut_roads_from_solid_terrain(
    terrain_mesh: trimesh.Trimesh,
    road_polygons: BaseGeometry,
    clearance_m: float,
    scale_factor: float,
    road_height_m: Optional[float] = None,
    road_mesh: Optional[trimesh.Trimesh] = None,
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def cut_all_grooves(
    terrain_mesh: trimesh.Trimesh,
    road_polygons: Optional[BaseGeometry] = None,
    road_clearance_m: float = None,
    parks_polygons: Optional[BaseGeometry] = None,
    parks_clearance_m: float = None,
    parks_mesh: Optional[trimesh.Trimesh] = None,
    water_polygons: Optional[BaseGeometry] = None,
    water_clearance_m: float = None,
    water_mesh: Optional[trimesh.Trimesh] = None,
    scale_factor: float = None,
    road_mesh: Optional[trimesh.Trimesh] = None,
    groove_depth_m: Optional[float] = None,
) -> Optional[trimesh.Trimesh]:
    """Вирізає ВСІ пази (дороги + парки) ОДНИМ Blender Boolean."""
    raise NotImplementedError("proprietary: removed from public showcase")


def cut_grooves_sequentially(
    terrain_mesh: trimesh.Trimesh,
    road_polygons: Optional[BaseGeometry] = None,
    road_clearance_m: float = None,
    parks_polygons: Optional[BaseGeometry] = None,
    parks_clearance_m: float = None,
    parks_mesh: Optional[trimesh.Trimesh] = None,
    water_polygons: Optional[BaseGeometry] = None,
    water_clearance_m: float = None,
    water_mesh: Optional[trimesh.Trimesh] = None,
    scale_factor: float = None,
    road_mesh: Optional[trimesh.Trimesh] = None,
    groove_depth_m: Optional[float] = None,
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")
