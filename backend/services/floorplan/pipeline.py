# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Оркестратор сервісу «макет квартири»: файл → план → друкована модель."""

from __future__ import annotations
import base64
import io
import os
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple
import numpy as np
from .builder import BuildOptions, BuildResult, PlanBuildError, build_plan_mesh
from .plan_model import PlanVector
from .preprocess import PreparedImage, PreprocessError, prepare
from .scale import ScaleResult, interior_area_px2, resolve_scale
from .vectorize import VectorizeConfig, masks_to_plan

MAX_UPLOAD_BYTES = None
PREVIEW_MAX_SIDE = None
PREVIEW_JPEG_QUALITY = None
MIN_AREA_M2 = None
MAX_AREA_M2 = None
PARTITION_RANGE_M = None
BEARING_RANGE_M = None


class FloorplanError(ValueError):
    """Помилка, яку можна показати користувачу як є."""


@dataclass
class AnalyzeResult:
    plan: PlanVector
    scale: ScaleResult
    preview_data_url: str
    image_size_px: Tuple[int, int]
    detector: str
    confidence: float
    notes: List[str] = None
    warnings: List[str] = None
    timings_ms: Dict[str, int] = None

    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError("proprietary: removed from public showcase")


def _to_preview_data_url(rgb: np.ndarray) -> Tuple[str, Tuple[int, int]]:
    """Вирівняне зображення → data-URL для фронтенда."""
    raise NotImplementedError("proprietary: removed from public showcase")


def decode_data_url(value: str) -> bytes:
    """'data:image/png;base64,...' або чистий base64 → байти."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _downscale_masks(
    wall: np.ndarray, door: Optional[np.ndarray], window: Optional[np.ndarray], max_side: int
):
    """Зменшує маски до робочої роздільності (INTER_NEAREST — класи не змішуємо)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _scale_sanity(plan_px: PlanVector, m_per_px: float) -> List[str]:
    """Фізична перевірка масштабу: товщини стін і площа мусять бути з нашого світу."""
    raise NotImplementedError("proprietary: removed from public showcase")


def analyze(
    data: bytes,
    *,
    reference_px: Optional[float] = None,
    reference_m: Optional[float] = None,
    use_ocr: bool = True,
    use_nn: bool = True,
) -> AnalyzeResult:
    """Файл плану → векторний план у пікселях + гіпотези масштабу."""
    raise NotImplementedError("proprietary: removed from public showcase")


def build(
    plan_dict: Dict[str, Any],
    m_per_px: float,
    options: Optional[BuildOptions] = None,
    progress: Optional[Callable[[int, str], None]] = None,
) -> BuildResult:
    """Відредагований користувачем план (у пікселях) → друкований меш."""
    raise NotImplementedError("proprietary: removed from public showcase")


def export_outputs(result: BuildResult, out_dir: str, basename: str) -> Dict[str, str]:
    """Меш → 3MF/STL/GLB поруч із рештою моделей проєкту."""
    raise NotImplementedError("proprietary: removed from public showcase")
