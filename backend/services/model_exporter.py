# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""3D Model Export Service
Formats: STL (binary, slicer-safe), 3MF
Guarantees:
- no empty geometry
- no broken STL headers
- no Scene→STL corruption
- Cura / Prusa / Bambu safe"""

from typing import List, Tuple, Optional, Union, Dict
import os
import hashlib
from collections import OrderedDict
import numpy as np
import trimesh
import trimesh.visual
from services.mesh_quality import improve_mesh_for_3d_printing, detect_nonmanifold_edges
from services.detail_layer_utils import MICRO_REGION_THRESHOLD_MM

_BASE_REPAIR_MEMO: "OrderedDict[str, trimesh.Trimesh]" = None
_BASE_REPAIR_MEMO_MAX = None


def _mesh_content_fingerprint(mesh: trimesh.Trimesh) -> Optional[str]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _boundary_edge_count(mesh: trimesh.Trimesh) -> int:
    raise NotImplementedError("proprietary: removed from public showcase")


def _connected_component_count(mesh: trimesh.Trimesh) -> int:
    """Face-connectivity component count — same value as
    `len(list(mesh.split(only_watertight=False)))` (both derive from the same
    face_adjacency + scipy connected-components graph, and only_watertight=False
    means split() discards nothing), but WITHOUT materializing a submesh + calling
    fill_holes() per component. PERF: this count is called several times per base
    export repair on a ~167k-face mesh; the ol"""
    raise NotImplementedError("proprietary: removed from public showcase")


def _road_export_candidate_score(mesh: Optional[trimesh.Trimesh]) -> tuple:
    raise NotImplementedError("proprietary: removed from public showcase")


def _base_export_candidate_score(mesh: Optional[trimesh.Trimesh]) -> tuple:
    raise NotImplementedError("proprietary: removed from public showcase")


def _dominant_component_if_safe(
    mesh: Optional[trimesh.Trimesh], *, min_face_ratio: float = None
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def repair_base_export_mesh(mesh: Optional[trimesh.Trimesh]) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _restore_standing_bodies(result: trimesh.Trimesh, source: trimesh.Trimesh) -> trimesh.Trimesh:
    """Повертає будинки, які dominant-component відкинув як «boolean-сміття»."""
    raise NotImplementedError("proprietary: removed from public showcase")


def repair_base_export_mesh_aggressive(
    mesh: Optional[trimesh.Trimesh],
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _base_plane_profile(mesh: trimesh.Trimesh) -> Optional[dict]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _base_print_orientation_score(mesh: Optional[trimesh.Trimesh]) -> tuple:
    raise NotImplementedError("proprietary: removed from public showcase")


def _generic_print_orientation_score(mesh: Optional[trimesh.Trimesh]) -> tuple:
    raise NotImplementedError("proprietary: removed from public showcase")


def _flip_mesh_z(mesh: trimesh.Trimesh) -> trimesh.Trimesh:
    raise NotImplementedError("proprietary: removed from public showcase")


def _select_print_orientation(mesh: Optional[trimesh.Trimesh]) -> tuple[np.ndarray, str]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _select_generic_part_orientation(mesh: Optional[trimesh.Trimesh]) -> tuple[np.ndarray, str]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _normalize_part_for_print_export(
    mesh: Optional[trimesh.Trimesh], *, part_key: str
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _normalize_source_part_axes(
    mesh: Optional[trimesh.Trimesh], *, part_key: str
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _sanitize_mesh_visual(mesh: Optional[trimesh.Trimesh]) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _build_assembly_preview_parts(parts: Dict[str, trimesh.Trimesh]) -> Dict[str, trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def orient_base_for_print(mesh: Optional[trimesh.Trimesh]) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _rotation_align_vector_to_z(source_vec: np.ndarray) -> np.ndarray:
    raise NotImplementedError("proprietary: removed from public showcase")


def _estimate_bottom_plane_normal(mesh: Optional[trimesh.Trimesh]) -> Optional[np.ndarray]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _stabilize_scene_bottom_plane(
    parts: Dict[str, trimesh.Trimesh],
) -> tuple[Dict[str, trimesh.Trimesh], float]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _filter_mesh_components_for_export(
    mesh: Optional[trimesh.Trimesh],
    *,
    min_feature_mm: float = MICRO_REGION_THRESHOLD_MM,
    min_area_mm2: float = None,
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _quantize_mesh_vertices(
    mesh: Optional[trimesh.Trimesh], *, digits: int = None
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def repair_road_export_mesh(mesh: Optional[trimesh.Trimesh]) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def to_trimesh(
    obj: Union[trimesh.Trimesh, trimesh.Scene], repair: bool = False
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def fallback_box() -> trimesh.Trimesh:
    raise NotImplementedError("proprietary: removed from public showcase")


def get_transform_matrix(
    bounds: np.ndarray,
    scale_factor: float,
    reference_xy_m: Optional[Tuple[float, float]],
    preserve_xy: bool,
    preserve_z: bool,
    rotate_to_ground: bool,
) -> np.ndarray:
    """Calculates the 4x4 transformation matrix to apply to all meshes."""
    raise NotImplementedError("proprietary: removed from public showcase")


def create_flat_base(bounds: np.ndarray, thickness_mm: float) -> trimesh.Trimesh:
    """Creates a base box matching the bounds (pre-scaling? No, this function assumes
    we are generating the base matching the mesh provided)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def create_base_in_mesh_space(
    bounds: np.ndarray, target_thickness_mm: float, scale_factor: float
) -> trimesh.Trimesh:
    """Creates the base geometry in the same coordinate space as the input mesh (Meters),
    calculating the required thickness in Meters so that after scaling it becomes target_thickness_mm."""
    raise NotImplementedError("proprietary: removed from public showcase")


def smart_combine_meshes(
    mesh_items: List[Tuple[str, trimesh.Trimesh]], aggressive_cleanup: bool = True
) -> trimesh.Trimesh:
    """Intelligently combines mesh components with proper Z-ordering and cleanup."""
    raise NotImplementedError("proprietary: removed from public showcase")


def prepare_scene_parts(
    mesh_items: List[Tuple[str, trimesh.Trimesh]],
    model_size_mm: float,
    add_base: bool,
    base_thickness_mm: float,
    rotate_to_ground: bool,
    reference_xy_m: Optional[Tuple[float, float]],
    preserve_xy: bool,
    preserve_z: bool,
    repair_meshes: bool = True,
) -> Dict[str, trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def export_stl_safe(mesh: trimesh.Trimesh, filename: str) -> None:
    raise NotImplementedError("proprietary: removed from public showcase")


def export_stl(
    filename: str,
    mesh_items: List[Tuple[str, trimesh.Trimesh]],
    model_size_mm: float = None,
    add_flat_base: bool = True,
    base_thickness_mm: float = None,
    rotate_to_ground: bool = False,
    reference_xy_m: Optional[Tuple[float, float]] = None,
    preserve_z: bool = False,
    preserve_xy: bool = False,
    repair_meshes: bool = True,
) -> Dict[str, str]:
    raise NotImplementedError("proprietary: removed from public showcase")


COLOR_PALETTES: dict = None


def get_palette_color_map(name: str) -> dict:
    """Повертає часткову color-map для палітри (або None для classic/невідомої)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def export_3mf(
    filename: str,
    mesh_items: List[Tuple[str, trimesh.Trimesh]],
    model_size_mm: float = None,
    add_flat_base: bool = True,
    base_thickness_mm: float = None,
    rotate_to_ground: bool = False,
    reference_xy_m: Optional[Tuple[float, float]] = None,
    preserve_z: bool = False,
    preserve_xy: bool = False,
    repair_meshes: bool = True,
) -> Dict[str, str]:
    raise NotImplementedError("proprietary: removed from public showcase")


_SLICER_TINY_OBJECT_MM3 = None
_SLICER_CUT_GROUP_ID = None


def _mark_tiny_objects_for_slicer(
    filename: str, min_volume_mm3: float = _SLICER_TINY_OBJECT_MM3
) -> list:
    """Крихітні (< min_volume_mm3) build-об'єкти 3MF + найбільший → одна cut-група в
    Metadata/cut_information.xml (формат Bambu/Orca: <objects><object id=1-based
    індекс build-item><cut_id .../></object>). Слайсер тоді не вважає файл дюймовим.
    Повертає назви позначених крихітних об'єктів (порожньо = файл не змінено)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _patch_3mf_colors(filename: str, color_map: dict) -> None:
    """Reads the exported 3MF, injects m:colorgroup with one color per named object,
    and writes the file back. This makes Bambu Studio / PrusaSlicer auto-assign
    colors to each part without manual filament assignment."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _to_preview_trimesh(obj: Union[trimesh.Trimesh, trimesh.Scene]) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _prepare_preview_glb_parts_fast(
    mesh_items: List[Tuple[str, trimesh.Trimesh]],
    model_size_mm: float,
    add_base: bool,
    base_thickness_mm: float,
    reference_xy_m: Optional[Tuple[float, float]],
    preserve_xy: bool,
    preserve_z: bool,
) -> Dict[str, trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _decimate_for_preview(mesh: trimesh.Trimesh, key: str) -> trimesh.Trimesh:
    """PERF (download): the on-screen preview GLB was the SAME dense mesh as the print
    3MF (~337k faces, ~6.4 MB) — slow to transfer and parse in the browser. The GLB is a
    PREVIEW-ONLY output (orders/prints use the separate, untouched 3MF), so we quadric-
    decimate each preview part with open3d. Quadric-error decimation preserves the
    silhouette/shape (industry-standard, visually near-lossless for a height"""
    raise NotImplementedError("proprietary: removed from public showcase")


def export_glb(
    filename: str,
    mesh_items: List[Tuple[str, trimesh.Trimesh]],
    model_size_mm: float = None,
    add_flat_base: bool = True,
    base_thickness_mm: float = None,
    rotate_to_ground: bool = False,
    reference_xy_m: Optional[Tuple[float, float]] = None,
    preserve_z: bool = False,
    preserve_xy: bool = False,
) -> Dict[str, str]:
    raise NotImplementedError("proprietary: removed from public showcase")


def export_scene(
    terrain_mesh: Optional[trimesh.Trimesh],
    road_mesh: Optional[trimesh.Trimesh],
    building_meshes: List[trimesh.Trimesh],
    water_mesh: Optional[trimesh.Trimesh],
    filename: str,
    format: str = None,
    model_size_mm: float = None,
    add_flat_base: bool = True,
    base_thickness_mm: float = None,
    parks_mesh: Optional[trimesh.Trimesh] = None,
    poi_mesh: Optional[trimesh.Trimesh] = None,
    reference_xy_m: Optional[Tuple[float, float]] = None,
    preserve_z: bool = False,
    preserve_xy: bool = False,
    rotate_to_ground: bool = True,
    extra_mesh_items: Optional[List[Tuple[str, trimesh.Trimesh]]] = None,
    repair_meshes: bool = True,
):
    raise NotImplementedError("proprietary: removed from public showcase")


def export_preview_parts_stl(
    output_prefix: str,
    mesh_items: List[Tuple[str, trimesh.Trimesh]],
    model_size_mm: float = None,
    add_flat_base: bool = True,
    base_thickness_mm: float = None,
    rotate_to_ground: bool = False,
    reference_xy_m: Optional[Tuple[float, float]] = None,
    preserve_z: bool = False,
    preserve_xy: bool = False,
) -> Dict[str, str]:
    raise NotImplementedError("proprietary: removed from public showcase")


def export_preview_parts_3mf(
    output_prefix: str,
    mesh_items: List[Tuple[str, trimesh.Trimesh]],
    model_size_mm: float = None,
    add_flat_base: bool = True,
    base_thickness_mm: float = None,
    rotate_to_ground: bool = True,
    reference_xy_m: Optional[Tuple[float, float]] = None,
    preserve_z: bool = False,
    preserve_xy: bool = False,
    include_components: Optional[Dict[str, bool]] = None,
) -> Dict[str, str]:
    """Експортує прев'ю частини в форматі 3MF з кольорами та можливістю виключення компонентів."""
    raise NotImplementedError("proprietary: removed from public showcase")
