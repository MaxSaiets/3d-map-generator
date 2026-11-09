# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Сервіс для отримання даних висот (рельєфу) через API
Підтримує кілька джерел: OpenTopography (безкоштовний), Mapbox (потрібен ключ)"""

import numpy as np
import requests
from typing import Tuple, Optional, Dict, Any, List
import warnings
import os


def _debug(msg: str):
    raise NotImplementedError("proprietary: removed from public showcase")


def _backfill_voids(Z: np.ndarray, zfill_fallback: float, label: str = None) -> np.ndarray:
    """Заповнює NaN-дірки (океан / краї тайлів / nodata) РОЗУМНО."""
    raise NotImplementedError("proprietary: removed from public showcase")


def get_elevation_from_api(
    bbox: Tuple[float, float, float, float], resolution: int = None, api_type: str = None
) -> Optional[np.ndarray]:
    """Отримує дані висот через API"""
    raise NotImplementedError("proprietary: removed from public showcase")


def get_elevation_opentopography(
    bbox: Tuple[float, float, float, float], resolution: int = None
) -> Optional[np.ndarray]:
    """Отримує дані висот з OpenTopography API (безкоштовний, без API ключа)
    Використовує SRTM дані"""
    raise NotImplementedError("proprietary: removed from public showcase")


def get_elevation_mapbox(
    bbox: Tuple[float, float, float, float], resolution: int = None, api_key: Optional[str] = None
) -> Optional[np.ndarray]:
    """Отримує дані висот з Mapbox Terrain API (потрібен API ключ)"""
    raise NotImplementedError("proprietary: removed from public showcase")


def get_elevation_abs_meters_from_api(
    bbox_latlon: Tuple[float, float, float, float],
    X_meters: np.ndarray,
    Y_meters: np.ndarray,
    source_crs: Optional[object] = None,
    terrarium_zoom: Optional[int] = None,
) -> Optional[np.ndarray]:
    """Отримує абсолютні висоти в метрах над рівнем моря з API (без нормалізації).
    Використовується для отримання реальних висот перед нормалізацією в terrain_generator."""
    raise NotImplementedError("proprietary: removed from public showcase")


def get_elevation_data_from_api(
    bbox_latlon: Tuple[float, float, float, float],
    X_meters: np.ndarray,
    Y_meters: np.ndarray,
    z_scale: float = None,
    source_crs: Optional[object] = None,
    terrarium_zoom: Optional[int] = None,
) -> Optional[np.ndarray]:
    """Отримує дані висот з API для заданої сітки координат"""
    raise NotImplementedError("proprietary: removed from public showcase")


_ELEV_CACHE: Dict[str, float] = None


def _get_elevation_opentopodata_batch(
    lats: np.ndarray, lons: np.ndarray, dataset: str = None
) -> Optional[np.ndarray]:
    """Викликає OpenTopoData для набору точок.
    API лімітований, тому:
    - квантуємо координати (кеш)
    - робимо батчі по 100 точок"""
    raise NotImplementedError("proprietary: removed from public showcase")


def _get_elevation_from_geotiff(
    dem_path: str, X_meters: np.ndarray, Y_meters: np.ndarray, source_crs: object
) -> Optional[np.ndarray]:
    """Семплить DEM GeoTIFF (Copernicus/SRTM/LiDAR) у будь-якій CRS:
    - переводимо точки з source_crs (UTM/метри) у CRS растру
    - rasterio.sample() повертає висоти"""
    raise NotImplementedError("proprietary: removed from public showcase")


def get_elevation_simple_terrain(
    X: np.ndarray, Y: np.ndarray, bbox: Tuple[float, float, float, float], z_scale: float = None
) -> np.ndarray:
    """Генерує простий синтетичний рельєф для тестування
    (якщо API недоступний)"""
    raise NotImplementedError("proprietary: removed from public showcase")
