#!/usr/bin/env python3
"""Render the book's manim clips and copy them into assets/video/.

Manim never runs inside `quarto render`. This is a build pass of its own,
exactly parallel to the data-raw/ -> data/ convention: source of truth in
manim/, generated artefact committed in assets/video/.

    python manim/build.py            # re-render only what is out of date
    python manim/build.py ch01       # one chapter
    python manim/build.py --force    # ignore mtimes

For every scene it renders the mp4 and, separately, the final frame as a PNG
poster. The poster is what a PDF reader sees, so a well-built scene ends on
exactly the static figure the print reader needs.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "assets" / "video"
MEDIA = HERE / "media"

QUALITY = "-qh"          # 1920x1080, 60fps ceiling; see plan section D3
MAX_SECONDS = 90         # inline clips longer than this get a warning

# (module, SceneClass, asset stem). The manifest is the single registry of
# every clip in the book; a duplicate stem is a duplicate key and is caught
# here rather than by two files quietly overwriting each other.
MANIFEST: list[tuple[str, str, str]] = [
    ("ch01_matrix_algebra", "Ch01MatMul", "ch01-matmul"),
]


def venv_manim() -> list[str]:
    """Prefer an explicit venv, fall back to whatever manim is on PATH."""
    for candidate in (HERE / "venv" / "bin" / "manim",
                      Path.home() / "Claude" / "manim_test" / "venv" / "bin" / "manim"):
        if candidate.exists():
            return [str(candidate)]
    return ["manim"]


def check_manifest() -> None:
    stems = [m[2] for m in MANIFEST]
    dupes = {s for s in stems if stems.count(s) > 1}
    if dupes:
        sys.exit(f"ERROR: duplicate asset stems in MANIFEST: {sorted(dupes)}")


def objective_line(module: str, scene: str) -> str | None:
    """Every clip states its learning objective in its docstring."""
    src = (HERE / f"{module}.py").read_text()
    m = re.search(rf"class {scene}\(.*?\):\s*\"\"\"(.*?)\"\"\"", src, re.S)
    if not m:
        return None
    hit = re.search(r"#\s*Ch \d+, objective \d+", m.group(1))
    return hit.group(0) if hit else None


def newest(paths) -> float:
    times = [p.stat().st_mtime for p in paths if p.exists()]
    return max(times) if times else 0.0


def up_to_date(module: str, stem: str) -> bool:
    mp4 = OUT / f"{stem}.mp4"
    png = OUT / f"{stem}.png"
    if not (mp4.exists() and png.exists()):
        return False
    src = newest([HERE / f"{module}.py", *(HERE / "ambook").glob("*.py")])
    return min(mp4.stat().st_mtime, png.stat().st_mtime) > src


def find_output(subdir: str, scene: str, suffix: str) -> Path | None:
    root = MEDIA / subdir
    if not root.exists():
        return None
    hits = sorted(root.rglob(f"{scene}*{suffix}"), key=lambda p: p.stat().st_mtime)
    return hits[-1] if hits else None


def duration(mp4: Path) -> float | None:
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=nw=1:nk=1", str(mp4)],
            capture_output=True, text=True, check=True,
        )
        return float(out.stdout.strip())
    except Exception:
        return None


def render(module: str, scene: str, stem: str) -> None:
    manim = venv_manim()
    module_file = f"{module}.py"

    print(f"  rendering {scene} -> {stem}.mp4")
    subprocess.run(manim + [QUALITY, "--format=mp4", module_file, scene],
                   cwd=HERE, check=True)
    print(f"  rendering {scene} -> {stem}.png  (final frame, the PDF poster)")
    subprocess.run(manim + [QUALITY, "-s", module_file, scene],
                   cwd=HERE, check=True)

    OUT.mkdir(parents=True, exist_ok=True)
    mp4 = find_output("videos", scene, ".mp4")
    png = find_output("images", scene, ".png")
    if mp4 is None:
        sys.exit(f"ERROR: no mp4 produced for {scene}")
    if png is None:
        sys.exit(f"ERROR: no poster produced for {scene}")
    shutil.copy2(mp4, OUT / f"{stem}.mp4")
    shutil.copy2(png, OUT / f"{stem}.png")

    secs = duration(OUT / f"{stem}.mp4")
    if secs is not None:
        print(f"    {secs:.1f}s, {(OUT / f'{stem}.mp4').stat().st_size / 1e6:.1f} MB")
        if secs > MAX_SECONDS:
            print(f"    WARNING: {stem} runs {secs:.0f}s (over {MAX_SECONDS}s). "
                  "One idea per clip — consider splitting it.")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("prefix", nargs="?", default="",
                    help="only build stems starting with this (e.g. ch01)")
    ap.add_argument("--force", action="store_true", help="ignore mtimes")
    args = ap.parse_args()

    check_manifest()
    selected = [m for m in MANIFEST if m[2].startswith(args.prefix)]
    if not selected:
        sys.exit(f"No clips match prefix {args.prefix!r}")

    built = skipped = 0
    for module, scene, stem in selected:
        if objective_line(module, scene) is None:
            print(f"  WARNING: {scene} has no '# Ch N, objective N' line in its "
                  "docstring. A clip that cannot name its objective is a clip "
                  "we do not need.")
        if not args.force and up_to_date(module, stem):
            print(f"  {stem}: up to date")
            skipped += 1
            continue
        render(module, scene, stem)
        built += 1

    print(f"\n{built} built, {skipped} up to date -> {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
