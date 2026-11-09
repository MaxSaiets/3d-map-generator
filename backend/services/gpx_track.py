# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""D4 GPX-ТРЕК: маршрут користувача (біг/похід/вело) як ВРІЗАНИЙ (recessed) інлей
у поверхню мапи (раніше був підвищений над дорогами — змінено). Фронт парсить .gpx
сам і шле gpx_track=[[lon,lat],...]; тут трек перетворюється на буферизований
полігон у локальних метрах і:
  • повний пайплайн — врізана червона вставка по рельєфу (build_gpx_track_inlay_on_terrain),
    верх flush з поверхнею, тіло втоп"""

from __future__ import annotations
from typing import Any, Optional
import numpy as np
import trimesh
from shapely.geometry import LineString, MultiLineString
from shapely.geometry.base import BaseGeometry

TRACK_COLOR = None
MAX_GPX_POINTS = None
GPX_PHASE2_ENABLED = None


def _flatten_road_lines(road_lines_local: Any) -> list:
    """Нормалізує road_lines_local у плаский список shapely LineString.
    Каллер може передати list[LineString], list[MultiLineString] або суміш —
    розкладаємо MultiLineString на компоненти, відкидаємо порожнє/не-лінії,
    щоб _snap_coords_to_roads працював з однорідними геометріями."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _chaikin_smooth(coords: list, passes: int) -> list:
    """Згладження Чайкіна (corner-cutting): кожна ланка ділиться 25/75 → плавна
    крива без гострих GPS-зламів. Кінці фіксовані. Безпечно для друку."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _visvalingam_simplify(coords: list, area_threshold: float) -> list:
    """Visvalingam-Whyatt спрощення: ітеративно прибирає внутрішню точку з НАЙМЕНШОЮ
    площею трикутника (сусід-точка-сусід), поки min-площа < area_threshold (м²).
    Краще за Douglas-Peucker прибирає дрібні «зубці»/хвилястість сирого GPS, зберігаючи
    загальну форму → друкований трек, що НЕ виляє і не самоперетинається."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _snap_coords_to_roads(coords: list, road_lines_local: Any, snap_threshold_m: float) -> list:
    """Притягує точки треку до найближчої осі дороги (місто): для кожної точки
    шукаємо найближчу дорогу; якщо ближче за поріг — проєктуємо на неї (nearest
    point на лінії через project+interpolate), інакше лишаємо як є (бездоріжжя/
    стежка/парк). Так маршрут іде ПО ДОРОГАХ де можливо, але далекі від доріг
    точки (природа) НЕ зміщуються."""
    raise NotImplementedError("proprietary: removed from public showcase")


def gpx_track_to_local_geometry(
    gpx_track: Any,
    global_center: Any,
    *,
    simplify_m: float = None,
    smooth_passes: int = None,
    road_lines_local: Optional[list] = None,
    snap_threshold_m: float = None,
    vw_area_threshold: float = None,
) -> Optional[BaseGeometry]:
    """[[lon,lat],...] → LineString у локальних метрах (frame global_center).
    Розриви GPS (стрибок > 500м між сусідніми точками) ріжуть трек на сегменти.
    Для 3D-друку сирий GPS згладжується: (1) опційний snap до доріг міста,
    (2) Douglas-Peucker спрощення (прибирає тремтіння GPS), (3) Чайкін-згладження
    (прибирає хвилястість/зламки). Без цього буфер сирого треку — хвилястий і
    самоперетинається, погано друк"""
    raise NotImplementedError("proprietary: removed from public showcase")


def _ensure_valid_polygon(poly: Optional[BaseGeometry]) -> Optional[BaseGeometry]:
    """Гарантує валідний (is_valid) і непорожній полігон: спершу buffer(0), якщо
    лишився невалідним — make_valid (shapely 2.x) → відфільтрувати лише полігональні
    частини. Захищає від самоперетинів/виродження після snap+buffer+intersection."""
    raise NotImplementedError("proprietary: removed from public showcase")


def build_gpx_track_polygon(
    *,
    gpx_track: Any,
    global_center: Any,
    zone_polygon_local: Optional[BaseGeometry],
    scale_factor: float,
    width_mm: float = None,
    road_lines_local: Optional[list] = None,
) -> Optional[BaseGeometry]:
    """Буферизований полігон треку, обрізаний по зоні. width_mm — у model-мм.
    Трек спершу спрощується+згладжується (друкований, не хвилястий); якщо передано
    road_lines_local (місто) — притягується до доріг."""
    raise NotImplementedError("proprietary: removed from public showcase")


def build_gpx_track_inlay_on_terrain(
    *,
    gpx_track: Any,
    global_center: Any,
    zone_polygon_local: Optional[BaseGeometry],
    terrain_provider: Any,
    scale_factor: float,
    width_mm: float = None,
    recess_mm: float = None,
    clearance_mm: float = None,
    road_lines_local: Optional[list] = None,
) -> tuple:
    """ВРІЗАНИЙ маршрут (інлей): повертає (insert_mesh, groove_cutter).
    • insert_mesh — червона вставка, ВЕРХ якої співпадає з поверхнею (flush,
      НЕ виступає), низ втоплений у рельєф; це окрема деталь «Track».
    • groove_cutter — трохи ширший суцільний інструмент (по track+clearance,
      від трохи над поверхнею до глибини recess) для boolean-вирізу жолоба в
      рельєфі, щоб вставка сиділа В каналі ("""
    raise NotImplementedError("proprietary: removed from public showcase")


def build_gpx_track_mesh_on_terrain(
    *,
    gpx_track: Any,
    global_center: Any,
    zone_polygon_local: Optional[BaseGeometry],
    terrain_provider: Any,
    scale_factor: float,
    width_mm: float = None,
    raise_mm: float = None,
    road_lines_local: Optional[list] = None,
) -> Optional[trimesh.Trimesh]:
    """Сумісність: піднята «шапка» (raised). Новий код — build_gpx_track_inlay_on_terrain."""
    raise NotImplementedError("proprietary: removed from public showcase")
