# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Спільна модель векторного плану приміщення."""

from __future__ import annotations
import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

Point = None
DEFAULT_WALL_THICKNESS_M = None
DEFAULT_BEARING_THICKNESS_M = None
DEFAULT_WALL_HEIGHT_M = None
DEFAULT_DOOR_WIDTH_M = None
DEFAULT_DOOR_HEIGHT_M = None
DEFAULT_WINDOW_WIDTH_M = None
DEFAULT_WINDOW_SILL_M = None
DEFAULT_WINDOW_HEIGHT_M = None


def _f(value: Any, fallback: float = None) -> float:
    """float() який не падає на None/''/NaN — вхід приходить із JSON фронтенда."""
    raise NotImplementedError("proprietary: removed from public showcase")


@dataclass
class Wall:
    """Відрізок стіни, заданий ЦЕНТРАЛЬНОЮ лінією та товщиною."""

    x1: float
    y1: float
    x2: float
    y2: float
    thickness_m: float = None
    bearing: bool = None
    height_m: Optional[float] = None

    @property
    def p1(self) -> Point:
        raise NotImplementedError("proprietary: removed from public showcase")

    @property
    def p2(self) -> Point:
        raise NotImplementedError("proprietary: removed from public showcase")

    @property
    def length_m(self) -> float:
        raise NotImplementedError("proprietary: removed from public showcase")

    @property
    def angle_rad(self) -> float:
        raise NotImplementedError("proprietary: removed from public showcase")

    def unit(self) -> Point:
        raise NotImplementedError("proprietary: removed from public showcase")

    def point_at(self, t: float) -> Point:
        """Точка на центральній лінії, t ∈ [0, 1]."""
        raise NotImplementedError("proprietary: removed from public showcase")

    def is_degenerate(self, min_len_m: float = None) -> bool:
        raise NotImplementedError("proprietary: removed from public showcase")

    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError("proprietary: removed from public showcase")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Wall":
        raise NotImplementedError("proprietary: removed from public showcase")


@dataclass
class Opening:
    """Отвір у стіні: двері, вікно або арка."""

    wall: int
    center_t: float
    width_m: float = None
    kind: str = None
    sill_m: float = None
    height_m: float = None

    def clamp(self, wall_len_m: float) -> "Opening":
        """Не даємо отвору вилізти за краї стіни (після правок користувача)."""
        raise NotImplementedError("proprietary: removed from public showcase")

    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError("proprietary: removed from public showcase")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Opening":
        raise NotImplementedError("proprietary: removed from public showcase")


@dataclass
class Room:
    """Кімната — лише для підписів/підлоги; на друк впливає опційно."""

    polygon: List[Point] = None
    name: str = None
    area_m2: float = None

    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError("proprietary: removed from public showcase")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Room":
        raise NotImplementedError("proprietary: removed from public showcase")


@dataclass
class PlanVector:
    """Повний векторний план у метрах — контракт між детектором, редактором і мешем."""

    walls: List[Wall] = None
    openings: List[Opening] = None
    rooms: List[Room] = None
    wall_height_m: float = None
    scale_source: str = None
    m_per_px: float = None
    image_size_px: Optional[Tuple[int, int]] = None
    confidence: float = None
    notes: List[str] = None

    def bounds(self) -> Tuple[float, float, float, float]:
        """(minx, miny, maxx, maxy) з урахуванням товщини стін."""
        raise NotImplementedError("proprietary: removed from public showcase")

    def size_m(self) -> Tuple[float, float]:
        raise NotImplementedError("proprietary: removed from public showcase")

    def total_wall_length_m(self) -> float:
        raise NotImplementedError("proprietary: removed from public showcase")

    def sanitize(self) -> "PlanVector":
        """Прибирає вироджені стіни й отвори-сироти. Викликати ПІСЛЯ from_dict:
        редактор може віддати стіну нульової довжини або отвір на видаленій стіні."""
        raise NotImplementedError("proprietary: removed from public showcase")

    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError("proprietary: removed from public showcase")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PlanVector":
        raise NotImplementedError("proprietary: removed from public showcase")

    @classmethod
    def from_pixel_dict(cls, data: Dict[str, Any], m_per_px: float) -> "PlanVector":
        """Варіант from_dict для редактора, який рахує в ПІКСЕЛЯХ зображення."""
        raise NotImplementedError("proprietary: removed from public showcase")
