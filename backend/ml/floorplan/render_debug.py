# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Dev-утиліта: рендер мешу в PNG без GPU/вікна (matplotlib Poly3DCollection)."""

from __future__ import annotations
import math
import os
from typing import Optional, Sequence
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import trimesh
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def render_mesh(
    mesh: trimesh.Trimesh,
    out_path: str,
    elev: float = None,
    azim: float = None,
    title: str = None,
    size: int = None,
) -> str:
    raise NotImplementedError("proprietary: removed from public showcase")


def render_views(
    mesh: trimesh.Trimesh,
    out_dir: str,
    stem: str,
    views: Optional[Sequence[tuple]] = None,
    title: str = None,
) -> list:
    raise NotImplementedError("proprietary: removed from public showcase")
