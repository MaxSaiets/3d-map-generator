# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Local OSM PBF loader (Geofabrik) for Ukraine-wide best data."""

from __future__ import annotations
from pathlib import Path
from typing import Tuple, Optional
import os
import warnings
import hashlib
import time
import gc
import numpy as np
import geopandas as gpd
import osmnx as ox
import pandas as pd
import requests

GEOFABRIK_UKRAINE_PBF_URL = None


def _pyrosm_network_type() -> str:
    """Map our env-style OSM_ROADS_NETWORK_TYPE (osmnx-like) to pyrosm names."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _pbf_cache_dir() -> Path:
    raise NotImplementedError("proprietary: removed from public showcase")


def _cache_enabled() -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _bbox_cache_key(
    kind: str, north: float, south: float, east: float, west: float, *params: object
) -> str:
    raise NotImplementedError("proprietary: removed from public showcase")


def _read_gdf_parquet(path: Path) -> gpd.GeoDataFrame:
    raise NotImplementedError("proprietary: removed from public showcase")


def _write_gdf_parquet(gdf: gpd.GeoDataFrame, path: Path) -> None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _minimal_columns(gdf: gpd.GeoDataFrame, keep: list[str]) -> gpd.GeoDataFrame:
    raise NotImplementedError("proprietary: removed from public showcase")


def _download_file(url: str, dst: Path) -> None:
    raise NotImplementedError("proprietary: removed from public showcase")


def ensure_ukraine_pbf(pbf_path: Path) -> Path:
    """Ensures the PBF exists. If not, optionally auto-downloads from Geofabrik."""
    raise NotImplementedError("proprietary: removed from public showcase")


def fetch_city_data_from_pbf(
    north: float, south: float, east: float, west: float
) -> Tuple[gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame]:
    """Returns (buildings_gdf, water_gdf, roads_edges_gdf) in projected CRS (UTM)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def fetch_extras_from_pbf(north: float, south: float, east: float, west: float) -> gpd.GeoDataFrame:
    """Returns (green_polygons_gdf, poi_points_gdf) in projected CRS (UTM)."""
    raise NotImplementedError("proprietary: removed from public showcase")
