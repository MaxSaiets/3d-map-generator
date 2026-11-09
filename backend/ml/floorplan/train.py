# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Тренування сегментатора планів на синтетичних даних."""

from __future__ import annotations
import argparse
import math
import os
import time
from typing import Iterator, List, Optional, Tuple
import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset
from ml.floorplan import synth
from ml.floorplan.model import NUM_CLASSES, FloorPlanUNet, SegLoss, per_class_iou

HERE = None
CKPT_DIR = None


class SynthDataset(Dataset):
    """Нескінченний потік планів. `index` слугує зерном — набір детермінований
    і відтворюваний, попри те що не існує на диску."""

    def __init__(
        self,
        size: int,
        length: int,
        seed_base: int,
        clean_ratio: float = None,
        real_ratio: float = None,
        real_split: str = None,
        val_holdout: int = None,
        fpc_ratio: float = None,
        fpc_dir: str = None,
    ):
        raise NotImplementedError("proprietary: removed from public showcase")

    def _fpc_pool(self) -> List[str]:
        raise NotImplementedError("proprietary: removed from public showcase")

    def _fpc_sample(self, rng: np.random.Generator) -> Optional[Tuple[np.ndarray, np.ndarray]]:
        """Реальний план + ручна маска, з легкою аугментацією."""
        raise NotImplementedError("proprietary: removed from public showcase")

    def _real_pool(self) -> list:
        """Ліниво (у кожному воркері окремо) — pickle на 60 МБ не варто
        серіалізувати між процесами."""
        raise NotImplementedError("proprietary: removed from public showcase")

    def __len__(self) -> int:
        raise NotImplementedError("proprietary: removed from public showcase")

    def __getitem__(self, index: int) -> Tuple[torch.Tensor, torch.Tensor]:
        raise NotImplementedError("proprietary: removed from public showcase")


def _class_weights() -> List[float]:
    """Стіни ~10% пікселів, двері/вікна <1%. Без ваг мережа впевнено вчиться
    передбачати самий лише фон."""
    raise NotImplementedError("proprietary: removed from public showcase")


def amp_is_safe(model: torch.nn.Module, device: str, batch: int, size: int) -> bool:
    """Чи можна довіряти fp16 на ЦІЙ машині при цьому батчі."""
    raise NotImplementedError("proprietary: removed from public showcase")


def evaluate(
    model: torch.nn.Module, loader: DataLoader, device: str, amp: bool
) -> Tuple[float, List[float]]:
    raise NotImplementedError("proprietary: removed from public showcase")


def train(
    steps: int = None,
    batch: int = None,
    size: int = None,
    lr: float = None,
    workers: int = None,
    eval_every: int = None,
    resume: str = None,
    out_name: str = None,
) -> str:
    raise NotImplementedError("proprietary: removed from public showcase")


def main() -> None:
    raise NotImplementedError("proprietary: removed from public showcase")
