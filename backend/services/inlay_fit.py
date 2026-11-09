# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class InlayFitConfig:
    insert_side_clearance_mm: float = None
    groove_side_clearance_mm: float = None

    def insert_clearance_m(self, scale_factor: float | None) -> float:
        raise NotImplementedError("proprietary: removed from public showcase")

    def groove_clearance_m(self, scale_factor: float | None) -> float:
        raise NotImplementedError("proprietary: removed from public showcase")
