# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""procedural_generator.py — генерує ДРУКОВАНУ 3D-модель «світу» зі специфікації
(spec), яку дає llm_orchestrator (Claude) або rule-based парсер промту."""

from __future__ import annotations
from typing import Any
import numpy as np
import trimesh

try:
    from scipy.ndimage import gaussian_filter
except Exception:
    gaussian_filter = None
SHAPES = None
_SHAPES = None
_RES = None


def _clamp(v, lo, hi):
    raise NotImplementedError("proprietary: removed from public showcase")


def normalize_spec(spec: dict | None) -> dict:
    """Приводить spec у безпечні, друковані межі."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _smooth(a: np.ndarray, sigma: float) -> np.ndarray:
    raise NotImplementedError("proprietary: removed from public showcase")


def _norm01(a: np.ndarray) -> np.ndarray:
    raise NotImplementedError("proprietary: removed from public showcase")


def _value_noise(n: int, cells: int, rng: np.random.Generator) -> np.ndarray:
    """Гладкий value-noise: випадкова сітка cells×cells → білінійний апсемпл n×n
    зі згладжуванням (smoothstep), щоб не було «квадратів»."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _fbm(
    n: int, rng: np.random.Generator, roughness: float, octaves: int = None, base_cells: int = None
) -> np.ndarray:
    """Фрактальний шум (fBm) у [0,1]. roughness керує вагою дрібних октав."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _ridged(n: int, rng: np.random.Generator, roughness: float) -> np.ndarray:
    """Ridged-multifractal: |1-2*noise| дає гострі гребені замість «вати» —
    саме це відрізняє гірський хребет від купи шуму."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _warp(field_fn, n: int, rng: np.random.Generator, strength: float) -> np.ndarray:
    """Domain warping: зміщуємо координати шумом → «течія» рельєфу, а не сітка."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _thermal_erosion(h: np.ndarray, iterations: int, talus: float) -> np.ndarray:
    """Термальна ерозія: матеріал зсипається зі схилів, крутіших за talus.
    Векторно, 4-сусідська. Дає «осип» біля підніжжя і читабельні гребені —
    рельєф перестає виглядати як розмитий шум."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _valley_moisture(h: np.ndarray) -> np.ndarray:
    """Груба «вологість»: наскільки клітинка нижча за околицю. Використовуємо,
    щоб поглибити долини — дешева заміна гідравлічної ерозії."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _falloff(n: int, margin: float = None) -> np.ndarray:
    """М'який спад до країв плитки (щоб рельєф не обрізався стіною)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _peak_ridge(n: int, rng: np.random.Generator, peaks: int) -> np.ndarray:
    """Хребет: ламана лінія через полотно + піки на ній. Це те, що робить
    «гори» горами: кілька вершин уздовж напрямку, а не одна купа в центрі."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _shape_field(shape: str, n: int, rng: np.random.Generator, roughness: float) -> np.ndarray:
    """Форма → heightfield [0,1]. Кожна гілка — власна геометрія (див. шапку)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _grid_solid(top_z: np.ndarray, w: float) -> trimesh.Trimesh:
    """Heightfield (n×n, мм) → герметичний solid: верх + дно z=0 + 4 стіни.
    ПОВНІСТЮ ВЕКТОРНО (було два Python-цикли на ~78k граней ≈ 7–13 с)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def generate_world_mesh(spec: dict) -> trimesh.Trimesh:
    """spec → watertight-solid trimesh у мм (дно z=0). Manifold by construction."""
    raise NotImplementedError("proprietary: removed from public showcase")
