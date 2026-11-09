# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Рендер РЕАЛЬНОЇ геометрії планів у наших кресленнєвих стилях."""

from __future__ import annotations
import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple
import numpy as np
from PIL import Image, ImageDraw
from ml.floorplan.synth import (
    CLASS_DOOR,
    CLASS_WALL,
    CLASS_WINDOW,
    RenderStyle,
    _Canvas,
    _draw_hatch,
    _draw_room_badges,
    _draw_title_block,
    _font,
    _rand_style,
    _ROOM_SETS,
)

Point = None


@dataclass
class RealLayout:
    """Одна квартира/поверх у МЕТРАХ. Полігони — списки точок (x, y)."""

    walls: List[List[Point]] = None
    doors: List[List[Point]] = None
    windows: List[List[Point]] = None
    rooms: List[List[Point]] = None
    room_names: List[str] = None
    source: str = None

    def bounds(self) -> Tuple[float, float, float, float]:
        raise NotImplementedError("proprietary: removed from public showcase")

    def size_m(self) -> Tuple[float, float]:
        raise NotImplementedError("proprietary: removed from public showcase")

    def normalized(self) -> "RealLayout":
        """Зсуває план у початок координат — далі рендер рахує від (0, 0)."""
        raise NotImplementedError("proprietary: removed from public showcase")


def polygon_to_wall(polygon: Sequence[Point]) -> Optional[Tuple[Point, Point, float]]:
    """Полігон стіни → (кінець, кінець, товщина) у метрах."""
    raise NotImplementedError("proprietary: removed from public showcase")


def layout_to_plan(layout: RealLayout):
    """RealLayout → еталонний PlanVector у метрах (для метрик і тестів)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _polygon_area(polygon: Sequence[Point]) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _poly_px(canvas: _Canvas, polygon: Sequence[Point]) -> List[Tuple[float, float]]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _bbox_px(points: Sequence[Tuple[float, float]]) -> Tuple[float, float, float, float]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _draw_dim_chain_free(
    canvas: _Canvas,
    rng: np.random.Generator,
    values: Sequence[float],
    horizontal: bool,
    offset_px: float,
    units: str,
) -> None:
    """Розмірний ланцюжок уздовж габариту (для довільної геометрії)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def render_layout(
    layout: RealLayout, rng: np.random.Generator, style: Optional[RenderStyle] = None
) -> Tuple[np.ndarray, np.ndarray]:
    """RealLayout → (grayscale uint8, маска класів uint8) у наших стилях."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _thin_out(values: Sequence[float], min_gap: float) -> List[float]:
    """Прорідження координат — інакше розмірний ланцюжок перетворюється на кашу."""
    raise NotImplementedError("proprietary: removed from public showcase")
