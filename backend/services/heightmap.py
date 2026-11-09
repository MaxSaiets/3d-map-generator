# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
import numpy as np
import time
from typing import Tuple, Optional, Iterable
from shapely.geometry.base import BaseGeometry


def _iter_polygons(geom: BaseGeometry):
    """Yield Polygon parts from Polygon/MultiPolygon/GeometryCollection-ish inputs."""
    raise NotImplementedError("proprietary: removed from public showcase")


def flatten_heightfield_under_buildings(
    X: np.ndarray,
    Y: np.ndarray,
    Z: np.ndarray,
    building_geometries: Iterable[BaseGeometry],
    all_touched: bool = True,
    min_cells: int = None,
) -> np.ndarray:
    """Flattens terrain under buildings using median height for stability.
    Ensures buildings sit flat on the terrain."""
    raise NotImplementedError("proprietary: removed from public showcase")


def flatten_heightfield_under_polygons(
    X: np.ndarray,
    Y: np.ndarray,
    Z: np.ndarray,
    geometries: Iterable[BaseGeometry],
    quantile: float = None,
    all_touched: bool = True,
    min_cells: int = None,
) -> np.ndarray:
    """Generic flattening using quantile."""
    raise NotImplementedError("proprietary: removed from public showcase")


def depress_heightfield_under_polygons(
    X: np.ndarray,
    Y: np.ndarray,
    Z: np.ndarray,
    geometries: Iterable[BaseGeometry],
    depth: float,
    min_floor: Optional[float] = None,
    quantile: float = None,
    all_touched: bool = True,
    min_cells: int = None,
) -> np.ndarray:
    """Carves a depression (for water)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def get_elevation_data(
    X: np.ndarray,
    Y: np.ndarray,
    latlon_bbox: Optional[Tuple[float, float, float, float]],
    z_scale: float,
    source_crs: Optional[object] = None,
    terrarium_zoom: Optional[int] = None,
    elevation_ref_m: Optional[float] = None,
    baseline_offset_m: float = None,
) -> Tuple[np.ndarray, float]:
    """Оптимізоване отримання даних висот рельєфу з валідацією та очищенням."""
    raise NotImplementedError("proprietary: removed from public showcase")
