# Explorer Pages source preparation

Source-only implementation of [the publishing brief](../plans/briefs/explorer-github-pages.md). Baseline: fetched `origin/main` at `ee650f77ea4c599bd6276cb0fa1ca544d66d6195`, preserving the planned-layer implementation `9b31f6d4710c0a0710fcb3860196b84906e5125c`. Row-only claim: `8050fbb1808e09c13b21d231d5345c8546c919d9`; implementation branch: `codex/explorer-pages-source`.

The canonical Mac Mini clone at `/Users/jamespfeiffer/Documents/Codex/2026-11-05/task/math-circle-worksheets` was verified clean on `main`, with origin `git@github.com:jamesrp/math-circle-worksheets.git` and local HEAD `2e81d569119a26e28caad9bf93253f05ff4b9ddc`. All authored work used a separate clone under the new task workspace, reset to fetched `origin/main`; the canonical clone and other workers' checkouts were not edited. No `.agents/skills` directory exists in this repository. The task inventory showed no competing active worksheet worker; the planned-layer worker was terminal. The only open PR was historical draft #6, head `24a18cb02a3f45c91311c90d5a85b65886450278`, with no submitted reviews or reported commit statuses. It was read and left untouched.

## Implementation

`catalog/publish_pages.py` requires clean `main`, including untracked files. It runs the committed catalog builder in a temporary detached source worktree, rejects every tracked build difference, and verifies explorer bytes against the source commit. A second temporary worktree stages exactly `index.html` and empty `.nojekyll`; the first commit is orphaned, later commits have the fetched publication head as their parent. Commit messages contain the full source SHA. Matching publication trees make no commit or push. Publication uses a normal single-ref push, with no force or automatic retry, and checks the resulting remote SHA. Existing local branches, source files and other worktrees stay in place. The publisher does not configure Pages.

Cleanup removes only its own worktrees, directory and private fetch ref. It handles build, worktree and push failures and SIGTERM/KeyboardInterrupt; a removal failure retains the affected worktree and reports its location. SIGKILL or power loss cannot run cleanup. A failed/interrupted push can have an uncertain server outcome and requires inspecting the remote ref before any retry. Git environment overrides that could redirect the repository/index and mismatched origin fetch/push URLs are rejected.

## Checks

Run with Python 3.11+ (verified here with bundled Python 3.12 and Git 2.54):

```sh
python3 -m unittest discover -s catalog -p 'test_publish_pages.py' -v
python3 catalog/build.py
python3 catalog/build.py --check
python3 catalog/check_path.py
python3 catalog/readiness.py --print > /tmp/explorer-readiness-check.md
cmp /tmp/explorer-readiness-check.md plans/readiness.md
git diff --exit-code -- explorer/index.html CATALOG.md plans/readiness.md
git diff --check
```

- **18 reproducible publisher integration tests pass**, using repository-owned code/inline fixtures, throwaway local repositories, local bare remotes and Git file transport only. They cover initial orphan/provenance/exact two-file tree/UTF-8 and CRLF byte equality; unchanged second and documentation-only runs; changed publication ancestry; dirty unstaged/staged/untracked source; wrong branch/detached HEAD; HTML and other tracked build differences; build failure; SIGTERM; first-publication and later remote-advance rejection; push-hook rejection; existing publication worktree/local branch/FETCH_HEAD preservation; failed and partially successful worktree creation; recoverable cleanup failure; mismatched push destination; and index override refusal. Ordinary paths also assert source HEAD, branch, status, worktree registration, temporary directory and private-ref cleanup.
- An additional full-repository local smoke check used the actual `catalog/build.py`, a disposable clone and a local bare remote. Initial publication passed, the second run made no commit, and the remote tree/HTML/provenance and clean source/worktree cleanup were verified. It never used GitHub as a publishing remote. The current explorer SHA-256 is `57e347da9b87cbb4fb81520353a1d0e0ee98430b0d14c5d481463c0fd437f6a6`.
- Catalog build, validation-only build, standalone path check and standalone readiness comparison pass: 101 weekly themes, 90 atlas families, 12 draft themes, 108 plans, 11 pending weekly drafts, 149 concepts; 120 path sessions in 117 entries. The rebuild changes no output bytes. The only intended changed paths are the publisher, its tests, catalog README, this report and this task's workboard row. Catalog data, generated explorer/CATALOG/readiness, plan sources, student pages, guides and all unrelated files remain unchanged.
- The README documents reviewed redeploys, the intended but unverified public destination, free branch/root setup after approval, and the independently maintained private claude.ai artifact. The branch/root settings instructions were checked against [GitHub's official documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Remaining publication step

**Source preparation is complete; publication still waits for explicit user approval.** After approval, review current main and the explorer, run the publisher against the canonical remote, configure free deploy-from-branch Pages on `gh-pages` at `/(root)` if needed, and perform the brief's remote-tree/source-byte and live HTTP/title/browser/print-link checks. Stop if a paid plan or visibility change is required.

This task did not push a real GitHub `gh-pages` branch, enable Pages, call Pages write APIs, change repository settings, add a custom workflow/domain, deploy, verify the public site, republish claude.ai, merge or approve a PR, purchase anything, expand access, or contact Claude. The intended public URL remains pending/unverified. No source implementation blocker remains.

## Claude review (November 6, 2026)

Passed. Reviewed the publisher and tests on `a7d18bc`; the 18 tests passed unchanged with Python 3.13 and Git 2.43. Two small additions on `main`: `--dry-run` runs every check and builds the publication tree but creates no commit and pushes nothing (it only reads from `origin`), and the publisher now refuses a local `main` that is not `origin`'s `main`, so the source SHA in each `gh-pages` message exists on GitHub. Two tests cover them (20 in all, passing). A smoke run with the real builder in a throwaway clone and local bare remote confirmed: dry run left no `gh-pages`; the first publish made one orphan commit holding only `index.html` (byte-identical) and `.nojekyll`; a second run and a later dry run made nothing. The built page holds no local paths, addresses or tokens. No workflow file exists; branch-based Pages on this public repository is free (GitHub's own Pages build runs on Actions, which is free for public repositories). Nothing was pushed to GitHub's `gh-pages` and no setting changed.
