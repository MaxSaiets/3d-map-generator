# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""U-Net із енкодером ResNet-18 для сегментації планів."""

from __future__ import annotations
from typing import List, Optional, Tuple
import torch
import torch.nn as nn
import torch.nn.functional as F

NUM_CLASSES = None
IMAGENET_MEAN = None
IMAGENET_STD = None


class ConvBlock(nn.Module):
    def __init__(self, in_ch: int, out_ch: int):
        raise NotImplementedError("proprietary: removed from public showcase")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError("proprietary: removed from public showcase")


class UpBlock(nn.Module):
    def __init__(self, in_ch: int, skip_ch: int, out_ch: int):
        raise NotImplementedError("proprietary: removed from public showcase")

    def forward(self, x: torch.Tensor, skip: Optional[torch.Tensor]) -> torch.Tensor:
        raise NotImplementedError("proprietary: removed from public showcase")


class FloorPlanUNet(nn.Module):
    """ResNet-18 encoder + U-Net decoder → логіти (B, 4, H, W)."""

    def __init__(self, num_classes: int = NUM_CLASSES, pretrained: bool = True):
        raise NotImplementedError("proprietary: removed from public showcase")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError("proprietary: removed from public showcase")


class NormalizedModel(nn.Module):
    """Обгортка для ONNX: приймає uint8-подібний float 0..1 і сама нормалізує."""

    def __init__(self, model: nn.Module):
        raise NotImplementedError("proprietary: removed from public showcase")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError("proprietary: removed from public showcase")


def dice_loss(logits: torch.Tensor, target: torch.Tensor, eps: float = None) -> torch.Tensor:
    """М'який Dice по класах. Потрібен поряд із CE, бо стіни займають ~10%
    пікселів, а двері/вікна — менше 1%: чиста крос-ентропія вчиться передбачати
    фон і формально має гарний loss."""
    raise NotImplementedError("proprietary: removed from public showcase")


class SegLoss(nn.Module):
    def __init__(self, class_weights: Optional[List[float]] = None, dice_weight: float = None):
        raise NotImplementedError("proprietary: removed from public showcase")

    def forward(self, logits: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError("proprietary: removed from public showcase")


@torch.no_grad()
def per_class_iou(
    logits: torch.Tensor, target: torch.Tensor, num_classes: int = NUM_CLASSES
) -> List[float]:
    raise NotImplementedError("proprietary: removed from public showcase")
