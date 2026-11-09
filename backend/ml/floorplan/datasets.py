# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Реальні планування з відкритих датасетів → RealLayout."""

from __future__ import annotations
import argparse
import csv
import math
import os
import pickle
import sys
from typing import Any, Dict, Iterator, List, Optional, Sequence, Tuple
import numpy as np

HERE = None
CACHE_PATH = None
SWISS_CSV_CANDIDATES = None
WALL_SUBTYPES = None
DOOR_SUBTYPES = None
WINDOW_SUBTYPES = None
SKIP_AREAS = None
ROOM_NAME_UK = None
MIN_AREA_M2 = None
MAX_AREA_M2 = None
MIN_WALLS = None
MIN_ROOMS = None


def _swiss_csv_path(explicit: Optional[str] = None) -> Optional[str]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _parse_polygon(wkt: str) -> Optional[List[Tuple[float, float]]]:
    """Мінімальний парсер WKT POLYGON — shapely тут зайвий і повільніший."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _polygon_area(points: Sequence[Tuple[float, float]]) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _dominant_angle(walls: Sequence[Sequence[Tuple[float, float]]]) -> float:
    """Головний напрям стін (rad). Реальні координати — у СК будівлі, тобто
    план може стояти під довільним кутом; креслення ж завжди рівне."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _rotate(points: Sequence[Tuple[float, float]], angle: float) -> List[Tuple[float, float]]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _bbox(points: Sequence[Tuple[float, float]]) -> Tuple[float, float, float, float]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _bbox_overlap(
    a: Tuple[float, float, float, float], b: Tuple[float, float, float, float], pad: float = None
) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def iter_swiss_apartments(
    csv_path: str, limit: int = None, progress_every: int = None
) -> Iterator[Dict[str, Any]]:
    """Стрімить geometries.csv і віддає квартири по одній."""
    raise NotImplementedError("proprietary: removed from public showcase")


def to_real_layout(raw: Dict[str, Any]):
    """Сира квартира → RealLayout: поворот у рівне положення + фільтри якості."""
    raise NotImplementedError("proprietary: removed from public showcase")


def build_cache(
    limit: int = None, csv_path: Optional[str] = None, out_path: str = CACHE_PATH
) -> str:
    """Один прохід по датасету → компактний кеш RealLayout для тренування."""
    raise NotImplementedError("proprietary: removed from public showcase")


_CACHE: Optional[List] = None


def load_layouts(path: str = CACHE_PATH) -> List:
    """Кеш → список RealLayout. Порожній список, якщо кешу немає (це не помилка:
    тренування просто піде на самій синтетиці)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def main() -> None:
    raise NotImplementedError("proprietary: removed from public showcase")
