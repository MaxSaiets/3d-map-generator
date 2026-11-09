# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Класична детекція стін без нейромережі."""

from __future__ import annotations
import math
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import numpy as np
from .preprocess import binarize


@dataclass
class CvDetectConfig:
    core_ratio: float = None
    min_core_radius_px: float = None
    min_component_area_px: int = None
    max_wall_fraction: float = None
    min_wall_fraction: float = None


@dataclass
class CvDetectResult:
    wall_mask: np.ndarray
    ink_mask: np.ndarray
    strategy: str
    confidence: float
    notes: List[str]


def _largest_components(mask: np.ndarray, min_area: int) -> np.ndarray:
    raise NotImplementedError("proprietary: removed from public showcase")


def _geodesic_dilate(seed: np.ndarray, ink: np.ndarray, iterations: int = None) -> np.ndarray:
    """Нарощує ядра стін всередині чорнила — так стіна відновлюється до повної
    ширини, але не «перетікає» на текст, бо той не має зв'язку з ядром."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _thick_stroke_walls(
    ink: np.ndarray, cfg: CvDetectConfig
) -> Tuple[np.ndarray, float, List[str]]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _elongation_filter(mask: np.ndarray, min_elongation: float = None) -> np.ndarray:
    """Лишає лише ВИДОВЖЕНІ компоненти — стіни, а не меблі."""
    raise NotImplementedError("proprietary: removed from public showcase")


def keep_main_structure(mask: np.ndarray) -> np.ndarray:
    """Лишає лише каркас квартири: головний замкнений контур і все ВСЕРЕДИНІ нього."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _enclosed_area(mask: np.ndarray) -> int:
    """Площа приміщень, замкнених цією маскою. Головна метрика якості детекції:
    правильна маска стін оточує кімнати, неправильна — ні."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _closed_hollow_walls(
    ink: np.ndarray, cfg: CvDetectConfig
) -> Tuple[np.ndarray, float, List[str]]:
    """План намальовано ПОРОЖНІМИ або ШТРИХОВАНИМИ стінами."""
    raise NotImplementedError("proprietary: removed from public showcase")


def detect_walls(rgb: np.ndarray, cfg: Optional[CvDetectConfig] = None) -> CvDetectResult:
    """RGB план → маска стін класичним CV."""
    raise NotImplementedError("proprietary: removed from public showcase")
