# REVIEW — GTA VI in 45 seconds (fan-made explainer)

Render: `renders/gta6-explainer.mp4` — 1080×1920, 30 fps, 48.6 s, 4.9 MB.

## Creative calls
- Picked an educational explainer (user gave carte blanche) instead of storylines A/B/C in STORYLINES.md
  (those were ad-style; the user asked for an educational video).
- Look: screen-printed travel poster: flat inks (pink, orange, ocean, sea, sand, ink), 10 px
  misregistration shadows on hero type, halftone dots on the sun. League Gothic + Inter.
- Rights: no Rockstar logo, logotype, typeface, artwork, trailer frames, character likeness, music or
  voice. Lucia & Jason appear only as typeset names. Disclaimer on the end card.
- Voice: local Kokoro TTS (am_michael, ×1.1), English. Line 3 rewritten ("sequel's" was mispronounced).
- No music bed: no music source without a HeyGen sign-in, and the user's request for the game's own
  soundtrack was declined (copyrighted). Sound = voice + bundled effects on visible actions.
- Layout is left-aligned inside TikTok's safe area (y 240–1260; x 120–780 below y 840 because of the
  right-hand button rail). Bottom third holds only decoration (TikTok's own UI covers it).

## Measured
- `check`: ok, 0 errors. Kept warnings: `outside_safe_zone` top edge on "13", "GTA V", "LEONIDA",
  "GTA VI" for Shorts/Reels (glyph boxes start at 310–320 px; Shorts wants 288 px of glyph clearance —
  the visible glyph tops sit ~345 px). TikTok, the target, only flags "13" by its line box.
- Loudness after delivery normalisation (ffmpeg loudnorm on the final mix): −15.0 LUFS, true peak
  −1.4 dBFS. The project mix itself renders at −19.9 LUFS: re-run the same loudnorm after a re-render.
- Sound was measured, not heard.

## Facts on screen (as reported by press, checked 2026-11-17)
GTA V: Sept 2013, 200M+ copies. Trailer 1: Dec 2023, 90M+ views in 24 h. Setting: Leonida (fictional
Florida), Vice City. Leads: Lucia & Jason. Dates: 2025 → May 26 2026 → Nov 19 2026. PS5 + Xbox Series X|S,
no PC date. Re-check the release date before posting if time has passed.

## Weakest shot / next
- Scene 4 map: the mainland's straight top edge reads as a cut-out box; a ragged state border would read
  more like a map.
- Lower third is empty by design (TikTok UI) — on YouTube or Instagram it looks bare; a landscape or
  Shorts cut would need its own layout.
- With a HeyGen sign-in: a synthwave music bed under the voice (~0.14 volume) and a more natural voice.
