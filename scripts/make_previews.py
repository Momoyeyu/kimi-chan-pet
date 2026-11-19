#!/usr/bin/env python3
"""Rebuild the README animation previews from the packaged spritesheet."""

from pathlib import Path
import json
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "kimi-chan" / "pet.json"
SHEET_PATH = ROOT / "kimi-chan" / "spritesheet.png"
ASSETS = ROOT / "assets"
BACKGROUND = (247, 243, 255, 255)


def make_gif(sheet: Image.Image, manifest: dict, state_name: str) -> Path:
    state = manifest["states"][state_name]
    atlas = manifest["atlas"]
    width = atlas["frameWidth"]
    height = atlas["frameHeight"]
    frames = []
    for column in range(state["frames"]):
        box = (
            column * width,
            state["row"] * height,
            (column + 1) * width,
            (state["row"] + 1) * height,
        )
        sprite = sheet.crop(box).convert("RGBA")
        canvas = Image.new("RGBA", (width + 32, height + 32), BACKGROUND)
        canvas.alpha_composite(sprite, (16, 16))
        frames.append(canvas.convert("P", palette=Image.Palette.ADAPTIVE, colors=255))
    target = ASSETS / f"{state_name}-preview.gif"
    frames[0].save(
        target,
        save_all=True,
        append_images=frames[1:],
        duration=round(1000 / state["fps"]),
        loop=0,
        optimize=True,
    )
    return target


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    sheet = Image.open(SHEET_PATH).convert("RGBA")
    for state_name in ("idle", "flute_playing"):
        print(make_gif(sheet, manifest, state_name))


if __name__ == "__main__":
    main()
