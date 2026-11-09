# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Robust terrain solidifier - створює герметичний solid terrain mesh
ВИПРАВЛЕНО: Правильна обробка boundary, watertight bottom cap, валідація"""

import numpy as np
import trimesh
from typing import Optional, Tuple
from shapely.geometry import Polygon as ShapelyPolygon


def _sample_polygon_boundary(polygon: ShapelyPolygon, interval_m: float = None) -> np.ndarray:
    """Sample points along polygon boundary at regular intervals"""
    raise NotImplementedError("proprietary: removed from public showcase")


def _triangulate_polygon_simple(vertices_2d: np.ndarray) -> np.ndarray:
    """Проста і НАДІЙНА тріангуляція полігона
    Використовує ear clipping algorithm через shapely"""
    raise NotImplementedError("proprietary: removed from public showcase")


def _triangulate_ring_no_steiner(ring_2d: np.ndarray) -> Optional[np.ndarray]:
    """Тріангуляція НЕопуклого замкненого контуру лише по його вершинах (індекси 0..n-1)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def create_solid_terrain_robust(
    terrain_top: trimesh.Trimesh,
    zone_polygon: ShapelyPolygon,
    base_thickness: float = None,
    sampling_interval_m: float = None,
    floor_z: Optional[float] = None,
    boundary_verts_3d: Optional[np.ndarray] = None,
) -> Optional[trimesh.Trimesh]:
    """Створює ГЕРМЕТИЧНИЙ solid terrain mesh"""
    raise NotImplementedError("proprietary: removed from public showcase")
