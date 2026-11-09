# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Геометрія режиму «Гори»: поле висот → герметичне тіло без булевих."""

from __future__ import annotations
import struct
import zipfile
from typing import Optional
import numpy as np
from scipy.ndimage import gaussian_filter


def _value_noise(s, z, cell, seed):
    raise NotImplementedError("proprietary: removed from public showcase")


def _ridged(s, z, cs, cz, seed):
    raise NotImplementedError("proprietary: removed from public showcase")


def wall_depth_matrix(P, s_arc, Zrows, z_top, z_bot, seed=None, depth_mm=None):
    """Глибина заглиблення стінки всередину (rows × m): ребра/жолоби, витягнуті по вертикалі,
    великі випуклості, рвані уступи. Нависання обмежені 45° (Δd ≤ Δz знизу вгору)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def frame_solid(
    xs,
    ys,
    Z,
    fw=None,
    fh=None,
    ch=None,
    fillet: Optional[float] = None,
    segs=None,
    foot=None,
    wall_rows=None,
    wall_rock=False,
    wall_depth_mm=None,
):
    """→ (V, F, info). Координати: плита 0..S+2fw, рельєф у центрі, зсунутий на fw.
    fw=0 → без ободка (fh тоді = товщина під рельєфом, стінка від краю рельєфу до z=0)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def apply_slope_band(
    Zmm: np.ndarray, cell: float, band_mm: float, base_mm: float, seed: int = None
) -> np.ndarray:
    """Зовнішня смуга band_mm опускається до base_mm профілем (1−t)^1.7 зі збереженням дрібного
    рельєфу + скельні фасети вздовж нормалі. Все лишається полем висот ⇒ без нависань."""
    raise NotImplementedError("proprietary: removed from public showcase")


def write_3mf(V, F, path, name=None):
    """Один обʼєкт, мм; XML пишеться шматками (без збирання 150-МБ рядка в памʼяті)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def write_3mf_multi(objects, path):
    """Кілька обʼєктів (name, V, F) в одному 3MF потоково — для збірки «гора + фігурки» без
    trimesh.Scene.export (той збирає весь XML у памʼяті: +1 ГБ на 900k граней)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def write_stl(V, F, path):
    raise NotImplementedError("proprietary: removed from public showcase")


def tile_cuts(size_mm: float, bed_mm: float) -> list[float]:
    """Лінії розрізу (мм) так, щоб кожна плитка ≤ bed_mm, а центральна містила середину
    (вершина зазвичай у центрі): 1 плитка ≤ bed; інакше 3 з цілою серединою; далі рівні."""
    raise NotImplementedError("proprietary: removed from public showcase")


def split_tiles(mesh, cuts: list[float], size_mm: float):
    """Ріже trimesh площинами x/y = cuts → dict name → Trimesh (кожен зсунутий у нуль)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def preview_glb(
    V,
    F,
    path,
    size_mm: float,
    fw: float,
    texture_rgb: Optional[np.ndarray] = None,
    max_faces: int = None,
    mirror_x: bool = True,
):
    """Спрощений GLB для вʼюера: рельєф децимується, текстура (рядок 0 = південь) проєктується зверху."""
    raise NotImplementedError("proprietary: removed from public showcase")
