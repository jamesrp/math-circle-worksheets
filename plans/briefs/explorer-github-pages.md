# Brief: serve the explorer on GitHub Pages

**For Codex.** Written by Claude on November 6, 2026. Work board line: "Explorer on GitHub Pages". Background: [catalog/README.md](../../catalog/README.md).

## Goal

`explorer/index.html` is one self-contained page (data inline; Google Fonts with system fallbacks; per-browser marks in local storage). On GitHub it shows as source, so a reader has to download it. Serve it at `https://jamesrp.github.io/math-circle-worksheets/` with GitHub Pages, **free tier only**: the repository is public (checked November 6), so deploy-from-branch Pages costs nothing. No custom Actions workflow, no paid features, no custom domain.

Cloud Claude sessions can't push to `gh-pages`, so this is yours, including later redeploys.

## Steps

1. **Publish script.** Add `catalog/publish_pages.sh` (or `.py`) that, from a clean checkout of `main`: runs `python3 catalog/build.py`, refuses to continue if that leaves a diff, then commits `explorer/index.html` as `index.html` plus an empty `.nojekyll` to a `gh-pages` branch (create it as an orphan the first time; later runs add one commit each, never force-push), with the source commit's SHA in the message, and pushes it. Use a temporary worktree so the main checkout is untouched. Only those two files go on `gh-pages`: not the PDFs, not the rest of the repository.
2. **Enable Pages** on branch `gh-pages`, folder `/`, for example `gh api -X POST repos/jamesrp/math-circle-worksheets/pages -f "source[branch]=gh-pages" -f "source[path]=/"`. If GitHub reports that Pages needs a paid plan or that the repository is private, stop and report; don't change the repository's visibility or plan.
3. **Docs.** In `catalog/README.md`, add the public link beside the claude.ai copy, say when to redeploy (after an explorer change is reviewed) and how (the script), and that the claude.ai copy is a separate private page.

## Checks

- The public URL returns 200 and its page title is "Math Circle Explorer"; in a browser, the filters, a detail panel and the path view work, and print links open the PDFs on GitHub.
- The `gh-pages` branch holds only `index.html` and `.nojekyll`, and its `index.html` is byte-identical to `explorer/index.html` at the SHA in the commit message.
- Running the script twice with no change in between makes no new commit.

## Waits for Claude

Nothing. Claude reviews the script and docs afterwards.

## Report

The public URL, the `gh-pages` commit and its source SHA, the API response if Pages needed any setting, and whether you looked in a browser.
