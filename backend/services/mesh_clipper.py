# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Utilities for clipping meshes using geometric shapes."""

import numpy as np
import trimesh
from typing import Optional, List, Tuple
from shapely.geometry import Polygon


def clip_mesh_to_bbox(
    mesh: trimesh.Trimesh, bbox: Tuple[float, float, float, float], tolerance: float = None
) -> Optional[trimesh.Trimesh]:
    """Clips mesh to bbox (minx, miny, maxx, maxy) using plane slicing for exact edges."""
    raise NotImplementedError("proprietary: removed from public showcase")


def clip_mesh_to_polygon(
    mesh: trimesh.Trimesh,
    polygon_coords: List[Tuple[float, float]],
    global_center=None,
    tolerance: float = None,
) -> Optional[trimesh.Trimesh]:
    """ROBUST clipper:
    Keeps faces whose centroids are inside polygon.
    Edge precision limited by mesh resolution (lossy).
    Recommended for visual clipping, flattening logic, etc.
    NOT recommended for exact CAD operations unless mesh is dense."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _is_convex_polygon(poly) -> bool:
    """True лише для простого опуклого полігона без дірок (прямокутник, коло, шестикутник)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def clip_mesh_to_polygon_exact(mesh: trimesh.Trimesh, polygon) -> Optional[trimesh.Trimesh]:
    """Точне обрізання heightfield-поверхні по БУДЬ-ЯКОМУ полігону (неопуклий, з дірками)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def clip_mesh_to_polygon_planes(
    mesh: trimesh.Trimesh, polygon_coords: List[Tuple[float, float]], global_center=None
) -> Optional[trimesh.Trimesh]:
    """EXACT-ish clipper for terrain: clips mesh by slicing with vertical planes along polygon edges.
    This creates new vertices along the cut and removes the "sawtooth" boundary you get from
    centroid/vertex-inclusion clipping."""
    raise NotImplementedError("proprietary: removed from public showcase")


def clip_all_meshes_to_bbox(mesh_items, bbox, tolerance=None):
    raise NotImplementedError("proprietary: removed from public showcase")
