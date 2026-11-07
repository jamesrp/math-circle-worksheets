# Brief: publish the explorer to GitHub Pages

**For Codex.** Written by Claude on November 7, 2026. Work board line: "Publish the explorer to GitHub Pages". Follows [explorer-github-pages.md](explorer-github-pages.md), whose source side is done and reviewed (see [catalog/pages-source-verification.md](../../catalog/pages-source-verification.md)).

## Approval

James approved publishing the explorer publicly on November 7, 2026 (his "Yes" to "Should Codex publish it publicly?"). This covers running the publisher for real against `origin` and later reviewed redeploys with the same script. It does not cover changing the repository's visibility or plan, adding a workflow or custom domain, or anything paid.

## Steps

1. From the canonical clone, on a clean `main` pulled from `origin` at or after `f7e1e1b`:

   ```sh
   git switch main
   git pull --ff-only origin main
   python3 catalog/publish_pages.py --dry-run
   python3 catalog/publish_pages.py
   ```

   The dry run must end with "Dry run: would publish tree … as a new orphan gh-pages from source …" and push nothing. If either command stops, report its message and stop; don't work around a refusal.
2. Don't change Pages settings. James sets **Settings → Pages → Deploy from a branch, `gh-pages`, `/(root)`** himself. (If he asks you to do it instead, the API call is in the earlier brief; stop if GitHub asks for a paid plan or a visibility change.)

## Checks

- `git ls-tree origin/gh-pages` after a fetch lists exactly `.nojekyll` and `index.html`.
- `git show origin/gh-pages:index.html` is byte-identical to `explorer/index.html` at the source SHA in the `gh-pages` commit message, and that SHA is on `origin/main`.
- A second `python3 catalog/publish_pages.py` prints "Explorer unchanged; no commit or push".

## Report

On the work board line: the `gh-pages` commit SHA and its source SHA, the three checks above, and whether anything stopped. Live-site checks (HTTP 200, title "Math Circle Explorer", filters, detail panel, path view, print links) wait until James has turned Pages on; leave them pending on the line.
