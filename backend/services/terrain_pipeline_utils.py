# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Optional


def resolve_generation_source_crs(
    *,
    gdf_buildings: Any,
    G_roads: Any,
    global_center: Any,
    allow_global_center_fallback: bool = True,
    zone_prefix: str = None,
) -> Any:
    raise NotImplementedError("proprietary: removed from public showcase")


def compute_water_depth_m(
    *, water_depth_mm: float, scale_factor: Optional[float]
) -> Optional[float]:
    raise NotImplementedError("proprietary: removed from public showcase")


def compute_water_surface_thickness_m(
    *,
    water_depth_mm: float,
    water_depth_m: Optional[float],
    scale_factor: Optional[float],
    min_thickness_mm: float = None,
    max_cap_mm: float = None,
    ratio: float = None,
) -> Optional[float]:
    raise NotImplementedError("proprietary: removed from public showcase")
