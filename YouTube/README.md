# YouTube

Log takeaways from video resources. Suggested pattern: one markdown file per channel or playlist with timestamps, links, and key insights.

## Extract subtitles locally

### Virtual environment setup

```bash
python -m venv YTST
source YTST/bin/activate  # macOS/Linux
```

## Virtual Environment Usage

Always work within the activated Python virtual environment to ensure dependencies remain isolated. Each time you open a new shell, activate the environment with:

```bash
# macOS/Linux
source YTST/bin/activate
# Windows PowerShell
.\YTST\Scripts\activate
```

Requirements:
- pip install yt-dlp
- Optional progress bar: `pip install tqdm`

Usage:
```bash
cd YouTube
python subtitle_extractor.py --ids 'https://www.youtube.com/watch?v=yaPOxsZsB90'
python subtitle_extractor.py --file ids.txt --out transcripts_out --sleep 0.5
```

Key details:
- Accepts multiple IDs/URLs via `--ids` or reads one per line from `--file`.
- Saves plaintext transcripts under `<out_dir>/<YYYY-MM-DD>/<video_title>.txt`.
- Prioritizes English → Hindi → Telugu and falls back from manual to auto captions.
- Emits helpful reasons when captions are missing, rate-limited, or restricted.
