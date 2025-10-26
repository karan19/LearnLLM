#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
YouTube transcripts to .txt (English/Hindi/Telugu), using youtube-transcript-api 1.2.x.

- Public API only (no private _errors imports).
- Prefers manual captions; falls back to auto.
- Language priority: EN ('en') → HI ('hi') → TE ('te').
- Accepts IDs or full URLs; or a file with one per line.
- Writes: <out_dir>/<YYYY-MM-DD>/<video_title>.txt  (title sanitized; deduped)
"""

import argparse
import os
import re
import sys
import time
from datetime import datetime
from typing import List, Tuple, Optional, Dict

from youtube_transcript_api import YouTubeTranscriptApi  # public API only

try:
    from tqdm import tqdm  # optional
except Exception:
    tqdm = None

PREFERRED_LANGS = ["en", "hi", "te"]
YID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")
YID_FROM_URL = re.compile(r"(?:v=|youtu\.be/|shorts/)([A-Za-z0-9_-]{11})")

_INVALID_CHARS = set('<>:"/\\|?*')


def extract_id(s: str) -> Optional[str]:
    s = s.strip()
    if not s:
        return None
    if YID_RE.match(s):
        return s
    m = YID_FROM_URL.search(s)
    return m.group(1) if m else None


def get_video_title(video_id: str) -> Optional[str]:
    """Use yt-dlp metadata extraction to get the YouTube title (no download)."""
    try:
        import yt_dlp
    except Exception:
        return None
    url = f"https://www.youtube.com/watch?v={video_id}"
    ydl_opts = {"quiet": True, "skip_download": True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
        title = info.get("title")
        if isinstance(title, str):
            return title.strip().replace("\n", " ")
    except Exception:
        return None
    return None


def safe_filename(name: str, max_length: int = 150) -> str:
    """Sanitize a title for filesystem use (cross-platform-ish)."""
    if not name:
        return "video"
    # Remove control chars
    name = "".join(ch for ch in name if 31 < ord(ch) != 127)
    # Replace invalid chars with underscore
    name = "".join(("_" if ch in _INVALID_CHARS else ch) for ch in name)
    # Collapse whitespace
    name = re.sub(r"\s+", " ", name).strip()
    # Trim length, avoid trailing dot/space
    return name[:max_length].rstrip(" .")


def unique_path(dir_path: str, base_name: str) -> str:
    """Avoid overwriting by appending (2), (3)... if needed."""
    stem, ext = os.path.splitext(base_name)
    candidate = os.path.join(dir_path, base_name)
    if not os.path.exists(candidate):
        return candidate
    i = 2
    while True:
        candidate = os.path.join(dir_path, f"{stem} ({i}){ext}")
        if not os.path.exists(candidate):
            return candidate
        i += 1


def to_plain_text(snippets: List[Dict]) -> str:
    lines: List[str] = []
    for seg in snippets:
        t = (seg.get("text") or "").strip()
        if t:
            lines.append(t)
    return ("\n".join(lines).strip() + "\n") if lines else ""


def reason(exc: Exception) -> str:
    """
    Map exceptions to clear, user-friendly reasons without relying on private classes.
    We inspect the message text (library surfaces clear, stable messages).
    """
    msg = (str(exc) or "").lower()

    if "subtitles are disabled" in msg:
        return "Subtitles are disabled by the uploader."
    if "no transcripts are available" in msg or "no transcript could be found" in msg:
        return "No subtitles exist for this video."
    if "no transcripts were found for any of the requested language codes" in msg:
        return "No subtitles found in requested languages (en/hi/te)."
    if "the video is no longer available" in msg or "video is unavailable" in msg:
        return "Video is unavailable (private, deleted, or blocked)."
    if "age" in msg and "restrict" in msg:
        return "Age-restricted video (requires login)."
    if "too many requests" in msg or "429" in msg:
        return "Rate-limited by YouTube (429 Too Many Requests)."
    if "not been made available in your country" in msg or "country" in msg and "available" in msg:
        return "Location-restricted (not available in your country)."
    if "unplayable" in msg:
        return "Video is unplayable (refused by YouTube)."

    # Fallback with the raw exception type + message
    return f"{exc.__class__.__name__}: {str(exc) or 'Unknown error'}"


def fetch_one(api: YouTubeTranscriptApi, vid: str, out_dir: str, sleep_sec: float = 0.0) -> Tuple[bool, str]:
    # List available transcript tracks (instance API in 1.2.x)
    try:
        tlist = api.list(vid)  # TranscriptList
    except Exception as e:
        return False, reason(e)

    # Prefer manual in en/hi/te, then auto in en/hi/te
    try:
        tr = tlist.find_manually_created_transcript(PREFERRED_LANGS)
        is_generated = False
    except Exception:
        try:
            tr = tlist.find_generated_transcript(PREFERRED_LANGS)
            is_generated = True
        except Exception as e:
            # Surface what's available to be helpful
            available = []
            try:
                for tx in tlist:
                    kind = "auto" if tx.is_generated else "manual"
                    available.append(f"{tx.language_code} ({kind})")
            except Exception:
                pass
            if available:
                return False, f"No en/hi/te subtitles. Available: {', '.join(sorted(set(available)))}"
            return False, reason(e)

    # Fetch transcript data
    try:
        fetched = tr.fetch()
        raw = fetched.to_raw_data() if hasattr(fetched, "to_raw_data") else fetched
    except Exception as e:
        return False, reason(e)

    # Prepare output path using date folder + video title
    date_folder = datetime.now().strftime("%Y-%m-%d")
    final_dir = os.path.join(out_dir, date_folder)
    try:
        os.makedirs(final_dir, exist_ok=True)
    except Exception as e:
        return False, f"Failed to create output directory: {e}"

    title = get_video_title(vid) or vid  # fallback to ID if title can't be fetched
    safe_title = safe_filename(title)
    base_name = f"{safe_title}.txt"
    out_path = unique_path(final_dir, base_name)

    # Convert to plain text and write
    text = to_plain_text(raw)
    try:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        return False, f"Failed to write file: {e}"

    if sleep_sec > 0:
        time.sleep(sleep_sec)

    # Return path relative to base out_dir for a tidy summary
    rel = os.path.relpath(out_path, start=out_dir)
    return True, f"Saved {rel}"


def read_ids(path: str) -> List[str]:
    ids: List[str] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            vid = extract_id(line)
            if vid:
                ids.append(vid)
            else:
                print(f"Warning: could not parse a video ID from line: {line.strip()}", file=sys.stderr)
    return ids


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Download YouTube transcripts (en/hi/te) as .txt with clear failure reasons.")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--ids", nargs="+", help="One or more YouTube IDs or URLs.")
    g.add_argument("--file", help="Path to a file containing one ID/URL per line.")
    p.add_argument("--out", default="transcripts_out", help="Base output directory (default: transcripts_out)")
    p.add_argument("--sleep", type=float, default=0.0, help="Seconds to sleep between requests (avoid rate limits).")
    return p.parse_args()


def main():
    args = parse_args()
    raw = args.ids if args.ids else read_ids(args.file)

    vids: List[str] = []
    for item in raw:
        vid = extract_id(item)
        if not vid:
            print(f"ERROR: Could not extract a valid YouTube ID from: {item}", file=sys.stderr)
        else:
            vids.append(vid)

    if not vids:
        print("No valid video IDs to process.", file=sys.stderr)
        sys.exit(2)

    api = YouTubeTranscriptApi()  # 1.2.x instance API
    successes, failures = [], []

    iterator = tqdm(vids, desc="Processing", unit="video") if tqdm else vids
    for vid in iterator:
        ok, msg = fetch_one(api, vid, args.out, sleep_sec=args.sleep)
        if tqdm:
            iterator.set_postfix_str(msg[:50])
        else:
            print(f"{vid}: {msg}")
        (successes if ok else failures).append(vid if ok else (vid, msg))

    print("\n=== Summary ===")
    print(f"Total: {len(vids)} | Succeeded: {len(successes)} | Failed: {len(failures)}")
    if successes:
        print("Successful IDs:\n  " + ", ".join(successes))
    if failures:
        print("\nFailures:")
        for vid, why in failures:
            print(f"  {vid}: {why}")

    print("\nNotes:")
    print(" - Files are saved under <out_dir>/<YYYY-MM-DD>/<video_title>.txt")
    print(" - Only English ('en'), Hindi ('hi'), and Telugu ('te') are attempted.")
    print(" - For better titles, install 'yt-dlp' (optional).")
    print(" - Live/age/region/unplayable videos are reported and skipped (out of scope).")


if __name__ == "__main__":
    main()
