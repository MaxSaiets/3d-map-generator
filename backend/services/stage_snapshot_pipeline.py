# ---------------------------------------------------------------------------
# PROPRIETARY: implementation removed from the public showcase.
# The public interface (names, signatures, docstrings) is kept so the
# architecture stays readable. Full source is available on request.
# ---------------------------------------------------------------------------
from __future__ import annotations
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional
from services.debug_renderers import render_mesh_top_png, render_overlay_png
from services.geometry_diagnostics import ensure_valid_geometry


@dataclass
class StageSnapshotCollector:
    task_id: str
    run_dir: Path
    zone_prefix: str = None
    entries: list[dict[str, Any]] = None

    def _safe_rel(self, path: Optional[Path]) -> Optional[str]:
        raise NotImplementedError("proprietary: removed from public showcase")

    def _register(self, stage: str, name: str, path: Optional[Path]) -> None:
        raise NotImplementedError("proprietary: removed from public showcase")

    def _safe_overlay(self, stage: str, name: str, layers: list[dict[str, Any]]) -> Optional[Path]:
        raise NotImplementedError("proprietary: removed from public showcase")

    def _safe_mesh(self, stage: str, name: str, mesh: Any) -> Optional[Path]:
        raise NotImplementedError("proprietary: removed from public showcase")

    def capture_canonical(self, canonical_mask_bundle: Any) -> None:
        raise NotImplementedError("proprietary: removed from public showcase")

    def capture_terrain_stage(self, terrain_stage: Any) -> None:
        raise NotImplementedError("proprietary: removed from public showcase")

    def capture_detail_stage(self, detail_layers: Any) -> None:
        raise NotImplementedError("proprietary: removed from public showcase")

    def capture_postprocess_stage(self, postprocess_result: Any) -> None:
        raise NotImplementedError("proprietary: removed from public showcase")

    def capture_clip_stage(self, clip_result: Any) -> None:
        raise NotImplementedError("proprietary: removed from public showcase")

    def capture_merge_stage(self, merge_result: Any) -> None:
        raise NotImplementedError("proprietary: removed from public showcase")

    def capture_export_stage(self, export_result: Any) -> None:
        raise NotImplementedError("proprietary: removed from public showcase")

    def finalize(self) -> Path:
        raise NotImplementedError("proprietary: removed from public showcase")


def create_stage_snapshot_collector(
    *, task_id: str, debug_root: Path, zone_prefix: str = None
) -> StageSnapshotCollector:
    raise NotImplementedError("proprietary: removed from public showcase")
