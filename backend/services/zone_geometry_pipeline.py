# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional
from shapely.geometry import Polygon
from shapely.geometry.base import BaseGeometry
from services.crs_utils import bbox_latlon_to_utm
from services.hexagonal_grid import hexagon_center_to_corner


@dataclass
class ZoneGeometryResult:
    zone_polygon_local: Optional[BaseGeometry]
    reference_xy_m: Optional[tuple[float, float]]


def prepare_zone_geometry(
    *,
    global_center: Any,
    grid_bbox_latlon: Any,
    zone_row: Any,
    zone_col: Any,
    hex_size_m: Any,
    zone_polygon_coords: Optional[list],
    zone_prefix: str = None,
) -> ZoneGeometryResult:
    raise NotImplementedError("proprietary: removed from public showcase")
