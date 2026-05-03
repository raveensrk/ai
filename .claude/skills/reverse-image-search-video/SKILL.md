---
name: reverse-image-search-video
description: Reverse image search a video across many providers (Google Lens, Bing, Yandex, TinEye, SauceNAO, trace.moe, DuckDuckGo, etc.). Use when the user wants to identify the source, context, or earliest appearance of a video, find where a clip originated, or locate matches across multiple search engines. Triggers on phrases like "reverse image search this video", "find the source of this video", "where is this clip from", "search this video everywhere".
---

# Reverse Image Search Video

Read `prompts/reverse_image_search_video.md` (relative to the repo root) and
follow it exactly. That file is the single source of truth shared across
Claude, Codex, and Gemini. If the user supplied a video path/URL or other
arguments, treat them as the `VIDEO`, `MAX_FRAMES`, and `OUT_DIR` inputs
defined there.
