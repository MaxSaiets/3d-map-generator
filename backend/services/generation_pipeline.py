# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
import os
from dataclasses import dataclass
from typing import Any, Optional
import trimesh
from shapely.geometry import box
from shapely.geometry.base import BaseGeometry
from services.groove_pipeline import prepare_road_cut_mask
from services.terrain_generator import create_terrain_mesh


def _iter_extrudable_polygons(geom: Any, min_area_m2: float = None) -> list:
    """Витягує список ВАЛІДНИХ, не-вироджених Polygon-ів з будь-якої геометрії
    (Polygon / MultiPolygon / GeometryCollection) для безпечної екструзії."""
    raise NotImplementedError("proprietary: removed from public showcase")


@dataclass
class GenerationPipelineResult:
    terrain_mesh: Optional[trimesh.Trimesh]
    terrain_provider: Any
    road_cut_mask: Optional[BaseGeometry]
    road_height_m: Optional[float]
    road_embed_m: Optional[float]


def _compute_road_dimensions(
    *,
    request: Any,
    scale_factor: Optional[float],
    stl_extra_embed_m: float,
    road_height_m: Optional[float],
    road_embed_m: Optional[float],
) -> tuple[Optional[float], Optional[float]]:
    raise NotImplementedError("proprietary: removed from public showcase")


def process_generation_stage(
    *,
    task: Any,
    request: Any,
    scale_factor: Optional[float],
    bbox_meters: Any,
    latlon_bbox: Any,
    source_crs: Any,
    elevation_ref_m: float,
    baseline_offset_m: float,
    building_geometries_for_flatten: Any,
    merged_roads_geom_local: Optional[BaseGeometry],
    merged_roads_geom: Optional[BaseGeometry],
    building_union_local: Optional[BaseGeometry],
    gdf_water_local: Any,
    global_center: Any,
    zone_polygon_local: Optional[BaseGeometry],
    groove_clearance_mm: float,
    stl_extra_embed_m: float,
    zone_prefix: str = None,
    road_height_m: Optional[float] = None,
    road_embed_m: Optional[float] = None,
    road_cut_mask_override: Optional[BaseGeometry] = None,
) -> GenerationPipelineResult:
    raise NotImplementedError("proprietary: removed from public showcase")
