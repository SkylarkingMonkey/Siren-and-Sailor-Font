# Release decisions for Siren and Sailor

This package prepares a static Regular font for review and eventual Google Fonts submission. The owner applied OFL 1.1 locally, pushed an initial private upstream repository, and reports submitting the individual Google CLA. **This package does not make the repository public or submit the font to Google Fonts.**

## Proposed identity

| Item | Proposed value | Status |
| --- | --- | --- |
| Designer | Jean-Marc Daecius | Taken from the project owner's identity; confirm the complete copyright-holder list before release. |
| Presentation name | Siren&Sailor | User-selected branding. |
| Font-menu and catalog name | Siren and Sailor | Proposed spelling compatible with Google's naming guidance; final name check and confirmation remain open. |
| Initial style | Regular | One static style. |
| License | SIL Open Font License 1.1 | Applied by the owner with the `--approve-ofl` finalization flag. |
| Reserved Font Names | None | Proposed. |
| Upstream repository | https://github.com/SkylarkingMonkey/Siren-and-Sailor-Font | Initial push succeeded; public visibility has not been verified. |
| Public contact details | Not supplied | Do not fabricate an email address or website. |

## License decision

Google Fonts requires the entire family under SIL OFL 1.1, ordinarily without Reserved Font Names. Its onboarding terms also cover existing and future styles of that same family, rather than permitting an exclusive commercial extension of the family alongside the Google Fonts release.

Under the OFL, users may use, embed, modify, and redistribute the font under its conditions, including use in commercial work. Font software and derivatives remain under the OFL; documents and artwork created using the font do not have to use that license. The license does not permit selling the font software by itself. Copyright is not transferred to Google by the OFL or the CLA.

The owner ran the finalization script with `--approve-ofl`. The root `OFL.txt` and the staged Google Fonts copy use the same finalized project copyright notice; `AUTHORS.txt` identifies Jean-Marc Daecius. This action does not itself make the repository public.

The matching copyright notice in the source, rebuilt binary and root `OFL.txt` is:

```text
Copyright 2026 The Siren and Sailor Project Authors (https://github.com/SkylarkingMonkey/Siren-and-Sailor-Font)
```

The first line of the final OFL file matches the binary's copyright notice. Keep the standard OFL text intact.

Official references:

- <https://googlefonts.github.io/gf-guide/license-file.html>
- <https://openfontlicense.org/>
- <https://googlefonts.github.io/gf-guide/onboarding.html>
- <https://googlefonts.github.io/gf-guide/requirements.html>
- Template source: <https://github.com/googlefonts/googlefonts-project-template/blob/main/OFL.txt>

## Release steps still requiring completion

- [x] Owner applied OFL 1.1 to the family with the explicit finalization flag; confirm Google's whole-family requirement before submission.
- [ ] Owner confirms the copyright-holder list and any other contributions or rights needed for release.
- [ ] Final family-name uniqueness check is completed at <https://namecheck.fontdata.com/> and through a general font-name search.
- [ ] Owner confirms **Siren and Sailor** as the app-menu/catalog family name.
- [ ] Make the already-created upstream repository public and verify its URL.
- [x] The real repository URL replaces pending font and license metadata.
- [ ] The final source, binary metadata, AUTHORS/CONTRIBUTORS and OFL documents agree.
- [ ] Public author/contact details and the future maintainer are supplied.
- [x] Owner reports submitting the individual Google CLA at <https://cla.developers.google.com/>; confirm any additional rights holders if applicable.
- [ ] The exact final font is rebuilt from the committed source and receives a complete QA report.
- [ ] The designer approves the final visual specimen, including the extended Latin character set.
- [ ] The submission draft is updated from actual evidence and approved for posting.

## Catalog metadata is an intake template

`documentation/METADATA.pb.in` is an intentionally incomplete catalog template, not a live `METADATA.pb`. Its missing repository details and actual Google Fonts catalog date must not be invented. The current official protobuf schema requires `date_added`, so putting this incomplete template in the staging directory would produce parsing or validation failures rather than a usable catalog record.

The initial upstream submission is an issue linking the public source project; it does not require a finished Google catalog metadata file. The Google-style staging directory therefore contains no live `METADATA.pb` until the real intake date is known. QA must report catalog-dependent checks as skipped or inapplicable transparently; that does not establish that eventual catalog metadata has passed validation.

`scripts/finalize_release.py` updated the template, source copyright, OFL files, and staging description with the owner-approved repository URL. The font was rebuilt and applicable QA rerun. It emits live catalog metadata only when an explicit, valid `--catalog-date YYYY-MM-DD` is supplied. This date must be the actual Google Fonts intake date, not the preparation or local build date. Rerun catalog checks after creating live metadata.

- Metadata guide: <https://googlefonts.github.io/gf-guide/metadata.html>
- Current schema: <https://github.com/googlefonts/gf-metadata/blob/main/resources/protos/fonts_public.proto>

## How to interpret QA results

Technical readiness and design approval are distinct. A green automated report cannot establish attractive letterforms, natural curve-to-serif transitions, optical kerning, or fidelity to the designer's intended style. Review all newly added characters visually, including marks above capitals and lowercase, combined accents, nondecomposing Latin letters, punctuation, symbols, and tabular figures.

Current Google Fonts QA documentation identifies **Fontspector** as its primary tool; some older onboarding text still mentions FontBakery. Preserve reports, versions, command lines, and details of any skipped or errored checks. Fix technical failures and assess warnings; do not suppress checks to label a build as ready. Google retains discretion to request changes or reject a submission on design grounds.

- QA guide: <https://googlefonts.github.io/gf-guide/qa.html>
- Outline quality: <https://googlefonts.github.io/gf-guide/outlines.html>
- Diacritics: <https://googlefonts.github.io/gf-guide/diacritics.html>
- Submission template: <https://github.com/google/fonts/blob/main/.github/ISSUE_TEMPLATE/1_add-font.md>

Prepared September 25, 2026.
