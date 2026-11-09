# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
import os
import tempfile
from dataclasses import dataclass
from typing import Optional
import numpy as np
import trimesh
from shapely.geometry.base import BaseGeometry
from services.boolean_backends import BooleanBackend, GrooveBooleanRequest, resolve_boolean_backend
from services.detail_layer_utils import MICRO_REGION_THRESHOLD_MM, model_mm_to_world_m
from services.road_processor import merge_close_road_gaps
from services.terrain_cutter import cut_grooves_sequentially
from shapely.ops import unary_union


def _apply_exclusion_mask(geometry, exclusion_mask):
    raise NotImplementedError("proprietary: removed from public showcase")


def _drop_tiny_material_fragments(geometry, *, min_feature_m: float):
    raise NotImplementedError("proprietary: removed from public showcase")


def prepare_building_groove_mask(
    building_polygons, *, groove_clearance_m: float, zone_polygon=None
):
    """Thin ring around buildings where roads/parks/water must NOT reach."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _prepare_parks_groove_mask(
    parks_polygons,
    *,
    road_groove_mask=None,
    water_polygons=None,
    building_polygons=None,
    groove_clearance_m: float,
    boundary_snap_m: float,
    zone_prefix: str = None,
):
    raise NotImplementedError("proprietary: removed from public showcase")


def _prepare_water_groove_mask(
    water_polygons,
    *,
    road_groove_mask=None,
    parks_groove_mask=None,
    building_polygons=None,
    groove_clearance_m: float,
    boundary_snap_m: float,
    zone_prefix: str = None,
):
    raise NotImplementedError("proprietary: removed from public showcase")


def _fill_narrow_road_holes(road_cut_mask, min_printable_m, preserve_geom=None, zone_prefix=None):
    """Fill interior voids in road polygon that are too narrow to print (-> treated as road)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _restore_inner_hole_clearance(
    road_source_mask, *, clearance_m: float, preserve_geom=None, zone_prefix=None
):
    """Restore groove clearance on the inner side of road holes."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _absorb_terrain_slivers(
    zone_polygon,
    road_cut_mask,
    parks_polys,
    water_polys,
    min_printable_m,
    protected_voids=None,
    zone_prefix=None,
):
    """Find thin terrain strips that won't print and absorb each into the nearest groove."""
    raise NotImplementedError("proprietary: removed from public showcase")


@dataclass
class GrooveCutResult:
    terrain_mesh: Optional[trimesh.Trimesh]
    road_polygons_used: Optional[BaseGeometry]
    parks_polygons_used: Optional[BaseGeometry]
    water_polygons_used: Optional[BaseGeometry]
    boolean_backend_name: str
    grooves_expected: bool = None
    change_applied: bool = None
    rejected: bool = None
    rejection_reason: Optional[str] = None
    failure_reason: Optional[str] = None
    changed_vertices: bool = None
    volume_removed_m3: Optional[float] = None
    volume_removed_ratio: Optional[float] = None


def _mesh_component_count(mesh: Optional[trimesh.Trimesh]) -> int:
    raise NotImplementedError("proprietary: removed from public showcase")


def _geometry_has_area(geometry: Optional[BaseGeometry]) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _mesh_changed(
    before_mesh: Optional[trimesh.Trimesh],
    after_mesh: Optional[trimesh.Trimesh],
    *,
    atol: float = None,
) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _xy_bounds_delta(lhs: Optional[trimesh.Trimesh], rhs: Optional[trimesh.Trimesh]) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _roundtrip_mesh_via_stl(mesh: Optional[trimesh.Trimesh]) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _dominant_watertight_component(
    mesh: Optional[trimesh.Trimesh],
    *,
    original_mesh: Optional[trimesh.Trimesh],
    scale_factor: Optional[float],
    label: str,
    source_label: str,
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _stabilize_groove_result_mesh(
    candidate_mesh: Optional[trimesh.Trimesh],
    *,
    original_mesh: Optional[trimesh.Trimesh],
    scale_factor: Optional[float],
    label: str,
    allow_non_watertight_fallback: bool = False,
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _bounds_delta_xyz(
    lhs: Optional[trimesh.Trimesh], rhs: Optional[trimesh.Trimesh]
) -> tuple[float, float]:
    raise NotImplementedError("proprietary: removed from public showcase")


def prepare_road_cut_mask(
    merged_roads_geom_local: Optional[BaseGeometry],
    building_union_local: Optional[BaseGeometry],
    scale_factor: Optional[float],
    groove_clearance_mm: float,
    building_clearance_mm: float = None,
    zone_polygon_local: Optional[BaseGeometry] = None,
    min_printable_mm: float = MICRO_REGION_THRESHOLD_MM,
    road_gap_fill_threshold_mm: float = None,
    zone_prefix: str = None,
) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def cut_inlay_grooves(
    terrain_mesh: Optional[trimesh.Trimesh],
    road_mesh: Optional[trimesh.Trimesh],
    parks_mesh: Optional[trimesh.Trimesh],
    water_mesh: Optional[trimesh.Trimesh],
    road_cut_mask: Optional[BaseGeometry],
    merged_roads_geom_local: Optional[BaseGeometry],
    parks_polygons: Optional[BaseGeometry],
    water_polygons: Optional[BaseGeometry],
    building_polygons: Optional[BaseGeometry],
    scale_factor: Optional[float],
    groove_clearance_mm: float,
    road_embed_m: float,
    parks_embed_mm: float,
    water_depth_m: float,
    boolean_backend: Optional[BooleanBackend] = None,
    zone_prefix: str = None,
    zone_polygon_local: Optional[BaseGeometry] = None,
    min_printable_mm: float = MICRO_REGION_THRESHOLD_MM,
    parks_groove_override: Optional[BaseGeometry] = None,
    water_groove_override: Optional[BaseGeometry] = None,
    use_exact_masks: bool = False,
    cdt_allowed: bool = True,
    notch_cutter_mesh: Optional[trimesh.Trimesh] = None,
) -> GrooveCutResult:
    raise NotImplementedError("proprietary: removed from public showcase")
