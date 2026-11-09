# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Optional
import geopandas as gpd
from geopandas import GeoDataFrame
from shapely.geometry import MultiPolygon, Polygon
from shapely.ops import unary_union
from services.detail_layer_utils import MICRO_REGION_THRESHOLD_MM, model_mm_to_world_m
from services.processing_results import WaterLayerResult
from services.water_processor import process_water_surface


def _is_printable_water_mesh(mesh: Any, *, min_face_count: int = None) -> bool:
    """Return True if mesh has enough substance to slice cleanly."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _apply_water_fit_inset(
    geometry: Any, *, scale_factor: Optional[float], fit_clearance_mm: float
) -> Any:
    raise NotImplementedError("proprietary: removed from public showcase")


def _filter_water_fragments(geometry: Any, *, scale_factor: Optional[float]) -> Any:
    raise NotImplementedError("proprietary: removed from public showcase")


def _prepare_water_polygons(
    gdf_water: Optional[GeoDataFrame],
    *,
    road_polygons: Any = None,
    building_polygons: Any = None,
    scale_factor: Optional[float] = None,
    fit_clearance_mm: float = None,
) -> Any:
    raise NotImplementedError("proprietary: removed from public showcase")


def _build_water_mesh_input(
    gdf_water: Optional[GeoDataFrame], *, polygons: Any
) -> Optional[GeoDataFrame]:
    raise NotImplementedError("proprietary: removed from public showcase")


def process_water_layer(
    *,
    task: Any,
    request: Any,
    scale_factor: Optional[float],
    terrain_provider: Any,
    global_center: Any,
    gdf_water: Optional[GeoDataFrame],
    water_depth_m: float,
    road_polygons: Any = None,
    building_polygons: Any = None,
    coordinates_already_local: bool = False,
    zone_prefix: str = None,
    water_polygons_override: Any = None,
    fit_clearance_mm: float = None,
) -> WaterLayerResult:
    raise NotImplementedError("proprietary: removed from public showcase")
