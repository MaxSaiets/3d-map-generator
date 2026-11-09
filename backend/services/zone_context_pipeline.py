# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional
from shapely.geometry.base import BaseGeometry
from services.crs_utils import bbox_latlon_to_utm


@dataclass
class ZoneContextResult:
    bbox_meters: tuple[float, float, float, float]
    scale_factor: float


def build_zone_context(
    *,
    request: Any,
    global_center: Any,
    zone_polygon_local: Optional[BaseGeometry],
    reference_xy_m: Optional[tuple[float, float]],
    zone_prefix: str = None,
) -> ZoneContextResult:
    raise NotImplementedError("proprietary: removed from public showcase")
