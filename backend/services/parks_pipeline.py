# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Optional
import numpy as np
import trimesh
from geopandas import GeoDataFrame
from shapely.geometry.base import BaseGeometry
from services.detail_layer_utils import (
    MIN_LAND_WIDTH_MODEL_MM,
    clamp_mesh_to_terrain_floor,
    model_mm_to_world_m,
    prepare_green_areas_for_processing,
)
from services.green_processor import (
    _add_strong_faceted_texture,
    _create_high_res_mesh,
    process_green_areas,
)
from services.processing_results import GreenAreaProcessingResult, ParkLayerResult


def _ensure_printable_park_mesh(mesh: Any, *, zone_prefix: str = None) -> Any:
    """Парки, як вода/дороги/будівлі, мусять бути герметичні перед 3MF-експортом,
    інакше слайсер відкидає обʼєкт або тихо фейлить (відсутній рельєф парку). На
    відміну від water_layer (_is_printable_water_mesh) тут парки НЕ просто
    валідуються — спершу РЕМОНТУЄМО (merge+winding+fill_holes+fix_normals), щоб
    зберегти рельєф, і дропаємо ЛИШЕ якщо меш справді вироджений (0 фейсів/обʼєму)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _iter_polygons(geometry: BaseGeometry | None) -> list[Any]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _apply_fit_inset_to_override(
    geometry: BaseGeometry | None, *, scale_factor: float, fit_clearance_mm: float
) -> BaseGeometry | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _rebuild_park_mesh_from_polygons(
    *,
    park_polygons: BaseGeometry | None,
    terrain_provider: Any,
    scale_factor: float,
    park_height_m: float,
    park_embed_m: float,
    global_center: Any,
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def process_park_layer(
    *,
    task: Any,
    request: Any,
    scale_factor: Optional[float],
    terrain_provider: Any,
    terrain_mesh: Any,
    global_center: Any,
    zone_polygon_local: Any,
    road_cut_source: Any,
    building_union_local: Any,
    water_polygons: Any,
    road_exclusion_clearance_mm: float = None,
    fit_clearance_mm: float = None,
    gdf_green: Optional[GeoDataFrame],
    zone_prefix: str = None,
    park_polygons_override: Any = None,
) -> ParkLayerResult:
    raise NotImplementedError("proprietary: removed from public showcase")
