# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Підготовка вхідного зображення: PDF/фото/скан → чистий растр для детектора."""

from __future__ import annotations
import io
import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple
import numpy as np

MAX_SIDE_PX = None
MIN_SIDE_PX = None
PDF_RENDER_DPI = None


class PreprocessError(ValueError):
    """Вхідний файл не читається як зображення плану."""


@dataclass
class PreparedImage:
    rgb: np.ndarray
    original_rgb: np.ndarray
    warp_matrix: Optional[np.ndarray] = None
    scale_factor: float = None
    source: str = None
    notes: List[str] = None
    vector_paths: Optional[List[Dict[str, Any]]] = None

    @property
    def size(self) -> Tuple[int, int]:
        raise NotImplementedError("proprietary: removed from public showcase")


def _is_pdf(data: bytes) -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


def load_pdf_page(
    data: bytes, page: int = None, dpi: int = PDF_RENDER_DPI
) -> Tuple[np.ndarray, Optional[List[Dict[str, Any]]]]:
    """PDF → растр сторінки + (якщо є) векторні шляхи."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _pdf_vector_paths(
    data: bytes, index: int, scale: float, page_pts: Tuple[float, float]
) -> Optional[List[Dict[str, Any]]]:
    """Лінії/прямокутники сторінки через pdfplumber (MIT), у ПІКСЕЛЯХ растру."""
    raise NotImplementedError("proprietary: removed from public showcase")


def load_image(data: bytes) -> Tuple[np.ndarray, str, Optional[List[Dict[str, Any]]]]:
    """bytes → (RGB uint8, джерело, векторні шляхи PDF або None)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _order_quad(pts: np.ndarray) -> np.ndarray:
    """4 точки → порядок [top-left, top-right, bottom-right, bottom-left]."""
    raise NotImplementedError("proprietary: removed from public showcase")


def find_page_quad(rgb: np.ndarray, min_area_ratio: float = None) -> Optional[np.ndarray]:
    """Шукає чотирикутник аркуша на фото. None — якщо це вже плоский скан."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _quad_perspective(quad: np.ndarray) -> float:
    """Наскільки чотирикутник відхиляється від осьового прямокутника (0..1)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def dewarp_page(rgb: np.ndarray, quad: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Перспективна корекція за чотирикутником аркуша."""
    raise NotImplementedError("proprietary: removed from public showcase")


def estimate_skew_deg(gray: np.ndarray, limit_deg: float = None, step: float = None) -> float:
    """Кут перекосу за максимумом «осьової впорядкованості» темних пікселів."""
    raise NotImplementedError("proprietary: removed from public showcase")


def rotate_image(rgb: np.ndarray, angle_deg: float) -> Tuple[np.ndarray, np.ndarray]:
    """Поворот навколо центру з розширенням полотна (нічого не обрізаємо)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def normalize_illumination(rgb: np.ndarray) -> np.ndarray:
    """Прибирає тінь від руки/лампи: ділення на сильно розмите тло."""
    raise NotImplementedError("proprietary: removed from public showcase")


def prepare(
    data: bytes,
    *,
    dewarp: bool = True,
    deskew: bool = True,
    normalize: bool = True,
    max_side: int = MAX_SIDE_PX,
) -> PreparedImage:
    """Головний вхід: байти файлу → PreparedImage, готовий для детектора."""
    raise NotImplementedError("proprietary: removed from public showcase")


def binarize(rgb: np.ndarray, block: int = None, offset: int = None) -> np.ndarray:
    """Адаптивна бінаризація → uint8 {0,1}, 1 = «чорнило»."""
    raise NotImplementedError("proprietary: removed from public showcase")
