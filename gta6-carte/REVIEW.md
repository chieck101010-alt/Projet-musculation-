# REVIEW — GTA VI, version carte (FR, fan-made)

Render: `renders/gta6-carte.mp4` — 1080×1920, 30 fps, 42.6 s, ~12 MB, −15 LUFS / −1.5 dBTP.

## Creative calls
- Style taken from the user's reference TikTok (@c_clair0): a city map as the ground with a continuous
  camera, colour themes per section (night violet → day → sunset → night), pins on the map, a small
  label pill at the bottom, interface cards, and a closing poll.
- Content = the facts of `gta6-hype` (13 years, GTA V 2013 / 200M+, trailer 90M views in 24 h,
  Leonida / Vice City, Lucia & Jason, 2025 → May 2026 → Nov 19 2026, PS5 / Xbox Series, no PC date),
  rewritten in French in my own words. The reference's script was not reused.
- Rights: the user supplied official Rockstar artwork (key art with the characters, cover art, logo)
  and a fan-made map. None of it is in the film. The map is an invented geography generated in code
  (`compositions/map.html`); the leads are letter pins (L / J) with their names, no likeness.
- Voice: local Kokoro `ff_siwis` (French), ×1.1. Phonetic spellings in `assets/voice/script.tsv`
  ("Vaïsse Siti", "Ixe boxe Séries", "bande-annonce") because the French phonemiser mangled the
  English names. No music bed (no source without a HeyGen sign-in).

## Measured
- `check`: ok, 0 errors; kept warning `gsap_repeated_fromto_without_baseline` on the two counter
  proxies (plain objects, no DOM state).
- Loudness after delivery normalisation: −15.0 LUFS, true peak −1.5 dBFS. Measured, not heard.

## Weakest / next
- The night-theme close-up (0–16 s) is a dark field with a violet street grid; brighter roads or a
  slower reveal of the wider map would read better.
- The invented map is simple (blob coast, few highways); more districts and named areas would add life.
