# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""local_osm_db.py — швидкий локальний OSM extract з DuckDB-БД."""

from __future__ import annotations
import json
import os
import tempfile
import threading
from collections import OrderedDict
from pathlib import Path
from typing import Optional

try:
    import duckdb
except Exception:
    duckdb = None
_QUERY_CACHE: dict[str, dict] = None
_QUERY_CACHE_MAX = None
_CONN_LOCK = None
_CONN = None
_CELL_PAD_DEG = None
_CELL_CACHE: "OrderedDict[str, dict]" = None
_CELL_CACHE_MAX = None


def _find_cell_containing(
    table: str, select_cols: str, north: float, south: float, east: float, west: float
):
    """Returns the cache KEY of the most-recently-used cached padded region whose
    bounds fully contain the requested bbox (and matches table+columns), or None."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _fetch_rows_cached(
    conn, table: str, select_cols: str, north: float, south: float, east: float, west: float
):
    """Рядки (кортежі за select_cols, БЕЗ bbox-колонок) для точного запитаного bbox —
    або нарізані в пам'яті з закешованого поширеного (padded) регіону, або свіжо
    запитані (і закешовані) з DuckDB з відступом навколо запиту."""
    raise NotImplementedError("proprietary: removed from public showcase")


_BUILDING_COLS: Optional[str] = None


def db_path() -> Optional[Path]:
    """Шукає duckdb файл по env або стандартних шляхах."""
    raise NotImplementedError("proprietary: removed from public showcase")


def is_available() -> bool:
    """True якщо duckdb встановлено І файл БД існує."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _get_conn():
    """Lazy-initialized DuckDB connection (thread-safe)."""
    raise NotImplementedError("proprietary: removed from public showcase")


_EXTRA_LOCK = None
_EXTRA: Optional[list] = None


def _extra_dbs() -> list:
    raise NotImplementedError("proprietary: removed from public showcase")


def _extra_rows(
    table: str, select_cols: str, north: float, south: float, east: float, west: float
) -> list:
    """Рядки з додаткових баз, чий прямокутник перетинає bbox (точний запит, без кешу)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _bbox_key(north: float, south: float, east: float, west: float) -> str:
    raise NotImplementedError("proprietary: removed from public showcase")


def get_gdf(table: str, north: float, south: float, east: float, west: float, target_crs=None):
    """Повертає GeoDataFrame з геометріями для заданого bbox.
    Використовується у data_loader.py для backend генерації (заміна Overpass)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def get_roads_graph(north: float, south: float, east: float, west: float, target_crs=None):
    """Будує networkx MultiDiGraph з локальних roads, сумісний з OSMnx."""
    raise NotImplementedError("proprietary: removed from public showcase")


def extract_bbox(north: float, south: float, east: float, west: float) -> dict:
    """Витягує всі OSM-фічі що ПЕРЕТИНАЮТЬ bbox. Повертає dict зі списками:
    {
      "buildings": [{"id", "levels", "wkt"}, ...],
      "roads":     [{"id", "highway", "bridge", "wkt"}, ...],
      "bridges":   [{"id", "highway", "wkt"}, ...],
      "water":     [{"id", "type", "wkt"}, ...],
      "parks":     [{"id", "type", "wkt"}, ...],
    }"""
    raise NotImplementedError("proprietary: removed from public showcase")
