# Candidate 1.000 — September 25, 2026

- Preserved the approved 0.13 capital/lowercase/figure artwork and custom traced G, J and Q.
- Imported canonical cubic vectors to editable UFO; regular builds no longer retrace photographs.
- Expanded from 85 mapped characters to 338, including every GF Latin Core entry, plus extra accents, rupee and controls.
- Added a double-harpoon dollar based on S, J-derived barbs on both ends of the percent diagonal, a nautical asterisk, barbed parentheses and a matching number sign.
- Added family-specific diacritics and positioned composites, real curly quotes, extended Latin letters, punctuation and currencies.
- Added dot removal before upper accents, mark/mkmk positioning and tabular-figure alternates.
- Kept zero's O outline while giving it a separate character glyph.
- Replaced uniform sidebearings with optical spacing, 161 class-aware kerning entries and equivalent kerning for accented letters.
- Normalized units per em from 1400 to 2048 with proportionate scaling; this does not change relative letter size.
- Corrected actual outline sidebearings, Win/typo/hhea metrics, regular/style flags, gasp, STAT and script metadata.
- Removed unintended wave-dash tracing seams and sub-unit quantization burrs; retained deliberate barbs and pointed terminals.
- Prepared installable TTF, compressed WOFF2, deterministic build, offline tester, complete glyph sheet and current QA.
- Prepared initial OFL proposal and submission draft.

# Release finalization — September 25, 2026

- Owner applied SIL OFL 1.1 and submitted the individual Google CLA.
- Updated source, binary, OFL and description to reference https://github.com/SkylarkingMonkey/Siren-and-Sailor-Font.
- Rebuilt the TTF and WOFF2 and reran coverage, shaping, spacing and Fontspector checks. The external namecheck service was unreachable from this environment; warnings and designer review remain.
- Corrected the build script to stage the finalized root `OFL.txt` when present.
