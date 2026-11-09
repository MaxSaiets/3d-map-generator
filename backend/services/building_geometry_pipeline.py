# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional
import geopandas as gpd
from shapely.geometry.base import BaseGeometry
from shapely.ops import transform as transform_geometry
from shapely.ops import unary_union
from services.geometry_context import make_to_local_transformer


@dataclass
class BuildingGeometryPreparationResult:
    gdf_buildings_local: Optional[gpd.GeoDataFrame]
    building_geometries_for_flatten: Any
    building_union_local: Optional[BaseGeometry]


def prepare_building_geometry(
    *, gdf_buildings: Optional[gpd.GeoDataFrame], global_center: Any, zone_prefix: str = None
) -> BuildingGeometryPreparationResult:
    raise NotImplementedError("proprietary: removed from public showcase")
