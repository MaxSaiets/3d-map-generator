# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""CDT-based CLEAN groove-wall terrain construction for RELIEF maps."""

from __future__ import annotations
import json
import math
import os
import subprocess
import sys
import tempfile
from typing import Callable, Optional
import numpy as np

try:
    import trimesh
    from shapely.geometry import LineString, MultiPolygon, Point, Polygon
    from shapely.ops import unary_union
except Exception:
    trimesh = None


def _worker(spec_path: str, out_path: str) -> None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _run_triangle(vertices, segments, holes, triangle_args, tag, work_dir):
    raise NotImplementedError("proprietary: removed from public showcase")


def _poly_to_pslg(poly):
    raise NotImplementedError("proprietary: removed from public showcase")


def _points_pslg(points2d, closed_loops):
    raise NotImplementedError("proprietary: removed from public showcase")


def _ring_chains(poly):
    raise NotImplementedError("proprietary: removed from public showcase")


def _densify_ring(coords, max_seg):
    raise NotImplementedError("proprietary: removed from public showcase")


def _densify_polygon(poly, max_seg):
    raise NotImplementedError("proprietary: removed from public showcase")


_BLENDER_FILL = None


def _blender_fill_watertight(mesh, work_dir):
    """Закриває СТРУКТУРНІ відкриті ребра швів (кап-стінка) через Blender
    edge_face_add — надійніше за trimesh fill_holes на складній road-топології.
    Стінки лишаються чисті (філи — лише пласкі грані на дні/підлозі). Без Blender
    → повертає як є (на проді Blender завжди є)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _rings_pslg(rings, snap=None):
    """Manual PSLG from a list of closed rings [[(x,y),...],...] → (pts, segs).
    РОБАСТНО для `triangle` (інакше «invalid geometry on input» на реальних масках):
    snap координат до сітки + ГЛОБАЛЬНИЙ dedup вершин (ті самі координати між
    кільцями = ОДИН індекс, не дубль) + викид вироджених (нульова довжина) сегментів.
    Спільні вершини між викликами зберігаються детерміновано → шви закриваються."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _boundary_loops(mesh):
    raise NotImplementedError("proprietary: removed from public showcase")


def build_cdt_grooved_terrain(
    zone_polygon,
    inlay_mask,
    height_fn: Callable[[np.ndarray, np.ndarray], np.ndarray],
    *,
    slab_z: float,
    floor_z: float,
    seg_len: float = None,
    tri_area: float = None,
    follow_depth_m: Optional[float] = None,
):
    """Будує ГЕРМЕТИЧНИЙ рельєф-солід із ЧИСТИМИ стінками слотів інлеїв."""
    raise NotImplementedError("proprietary: removed from public showcase")
