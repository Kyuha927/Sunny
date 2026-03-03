from __future__ import annotations

import argparse
import ctypes
import time
from pathlib import Path

import pyautogui


def esc_pressed() -> bool:
    try:
        return bool(ctypes.windll.user32.GetAsyncKeyState(0x1B) & 0x8000)
    except Exception:
        return False


def wait_interruptible(seconds: float) -> bool:
    end = time.time() + max(0.0, seconds)
    while time.time() < end:
        if esc_pressed():
            return False
        time.sleep(0.05)
    return True


def read_text(path: Path) -> str:
    for enc in ("utf-8", "utf-8-sig", "cp949", "euc-kr", "latin-1"):
        try:
            return path.read_text(encoding=enc)
        except Exception:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def set_clipboard(text: str) -> None:
    import tkinter as tk

    root = tk.Tk()
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    root.destroy()


def main() -> int:
    parser = argparse.ArgumentParser(description="Auto paste prompt packets to focused Perplexity input")
    parser.add_argument("--out-dir", default=r"C:\Users\jhk92\OneDrive\문서\Obsidian Vault\copilot\perplexity-tools\out")
    parser.add_argument("--start", type=int, default=0, help="1-based start index. 0 means cursor+1")
    parser.add_argument("--count", type=int, default=0, help="0 means all remaining")
    parser.add_argument("--start-delay", type=float, default=4.0, help="Seconds before first paste")
    parser.add_argument("--between-delay", type=float, default=35.0, help="Seconds between sends")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    if not out_dir.exists():
        print(f"[FAIL] out dir not found: {out_dir}")
        return 1

    files = sorted([p for p in out_dir.glob("*.prompt.md") if p.is_file()])
    if not files:
        print("[FAIL] no prompt files")
        return 1

    cursor_path = out_dir / ".cursor.txt"
    start = args.start
    if start <= 0:
        if cursor_path.exists():
            raw = cursor_path.read_text(encoding="utf-8", errors="ignore").strip()
            if raw.isdigit():
                start = int(raw) + 1
        if start <= 0:
            start = 1

    if start > len(files):
        print(f"[DONE] start({start}) > file count({len(files)})")
        return 0

    end = len(files) if args.count <= 0 else min(len(files), start + args.count - 1)
    targets = [(idx, files[idx - 1]) for idx in range(start, end + 1)]

    print(f"[INFO] total files={len(files)}, sending {len(targets)} from index={start} to {end}")
    print("[INFO] Focus Perplexity input now. ESC to abort.")
    if not wait_interruptible(args.start_delay):
        print("[STOP] interrupted before start")
        return 1

    pyautogui.PAUSE = 0.02

    for i, (index, path) in enumerate(targets, start=1):
        if esc_pressed():
            print("[STOP] interrupted by ESC")
            return 1

        content = read_text(path)
        set_clipboard(content)
        if not wait_interruptible(0.15):
            print("[STOP] interrupted before paste")
            return 1

        pyautogui.hotkey("ctrl", "v")
        if not wait_interruptible(0.05):
            print("[STOP] interrupted before enter")
            return 1

        pyautogui.press("enter")
        cursor_path.write_text(str(index), encoding="utf-8")
        print(f"[OK] sent {index:03d}/{len(files)} -> {path.name}")

        if i < len(targets):
            if not wait_interruptible(args.between_delay):
                print("[STOP] interrupted during between-delay")
                return 1

    print("[DONE] completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
