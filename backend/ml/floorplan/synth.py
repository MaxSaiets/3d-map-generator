# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Процедурний генератор технічних планів квартир + піксель-точні маски."""

from __future__ import annotations
import math
import os
import random
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Tuple
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

CLASS_BG = None
CLASS_WALL = None
CLASS_DOOR = None
CLASS_WINDOW = None
NUM_CLASSES = None
CLASS_NAMES = None
Rect = None


def _font_candidates() -> List[str]:
    raise NotImplementedError("proprietary: removed from public showcase")


_FONT_PATHS = None
_FONT_CACHE: Dict[Tuple[str, int], ImageFont.FreeTypeFont] = None


def _font(size: int, rng: Optional[np.random.Generator] = None) -> ImageFont.ImageFont:
    raise NotImplementedError("proprietary: removed from public showcase")


@dataclass
class Seg:
    """Осе-паралельний відрізок центральної лінії стіни."""

    horizontal: bool
    const: float
    a: float
    b: float
    thickness: float = None
    bearing: bool = None
    exterior: bool = None

    def __post_init__(self) -> None:
        raise NotImplementedError("proprietary: removed from public showcase")

    @property
    def length(self) -> float:
        raise NotImplementedError("proprietary: removed from public showcase")

    def endpoints(self) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        raise NotImplementedError("proprietary: removed from public showcase")

    def subtract(self, lo: float, hi: float) -> List["Seg"]:
        """Відняти інтервал [lo, hi] — використовується при вирізанні кута."""
        raise NotImplementedError("proprietary: removed from public showcase")


@dataclass
class OpeningSpec:
    """Отвір у координатах метрів (осе-паралельний, як і стіни)."""

    seg_index: int
    center: float
    width: float
    kind: str
    swing_dir: int = None


@dataclass
class LayoutSpec:
    """Готова розкладка: кімнати, стіни, отвори — все в метрах."""

    width_m: float
    height_m: float
    rooms: List[Rect] = None
    room_names: List[str] = None
    segs: List[Seg] = None
    openings: List[OpeningSpec] = None


_ROOM_NAMES_UK = None
_ROOM_NAMES_RU = None
_ROOM_NAMES_EN = None
_ROOM_NAMES_PL = None
_ROOM_SETS = None


def _bsp(
    rng: np.random.Generator,
    rect: Rect,
    depth: int,
    min_side: float,
    min_area: float,
    rooms: List[Rect],
    cuts: List[Tuple[int, Seg]],
) -> None:
    """Рекурсивне бінарне розбиття прямокутника на кімнати."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _shared_edge(a: Rect, b: Rect, tol: float = None) -> Optional[Tuple[bool, float, float, float]]:
    """Спільна межа двох кімнат → (horizontal, const, lo, hi) або None."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _merge_collinear(segs: List[Seg]) -> List[Seg]:
    """Зливає колінеарні відрізки, що перекриваються/торкаються (одна товщина)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def generate_layout(rng: np.random.Generator) -> LayoutSpec:
    """Створює правдоподібну розкладку квартири/будинку."""
    raise NotImplementedError("proprietary: removed from public showcase")


@dataclass
class RenderStyle:
    px_per_m: float = None
    margin_px: int = None
    wall_fill: int = None
    line_width: int = None
    draw_dims: bool = None
    draw_labels: bool = None
    draw_areas: bool = None
    draw_hatch: bool = None
    draw_furniture: bool = None
    draw_frame: bool = None
    hollow_walls: bool = None
    dim_units: str = None
    draw_axes: bool = None
    draw_title_block: bool = None
    draw_room_badges: bool = None
    hatch_angle_alt: bool = None
    wall_gray: int = None
    marketing: bool = None
    paper_tone: int = None


def _rand_style(rng: np.random.Generator) -> RenderStyle:
    raise NotImplementedError("proprietary: removed from public showcase")


class _Canvas:
    """Малює одночасно у видиме зображення і в маску класів (без згладжування)."""

    def __init__(self, w: int, h: int, style: RenderStyle, ox: float, oy: float):
        raise NotImplementedError("proprietary: removed from public showcase")

    def px(self, x: float, y: float) -> Tuple[float, float]:
        raise NotImplementedError("proprietary: removed from public showcase")

    def wall_rect(self, seg: Seg) -> Tuple[float, float, float, float]:
        raise NotImplementedError("proprietary: removed from public showcase")

    def opening_rect(self, seg: Seg, op: OpeningSpec) -> Tuple[float, float, float, float]:
        raise NotImplementedError("proprietary: removed from public showcase")


def _draw_hatch(
    canvas: _Canvas,
    box: Tuple[float, float, float, float],
    step: int,
    shade: int,
    flip: bool = False,
) -> None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _draw_axes(canvas: _Canvas, rng: np.random.Generator, spec: "LayoutSpec", margin: int) -> None:
    """Розбивочні осі з кружечками — обов'язковий елемент будівельних креслень."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _draw_title_block(canvas: _Canvas, rng: np.random.Generator) -> None:
    """Штамп у куті: рамка з рядками тексту. Товсті лінії рамки — ще одне
    джерело хибних «стін», якщо модель такого не бачила."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _draw_room_badges(canvas: _Canvas, rng: np.random.Generator, spec: "LayoutSpec") -> None:
    """Номер кімнати в кружечку — типово для БТІ."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _fmt_dim(value_m: float, units: str) -> str:
    raise NotImplementedError("proprietary: removed from public showcase")


def _draw_dim_chain(
    canvas: _Canvas,
    rng: np.random.Generator,
    positions: Sequence[float],
    const_m: float,
    horizontal: bool,
    offset_px: float,
    units: str,
) -> None:
    """Розмірний ланцюжок з засічками й числами — головна ознака техплану."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _draw_furniture(canvas: _Canvas, rng: np.random.Generator, room: Rect) -> None:
    """Тонкі меблі/сантехніка — головний джерело хибних спрацювань детектора,
    тому модель мусить бачити їх під час навчання і вчитися ігнорувати."""
    raise NotImplementedError("proprietary: removed from public showcase")


def render_layout(
    spec: LayoutSpec, rng: np.random.Generator, style: Optional[RenderStyle] = None
) -> Tuple[np.ndarray, np.ndarray]:
    """Малює план → (grayscale uint8 HxW, mask uint8 HxW з класами)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def degrade(
    img: np.ndarray, mask: np.ndarray, rng: np.random.Generator, out_size: int = None
) -> Tuple[np.ndarray, np.ndarray]:
    """Чистий рендер → правдоподібне фото сторінки. Маска трансформується так само."""
    raise NotImplementedError("proprietary: removed from public showcase")


def finalize(
    img: np.ndarray,
    mask: np.ndarray,
    rng: np.random.Generator,
    out_size: int = None,
    clean: bool = False,
) -> Tuple[np.ndarray, np.ndarray]:
    """Чистий рендер → навчальний приклад фіксованого розміру."""
    raise NotImplementedError("proprietary: removed from public showcase")


def make_sample(
    seed: int, out_size: int = None, clean: bool = False
) -> Tuple[np.ndarray, np.ndarray, LayoutSpec]:
    """Один навчальний приклад: (RGB out_size², маска out_size², розкладка)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def layout_to_plan(spec: LayoutSpec):
    """LayoutSpec → PlanVector: ідеальна «правильна відповідь» у метрах."""
    raise NotImplementedError("proprietary: removed from public showcase")
