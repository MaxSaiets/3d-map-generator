# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from dataclasses import dataclass, replace
from typing import Any


@dataclass(frozen=True)
class PrinterProfile:
    printer_model: str
    nozzle_diameter_mm: float
    nominal_line_width_mm: float
    external_line_width_mm: float
    first_layer_line_width_mm: float
    groove_side_clearance_mm: float
    min_printable_feature_mm: float
    tiny_cleanup_mm: float
    road_gap_fill_mm: float
    acute_corner_collapse_mm: float
    terrain_boolean_overcut_mm: float
    elephant_foot_compensation_mm: float

    def with_overrides(
        self,
        *,
        nozzle_diameter_mm: float | None = None,
        groove_side_clearance_mm: float | None = None,
        min_printable_feature_mm: float | None = None,
        road_gap_fill_mm: float | None = None,
        elephant_foot_compensation_mm: float | None = None,
    ) -> "PrinterProfile":
        raise NotImplementedError("proprietary: removed from public showcase")


DEFAULT_BAMBU_P1S_04 = None


def get_default_printer_profile() -> PrinterProfile:
    raise NotImplementedError("proprietary: removed from public showcase")


def get_printer_profile_for_request(request: Any | None) -> PrinterProfile:
    raise NotImplementedError("proprietary: removed from public showcase")
