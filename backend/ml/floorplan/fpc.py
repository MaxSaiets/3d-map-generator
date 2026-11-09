# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Floor Plan CIS — РЕАЛЬНІ пострадянські плани з ручною розміткою стін."""

from __future__ import annotations
import argparse
import json
import os
from typing import Dict, Iterator, List, Optional, Tuple
import numpy as np

HERE = None
FPC_ROOT_CANDIDATES = None
COCO_TO_CLASS = None


def fpc_root(explicit: Optional[str] = None) -> Optional[str]:
    raise NotImplementedError("proprietary: removed from public showcase")


def iter_split(
    split: str = None, root: Optional[str] = None
) -> Iterator[Tuple[str, np.ndarray, np.ndarray]]:
    """Віддає (шлях, RGB, маска класів) для кожного зображення сплiту."""
    raise NotImplementedError("proprietary: removed from public showcase")


def evaluate(split: str = None, root: Optional[str] = None, limit: int = None) -> Dict[str, float]:
    """Метрики маски нашої мережі проти ручної розмітки на РЕАЛЬНИХ планах."""
    raise NotImplementedError("proprietary: removed from public showcase")


def export_pairs(split: str, out_dir: str, root: Optional[str] = None) -> int:
    """Зберігає (зображення, маска) у npz — щоб тренування не парсило COCO щоразу."""
    raise NotImplementedError("proprietary: removed from public showcase")


def main() -> None:
    raise NotImplementedError("proprietary: removed from public showcase")
