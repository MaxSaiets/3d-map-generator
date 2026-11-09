# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Визначення масштабу: скільки метрів в одному пікселі плану."""

from __future__ import annotations
import math
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple
import numpy as np
from .plan_model import PlanVector

TYPICAL_DOOR_M = None
TYPICAL_APARTMENT_SPAN_M = None
MIN_PLAN_SPAN_M = None
MAX_PLAN_SPAN_M = None


@dataclass
class ScaleCandidate:
    m_per_px: float
    source: str
    confidence: float
    detail: str = None

    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError("proprietary: removed from public showcase")


@dataclass
class ScaleResult:
    chosen: ScaleCandidate
    candidates: List[ScaleCandidate] = None
    ocr_texts: List[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError("proprietary: removed from public showcase")


def from_reference(pixel_length: float, real_length_m: float) -> Optional[ScaleCandidate]:
    """Користувач: «оця лінія — 5.2 м». Найточніше, що взагалі можливо."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _wall_bbox_area_px2(plan_px: PlanVector) -> float:
    """Площа габаритного прямокутника мережі стін — верхня межа для площі
    приміщень і знаменник у перевірці правдоподібності."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _hull_area_px2(union: Any) -> float:
    """Запасний спосіб: ОПУКЛА ОБОЛОНКА мережі стін мінус самі стіни."""
    raise NotImplementedError("proprietary: removed from public showcase")


def interior_area_px2(plan_px: PlanVector) -> float:
    """Площа ПРИМІЩЕНЬ (без стін) у пікселях²."""
    raise NotImplementedError("proprietary: removed from public showcase")


def from_area(plan_px: PlanVector, area_m2: float) -> Optional[ScaleCandidate]:
    """Користувач вписав загальну площу → масштаб = √(площа / площа в пікселях)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def from_doors(plan_px: PlanVector, typical_m: float = TYPICAL_DOOR_M) -> Optional[ScaleCandidate]:
    """Медіанна ширина знайдених дверей ≈ 0.85 м."""
    raise NotImplementedError("proprietary: removed from public showcase")


def from_assumed(plan_px: PlanVector) -> ScaleCandidate:
    """Останній варіант: типова квартира. Показуємо явно, що це припущення."""
    raise NotImplementedError("proprietary: removed from public showcase")


def from_pdf_note(
    page_pts: Sequence[float], image_px: Sequence[int], denominator: float
) -> Optional[ScaleCandidate]:
    """PDF: сторінка в пунктах + «М 1:100» → точний масштаб без жодного CV."""
    raise NotImplementedError("proprietary: removed from public showcase")


_SCALE_NOTE_RE = None
_NUM_RE = None


def _parse_dimension(text: str) -> Optional[float]:
    """Рядок із плану → довжина в МЕТРАХ, або None."""
    raise NotImplementedError("proprietary: removed from public showcase")


def run_ocr(rgb: np.ndarray) -> List[Dict[str, Any]]:
    """RapidOCR (ONNXRuntime, ~46 МБ ваг, CPU) → [{text, box, score, value_m}]."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _box_rect(item: Dict[str, Any]) -> Optional[Tuple[float, float, float, float]]:
    raise NotImplementedError("proprietary: removed from public showcase")


def merge_split_numbers(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Склеює розмір, який OCR розірвав по пробілу-роздільнику тисяч."""
    raise NotImplementedError("proprietary: removed from public showcase")


_OCR_SINGLETON: Dict[str, Any] = None


def _ocr_engine(cls):
    """Один інстанс на процес: ініціалізація тягне ваги з диска ~1 с."""
    raise NotImplementedError("proprietary: removed from public showcase")


def scale_note_from_ocr(ocr_items: Sequence[Dict[str, Any]]) -> Optional[float]:
    """Шукає напис «М 1:100» / «1:50» у розпізнаному тексті."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _candidate_spans(
    plan_px: PlanVector,
) -> Dict[str, List[Tuple[float, float, float, float, float]]]:
    """Пари стін по кожній осі: {"x": [(ліва, права, У_СВІТЛІ)], "y": [...]}."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _text_axis_center(item: Dict[str, Any], to_plan: float) -> Optional[Tuple[str, float]]:
    """Напис розміру → (вісь, координата центру) у пікселях ПЛАНУ."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _candidate_distances_px(plan_px: PlanVector) -> List[float]:
    """Реальні відстані на плані, до яких можуть належати розмірні числа:
    між паралельними стінами + загальні габарити."""
    raise NotImplementedError("proprietary: removed from public showcase")


def from_ocr(
    ocr_items: Sequence[Dict[str, Any]], plan_px: PlanVector, ocr_to_plan: float = None
) -> Optional[ScaleCandidate]:
    """Голосування: який масштаб робить найбільше розмірних чисел правдою?"""
    raise NotImplementedError("proprietary: removed from public showcase")


def resolve_scale(
    plan_px: PlanVector,
    *,
    rgb: Optional[np.ndarray] = None,
    reference_px: Optional[float] = None,
    reference_m: Optional[float] = None,
    pdf_page_pts: Optional[Sequence[float]] = None,
    image_px: Optional[Sequence[int]] = None,
    use_ocr: bool = True,
) -> ScaleResult:
    """Збирає всі гіпотези масштабу й вибирає найвпевненішу."""
    raise NotImplementedError("proprietary: removed from public showcase")
