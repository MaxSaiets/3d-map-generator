# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Модуль для попереднього завантаження всіх OSM даних при старті сервера
та використання spatial index для швидкого вибору об'єктів за bbox."""

import os
import warnings
import time
from pathlib import Path
from typing import Tuple, Optional
import geopandas as gpd
import pandas as pd

_preloaded_buildings: Optional[gpd.GeoDataFrame] = None
_preloaded_water: Optional[gpd.GeoDataFrame] = None
_preloaded_roads: Optional[gpd.GeoDataFrame] = None
_preloaded_green: Optional[gpd.GeoDataFrame] = None
_is_loaded = None


def load_all_data() -> None:
    """Завантажує всі дані з PBF файлу один раз при старті сервера."""
    raise NotImplementedError("proprietary: removed from public showcase")


def get_data_for_bbox(
    north: float, south: float, east: float, west: float
) -> Tuple[gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame]:
    """Отримує дані для вказаного bbox з preloaded даних, використовуючи spatial index."""
    raise NotImplementedError("proprietary: removed from public showcase")


def get_extras_for_bbox(north: float, south: float, east: float, west: float) -> gpd.GeoDataFrame:
    """Отримує extras (green) для вказаного bbox."""
    raise NotImplementedError("proprietary: removed from public showcase")


def is_loaded() -> bool:
    """Перевіряє, чи завантажені дані"""
    raise NotImplementedError("proprietary: removed from public showcase")
