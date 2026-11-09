# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Extra layers loader:
- parks/green areas (polygons)
- POIs (benches etc.)"""

from __future__ import annotations
import os
import time
import warnings
from typing import Tuple
from pathlib import Path
import hashlib
import pandas as pd
import geopandas as gpd
import osmnx as ox
from services import overpass_health
from services.osm_source import resolve_osm_source

_CACHE_DIR = None
_CACHE_VERSION = None
_OVERPASS_ENDPOINTS_DEFAULT = None


def _bbox_key(
    north: float, south: float, east: float, west: float
) -> tuple[float, float, float, float]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _cache_enabled() -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _overpass_endpoints() -> list[str]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _run_overpass_with_retries(label: str, fetch_fn):
    raise NotImplementedError("proprietary: removed from public showcase")


def _clean_gdf_for_parquet(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    raise NotImplementedError("proprietary: removed from public showcase")


def _cache_key(
    source: str, north: float, south: float, east: float, west: float, target_crs: str | None
) -> str:
    raise NotImplementedError("proprietary: removed from public showcase")


def _load_from_cache(
    *, source: str, north: float, south: float, east: float, west: float, target_crs: str | None
) -> gpd.GeoDataFrame | None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _save_to_cache(
    *,
    source: str,
    north: float,
    south: float,
    east: float,
    west: float,
    target_crs: str | None,
    gdf_green: gpd.GeoDataFrame,
) -> None:
    raise NotImplementedError("proprietary: removed from public showcase")


def fetch_extras(
    north: float,
    south: float,
    east: float,
    west: float,
    target_crs: str | None = None,
    bundle: object | None = None,
) -> gpd.GeoDataFrame:
    raise NotImplementedError("proprietary: removed from public showcase")
