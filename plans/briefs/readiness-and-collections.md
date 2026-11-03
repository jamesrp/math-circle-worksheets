# Brief: readiness and collections in the catalog build

**For Codex.** Written by Claude on November 3, 2026. Work board line: "Catalog build: validate the use log and collections, show readiness and collections in the explorer". Background: [plans/corpus-plan.md](../corpus-plan.md).

## Goal

Three new files describe how far each theme is from done and which curated lists it belongs to: [catalog/use-log.toml](../../catalog/use-log.toml) (sessions where a theme was used), [catalog/collections.toml](../../catalog/collections.toml) (curated views) and [catalog/readiness.py](../../catalog/readiness.py) (writes [plans/readiness.md](../readiness.md)). Today nothing checks the first two, and the explorer and CATALOG.md don't show either. Make the build check them and show them, without changing any worksheet, record or the path.

## Steps

Work on a branch from fetched `origin/main`.

1. **Validate in `catalog/build.py`.** Stop the build when:
   - a use-log entry lacks `date`, `setting`, `weeks`, `activity`, `outcome` or `source`; `date` is not `YYYY-MM` or `YYYY-MM-DD`; `setting` is not `circle` or `home`; or a week id is unknown;
   - a collection lacks `id`, `title`, `purpose`, `done`, `status` or `weeks`; ids repeat; `status` is not `proposal` or `organizer-approved`; a week id is unknown; a `drafts` id has no `catalog/drafts/` record; or a week appears twice in one collection.
2. **Run the report from the build.** `build.py` calls `readiness.py`'s main (import it; keep `readiness.py` runnable on its own) so `plans/readiness.md` is rewritten on every build. Its output must stay byte-identical for the current data, apart from changes you list in the report.
3. **Explorer.** In the activity list's detail panel, show a theme's rung (library, signed off, circle-ready, taught) and its use-log lines (date, setting, outcome), and the collections it belongs to. Add two list filters: "Rung" and "Collection". Drafts named in a collection's `drafts` show that collection in their detail panel. Keep the page one self-contained file, as now.
4. **CATALOG.md.** Add a "Taught" marker to the Status column for themes with a use-log line (for example "unpiloted; taught at home"), and a short "Collections" section after the area tables listing each collection's title, purpose, done bar, status and members with links.
5. **Docs.** Add both files and the report to the file list and rebuild instructions in `catalog/README.md`, with one field table each, as for week records.

## Checks

- `python3 catalog/build.py` and `python3 catalog/check_path.py` run clean; `python3 catalog/readiness.py --print` still works alone.
- Break each new rule once on a scratch copy and confirm the build stops with a clear message; leave no broken data committed.
- Open `explorer/index.html` in a browser if you have one; otherwise check the generated HTML for the new filters and panel text, and say which.
- `git diff --stat` touches only `catalog/build.py`, `catalog/readiness.py` (only if needed for import), `catalog/explorer_template.html`, `catalog/README.md`, `CATALOG.md`, `explorer/index.html`, `plans/readiness.md` and the work board.

## Waits for Claude

Nothing before you start. Claude reviews the result and republishes the published explorer artifact; don't try to publish it.

## Report

What changed in each file, the validation rules added, anything in the current data the new checks caught (fix nothing in the data; list it), and whether you looked at the explorer in a browser.
