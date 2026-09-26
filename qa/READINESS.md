# Siren and Sailor — submission readiness

Prepared September 25, 2026. Candidate 1.000. Designer: Jean-Marc Daecius.

The owner pushed the initial project to `https://github.com/SkylarkingMonkey/Siren-and-Sailor-Font`, applied SIL OFL 1.1 with the project's explicit approval flag, and reports submitting the Google Individual CLA. The source, rebuilt binaries, root/staged OFL files and description now use the same project copyright and repository URL. Public visibility has not been verified; the updated project files still need to be committed and pushed from the owner's Mac. Google has not received or accepted a submission.

## Verified technical result

| Check | Result |
| --- | --- |
| Glyphs / encoded characters | 352 / 338 |
| GF Latin Core (glyphsets 1.1.3) | 319 of 319 required Unicode entries |
| Precomposed vs decomposed shaping | 145 equivalence cases pass |
| Missing glyphs in sample strings | None |
| Incorrect left sidebearings / Win metric clipping | None |
| Tabular figures | Ten equal-width alternatives, 1336-unit advance |
| Character-pair near-collision audit | 5,476 tested pairs, zero below the 14-unit threshold |
| TTF and WOFF2 Unicode mappings | Match |
| Staged TTF / distributable TTF | Identical |

Fontspector **1.8.0**, full `googlefonts` profile with no exclusions: **121 PASS, 10 INFO, 5 WARN, 0 FAIL, 77 SKIP, 1 ERROR, 0 FATAL**. The one ERROR is the external `fontdata_namecheck` service: this execution environment could not reach `http://namecheck.fontdata.com/`. It is not a font-outline or license failure, but the name-uniqueness check has not passed on this final run. The earlier candidate's namecheck passed before the license update; rerun it on a network where the service is accessible. Raw JSON, HTML, Markdown and log are included.

## Warnings to review

- **outline_jaggy_segments:** deliberate pointed hooks and barbs also trigger the heuristic; Google may request optical refinements.
- **outline_semi_vertical:** some stems/crossbars differ by approximately one or two units from a perfect axis.
- **googlefonts/glyphsets/shape_languages:** some auxiliary orthographies extend beyond GF Latin Core.
- **googlefonts/metadata/unreachable_subsetting:** actual catalog subset declarations are not yet present; catalog metadata is an undated template until intake.
- **googlefonts/vendor_id:** the vendor ID is `NONE`, not a registered foundry code.

The Google catalog `METADATA.pb` has not been created because its `date_added` must be the actual intake date. Catalog-dependent checks remain inapplicable until then. A passing technical test cannot approve the visual design or guarantee Google Fonts acceptance.

## Remaining owner steps

1. Review the final glyph sheet, accented forms, symbols, spacing and specimen. Confirm the family name and complete copyright-holder list, and accept the whole-family OFL release condition.
2. Push the rebuilt files and documentation to the upstream repository, verify it is complete, and make it public.
3. Rerun the external family-name check, assess the five warnings, and confirm the Google CLA applies to the GitHub account used to submit.
4. Submit the prepared issue in `documentation/SUBMISSION-DRAFT.md` with the public source link and specimen; respond to any review requests.

Official references: https://googlefonts.github.io/gf-guide/onboarding.html and https://googlefonts.github.io/gf-guide/qa.html .
