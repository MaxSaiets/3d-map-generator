# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from dataclasses import dataclass
import os
import time
from typing import Any, Optional
import trimesh
from geopandas import GeoDataFrame
from shapely.geometry.base import BaseGeometry
from services.boolean_backends import BooleanBackend
from services.buildings_pipeline import process_building_layer
from services.canonical_mask_bundle import CanonicalMaskBundle
from services.detail_layer_utils import (
    MIN_LAND_WIDTH_MODEL_MM,
    MICRO_REGION_THRESHOLD_MM,
    model_mm_to_world_m,
)
from services.groove_pipeline import GrooveCutResult, cut_inlay_grooves, prepare_road_cut_mask
from services.inlay_fit import InlayFitConfig
from services.parks_pipeline import process_park_layer
from services.processing_results import (
    GreenAreaProcessingResult,
    RoadLayerResult,
    RoadProcessingResult,
)
from services.roads_pipeline import process_road_layer
from services.water_layer_pipeline import process_water_layer


@dataclass
class DetailLayerPipelineResult:
    terrain_mesh: Optional[trimesh.Trimesh]
    road_mesh: Optional[trimesh.Trimesh]
    road_result: Optional[RoadProcessingResult]
    road_cut_source: Any
    road_groove_mask: Optional[BaseGeometry]
    building_meshes: Any
    water_mesh: Optional[trimesh.Trimesh]
    water_cut_polygons: Optional[BaseGeometry]
    parks_mesh: Optional[trimesh.Trimesh]
    parks_result: Optional[GreenAreaProcessingResult]
    groove_result: Optional[GrooveCutResult]
    merged_building_mesh: Optional[trimesh.Trimesh]
    support_meshes: Any
    building_footprints: Optional[BaseGeometry]
    landmark_centroids: Optional[list] = None


@dataclass
class CanonicalRoadMasks:
    road_insert_mask: Optional[BaseGeometry]
    road_groove_mask: Optional[BaseGeometry]
    building_exclusion_mask: Optional[BaseGeometry]
    support_exclusion_mask: Optional[BaseGeometry]


def _build_canonical_road_masks(
    *,
    road_insert_source: Optional[BaseGeometry],
    building_union_local: Optional[BaseGeometry],
    scale_factor: Optional[float],
    groove_clearance_mm: float,
    tiny_feature_threshold_mm: float,
    road_gap_fill_threshold_mm: float,
    zone_polygon_local: Optional[BaseGeometry],
    zone_prefix: str,
    road_groove_mask_override: Optional[BaseGeometry] = None,
    preserve_exact_masks: bool = False,
) -> CanonicalRoadMasks:
    raise NotImplementedError("proprietary: removed from public showcase")


def process_detail_layers(
    *,
    task: Any,
    request: Any,
    scale_factor: Optional[float],
    terrain_provider: Any,
    terrain_mesh: Optional[trimesh.Trimesh],
    global_center: Any,
    G_roads: Any,
    water_geoms_for_bridges: Any,
    road_width_multiplier_effective: float,
    zone_polygon_local: Any,
    building_union_local: Any,
    merged_roads_geom_local: Any,
    road_cut_mask: Any,
    road_height_m: float,
    road_embed_m: float,
    stl_extra_embed_m: float,
    gdf_buildings_local: Optional[GeoDataFrame],
    gdf_water: Optional[GeoDataFrame],
    water_depth_m: float,
    gdf_green: Optional[GeoDataFrame],
    groove_clearance_mm: float,
    boolean_backend: Optional[BooleanBackend] = None,
    zone_prefix: str = None,
    canonical_mask_bundle: Optional[CanonicalMaskBundle] = None,
) -> DetailLayerPipelineResult:
    raise NotImplementedError("proprietary: removed from public showcase")
