# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Валідація доріг та пазів для 3D друку.
Виводить точні розміри після генерації моделі: ширина доріг, пазів, перевірка сумісності."""

from typing import Optional, Any
import numpy as np

MIN_PRINTABLE_WIDTH_MM = None


def _estimate_road_widths_from_mesh(road_mesh, scale_factor: float) -> dict:
    """Оцінка ширини доріг з mesh (bounding box та апроксимація по вершинах)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _estimate_groove_from_polygons(road_polygons, scale_factor: float) -> dict:
    """Оцінка пазів з полігонів (road_cut_mask = roads.buffer(clearance) — вже з зазором)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def print_road_groove_validation_report(
    road_mesh=None,
    terrain_mesh=None,
    road_polygons=None,
    scale_factor: Optional[float] = None,
    groove_clearance_mm: float = None,
    zone_prefix: str = None,
) -> None:
    """Виводить звіт валідації доріг та пазів після генерації моделі.
    Перевіряє ширини, зазори та сумісність для 3D друку."""
    raise NotImplementedError("proprietary: removed from public showcase")
