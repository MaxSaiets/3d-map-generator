# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Сервіс для завантаження даних з OpenStreetMap
Використовує osmnx для отримання структурованих даних
Підтримка кешування для швидкого повторного доступу"""

import osmnx as ox
import geopandas as gpd
import pandas as pd
import warnings
from typing import Tuple, Optional
import os
import hashlib
import json
import math
import time
from pathlib import Path
from osmnx._errors import InsufficientResponseError
import networkx as nx
from services.osm_source import resolve_osm_source
from services import overpass_health

_CACHE_DIR = None
_CACHE_VERSION = None
RAILWAY_FETCH_TIMEOUT_S = None
_RAIL_TILE_DEG = None
_RAIL_TILE_TTL_S = None
_RAIL_TILE_CACHE_PATH = None


def _rail_tiles_for_bbox(north: float, south: float, east: float, west: float):
    raise NotImplementedError("proprietary: removed from public showcase")


def _load_rail_empty_tiles() -> dict:
    raise NotImplementedError("proprietary: removed from public showcase")


def _mark_rail_tiles_empty(tiles, empty: bool) -> None:
    """Позначає плитки як порожні/непорожні. Непорожні ВИДАЛЯЄМО з кешу —
    щоб раптова поява колій у OSM не була заблокована старим негативом."""
    raise NotImplementedError("proprietary: removed from public showcase")


_OVERPASS_ENDPOINTS_DEFAULT = None


def _cache_enabled() -> bool:
    """Перевіряє, чи увімкнено кешування"""
    raise NotImplementedError("proprietary: removed from public showcase")


def _overpass_endpoints() -> list[str]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _bundle_miss_types():
    """Клас винятку «пакет не може віддати шар» (лінивий імпорт — модуль
    пакета сам імпортує `_run_overpass_with_retries` звідси)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _run_overpass_with_retries(label: str, fetch_fn):
    raise NotImplementedError("proprietary: removed from public showcase")


def _estimate_bbox_radius_m(north: float, south: float, east: float, west: float) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _cache_key(north: float, south: float, east: float, west: float, padding: float) -> str:
    """Створює ключ кешу на основі bbox та padding"""
    raise NotImplementedError("proprietary: removed from public showcase")


def _clean_gdf_for_parquet(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Очищує GeoDataFrame від колонок зі складними типами даних для збереження в Parquet"""
    raise NotImplementedError("proprietary: removed from public showcase")


def _save_to_cache(
    north: float,
    south: float,
    east: float,
    west: float,
    padding: float,
    buildings: gpd.GeoDataFrame,
    water: gpd.GeoDataFrame,
    roads_graph,
) -> None:
    """Зберігає дані в кеш"""
    raise NotImplementedError("proprietary: removed from public showcase")


def _load_from_cache(
    north: float, south: float, east: float, west: float, padding: float
) -> Optional[Tuple[gpd.GeoDataFrame, gpd.GeoDataFrame, object]]:
    """Завантажує дані з кешу"""
    raise NotImplementedError("proprietary: removed from public showcase")


def fetch_city_data(
    north: float,
    south: float,
    east: float,
    west: float,
    padding: float = None,
    target_crs: Optional[str] = None,
    include_building_parts: bool = True,
    bundle: Optional[object] = None,
) -> Tuple[gpd.GeoDataFrame, gpd.GeoDataFrame, object]:
    """Завантажує дані OSM для вказаної області з буферизацією для коректної обробки країв"""
    raise NotImplementedError("proprietary: removed from public showcase")
