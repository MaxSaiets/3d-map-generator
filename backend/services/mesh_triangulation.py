# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Utilities for polygon extrusion with more uniform triangulation."""

from typing import Optional
import numpy as np
import shapely
import trimesh
from shapely.geometry import Point, Polygon


def densify_polygon_boundary(poly: Polygon, max_segment_m: float = None) -> Polygon:
    raise NotImplementedError("proprietary: removed from public showcase")


def extrude_polygon_uniform(
    polygon: Polygon, height: float, densify_max_m: float = None
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def extrude_polygon_grid(
    polygon: Polygon,
    height: float,
    target_edge_len_m: float = None,
    max_grid_points: int = None,
    fast_filter: bool = False,
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def extrude_polygon_quality(
    polygon: Polygon, height: float, target_edge_len_m: float = None
) -> Optional[trimesh.Trimesh]:
    """ЯКІСНА constrained-Delaunay тріангуляція (бібліотека `triangle`, прапори
    'pq30a{area}'): ТОЧНИЙ контур (PSLG-сегменти) + рівні внутрішні точки (Steiner,
    обмеження площі) + БЕЗ слівери/голок (q30 = мін. кут 30°). Поважає дірки."""
    raise NotImplementedError("proprietary: removed from public showcase")


def refine_mesh_long_edges(
    mesh: Optional[trimesh.Trimesh], max_edge_m: float, max_vertices: int = None
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")
