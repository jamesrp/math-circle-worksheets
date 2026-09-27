# Print edition specification

The print products in this round are **facilitator plans**, following the organizer's request to work at plan level before detailed student worksheets. They are not a replacement for the existing Weeks 1-10 print packets. Keep those files unchanged.

After mathematical/editorial review and repair, make two linked books in `lowell-math-circle-year-2/combined/`:

1. **Mathematics atlas - investigation plans.** All family records, grouped into algebra/discrete, geometry/analysis, and probability/applications. Provide a readable contents/index, prerequisite key, honest scope and review note, source links, page numbers, and PDF bookmarks. A repeatable two-page planning-card format is preferred where it fits naturally: participation/launch on the first page; explanation, boundaries and extensions on the second. Do not shrink type to force the pattern. Preserve exact rules, numbers and hypotheses. Do not imply that all families are elementary or classroom-tested.
2. **Mathematics atlas - research map.** The complete three research surveys, source locators, map-lock/coverage summary, and frontier. Use field headings and bookmarks so it is browsable. Explain the 63-field / 231-seed / 90-planned-family relationship without claiming exhaustive fine-grained review. Keep source access limitations visible. Include the MSC attribution for classification-derived content.

The editable plan/data source stays in `plans/atlas/`. PDF builders and their build instructions belong in `lowell-math-circle-year-2/source/atlas/`. Intermediates, fonts copied for build if needed, logs, rendered page images and contact sheets belong in `tmp/atlas/` or `tmp/pdfs/atlas/`.

Use readable mathematical typography. Do not print raw LaTeX commands, missing-glyph boxes, broken Markdown links, or long URLs that force tiny type. Source titles should be links, with locators in text. Use proper Unicode-capable fonts or a mathematical renderer. Verify the exact symbol repertoire before production, particularly subscripts, superscripts, Greek letters and set notation.

Generate all pages and render them. Independent reviewers should inspect all-page contact sheets and representative full pages, plus every page flagged by automated geometry/text checks. Record review scope, corrections, and the final content hashes. A final repair pass follows the independent PDF review; verify the repaired pages again.
