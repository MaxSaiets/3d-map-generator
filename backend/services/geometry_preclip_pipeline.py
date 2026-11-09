# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional
import geopandas as gpd
from shapely.geometry import MultiPolygon
from shapely.geometry.base import BaseGeometry
from shapely.ops import transform as transform_geometry
from services.geometry_context import make_to_local_transformer


@dataclass
class GeometryPreclipResult:
    gdf_buildings_local: Optional[gpd.GeoDataFrame]
    building_geometries_for_flatten: Any
    gdf_water_local: Optional[gpd.GeoDataFrame]
    water_geometries_local_for_bridges: Any
    preclipped_to_zone: bool


def _keep_polygons(geometry: Optional[BaseGeometry]) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _clip_geometry_to_zone(
    geometry: Optional[BaseGeometry], zone_polygon_local: Optional[BaseGeometry]
) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def prepare_preclipped_geometry(
    *,
    gdf_buildings_local: Optional[gpd.GeoDataFrame],
    building_geometries_for_flatten: Any,
    gdf_water: Optional[gpd.GeoDataFrame],
    global_center: Any,
    zone_polygon_local: Optional[BaseGeometry],
    zone_prefix: str = None,
) -> GeometryPreclipResult:
    raise NotImplementedError("proprietary: removed from public showcase")
