# Reverse Image Search a Video Across Many Providers

You are given a video file (path or URL). Identify the source, context, and any
matching content on the web by reverse-image-searching representative frames
across a wide variety of providers.

## Inputs

- `VIDEO`: path or URL to the video.
- `MAX_FRAMES` (default `8`): maximum keyframes to extract.
- `OUT_DIR` (default `tmp/ris/<video-stem>/`): where frames and results are saved.

## Steps

1. **Extract keyframes**
   - Use `ffmpeg` scene detection to pick visually distinct frames:
     `ffmpeg -i "$VIDEO" -vf "select='gt(scene,0.4)',scale=1280:-1" -vsync vfr "$OUT_DIR/frame_%03d.jpg"`
   - If fewer than 3 frames are produced, fall back to evenly spaced sampling
     (`fps=1/<duration/MAX_FRAMES>`).
   - Cap at `MAX_FRAMES`. Drop near-duplicates with perceptual hash (`pHash`).

2. **Run reverse image search per frame** across these providers. Open each in
   a browser tab or call its API where available. Record the top 5 hits per
   provider per frame (title, URL, snippet, similarity score if shown).

   General web:
   - Google Images / Google Lens
   - Bing Visual Search
   - Yandex Images (often the strongest for faces and obscure sources)
   - TinEye (best for finding earliest occurrence)
   - Baidu Image Search
   - Sogou Image Search
   - Naver Image Search

   Specialized:
   - SauceNAO (anime, manga, art)
   - IQDB (anime/booru)
   - trace.moe (anime by frame -> exact episode + timestamp)
   - ascii2d (illustrations)
   - Karma Decay (Reddit)
   - PimEyes / FaceCheck.ID (faces — note ToS and consent)
   - Pixsy / Berify (stock and copyright tracking)

3. **Video-native search** (skip frame extraction where supported):
   - YouTube — paste a frame into Google Lens, then filter by `site:youtube.com`.
   - trace.moe accepts a video URL directly.
   - Submit the full video to TikTok / Instagram / X search by uploading or by
     pasting a representative frame.

4. **Aggregate** results into `OUT_DIR/results.json`:
   ```json
   {
     "video": "<path>",
     "frames": [
       {"file": "frame_001.jpg", "timestamp": "00:00:12",
        "matches": [{"provider": "yandex", "url": "...", "title": "...", "score": 0.92}]}
     ],
     "consensus": ["<URLs that appeared across >=2 providers>"]
   }
   ```
   Also write `results.md` with a human-readable summary, ordered by consensus
   strength.

5. **Report** the most likely source, earliest known appearance (TinEye), and
   any conflicting attributions. Flag results that depend on face-recognition
   providers separately so the user can decide whether to trust them.

## Notes

- Prefer API access where keys are available; fall back to opening browser URLs
  with the image attached as a query param or upload.
- Respect each provider's ToS and rate limits. Add a 2–5 s jitter between
  automated requests.
- Some providers (Yandex, Baidu) may require a residential IP or proxy to
  return useful results from outside their region.
- Disable SafeSearch on every provider so adult/graphic matches are not
  filtered out. Examples: Google `&safe=off`, Bing `&adlt=off`, Yandex
  `&family=no`, DuckDuckGo `&kp=-2`, Baidu safe-mode off, Naver `&where=image`
  with adult filter disabled. For API calls, pass the equivalent flag
  (`safeSearch=off`, `safe_search=off`, etc.).
- Save raw HTML/JSON responses under `OUT_DIR/raw/<provider>/` so the run is
  reproducible without re-querying.
