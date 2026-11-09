# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Optional
import trimesh
from shapely.geometry import box
from shapely.geometry.base import BaseGeometry
from services.detail_layer_utils import clamp_mesh_to_terrain_floor
from services.inlay_fit import InlayFitConfig
from services.printable_3d_validator import validate_road_mesh
from services.processing_results import RoadLayerResult, RoadProcessingResult
from services.road_processor import create_road_surface_cap, process_roads


def _iter_polygons(geometry: BaseGeometry | None) -> list[Any]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _rebuild_road_mesh_from_mask(
    *,
    road_polygons: BaseGeometry | None,
    terrain_provider: Any,
    scale_factor: float,
    road_height_m: float,
    road_embed_m: float,
) -> trimesh.Trimesh | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def process_road_layer(
    *,
    task: Any,
    request: Any,
    scale_factor: Optional[float],
    terrain_provider: Any,
    terrain_mesh: Optional[trimesh.Trimesh],
    global_center: Any,
    G_roads: Any,
    water_geoms_for_bridges: Any,
    road_width_multiplier_effective: float,
    zone_polygon_local: Any,
    building_union_local: Any,
    merged_roads_geom_local: Any,
    road_height_m: float,
    road_embed_m: float,
    stl_extra_embed_m: float,
    fit_config: Optional[InlayFitConfig] = None,
    road_polygons_override: Any = None,
) -> RoadLayerResult:
    raise NotImplementedError("proprietary: removed from public showcase")
