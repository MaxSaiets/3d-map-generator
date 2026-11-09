# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Генерація сітки (шестикутники або квадрати) для ділення карти на зони.
Використовує offset coordinates для ідеального підходу без границь."""

import math
from typing import List, Tuple, Dict
from shapely.geometry import Polygon, Point, box
from shapely.ops import unary_union


def hexagon_center_to_corner(
    center_x: float, center_y: float, size: float
) -> List[Tuple[float, float]]:
    """Створює координати вершин шестикутника навколо центру."""
    raise NotImplementedError("proprietary: removed from public showcase")


def generate_square_grid(
    bbox: Tuple[float, float, float, float], square_size_m: float = None
) -> List[Dict]:
    """Генерує квадратну сітку для заданого bbox."""
    raise NotImplementedError("proprietary: removed from public showcase")


def generate_hexagonal_grid(
    bbox: Tuple[float, float, float, float], hex_size_m: float = None
) -> List[Dict]:
    """Генерує гексагональну сітку для заданого bbox."""
    raise NotImplementedError("proprietary: removed from public showcase")


def generate_circular_grid(
    bbox: Tuple[float, float, float, float], radius_m: float = None
) -> List[Dict]:
    """Генерує сітку з круговими зонами для заданого bbox.
    Кожен круг має однакову площу (рівні зони)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def hexagons_to_geojson(cells: List[Dict], to_wgs84=None) -> Dict:
    """Конвертує список клітинок (шестикутники або квадрати) в GeoJSON формат."""
    raise NotImplementedError("proprietary: removed from public showcase")


def calculate_grid_center_from_geojson(geojson: Dict, to_wgs84=None) -> Tuple[float, float]:
    """Обчислює оптимальний центр для всієї сітки на основі GeoJSON features.
    Це забезпечує, що всі клітинки використовують одну точку відліку (0,0)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def validate_hexagonal_grid(
    hexagons: List[Dict], tolerance: float = None
) -> Tuple[bool, List[str]]:
    """Перевіряє, чи гексагональна сітка ідеально підходить без границь."""
    raise NotImplementedError("proprietary: removed from public showcase")
