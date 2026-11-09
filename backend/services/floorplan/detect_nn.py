# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Інференс сегментатора планів на onnxruntime (CPU)."""

from __future__ import annotations
import os
import threading
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import numpy as np

CLASS_BG, CLASS_WALL, CLASS_DOOR, CLASS_WINDOW = None
DEFAULT_INPUT_SIZE = None
_LOCK = None
_SESSION: Dict[str, object] = None


def model_path() -> Optional[str]:
    """Шлях до ваг: env FLOORPLAN_ONNX або backend/models/floorplan_seg.onnx."""
    raise NotImplementedError("proprietary: removed from public showcase")


def is_available() -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def _session():
    raise NotImplementedError("proprietary: removed from public showcase")


@dataclass
class NnDetectResult:
    wall_mask: np.ndarray
    door_mask: np.ndarray
    window_mask: np.ndarray
    confidence: float
    notes: List[str]


def _letterbox(rgb: np.ndarray, size: int) -> Tuple[np.ndarray, float, int, int]:
    """Вписує зображення у квадрат size×size БЕЗ спотворення пропорцій."""
    raise NotImplementedError("proprietary: removed from public showcase")


def choose_input_size(rgb: np.ndarray, floor: int = None, ceiling: int = None) -> int:
    """Роздільність інференсу під конкретне зображення."""
    raise NotImplementedError("proprietary: removed from public showcase")


def detect(rgb: np.ndarray, input_size: Optional[int] = None) -> Optional[NnDetectResult]:
    """RGB-план → маски стін/дверей/вікон у РОЗМІРІ ВХІДНОГО зображення."""
    raise NotImplementedError("proprietary: removed from public showcase")
