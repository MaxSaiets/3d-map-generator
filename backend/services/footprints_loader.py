# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Building footprints integration."""

from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Tuple, List
import os
import geopandas as gpd
import numpy as np
from shapely.geometry import box

HEIGHT_KEYS: List[str] = None


def _get_cfg_path() -> Optional[Path]:
    raise NotImplementedError("proprietary: removed from public showcase")


def is_footprints_enabled() -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def load_footprints_bbox(
    north: float, south: float, east: float, west: float, target_crs: Optional[object]
) -> gpd.GeoDataFrame:
    """Loads footprints polygons within bbox.
    Input bbox is lat/lon degrees.
    Output is projected to target_crs if provided."""
    raise NotImplementedError("proprietary: removed from public showcase")


def transfer_osm_attributes_to_footprints(
    footprints: gpd.GeoDataFrame, osm_buildings: gpd.GeoDataFrame
) -> gpd.GeoDataFrame:
    """Spatially transfers OSM attributes (height/levels/roof/building) onto footprints.
    We keep footprint geometry but copy best-matching OSM tags."""
    raise NotImplementedError("proprietary: removed from public showcase")
