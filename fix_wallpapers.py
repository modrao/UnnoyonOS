#!/usr/bin/env python3
"""
fix_wallpapers.py - Run this on WINDOWS before building on Linux.

Does two things:
  1. Copies each UnnoyonOS wallpaper to all required KDE resolution names.
  2. Removes all non-UnnoyonOS wallpaper folders from includes.chroot
     so Debian/KDE defaults never appear in the Settings.

Usage:
    python fix_wallpapers.py
"""

import shutil
from pathlib import Path

WALLPAPERS_DIR = Path(__file__).parent / "UnnoyonOS/config/includes.chroot/usr/share/wallpapers"

# All resolutions KDE Plasma looks for
RESOLUTIONS = [
    "1280x720", "1280x800", "1280x1024",
    "1366x768", "1376x768",
    "1440x900",
    "1600x900", "1600x1024", "1600x1200",
    "1920x1080", "1920x1200",
    "2560x1440", "2560x1600",
    "3840x2160",
]

def fix_wallpaper(wall_dir: Path):
    images_dir = wall_dir / "contents" / "images"
    if not images_dir.exists():
        print(f"  [X] No images/ dir in {wall_dir.name}")
        return

    files = [f for f in images_dir.iterdir() if f.is_file()]
    if not files:
        print(f"  [X] No images found in {wall_dir.name}")
        return

    src = files[0]
    ext = src.suffix

    print(f"  [OK] {wall_dir.name}  (source: {src.name})")
    added = 0
    for res in RESOLUTIONS:
        dest = images_dir / f"{res}{ext}"
        if not dest.exists():
            shutil.copy2(src, dest)
            added += 1
    if added:
        print(f"       -> Added {added} resolution variants")


def main():
    print("=" * 60)
    print("UnnoyonOS Wallpaper Setup")
    print("=" * 60)

    if not WALLPAPERS_DIR.exists():
        print(f"ERROR: {WALLPAPERS_DIR} not found.")
        return

    all_wall_dirs = [d for d in WALLPAPERS_DIR.iterdir() if d.is_dir()]
    unnoyonos_walls = [d for d in all_wall_dirs if d.name.startswith("unnoyonos")]
    other_walls     = [d for d in all_wall_dirs if not d.name.startswith("unnoyonos")]

    # ── Step 1: Remove non-UnnoyonOS wallpapers ──────────────────────────────
    print(f"\n[Step 1] Removing {len(other_walls)} non-UnnoyonOS wallpaper(s)...")
    for w in sorted(other_walls):
        shutil.rmtree(w)
        print(f"  [REMOVED] {w.name}")

    # ── Step 2: Fix resolution variants ──────────────────────────────────────
    print(f"\n[Step 2] Adding resolution variants for {len(unnoyonos_walls)} UnnoyonOS wallpaper(s)...")
    for w in sorted(unnoyonos_walls):
        fix_wallpaper(w)

    print("\nDone! Commit changes and build on Linux.")
    print("Default Debian/KDE wallpapers will not appear in UnnoyonOS.")

if __name__ == "__main__":
    main()
