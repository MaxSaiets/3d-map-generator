# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Чекпоінт PyTorch → ONNX для CPU-інференсу в проді."""

from __future__ import annotations
import argparse
import os
import time
import numpy as np
import torch
from ml.floorplan.model import NUM_CLASSES, FloorPlanUNet

HERE = None
DEFAULT_OUT = None


def export(
    ckpt: str, out_path: str = DEFAULT_OUT, size: int = None, opset: int = None, verify: bool = True
) -> str:
    raise NotImplementedError("proprietary: removed from public showcase")


def main() -> None:
    raise NotImplementedError("proprietary: removed from public showcase")
