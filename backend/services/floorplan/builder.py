# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""PlanVector → друкований 3D-макет приміщення."""

from __future__ import annotations
import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple
import numpy as np
import trimesh
from shapely import affinity
from shapely.geometry import LineString, MultiPolygon, Polygon, box
from shapely.ops import unary_union
from .plan_model import Opening, PlanVector, Wall

NOZZLE_MM = None
MIN_WALL_MM = None
ABS_MIN_WALL_MM = None
MIN_BASE_MM = None
DEFAULT_BASE_MM = None
DEFAULT_MODEL_MM = None
MAQUETTE_WALL_HEIGHT_MM = None
WELD_MM = None


@dataclass
class BuildOptions:
    """Усе, що впливає на друковану геометрію."""

    model_size_mm: float = None
    scale_denominator: Optional[float] = None
    wall_height_mm: Optional[float] = None
    wall_height_mode: str = None
    maquette_wall_height_mm: float = None
    min_wall_mm: float = None
    base_plate: bool = None
    base_thickness_mm: float = None
    base_margin_mm: float = None
    cut_doors: bool = None
    cut_windows: bool = None
    door_threshold_mm: float = None
    max_model_mm: float = None
    min_model_mm: float = None

    def normalized(self) -> "BuildOptions":
        raise NotImplementedError("proprietary: removed from public showcase")


@dataclass
class BuildResult:
    mesh: trimesh.Trimesh
    parts: Dict[str, trimesh.Trimesh] = None
    stats: Dict[str, Any] = None
    warnings: List[str] = None


class PlanBuildError(RuntimeError):
    """Геометрію побудувати неможливо (порожній/зіпсований план)."""


def _as_polygons(geom) -> List[Polygon]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _clean(geom, grid: float = None):
    """Нормалізує геометрію: валідність + прив'язка координат до сітки."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _fill_holes(geom) -> List[Polygon]:
    """Полігони без внутрішніх дірок — підошва будівлі (стіни + кімнати всередині)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _close_footprint(wall_area, scale: float, bbox_area: float):
    """Зімкнути підошву квартири через ПРОРІЗИ у зовнішній стіні."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _extrude_one(poly: Polygon, height: float) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _extrude(geom, height: float, z0: float = None) -> Optional[trimesh.Trimesh]:
    """Екструзія shapely-геометрії у меш. Кожен полігон окремо → потім union."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _boolean(op: str, meshes: Sequence[trimesh.Trimesh]) -> Optional[trimesh.Trimesh]:
    """union/difference через manifold3d з м'яким fallback на конкатенацію."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _usable_solid(mesh: Optional[trimesh.Trimesh]) -> bool:
    """Чи можна віддавати цей меш далі: замкнений, з додатним обʼємом."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _wall_strip(wall: Wall, thickness_mm: float, scale: float) -> Optional[Polygon]:
    """Смуга стіни у мм: buffer центральної лінії з КВАДРАТНИМИ торцями."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _opening_box(
    wall: Wall, op: Opening, thickness_mm: float, scale: float, overcut_mm: float
) -> Optional[Polygon]:
    """Прямокутник прорізу в плані (мм), трохи довший за товщину стіни."""
    raise NotImplementedError("proprietary: removed from public showcase")


def build_plan_mesh(
    plan: PlanVector, options: Optional[BuildOptions] = None, progress=None
) -> BuildResult:
    """Векторний план (метри) → друкований меш (міліметри, Z вгору)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _filament_estimate_g(
    mesh: trimesh.Trimesh, shell_mm: float = None, infill: float = None, density: float = None
) -> Optional[float]:
    """Оцінка ваги PLA з урахуванням того, що слайсер друкує оболонку + заповнення."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _repair(mesh: trimesh.Trimesh) -> trimesh.Trimesh:
    """Ремонт ЛИШЕ якщо меш справді зламаний."""
    raise NotImplementedError("proprietary: removed from public showcase")
