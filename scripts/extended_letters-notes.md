# Extended Latin drawings

`add_extended_letters(font)` adds 22 Unicode-mapped glyphs to the imported
1400-UPM master. It assumes the approved alphabet still occupies the coordinates
in `glyph-construction.json`; apply production spacing after this function.

Added: AE, ae, OE, oe, Eth, eth, Thorn, thorn, germandbls, uni1E9E,
Dcroat, dcroat, Hbar, hbar, Lslash, lslash, Oslash, oslash, dotlessi,
dotlessj, ordfeminine, ordmasculine.

- The original alphabet is not modified.
- AE/OE share the original E upright; ae/oe retain the angled e bar and hook.
- Stroked forms use unchanged base components with consistently wound crossbars.
- Thorn/thorn reuse the original upright and bowl contours.
- Eth and both sharp-s forms are newly drawn continuous contours.
- Dotless letters remove only the detached high dot contour.
- New paths have normalized winding and explicit duplicate line segments removed.
- Existing tiny cubic fragments can still round into zero-length segments during
  integer TrueType conversion; the final build should remove these after rounding.

Dependencies: ufoLib2, fontTools, skia-pathops. An actual-TTF proof of all additions
was inspected at approximately 300-pixel type size. Source additions compiled
successfully; no adjacent duplicate line points remained in the new contours.
