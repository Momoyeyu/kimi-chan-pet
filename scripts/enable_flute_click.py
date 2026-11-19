#!/usr/bin/env python3
"""Enable the optional click-triggered flute action for an installed Kimi Pet."""

from __future__ import annotations

import argparse
from datetime import datetime
import json
from pathlib import Path
import sys

PET_ID = "kimi-chan"
MARKER = "playFluteOnClick"
DEFAULT_WIDGETS_ROOT = Path.home() / (
    "Library/Application Support/kimi-desktop/daimon-share/daimon/"
    "agents/main/blueprint/widgets"
)
NEEDLE = "    function tick(now) {\n      animationFrameRequest = 0;"
SNIPPET = """    function playFluteOnClick(event) {
      if (!manifest || isThreeManifest(manifest) || !manifest.states.flute_playing) return;
      if (reducedMotion.matches || event.detail.button !== 0 || stateName === 'flute_playing') return;
      const stageBounds = stage.getBoundingClientRect();
      const petBounds = pet.getBoundingClientRect();
      const clientX = stageBounds.left + event.detail.normalizedX * stageBounds.width;
      const clientY = stageBounds.top + event.detail.normalizedY * stageBounds.height;
      const insidePet =
        clientX >= petBounds.left &&
        clientX <= petBounds.right &&
        clientY >= petBounds.top &&
        clientY <= petBounds.bottom;
      if (!insidePet) return;
      clearIdleVariantTimer();
      interactionStateActive = true;
      setState('flute_playing');
      restartAnimationSchedule();
    }

    stage.addEventListener(CLICK_MESSAGE_TYPE, playFluteOnClick);

    // Fallback for Kimi Work hosts that forward real DOM pointer events into
    // the pet iframe instead of posting daimon-pet:click messages: drive the
    // same action from DOM clicks (>=6px movement is a host-handled drag).
    let fluteDomDownPos = null;
    document.addEventListener('pointerdown', (event) => {
      fluteDomDownPos = { x: event.clientX, y: event.clientY };
    }, true);
    document.addEventListener('click', (event) => {
      if (!manifest || isThreeManifest(manifest) || !manifest.states.flute_playing) return;
      if (reducedMotion.matches || event.button !== 0 || stateName === 'flute_playing') return;
      const moved = fluteDomDownPos
        ? Math.hypot(event.clientX - fluteDomDownPos.x, event.clientY - fluteDomDownPos.y)
        : 0;
      if (moved >= 6) return;
      if (event.target !== stage && event.target !== pet && event.target !== document.body) return;
      const petBounds = pet.getBoundingClientRect();
      if (
        event.clientX < petBounds.left ||
        event.clientX > petBounds.right ||
        event.clientY < petBounds.top ||
        event.clientY > petBounds.bottom
      ) return;
      clearIdleVariantTimer();
      interactionStateActive = true;
      setState('flute_playing');
      restartAnimationSchedule();
    }, true);"""


def find_installed_runtime(widgets_root: Path) -> tuple[Path, dict]:
    """Find the installed pet by id without guessing a widget id."""
    if not widgets_root.is_dir():
        raise RuntimeError(f"Widget directory does not exist: {widgets_root}")
    for manifest_path in sorted(widgets_root.glob("*/workspace/pet.json")):
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if manifest.get("id") != PET_ID:
            continue
        if "flute_playing" not in manifest.get("states", {}):
            raise RuntimeError(
                "The installed pet is kimi-chan, but its flute_playing state is missing. "
                "Install the complete package from this repository first."
            )
        runtime = manifest_path.with_name("index.html")
        if not runtime.is_file():
            raise RuntimeError(f"Installed runtime is missing: {runtime}")
        return runtime, manifest
    raise RuntimeError(
        "No installed kimi-chan pet was found. Install the package in Kimi Work first, "
        "or pass the correct --widgets-root directory."
    )


def enable_click(widgets_root: Path) -> str:
    runtime, _manifest = find_installed_runtime(widgets_root)
    source = runtime.read_text(encoding="utf-8")
    if MARKER in source:
        return f"Already enabled; no changes made: {runtime}"
    if source.count(NEEDLE) != 1:
        raise RuntimeError(
            "The installed Pet runtime has an unsupported layout. No changes were made. "
            "Please ask Kimi Work to add the flute click listener manually."
        )
    updated = source.replace(NEEDLE, SNIPPET + "\n\n" + NEEDLE, 1)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = runtime.with_name(f"index.html.backup-{timestamp}")
    backup.write_text(source, encoding="utf-8")
    runtime.write_text(updated, encoding="utf-8")
    return (
        f"Enabled flute click: {runtime}\n"
        f"Backup saved: {backup}\n"
        "Hide and show the pet again, then left-click the character to play."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--widgets-root",
        type=Path,
        default=DEFAULT_WIDGETS_ROOT,
        help="Blueprint widgets directory (defaults to the macOS Kimi Work location)",
    )
    args = parser.parse_args()
    try:
        print(enable_click(args.widgets_root.expanduser()))
        return 0
    except RuntimeError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
