# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
import concurrent.futures
import os
from dataclasses import dataclass
from typing import Any
import geopandas as gpd
from services.data_loader import fetch_city_data
from services.extras_loader import fetch_extras
from services.osm_source import resolve_osm_source

_BUNDLE_CITY_TAGS = None
_BUNDLE_EXTRAS_TAGS = None


def _env_float(name: str, default: float) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _source_wait_callback(task):
    """Пакет чекає на джерело → задача про це знає (`source_wait_s` іде у
    /api/status, фронт показує людині чесний стан замість «зависло»)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _make_bundle(
    *, request, road_padding, loader_padding, keychain_mode, zone_prefix=None, status_cb=None
):
    """LazyBundle для зони або None (вимкнено / джерело не Overpass / помилка)."""
    raise NotImplementedError("proprietary: removed from public showcase")


@dataclass
class DataFetchPipelineResult:
    gdf_buildings: gpd.GeoDataFrame
    gdf_water: gpd.GeoDataFrame
    G_roads: Any
    gdf_green: gpd.GeoDataFrame


def fetch_generation_data(
    *, request: Any, global_center: Any, task: Any, zone_prefix: str = None
) -> DataFetchPipelineResult:
    raise NotImplementedError("proprietary: removed from public showcase")
