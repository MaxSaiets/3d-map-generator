# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from shapely.geometry import shape
from shapely.geometry.base import BaseGeometry
from shapely.ops import unary_union


def _normalize_loaded_geometry(geometry: BaseGeometry | None) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _load_geojson_union(path: Path) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


@dataclass
class CanonicalMaskBundle:
    source_dir: Path
    zone_polygon: Optional[BaseGeometry]
    roads_final: Optional[BaseGeometry]
    road_groove_mask: Optional[BaseGeometry]
    parks_final: Optional[BaseGeometry]
    parks_groove_mask: Optional[BaseGeometry]
    water_final: Optional[BaseGeometry]
    water_groove_mask: Optional[BaseGeometry]
    buildings_footprints: Optional[BaseGeometry]
    roads_semantic_preview: Optional[BaseGeometry] = None


def load_canonical_mask_bundle(bundle_dir: str | Path) -> CanonicalMaskBundle:
    raise NotImplementedError("proprietary: removed from public showcase")
