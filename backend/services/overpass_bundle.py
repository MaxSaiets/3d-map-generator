# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
"""Один Overpass-запит на всю генерацію (зони поза ukraine.duckdb)."""

from __future__ import annotations
import os
import re
import threading
import time
from collections import OrderedDict
from typing import Any, Iterable, Optional
import networkx as nx
import osmnx as ox
from osmnx._errors import InsufficientResponseError
from shapely.geometry import MultiPolygon, Polygon

__all__ = [
    "BundleMiss",
    "LazyBundle",
    "Bundle",
    "build_query",
    "enabled",
    "parse_way_filter",
    "wait_max_s",
]


class BundleMiss(RuntimeError):
    """Пакет не може віддати цей шар — беріть його окремим запитом, як раніше."""


def enabled() -> bool:
    raise NotImplementedError("proprietary: removed from public showcase")


TagValue = None


def _tag_pairs(tags: dict) -> list[tuple[str, Any]]:
    """Той самий порядок і та сама нормалізація, що в osmnx
    `_create_overpass_features_query`: bool → сам ключ, str → [str], list → як є."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _feature_components(polygon_coord_str: str, tags: dict) -> str:
    """Рядок-у-рядок те, що osmnx кладе у власний запит шару (без `out;`)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _polygon_coord_strs(polygon) -> list[str]:
    raise NotImplementedError("proprietary: removed from public showcase")


def _network_filter(network_type: str) -> str:
    raise NotImplementedError("proprietary: removed from public showcase")


def _overpass_settings() -> str:
    raise NotImplementedError("proprietary: removed from public showcase")


def roads_query_polygon(polygon):
    """Буфер 500 м, як у `graph_from_polygon` (Overpass віддає way цілком, якщо
    хоч один вузол у полігоні; буфер потрібен, щоб потім чесно обрізати)."""
    raise NotImplementedError("proprietary: removed from public showcase")


def build_query(
    feature_layers: Iterable[tuple[Any, dict]], roads_polygon, network_type: str = None
) -> tuple[str, str]:
    """Збирає один union-запит. Повертає (query, way_filter доріг)."""
    raise NotImplementedError("proprietary: removed from public showcase")


_CLAUSE_RX = None


def parse_way_filter(filter_str: str):
    """`["highway"]["area"!~"yes"]["highway"!~"a|b"]` → предикат tags→bool."""
    raise NotImplementedError("proprietary: removed from public showcase")


def _copy_element(el: dict) -> dict:
    """Неглибока копія елемента з власним dict тегів (списки nodes/members osmnx
    не змінює — лише забирає ключі з dict)."""
    raise NotImplementedError("proprietary: removed from public showcase")


class Bundle:
    """Розібрана відповідь одного union-запиту: віддає шари так само, як osmnx."""

    def __init__(
        self, elements: list[dict], requested_pairs: set[tuple[str, Any]], way_filter: str
    ):
        raise NotImplementedError("proprietary: removed from public showcase")

    @staticmethod
    def _matches(tags: dict, pairs: list[tuple[str, Any]]) -> bool:
        raise NotImplementedError("proprietary: removed from public showcase")

    def _closure(self, top: Iterable[dict]) -> list[dict]:
        """Те, що робить `(._;>;)`: члени relation (way+node) і вузли way."""
        raise NotImplementedError("proprietary: removed from public showcase")

    def features(self, tags: dict, polygon):
        """Аналог `ox.features_from_polygon(polygon, tags)` з пакета."""
        raise NotImplementedError("proprietary: removed from public showcase")

    def graph(
        self,
        polygon,
        *,
        simplify: bool = True,
        retain_all: bool = False,
        truncate_by_edge: bool = False,
    ):
        """Аналог `ox.graph_from_polygon(polygon, network_type='all', …)` з пакета."""
        raise NotImplementedError("proprietary: removed from public showcase")

    def release(self) -> None:
        raise NotImplementedError("proprietary: removed from public showcase")


def _rss_mb() -> float:
    """RSS процесу (Linux); -1, де /proc нема. Для логу: скільки коштує великий пакет."""
    raise NotImplementedError("proprietary: removed from public showcase")


def wait_max_s() -> float:
    """Скільки максимум чекати на джерело, що лягло (0 = не чекати, як раніше)."""
    raise NotImplementedError("proprietary: removed from public showcase")


SOURCE_WAIT_MESSAGE = None


def _fetch_with_recovery(attempt, overpass_health, *, status_cb=None, sleep=None, clock=None):
    """Повторює `attempt`, поки джерело в карантині запобіжника і ще є час."""
    raise NotImplementedError("proprietary: removed from public showcase")


class LazyBundle:
    """Один пакет на генерацію: качається ПРИ ПЕРШОМУ зверненні будь-якого шару."""

    def __init__(
        self,
        *,
        city_bbox: tuple[float, float, float, float],
        extras_bbox: Optional[tuple[float, float, float, float]],
        feature_tags: Iterable[dict],
        extras_tags: Iterable[dict] = None,
        network_type: str = None,
        label: str = None,
        status_cb=None,
    ) -> None:
        raise NotImplementedError("proprietary: removed from public showcase")

    def _fetch(self) -> Bundle:
        raise NotImplementedError("proprietary: removed from public showcase")

    def _ensure(self) -> Bundle:
        raise NotImplementedError("proprietary: removed from public showcase")

    @property
    def fetched(self) -> bool:
        raise NotImplementedError("proprietary: removed from public showcase")

    @property
    def failed(self) -> bool:
        raise NotImplementedError("proprietary: removed from public showcase")

    def features(self, tags: dict, polygon):
        raise NotImplementedError("proprietary: removed from public showcase")

    def graph(self, polygon, **kwargs):
        raise NotImplementedError("proprietary: removed from public showcase")

    def release(self) -> None:
        raise NotImplementedError("proprietary: removed from public showcase")
