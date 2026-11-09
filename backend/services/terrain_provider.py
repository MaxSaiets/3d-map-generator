# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""TerrainProvider - клас для інтерполяції висот рельєфу
Дозволяє отримувати висоту землі в будь-якій точці (X, Y)"""

import numpy as np
from scipy.interpolate import RegularGridInterpolator
from typing import Optional, Tuple


class TerrainSurfaceSampler:
    """Samples Z from an arbitrary terrain *surface mesh* (top surface) by interpolating
    within triangles in XY."""

    def __init__(self, vertices: np.ndarray, faces: np.ndarray):
        raise NotImplementedError("proprietary: removed from public showcase")

    @staticmethod
    def _barycentric_z(
        pxy: np.ndarray, txy: np.ndarray, tz: np.ndarray, eps: float = None
    ) -> Optional[float]:
        """Compute barycentric interpolation of z at point p inside triangle.
        pxy: (2,), txy: (3,2), tz: (3,)
        Returns z if inside (with epsilon), else None."""
        raise NotImplementedError("proprietary: removed from public showcase")

    def sample(self, points_xy: np.ndarray) -> np.ndarray:
        raise NotImplementedError("proprietary: removed from public showcase")


class TerrainProvider:
    """Надає інтерполяцію висот рельєфу для будь-якої точки (X, Y)"""

    def __init__(
        self, X: np.ndarray, Y: np.ndarray, Z: np.ndarray, original_Z: Optional[np.ndarray] = None
    ):
        """Ініціалізує TerrainProvider з сіткою висот"""
        raise NotImplementedError("proprietary: removed from public showcase")

    def _heights_on_terrain_triangles(self, xs: np.ndarray, ys: np.ndarray) -> np.ndarray:
        """Інтерполяція висоти, яка ПОВНІСТЮ збігається з трикутниками terrain mesh."""
        raise NotImplementedError("proprietary: removed from public showcase")

    def get_height_at(self, x: float, y: float) -> float:
        """Отримує висоту землі в точці (x, y)"""
        raise NotImplementedError("proprietary: removed from public showcase")

    def get_heights_for_points(self, points: np.ndarray) -> np.ndarray:
        """Отримує висоти для масиву точок"""
        raise NotImplementedError("proprietary: removed from public showcase")

    def get_surface_heights_for_points(self, points: np.ndarray) -> np.ndarray:
        """Returns heights sampled from the final terrain *surface mesh* when available.
        Falls back to the regular heightfield interpolation otherwise."""
        raise NotImplementedError("proprietary: removed from public showcase")

    def get_bounds(self) -> Tuple[float, float, float, float]:
        """Повертає межі рельєфу (min_x, max_x, min_y, max_y)"""
        raise NotImplementedError("proprietary: removed from public showcase")
