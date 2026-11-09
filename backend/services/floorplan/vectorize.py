# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Маска стін → векторний план (відрізки центральних ліній + товщини + отвори)."""

from __future__ import annotations
import math
from dataclasses import dataclass, replace
from typing import Any, Dict, List, Optional, Sequence, Tuple
import numpy as np
from .plan_model import (
    DEFAULT_DOOR_HEIGHT_M,
    DEFAULT_WINDOW_HEIGHT_M,
    DEFAULT_WINDOW_SILL_M,
    Opening,
    PlanVector,
    Wall,
)

Pt = None


@dataclass
class VectorizeConfig:
    min_wall_len_px: float = None
    min_thickness_px: float = None
    max_thickness_px: float = None
    rdp_tolerance_px: float = None
    ortho_tolerance_deg: float = None
    snap_px: float = None
    spur_factor: float = None
    min_component_px: int = None
    close_gap_px: int = None
    min_wall_fraction_of_image: float = None
    abs_min_half_thickness_px: float = None
    thin_cut_safety: float = None
    smooth_factor: float = None
    gap_min_ratio: float = None
    gap_max_ratio: float = None


_NB8 = None


def expected_min_wall_px(shape: Sequence[int], cfg: Optional[VectorizeConfig] = None) -> float:
    """Очікувана ПОВНА ширина найтоншої справжньої стіни, у пікселях аркуша."""
    raise NotImplementedError("proprietary: removed from public showcase")


def thin_component_cut_px(shape: Sequence[int], cfg: Optional[VectorizeConfig] = None) -> float:
    """Поріг півтовщини, нижче якого компонента вважається волосяною лінією."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _clean_mask(mask: np.ndarray, cfg: VectorizeConfig) -> np.ndarray:
    """Прибирає з маски все, що не є стіною: волосяні лінії й дрібні плями."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _trace_chains(skel: np.ndarray) -> List[List[Tuple[int, int]]]:
    """Скелет (0/1) → список ланцюжків пікселів (y, x)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _simplify(chain: Sequence[Tuple[int, int]], tolerance: float) -> np.ndarray:
    """Дуглас-Пекер по ланцюжку пікселів → (N,2) масив (x, y)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _apartment_bbox(
    solid: np.ndarray, min_room_px: int = None
) -> Optional[Tuple[float, float, float, float]]:
    """Габарит квартири = габарит усіх ЗАМКНЕНИХ приміщень у масці."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _drop_outside(
    segments: List[Tuple[Pt, Pt, float]], bbox: Optional[Tuple[float, float, float, float]]
) -> List[Tuple[Pt, Pt, float]]:
    """Викидає відрізки, середина яких лежить поза габаритом квартири."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _dominant_angle(segments: List[Tuple[Pt, Pt, float]]) -> float:
    """Головний напрям плану (rad, у діапазоні [-45°, 45°)), зважений довжиною."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _snap_ortho(
    segments: List[Tuple[Pt, Pt, float]], base_angle: float, tol_deg: float
) -> List[Tuple[Pt, Pt, float]]:
    """Доводить майже-осьові відрізки до точної осі, зберігаючи центр і довжину."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _snap_axis_offsets(
    segments: List[Tuple[Pt, Pt, float]], base_angle: float, tol_deg: float, cluster_px: float
) -> List[Tuple[Pt, Pt, float]]:
    """Зводить паралельні стіни на СПІЛЬНУ пряму."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _apply_offset_group(
    segments: List[Tuple[Pt, Pt, float]],
    group: List[int],
    offsets: Dict[int, float],
    base_angle: float,
) -> None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _merge_parallel_duplicates(
    segments: List[Tuple[Pt, Pt, float]], snap: float
) -> List[Tuple[Pt, Pt, float]]:
    """Зливає ПАРАЛЕЛЬНІ ДУБЛІКАТИ однієї стіни."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _merge_collinear(
    segments: List[Tuple[Pt, Pt, float]], snap: float
) -> List[Tuple[Pt, Pt, float]]:
    """Зливає відрізки, що лежать на одній лінії й майже торкаються."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _bridge_openings(
    segments: List[Tuple[Pt, Pt, float]], cfg: VectorizeConfig
) -> Tuple[List[Tuple[Pt, Pt, float]], List[Tuple[Pt, float]]]:
    """Зшиває колінеарні «пеньки» стіни через проріз і повертає самі прорізи."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _openings_from_points(
    segments: List[Tuple[Pt, Pt, float]], records: List[Tuple[Pt, float]], kind: str
) -> List[Opening]:
    """Прив'язує знайдені прорізи (точка + ширина) до фінальних відрізків стін."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _segments_touch(a: Tuple[Pt, Pt, float], b: Tuple[Pt, Pt, float], tol: float) -> bool:
    """Чи стикаються два відрізки (кінцями або перетином)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _ray_hit(
    origin: Pt, direction: Pt, target: Tuple[Pt, Pt, float], max_distance: float
) -> Optional[float]:
    """Відстань від origin уздовж direction до перетину з відрізком target."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _extend_dangling_ends(
    segments: List[Tuple[Pt, Pt, float]], touch_tol: float
) -> List[Tuple[Pt, Pt, float]]:
    """Продовжує «висячі» кінці стін до перетину з іншою стіною."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _keep_largest_network(
    segments: List[Tuple[Pt, Pt, float]], tol: float
) -> List[Tuple[Pt, Pt, float]]:
    """Лишає найбільшу ЗВ'ЯЗНУ мережу стін."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _quantize_thickness(
    segments: List[Tuple[Pt, Pt, float]], rel_gap: float = None
) -> List[Tuple[Pt, Pt, float]]:
    """Зводить товщини до кількох типів стін (несуча / перегородка / ...)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _heal_junctions(
    segments: List[Tuple[Pt, Pt, float]], snap: float
) -> List[Tuple[Pt, Pt, float]]:
    """Кластеризує близькі кінці й дотягує «висячі» кінці до сусідніх стін."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _assign_openings(
    segments: List[Tuple[Pt, Pt, float]],
    mask: Optional[np.ndarray],
    kind: str,
    cfg: VectorizeConfig,
) -> List[Opening]:
    """Компоненти маски дверей/вікон → Opening, прив'язані до найближчої стіни."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _openings_from_gaps(
    segments: List[Tuple[Pt, Pt, float]], wall_mask: np.ndarray, cfg: VectorizeConfig
) -> List[Opening]:
    """Резервний спосіб без нейромережі: розрив у суцільній стіні = проріз."""
    raise NotImplementedError("proprietary: removed from public showcase")


def masks_to_plan(
    wall_mask: np.ndarray,
    door_mask: Optional[np.ndarray] = None,
    window_mask: Optional[np.ndarray] = None,
    *,
    cfg: Optional[VectorizeConfig] = None,
    m_per_px: float = None,
    confidence: float = None,
) -> PlanVector:
    """Маски → PlanVector у ПІКСЕЛЯХ вхідного зображення."""
    raise NotImplementedError("proprietary: removed from public showcase")
