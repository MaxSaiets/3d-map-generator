# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
import os
import time
from dataclasses import dataclass
from typing import Optional, Protocol
import trimesh
from shapely.geometry.base import BaseGeometry
from services.groove_cutter_builder import build_unified_groove_cutter
from services.terrain_cutter import cut_all_grooves, cut_grooves_sequentially


@dataclass
class GrooveBooleanRequest:
    terrain_mesh: trimesh.Trimesh
    road_polygons: Optional[BaseGeometry]
    road_clearance_m: float
    parks_polygons: Optional[BaseGeometry]
    parks_clearance_m: float
    parks_mesh: Optional[trimesh.Trimesh]
    water_polygons: Optional[BaseGeometry]
    water_clearance_m: float
    water_mesh: Optional[trimesh.Trimesh]
    scale_factor: float
    road_mesh: Optional[trimesh.Trimesh]
    groove_depth_m: float


class BooleanBackend(Protocol):
    def cut_grooves(self, request: GrooveBooleanRequest) -> Optional[trimesh.Trimesh]:
        raise NotImplementedError("proprietary: removed from public showcase")


class BlenderBooleanBackend:
    name = None

    def cut_grooves(self, request: GrooveBooleanRequest) -> Optional[trimesh.Trimesh]:
        raise NotImplementedError("proprietary: removed from public showcase")


class NoOpBooleanBackend:
    name = None

    def cut_grooves(self, request: GrooveBooleanRequest) -> Optional[trimesh.Trimesh]:
        raise NotImplementedError("proprietary: removed from public showcase")


def _weld_repair_subtract(terrain_mesh, cutter_mesh):
    """Self-contained robust cut: pass a NON-watertight terrain through the manifold3d
    constructor (topological repair into a valid solid — which fill_holes/Blender cannot
    do), then boolean-difference IN-PROCESS. Proven on a dense 290k-face non-watertight
    mesh for the connector notch. This is what keeps large-city grooves OFF the Blender
    subprocess (whose BMesh load OOM-kills a 4GB server). Inlined here"""
    raise NotImplementedError("proprietary: removed from public showcase")


class ManifoldBooleanBackend:
    name = None

    def __init__(self, *, fallback_backend: Optional[BooleanBackend] = None) -> None:
        raise NotImplementedError("proprietary: removed from public showcase")

    def cut_grooves(self, request: GrooveBooleanRequest) -> Optional[trimesh.Trimesh]:
        raise NotImplementedError("proprietary: removed from public showcase")


def get_available_boolean_backends() -> list[str]:
    raise NotImplementedError("proprietary: removed from public showcase")


def resolve_boolean_backend(
    backend: Optional[BooleanBackend] = None, *, backend_name: Optional[str] = None
) -> BooleanBackend:
    raise NotImplementedError("proprietary: removed from public showcase")
