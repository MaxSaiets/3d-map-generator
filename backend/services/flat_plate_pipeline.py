# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from pathlib import Path
from typing import Any, Iterable, Optional
import numpy as np
import trimesh
import mapbox_earcut
from geopandas import GeoDataFrame
from shapely import affinity
from shapely.geometry import GeometryCollection, LineString, MultiPolygon, Point, Polygon, box
from shapely.geometry.base import BaseGeometry
from shapely.ops import nearest_points, triangulate, unary_union
from services.building_processor import process_buildings
from services.buildings_pipeline import split_building_parts_from_parent_footprints
from services.detail_layer_utils import MICRO_REGION_THRESHOLD_MM, model_mm_to_world_m
from services.export_pipeline import ExportPipelineResult, export_generation_outputs

LAYER_COLORS = None
MIN_KEYCHAIN_PRINT_FEATURE_MM = None
MIN_KEYCHAIN_TEXT_STROKE_MM = None
KEYCHAIN_TEXT_RAISE_MM = None
_FONT_5X7 = None
_CYR_TO_LAT = None


def _model_mm_to_world_m(value_mm: float, scale_factor: float) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _clean_polygonal_geometry(geometry: Optional[BaseGeometry]) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _iter_polygons(geometry: Optional[BaseGeometry]) -> Iterable[Polygon]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _with_color(mesh: Optional[trimesh.Trimesh], color: list[int]) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _extrude_polygon_prism(poly: Polygon, thickness_m: float) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def build_flat_layer_mesh_from_mask(
    geometry: Optional[BaseGeometry],
    *,
    bottom_z_m: float,
    thickness_m: float,
    color: list[int],
    min_area_m2: float = None,
) -> Optional[trimesh.Trimesh]:
    """Extrude a polygonal 2D mask into one printable flat layer."""
    raise NotImplementedError("proprietary: removed from public showcase")


def build_flat_zone_base_mesh(
    zone_polygon_local: Optional[BaseGeometry],
    *,
    bbox_meters: tuple[float, float, float, float],
    thickness_m: float,
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _geometry_min_dimension(poly: Polygon) -> float:
    raise NotImplementedError("proprietary: removed from public showcase")


def _drop_subprintable_fragments(
    geometry: Optional[BaseGeometry], *, min_feature_m: float, min_area_m2: float
) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _sanitize_layer_mask(
    geometry: Optional[BaseGeometry], *, min_feature_m: float, min_area_m2: float, label: str
) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _drop_thin_footprints_gdf(gdf, *, erode_m: float, min_iso_ratio: float = None):
    """Прибирає будівлі-«волосини» (slivers) ДВОМА тестами:
    (1) ІЗОПЕРИМЕТРИЧНИЙ коефіцієнт 4π·area/perimeter² — БЕЗРОЗМІРНИЙ (scale-free):
        ~0.78 для квадрата, →0 для довгої нитки. <min_iso_ratio = витягнута нитка
        (типовий clip-artifact: будинок розрізаний краєм вікна карти в смужку
        0.06×60мм, aspect >25:1) → викидаємо. Працює НЕЗАЛЕЖНО від масштабу —
        тому надійніше за ерозію (масштаб кар"""
    raise NotImplementedError("proprietary: removed from public showcase")


def _mesh_footprint_min_width_m(mesh) -> float:
    """Мін-ширина footprint меша (orientation-invariant) через короткий бік
    minimum_rotated_rectangle опуклої оболонки XY-проєкції. Ловить ВОЛОСИНИ за
    будь-якої орієнтації (на відміну від AABB). Для увігнутих (L) оболонка
    заповнює — реальна будівля лишається; для нитки оболонка ≈ нитка → мала ширина."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _mask_union_from_geometries(geometries: Any) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _subtract_geometry(
    geometry: Optional[BaseGeometry], *masks: Optional[BaseGeometry]
) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _rounded_rect(minx: float, miny: float, maxx: float, maxy: float, radius_m: float) -> Polygon:
    raise NotImplementedError("proprietary: removed from public showcase")


def build_magnet_pocket_geometry(
    zone_polygon_local: BaseGeometry,
    *,
    diameter_mm: float,
    count: int,
    inset_mm: float,
    export_scale_factor: float,
) -> Optional[BaseGeometry]:
    """Кишені під магніти у дні плоскої мапи. count=1 — одна в центроїді
    (старий режим, golden-сумісний). count≥2 — діагональне кільце навколо
    центру (кути 45°+k·90°): працює і для квадрата, і для кола/серця;
    кандидат відкидається, якщо кишеня + 0.6мм бічної стінки не вміщується
    в тіло; якщо лишилось <2 — fallback до однієї в центроїді."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _mesh_xy_footprint(
    mesh: trimesh.Trimesh, *, simplify_m: float = None
) -> Optional[BaseGeometry]:
    """РЕАЛЬНИЙ XY-контур (увігнуто-стійкий) екструдованого будинку = об'єднання
    проєкцій усіх трикутників на площину XY. Опукла оболонка заповнила б L/U-виїмки;
    цей контур зберігає справжню форму → точний паз/peg. Повертає найбільший полігон."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _select_highlight_building_index(
    building_meshes: list,
    *,
    target_xy: Optional[tuple[float, float]],
    exclude: Optional[set] = None,
) -> Optional[int]:
    """Індекс будинку для виділення — ОДНАКОВА логіка з /api/building-at (main.py),
    щоб червоний контур на карті = той самий будинок, що отримає вставку:
      1) РЕАЛЬНИЙ XY-контур будинку (_mesh_xy_footprint) МІСТИТЬ target_xy → беремо
         його одразу (клік юзера всередині свого будинку — точний вибір);
      2) інакше — найближчий за ВІДСТАННЮ ДО КРАЮ (polygon.distance(point), як
         geom.distance(pt) у /ap"""
    raise NotImplementedError("proprietary: removed from public showcase")


def build_highlight_insert(
    building_mesh: trimesh.Trimesh,
    *,
    base_top_m: float,
    export_scale_factor: float,
    depth_mm: float = None,
    lip_mm: float = None,
    clearance_mm: float = None,
    z_clear_mm: float = None,
) -> tuple[trimesh.Trimesh, Optional[BaseGeometry], float]:
    """Виділений будинок → ВСТАВНА деталь (механічна вставка у паз бази, БЕЗ клею).
    Повертає (highlight_mesh, pocket_poly, pocket_depth_m):
      * highlight_mesh = будинок + peg-ніжка (під базу), колір highlight (ЧЕРВОНИЙ);
      * pocket_poly/pocket_depth_m → виріз ПАЗУ у ВЕРХ бази через
        _build_keychain_base_parts(top_cut_poly=pocket_poly, top_cut_depth_m=depth)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def clip_buildings_around_highlight(
    building_meshes: list,
    highlight_footprints: list,
    *,
    export_scale_factor: float,
    clearance_mm: float = None,
    label: str = None,
) -> list:
    """Обрізає СУСІДНІ будинки з-під зони вставної (виділеної) деталі."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _ensure_no_through_hole(
    *,
    base_top_m: float,
    top_cut_poly: Optional[BaseGeometry],
    top_cut_depth_m: float,
    bottom_cut_poly: Optional[BaseGeometry],
    bottom_cut_depth_m: float,
    export_scale_factor: float,
    min_solid_mm: float = None,
    label: str = None,
) -> tuple[float, float]:
    """THROUGH-HOLE GUARD (LATE, defensive): паз ЗВЕРХУ (highlight, ~0.8мм) та виріз
    ЗНИЗУ (магніт-кишеня / конектор-паз / гравіювання звороту) у зоні XY-перекриття
    лишають лише `base_top − top_depth − bottom_depth` суцільного матеріалу. Якщо
    цього < min_solid_mm (0.4мм) — деталь стала б наскрізною дірою."""
    raise NotImplementedError("proprietary: removed from public showcase")


def parse_connector_azimuths(s) -> Optional[list]:
    """ "30,90,150" → [30.0, 90.0, 150.0]; порожнє/None → None (стара NSEW-поведінка)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def build_map_connector_geometry(
    base_polygon: BaseGeometry,
    *,
    edges: str,
    span_mm: float,
    length_mm: float,
    waist_frac: float,
    clearance_mm: float,
    export_scale_factor: float,
    key_edges: Optional[str] = None,
    edge_dirs: Optional[list] = None,
    key_dirs: Optional[list] = None,
) -> tuple[Optional[BaseGeometry], Optional[BaseGeometry]]:
    """З'ЄДНУВАЧ-ПАЗИ (метелик/bowtie) на серединах граней плоскої карти-плитки."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _frame_place_text(
    text: str, *, height_m: float, x: float, y: float, ha: str = None, va: str = None
) -> Optional[BaseGeometry]:
    """TTF-текст у локально-метровій системі, заякорений у (x,y) за ha/va.
    ha: left|center|right (горизонт.), va: bottom|center|top (верт.)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _nice_round_number(value: float) -> float:
    """Найближче «гарне» число (1/2/5×10ⁿ) ≤ value — для довжини масштабної лінійки."""
    raise NotImplementedError("proprietary: removed from public showcase")


def build_map_frame_overlay(
    base_polygon: BaseGeometry,
    *,
    north: float,
    south: float,
    east: float,
    west: float,
    export_scale_factor: float,
    want_compass: bool = True,
    want_scale: bool = True,
    want_coords: bool = True,
    frame_style: str = None,
) -> Optional[BaseGeometry]:
    """ПРЕМІУМ-РАМКА плоскої карти: компас (стрілка-N), масштабна лінійка
    (шахова + підписи 0…N м) і координати центру (lat/lon) — як ОДИН підведений
    полігон у кутах/краях, що потім екструдується окремою чорною деталлю «Frame»
    і вирізається з шарів карти (як map_label) щоб читалось чисто."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _round_polygon_tip(pts: list, *, tip_index: int, radius: float, samples: int = None) -> list:
    """Заокруглення одного гострого вузла замкнутого контуру: вершини в радіусі
    `radius` від кінчика замінюються семплами квадратичної Безьє (контрольна
    точка = старий кінчик). Використовується для вістря серця.
    СИМЕТРИЧНО: беремо однакову кількість вузлів з обох боків (k=min) — інакше
    нерівний крок семплінгу давав асиметричну «зазубрину» внизу серця."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _keychain_body_shape(
    minx: float,
    miny: float,
    maxx: float,
    maxy: float,
    *,
    radius_m: float,
    shape: str,
    mm_to_world: float = None,
) -> BaseGeometry:
    raise NotImplementedError("proprietary: removed from public showcase")


def _keychain_loop_outer(
    *, center_x: float, center_y: float, outer_m: float, style: str
) -> BaseGeometry:
    raise NotImplementedError("proprietary: removed from public showcase")


def _keychain_loop_inner(
    *, center_x: float, center_y: float, inner_m: float, style: str
) -> BaseGeometry:
    raise NotImplementedError("proprietary: removed from public showcase")


def build_keychain_layout(
    *,
    bbox_meters: tuple[float, float, float, float],
    scale_factor: float,
    model_size_mm: float,
    body_width_mm: Optional[float] = None,
    body_height_mm: Optional[float] = None,
    map_x_mm: Optional[float] = None,
    map_y_mm: Optional[float] = None,
    map_width_mm: Optional[float] = None,
    map_height_mm: Optional[float] = None,
    base_shape: str = None,
    loop_style: str = None,
    loop_angle_deg: float = None,
    loop_center_x_mm: Optional[float] = None,
    loop_center_y_mm: Optional[float] = None,
    label_center_x_mm: Optional[float] = None,
    label_center_y_mm: Optional[float] = None,
    label_width_mm: Optional[float] = None,
    label_angle_deg: float = None,
    loop_outer_radius_mm: float,
    loop_inner_radius_mm: float,
    corner_radius_mm: float,
    label_band_height_mm: float,
) -> dict[str, BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _clip_geometry(
    geometry: Optional[BaseGeometry], clip: Optional[BaseGeometry]
) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _fit_geometry_into_bounds(
    geometry: Optional[BaseGeometry],
    *,
    source_bounds: tuple[float, float, float, float],
    target_bounds: tuple[float, float, float, float],
) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _stretch_geometry_into_bounds(
    geometry: Optional[BaseGeometry],
    *,
    source_bounds: tuple[float, float, float, float],
    target_bounds: tuple[float, float, float, float],
) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _rotated_source_bounds(
    source_bounds: tuple[float, float, float, float], angle_deg: float
) -> tuple[float, float, float, float]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _orient_then_stretch_geometry_into_bounds(
    geometry: Optional[BaseGeometry],
    *,
    source_bounds: tuple[float, float, float, float],
    target_bounds: tuple[float, float, float, float],
    angle_deg: float,
) -> Optional[BaseGeometry]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _fit_gdf_into_bounds(
    gdf: Optional[GeoDataFrame],
    *,
    source_bounds: tuple[float, float, float, float],
    target_bounds: tuple[float, float, float, float],
) -> Optional[GeoDataFrame]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _stretch_gdf_into_bounds(
    gdf: Optional[GeoDataFrame],
    *,
    source_bounds: tuple[float, float, float, float],
    target_bounds: tuple[float, float, float, float],
) -> Optional[GeoDataFrame]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _orient_then_stretch_gdf_into_bounds(
    gdf: Optional[GeoDataFrame],
    *,
    source_bounds: tuple[float, float, float, float],
    target_bounds: tuple[float, float, float, float],
    angle_deg: float,
) -> Optional[GeoDataFrame]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _clip_buildings_to_content(
    gdf: Optional[GeoDataFrame], content_area: Optional[BaseGeometry]
) -> Optional[GeoDataFrame]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _normalize_label_text(text: str) -> str:
    raise NotImplementedError("proprietary: removed from public showcase")


def _ttf_text_polygons(text: str, height_m: float, font_family: str = None) -> list[BaseGeometry]:
    """Рендерить текст через matplotlib TTF + повертає список shapely Polygons.
    Дає СПРАВЖНІ smooth letters замість пікселього 5×7 шрифту."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _compute_text_letter_polygon(
    *,
    text: str,
    body_geometry: BaseGeometry,
    label_band_geometry: BaseGeometry,
    text_height_m: float,
    angle_deg: float,
    min_stroke_m: float,
    max_width: float,
    max_height: float,
) -> Optional[BaseGeometry]:
    """Compute the 2D letter polygon (positioned, rotated, clipped to body) for
    carving out of map layers before meshes are built.  Same math as the TTF
    branch of build_keychain_label_mesh so the carve and the raised text align
    perfectly."""
    raise NotImplementedError("proprietary: removed from public showcase")


def build_keychain_label_mesh(
    text: str,
    *,
    body_geometry: BaseGeometry,
    label_band_geometry: BaseGeometry,
    bottom_z_m: float,
    thickness_m: float,
    text_height_m: float,
    color: list[int],
    stroke_width_m: float = None,
    angle_deg: float = None,
    min_stroke_m: float = None,
    font_style: str = None,
    precomputed_polygon: Optional[BaseGeometry] = None,
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _rotate_meshes_for_keychain_layout(
    *,
    meshes: list[Optional[trimesh.Trimesh]],
    building_meshes: list[trimesh.Trimesh],
    angle_deg: float,
    origin_xy: tuple[float, float],
    origin_z: float,
) -> None:
    raise NotImplementedError("proprietary: removed from public showcase")


def _build_keychain_base_parts(
    base_mask: BaseGeometry,
    *,
    base_top_m: float,
    back_text_poly: Optional[BaseGeometry] = None,
    engrave_m: float = None,
    top_cut_poly: Optional[BaseGeometry] = None,
    top_cut_depth_m: float = None,
    min_area_m2: float = None,
) -> tuple[Optional[trimesh.Trimesh], Optional[trimesh.Trimesh]]:
    """База брелка (чисті watertift-екструди, БЕЗ 3D-boolean).
    Без cut'ів — одна суцільна плита. `back_text_poly`+`engrave_m` → НИЖНІЙ шар
    (0..engrave) з гравіюванням, видно знизу (також магніт-кишеня). НОВЕ:
    `top_cut_poly`+`top_cut_depth_m` → ПАЗ у ВЕРХНЬОМУ шарі для вставки окремої
    деталі-будинку зверху. Сумісно: коли top_cut=None — поведінка ІДЕНТИЧНА старій."""
    raise NotImplementedError("proprietary: removed from public showcase")


def build_keychain_rim_mesh(
    *, base_geometry: BaseGeometry, bottom_z_m: float, width_m: float, height_m: float
) -> Optional[trimesh.Trimesh]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _clamp_mesh_height(
    mesh: trimesh.Trimesh, *, min_height_m: float, max_height_m: float
) -> trimesh.Trimesh:
    raise NotImplementedError("proprietary: removed from public showcase")


def _set_mesh_height(mesh: trimesh.Trimesh, *, target_height_m: float) -> trimesh.Trimesh:
    raise NotImplementedError("proprietary: removed from public showcase")


def _mesh_manifest(mesh: Optional[trimesh.Trimesh], *, scale_factor: float) -> dict[str, Any]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _fetch_zone_heightfield_provider(
    *, request: Any, zone: Any, global_center: Any, max_axis_cells: int = None
):
    """C3 ТОПО: качає DEM-висоти (Terrarium) для bbox зони у ЛОКАЛЬНИХ метрах
    і повертає TerrainProvider для інтерполяції. None — якщо висоти недоступні
    (генерація тоді тихо лишає плоску базу)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _keychain_topo_inverse_map(
    *,
    unwrap_params: Optional[dict],
    source_bounds: tuple[float, float, float, float],
    target_bounds: tuple[float, float, float, float],
    angle_deg: float,
):
    """Обернене відображення: координати ЖЕТОНА (layout) → координати ЗОНИ
    (локальні метри). Інверсія до _xform/unwrap у run_flat_plate_pipeline."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _extrude_polygon_heightfield(
    poly: Polygon, *, bottom_z_m: float, top_z_func, max_area_m2: float
) -> Optional[trimesh.Trimesh]:
    """Watertight-екструд полігона з ПЕРЕМІННОЮ верхньою гранню (heightfield).
    Та сама техніка, що _extrude_polygon_prism, але triangle-двигун додає
    Steiner-точки всередині (q28 + max area) і верхній z береться з top_z_func."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _build_keychain_topo_base(
    *,
    request: Any,
    zone: Any,
    global_center: Any,
    base_mask: BaseGeometry,
    relief_zone: Optional[BaseGeometry],
    base_top_m: float,
    relief_m: float,
    feather_m: float,
    unwrap_params: Optional[dict],
    source_bounds: tuple[float, float, float, float],
    target_bounds: tuple[float, float, float, float],
    map_rotation_deg: float,
    back_text_poly: Optional[BaseGeometry],
    engrave_m: float,
    export_scale_factor: float,
) -> tuple[Optional[trimesh.Trimesh], Optional[trimesh.Trimesh]]:
    """C3 ТОПО-БРЕЛОК: база жетона з heightfield-рельєфом на верхній грані.
    Рельєф нормалізується по видимій зоні (p2..p98), кліпиться по контуру
    relief_zone (тіло мінус rim/текстові смуги) з feather-переходом до плоских
    країв — вушко/обід/смуга напису лишаються рівними на base_top.
    Повертає (topo_mesh, bottom_engrave_mesh) або (None, None) → плоский fallback."""
    raise NotImplementedError("proprietary: removed from public showcase")


def build_flat_building_meshes(
    *,
    request: Any,
    scale_factor: float,
    gdf_buildings_local: Optional[GeoDataFrame],
    base_top_m: float,
    export_scale_factor: Optional[float] = None,
) -> tuple[list[trimesh.Trimesh], list[trimesh.Trimesh]]:
    """Повертає (ordinary_building_meshes, landmark_meshes). Орієнтири йдуть
    окремим списком → у експорті стають частиною «Landmark» з бронзовим кольором."""
    raise NotImplementedError("proprietary: removed from public showcase")


def run_flat_plate_pipeline(
    *,
    task: Any,
    request: Any,
    task_id: str,
    output_dir: Path,
    zone: Any,
    source: Any,
    canonical_2d_stage: Any,
    global_center: Any,
    file_basename: Optional[str] = None,
) -> ExportPipelineResult:
    raise NotImplementedError("proprietary: removed from public showcase")
