# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Сервіс для перевірки та покращення якості mesh для 3D принтера
Перевіряє мінімальні розміри, товщини, watertight та інші параметри
Включає детекцію та ремонт non-manifold edges"""

import trimesh
import numpy as np
from typing import Optional, Tuple, List, Dict
import trimesh.repair

MIN_WALL_THICKNESS_MM = None
MIN_FEATURE_SIZE_MM = None
MIN_OVERHANG_ANGLE = None


def detect_nonmanifold_edges(mesh: trimesh.Trimesh) -> Tuple[int, List[int]]:
    """Детектує non-manifold edges в mesh."""
    raise NotImplementedError("proprietary: removed from public showcase")


def repair_nonmanifold(
    mesh: trimesh.Trimesh,
    aggressive: bool = True,
    verbose: bool = True,
    skip_fix_normals: bool = False,
) -> Tuple[trimesh.Trimesh, Dict[str, any]]:
    """Виправляє non-manifold edges та інші проблеми mesh."""
    raise NotImplementedError("proprietary: removed from public showcase")


def validate_mesh_for_3d_printing(
    mesh: trimesh.Trimesh, scale_factor: Optional[float] = None, model_size_mm: float = None
) -> Tuple[bool, List[str]]:
    """Перевіряє mesh на придатність для 3D принтера"""
    raise NotImplementedError("proprietary: removed from public showcase")


def improve_mesh_for_3d_printing(
    mesh: trimesh.Trimesh,
    aggressive: bool = True,
    verbose: bool = False,
    skip_fix_normals: bool = False,
) -> trimesh.Trimesh:
    """Покращує mesh для 3D принтера, включаючи ремонт non-manifold edges"""
    raise NotImplementedError("proprietary: removed from public showcase")


def check_minimum_thickness(
    mesh: trimesh.Trimesh, scale_factor: Optional[float] = None, model_size_mm: float = None
) -> Tuple[bool, float]:
    """Перевіряє мінімальну товщину mesh"""
    raise NotImplementedError("proprietary: removed from public showcase")
