#!/usr/bin/env python3
"""Publish the reviewed explorer from clean main; requires publication approval.

Usage: python3 catalog/publish_pages.py [--dry-run]
Only origin's gh-pages ref is pushed. No Pages settings are changed.
--dry-run does every check and builds the publication tree, but creates no
commit and pushes nothing; it only reads from origin.
"""
import os
from pathlib import Path
import signal
import shutil
import subprocess
import sys
import tempfile
import uuid


class PublishError(Exception):
    pass


def git(root, *args, check=True, input=None):
    result = subprocess.run(
        ["git", "-C", str(root), *args], input=input, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and result.returncode:
        raise PublishError(result.stderr.decode(errors="replace").strip()
                           or f"git {args[0]} failed ({result.returncode})")
    return result


def require_source(root, source=None):
    if git(root, "symbolic-ref", "--quiet", "--short", "HEAD", check=False).stdout.strip() != b"main":
        raise PublishError("Run from branch main.")
    if git(root, "status", "--porcelain", "--untracked-files=all").stdout:
        raise PublishError("main must be clean, including untracked files.")
    current = git(root, "rev-parse", "HEAD").stdout.decode().strip()
    if source is not None and current != source:
        raise PublishError("Source main changed during publication; review and retry.")
    return current


def publish(root, dry_run=False):
    source = require_source(root)
    # Fetch into a private ref, without moving origin/gh-pages or a local branch.
    remote_ref = "refs/heads/gh-pages"
    private_ref = f"refs/explorer-publish/{uuid.uuid4().hex}"
    worktrees = []
    temp = Path(tempfile.mkdtemp(prefix="explorer-pages-"))
    try:
        build = temp / "build"
        worktrees.append(build)  # Also clean up a partially successful add.
        git(root, "worktree", "add", "--detach", str(build), source)
        result = subprocess.run([sys.executable, "catalog/build.py"], cwd=build)
        if result.returncode:
            raise PublishError("Catalog build failed; nothing published.")
        # Ignore Python caches, but reject every tracked change (not just HTML).
        if git(build, "status", "--porcelain", "--untracked-files=no").stdout:
            raise PublishError("Build changed tracked outputs; rebuild, review and commit on main first.")
        html = (build / "explorer/index.html").read_bytes()
        if html != git(root, "show", f"{source}:explorer/index.html").stdout:
            raise PublishError("Built explorer differs from its source commit.")

        # Inspect the push destination too: Git can configure origin's push URL
        # independently. Refuse such ambiguity rather than publish elsewhere.
        urls = git(root, "remote", "get-url", "--all", "origin").stdout.splitlines()
        push_urls = git(root, "remote", "get-url", "--push", "--all", "origin").stdout.splitlines()
        if len(urls) != 1 or push_urls != urls:
            raise PublishError("origin must have one matching fetch/push URL.")
        # Publish only reviewed, pushed main, so the SHA in the commit message
        # exists on origin and the published bytes can be checked against it.
        remote_main = git(root, "ls-remote", "--exit-code", "--refs", "origin", "refs/heads/main", check=False)
        if remote_main.returncode or remote_main.stdout.split()[0].decode() != source:
            raise PublishError("Local main is not origin's main; pull or push first.")
        remote = git(root, "ls-remote", "--exit-code", "--refs", "origin", remote_ref, check=False)
        if remote.returncode not in (0, 2):
            raise PublishError(remote.stderr.decode(errors="replace").strip() or "Cannot read origin.")
        parent = None
        if remote.returncode == 0:
            git(root, "fetch", "--no-tags", "--no-write-fetch-head", "origin", f"{remote_ref}:{private_ref}")
            parent = git(root, "rev-parse", private_ref).stdout.decode().strip()

        pages = temp / "pages"
        worktrees.append(pages)
        git(root, "worktree", "add", "--detach", "--no-checkout", str(pages), parent or source)
        # Empty this worktree's index only; never check out or alter main or an
        # existing gh-pages worktree. The resulting tree has exactly two blobs.
        git(pages, "read-tree", "--empty")
        (pages / "index.html").write_bytes(html)
        (pages / ".nojekyll").write_bytes(b"")
        git(pages, "-c", "core.autocrlf=false", "add", "--force", "--", "index.html", ".nojekyll")
        tree = git(pages, "write-tree").stdout.decode().strip()
        # Verify the staged bytes, including against global Git filters.
        if (git(pages, "show", f"{tree}:index.html").stdout != html
                or git(pages, "show", f"{tree}:.nojekyll").stdout != b""):
            raise PublishError("Git transformed publication bytes; nothing published.")
        require_source(root, source)
        if parent and tree == git(root, "rev-parse", f"{parent}^{{tree}}").stdout.decode().strip():
            print(f"Explorer unchanged; no commit or push (gh-pages {parent}).")
            return
        if dry_run:
            where = f"on top of gh-pages {parent}" if parent else "as a new orphan gh-pages"
            print(f"Dry run: would publish tree {tree} {where} from source {source}; nothing pushed.")
            return
        args = ["commit-tree", tree]
        if parent:
            args += ["-p", parent]
        commit = git(pages, *args, input=f"Publish explorer from source {source}\n".encode()).stdout.decode().strip()
        # No force, lease override or retry: an intervening publisher wins and
        # the user must fetch/review before retrying. Push exactly this one ref.
        git(root, "-c", "push.followTags=false", "push", "--no-follow-tags", "origin", f"{commit}:{remote_ref}")
        actual = git(root, "ls-remote", "--exit-code", "--refs", "origin", remote_ref).stdout.split()[0].decode()
        if actual != commit:
            raise PublishError(f"Push completed but remote is now {actual}; inspect before retrying.")
        print(f"Published gh-pages {commit} from source {source}.")
    finally:
        # Do not prune worktrees or delete shared branch refs. On removal failure,
        # retain the directory for recovery and report its precise location.
        errors = []
        for path in reversed(worktrees):
            result = git(root, "worktree", "remove", "--force", str(path), check=False)
            registered = b"worktree " + os.fsencode(path.resolve()) + b"\n"
            if result.returncode and (
                    (path / ".git").exists()
                    or registered in git(root, "worktree", "list", "--porcelain").stdout):
                errors.append(f"Retained temporary worktree {path}: {result.stderr.decode().strip()}")
        result = git(root, "update-ref", "-d", private_ref, check=False)
        if result.returncode:
            errors.append(f"Could not remove private ref {private_ref}.")
        if errors:
            raise PublishError("\n".join(errors))
        shutil.rmtree(temp)


def main():
    args = sys.argv[1:]
    if args not in ([], ["--dry-run"]):
        raise PublishError("Usage: python3 catalog/publish_pages.py [--dry-run] (publishes to origin/gh-pages)")
    # Git environment overrides could redirect a worktree's index or repository.
    if any(key in os.environ for key in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR")):
        raise PublishError("Unset GIT_DIR, GIT_WORK_TREE, GIT_INDEX_FILE and GIT_COMMON_DIR first.")
    root = Path(git(Path(__file__).resolve().parent, "rev-parse", "--show-toplevel").stdout.decode().strip())
    publish(root, dry_run=args == ["--dry-run"])


def interrupted(signum, frame):
    raise KeyboardInterrupt


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, interrupted)
    try:
        main()
    except (PublishError, OSError) as exc:
        print(f"Publication stopped: {exc}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("Publication interrupted; check remote gh-pages before retrying.", file=sys.stderr)
        sys.exit(130)
