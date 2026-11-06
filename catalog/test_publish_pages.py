#!/usr/bin/env python3
"""Publisher integration tests: throwaway local repos and file transport only.

    python3 -m unittest discover -s catalog -p 'test_publish_pages.py' -v
"""
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


PUBLISHER = Path(__file__).with_name("publish_pages.py")
HTML = "<!doctype html>\r\n<title>Math Circle Explorer</title>\n<p>π</p>\n".encode()
BUILD = """from pathlib import Path
root = Path(__file__).resolve().parent.parent
(root / 'explorer/index.html').write_bytes((root / 'catalog/fixture.html').read_bytes())
"""


class PublisherTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="test-explorer-publish-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.repo = self.base / "source"
        self.remote = self.base / "remote.git"
        self.scratch = self.base / "scratch"
        self.scratch.mkdir()
        self.real_git = shutil.which("git")
        self.env = {key: value for key, value in os.environ.items()
                    if not key.startswith("GIT_")}
        self.env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
                        GIT_ALLOW_PROTOCOL="file", GIT_TERMINAL_PROMPT="0",
                        GIT_AUTHOR_NAME="Publisher Test", GIT_AUTHOR_EMAIL="test@example.invalid",
                        GIT_COMMITTER_NAME="Publisher Test", GIT_COMMITTER_EMAIL="test@example.invalid",
                        TMPDIR=str(self.scratch), PYTHONDONTWRITEBYTECODE="1")
        self.git(self.base, "init", "--bare", str(self.remote))
        self.git(self.base, "init", "-b", "main", str(self.repo))
        (self.repo / "catalog").mkdir()
        (self.repo / "explorer").mkdir()
        shutil.copyfile(PUBLISHER, self.repo / "catalog/publish_pages.py")
        self.write("catalog/build.py", BUILD)
        self.write("catalog/fixture.html", HTML)
        self.write("explorer/index.html", HTML)
        self.write(".gitignore", "__pycache__/\n")
        self.write("not-for-publication.txt", "stay on main\n")
        self.commit("Initial source")
        self.git(self.repo, "remote", "add", "origin", str(self.remote))
        self.git(self.repo, "push", "origin", "main")

    def git(self, root, *args, input=None, check=True):
        result = subprocess.run([self.real_git, "-C", str(root), *args],
                                input=input, capture_output=True, env=self.env)
        if check and result.returncode:
            self.fail(f"git {args}: {result.stderr.decode()}")
        return result.stdout if check else result

    def write(self, name, content):
        path = self.repo / name
        path.write_bytes(content.encode() if isinstance(content, str) else content)

    def commit(self, message):
        self.git(self.repo, "add", ".")
        self.git(self.repo, "commit", "-m", message)
        return self.git(self.repo, "rev-parse", "HEAD").strip()

    def remote_head(self):
        result = self.git(self.remote, "rev-parse", "--verify", "refs/heads/gh-pages", check=False)
        return result.stdout.strip() if result.returncode == 0 else None

    def publish(self, success=True):
        before = self.git(self.repo, "status", "--porcelain", "--untracked-files=all")
        worktrees = self.git(self.repo, "worktree", "list", "--porcelain")
        scratch_before = set(self.scratch.iterdir())
        head = self.git(self.repo, "rev-parse", "HEAD")
        branch = self.git(self.repo, "symbolic-ref", "HEAD", check=False).stdout
        result = subprocess.run([sys.executable, str(self.repo / "catalog/publish_pages.py")],
                                cwd=self.repo / "catalog", capture_output=True, env=self.env)
        text = (result.stdout + result.stderr).decode(errors="replace")
        if success:
            self.assertEqual(result.returncode, 0, text)
        else:
            self.assertNotEqual(result.returncode, 0, text)
        self.assertEqual(self.git(self.repo, "rev-parse", "HEAD"), head)
        self.assertEqual(self.git(self.repo, "symbolic-ref", "HEAD", check=False).stdout, branch)
        self.assertEqual(self.git(self.repo, "status", "--porcelain", "--untracked-files=all"), before)
        self.assertEqual(self.git(self.repo, "worktree", "list", "--porcelain"), worktrees)
        self.assertEqual(set(self.scratch.iterdir()), scratch_before)
        self.assertEqual(self.git(self.repo, "for-each-ref", "refs/explorer-publish"), b"")
        return text

    def assert_tree(self, html=HTML):
        self.assertEqual(self.git(self.remote, "ls-tree", "--name-only", "gh-pages").splitlines(),
                         [b".nojekyll", b"index.html"])
        self.assertEqual(self.git(self.remote, "show", "gh-pages:index.html"), html)
        self.assertEqual(self.git(self.remote, "show", "gh-pages:.nojekyll"), b"")

    def test_initial_orphan_exact_tree_bytes_and_provenance(self):
        source = self.git(self.repo, "rev-parse", "HEAD").strip()
        self.publish()
        self.assert_tree()
        self.assertEqual(self.git(self.remote, "rev-list", "--parents", "-1", "gh-pages").split(),
                         [self.remote_head()])
        self.assertIn(source, self.git(self.remote, "log", "-1", "--format=%B", "gh-pages"))
        self.assertIsNone(self.git(self.repo, "rev-parse", "--verify", "refs/heads/gh-pages", check=False).stdout.strip() or None)

    def test_unchanged_second_run_makes_no_commit_even_after_source_doc_change(self):
        self.publish()
        first = self.remote_head()
        self.assertIn("no commit or push", self.publish())
        self.assertEqual(self.remote_head(), first)
        self.write("not-for-publication.txt", "reviewed documentation change\n")
        self.commit("Docs only")
        self.assertIn("no commit or push", self.publish())
        self.assertEqual(self.remote_head(), first)

    def test_changed_publication_is_normal_child_with_new_source_sha(self):
        self.publish()
        first = self.remote_head()
        html = HTML + b"<!-- reviewed new content -->\n"
        self.write("catalog/fixture.html", html)
        self.write("explorer/index.html", html)
        source = self.commit("Reviewed explorer change")
        self.publish()
        self.assert_tree(html)
        self.assertEqual(self.git(self.remote, "rev-parse", "gh-pages^").strip(), first)
        self.assertIn(source, self.git(self.remote, "log", "-1", "--format=%B", "gh-pages"))

    def test_dirty_unstaged_staged_and_untracked_checkouts(self):
        for mode in ("unstaged", "staged", "untracked"):
            with self.subTest(mode=mode):
                target = "untracked.txt" if mode == "untracked" else "not-for-publication.txt"
                self.write(target, "unreviewed\n")
                if mode == "staged":
                    self.git(self.repo, "add", target)
                self.assertIn("main must be clean", self.publish(False))
                self.assertIsNone(self.remote_head())
                if mode == "untracked":
                    (self.repo / target).unlink()
                else:
                    self.git(self.repo, "restore", "--staged", "--worktree", target)

    def test_wrong_branch_and_detached_head(self):
        for args in (("switch", "-c", "feature"), ("switch", "--detach")):
            self.git(self.repo, *args)
            self.assertIn("Run from branch main", self.publish(False))
            self.assertIsNone(self.remote_head())

    def test_build_generated_html_diff_refused_without_dirtying_main(self):
        self.write("catalog/fixture.html", b"stale output must be reviewed\n")
        self.commit("Input changed without rebuild")
        self.assertIn("Build changed tracked outputs", self.publish(False))
        self.assertEqual((self.repo / "explorer/index.html").read_bytes(), HTML)
        self.assertIsNone(self.remote_head())

    def test_build_generated_other_tracked_diff_refused(self):
        self.write("catalog/build.py", BUILD + "(root / 'not-for-publication.txt').write_text('changed')\n")
        self.commit("Builder changes another tracked output")
        self.assertIn("Build changed tracked outputs", self.publish(False))
        self.assertIsNone(self.remote_head())

    def test_build_failure_cleanup(self):
        self.write("catalog/build.py", "raise SystemExit(23)\n")
        self.commit("Failing build")
        self.assertIn("Catalog build failed", self.publish(False))
        self.assertIsNone(self.remote_head())

    def test_sigterm_cleanup(self):
        self.write("catalog/build.py", "import os, signal\nos.kill(os.getppid(), signal.SIGTERM)\n")
        self.commit("Interrupted build")
        self.assertIn("Publication interrupted", self.publish(False))
        self.assertIsNone(self.remote_head())

    def install_git_wrapper(self, body):
        directory = self.base / "bin"
        directory.mkdir()
        wrapper = directory / "git"
        wrapper.write_text(f"#!{sys.executable}\nimport os, sys, subprocess\n"
                           f"real_git = {self.real_git!r}\nargs = sys.argv[1:]\n" + body
                           + "\nos.execv(real_git, [real_git, *args])\n")
        wrapper.chmod(0o755)
        self.env["PATH"] = str(directory) + os.pathsep + self.env["PATH"]

    def test_remote_advance_rejects_push_and_cleans_up(self):
        self.publish()
        first = self.remote_head()
        tree = self.git(self.remote, "rev-parse", "gh-pages^{tree}").decode().strip()
        racer = self.git(self.remote, "commit-tree", tree, "-p", first.decode(), input=b"Concurrent publisher\n").decode().strip()
        self.write("catalog/fixture.html", HTML + b"changed\n")
        self.write("explorer/index.html", HTML + b"changed\n")
        self.commit("Reviewed update")
        self.install_git_wrapper(
            "if 'push' in args:\n"
            f"    subprocess.run([real_git, '-C', {str(self.remote)!r}, 'update-ref', 'refs/heads/gh-pages', {racer!r}], check=True)\n")
        text = self.publish(False)
        self.assertTrue("fetch first" in text or "non-fast-forward" in text, text)
        self.assertEqual(self.remote_head(), racer.encode())

    def test_first_publication_race_is_rejected(self):
        # Create a competing orphan using repository-owned objects, without publishing it yet.
        source = self.git(self.repo, "rev-parse", "HEAD").decode().strip()
        tree = self.git(self.repo, "rev-parse", "HEAD^{tree}").decode().strip()
        racer = self.git(self.repo, "commit-tree", tree, input=b"Other initial publisher\n").decode().strip()
        self.git(self.repo, "push", "origin", f"{racer}:refs/heads/test-object-storage")
        self.install_git_wrapper(
            "if 'push' in args:\n"
            f"    subprocess.run([real_git, '-C', {str(self.remote)!r}, 'update-ref', 'refs/heads/gh-pages', {racer!r}], check=True)\n")
        self.publish(False)
        self.assertEqual(self.remote_head(), racer.encode())
        self.assertNotEqual(racer, source)

    def test_push_hook_failure_cleanup(self):
        hook = self.remote / "hooks/pre-receive"
        hook.write_text("#!/bin/sh\nexit 1\n")
        hook.chmod(0o755)
        self.assertIn("declined", self.publish(False))
        self.assertIsNone(self.remote_head())

    def test_existing_gh_pages_worktree_local_branch_and_fetch_head_unchanged(self):
        self.publish()
        first = self.remote_head().decode()
        self.git(self.repo, "fetch", "origin", "gh-pages:gh-pages")
        pages = self.base / "existing-pages"
        self.git(self.repo, "worktree", "add", str(pages), "gh-pages")
        (pages / "private-untracked.txt").write_text("do not touch\n")
        files_before = {p.name: p.read_bytes() for p in pages.iterdir()}
        fetch_head_before = (self.repo / ".git/FETCH_HEAD").read_bytes()
        self.write("catalog/fixture.html", HTML + b"new\n")
        self.write("explorer/index.html", HTML + b"new\n")
        self.commit("Next reviewed update")
        self.publish()
        self.assertEqual(self.git(pages, "rev-parse", "HEAD").decode().strip(), first)
        self.assertEqual({p.name: p.read_bytes() for p in pages.iterdir()}, files_before)
        # A successful push may update origin/gh-pages, but no local branch or
        # other worktree is moved. Its private fetch leaves FETCH_HEAD untouched.
        self.assertEqual(self.git(self.repo, "rev-parse", "gh-pages").decode().strip(), first)
        self.assertEqual((self.repo / ".git/FETCH_HEAD").read_bytes(), fetch_head_before)

    def test_worktree_add_failure_cleanup(self):
        self.install_git_wrapper(
            "if 'worktree' in args and 'add' in args and any(a.endswith('/pages') for a in args):\n"
            "    sys.stderr.write('injected pages worktree failure\\n')\n"
            "    sys.exit(25)\n")
        self.assertIn("injected pages worktree failure", self.publish(False))
        self.assertIsNone(self.remote_head())

    def test_partially_successful_worktree_add_cleanup(self):
        self.install_git_wrapper(
            "if 'worktree' in args and 'add' in args and any(a.endswith('/pages') for a in args):\n"
            "    subprocess.run([real_git, *args], check=True)\n"
            "    sys.stderr.write('failure after worktree registration\\n')\n"
            "    sys.exit(25)\n")
        self.assertIn("failure after worktree registration", self.publish(False))
        self.assertIsNone(self.remote_head())

    def test_cleanup_failure_retains_only_owned_worktree_for_recovery(self):
        self.install_git_wrapper(
            "if 'worktree' in args and 'remove' in args and any(a.endswith('/pages') for a in args):\n"
            "    sys.stderr.write('injected cleanup failure\\n')\n"
            "    sys.exit(26)\n")
        source = self.git(self.repo, "rev-parse", "HEAD")
        result = subprocess.run([sys.executable, str(self.repo / "catalog/publish_pages.py")],
                                capture_output=True, env=self.env)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(b"Retained temporary worktree", result.stderr)
        self.assertIn(b"injected cleanup failure", result.stderr)
        self.assertEqual(self.git(self.repo, "rev-parse", "HEAD"), source)
        self.assertEqual(self.git(self.repo, "status", "--porcelain"), b"")
        retained = list(self.scratch.glob("explorer-pages-*"))
        self.assertEqual(len(retained), 1)
        self.assertFalse((retained[0] / "build").exists())
        self.assertTrue((retained[0] / "pages/.git").is_file())
        self.assert_tree()
        self.assertEqual(self.git(self.repo, "for-each-ref", "refs/explorer-publish"), b"")
        # Use real Git, bypassing the injected failure, to remove the test's worktree.
        self.git(self.repo, "worktree", "remove", "--force", str(retained[0] / "pages"))
        retained[0].rmdir()

    def test_mismatched_push_destination_refused(self):
        self.git(self.repo, "remote", "set-url", "--push", "origin", str(self.base / "elsewhere.git"))
        self.assertIn("matching fetch/push URL", self.publish(False))
        self.assertIsNone(self.remote_head())

    def test_git_index_override_refused(self):
        self.env["GIT_INDEX_FILE"] = str(self.base / "foreign-index")
        result = subprocess.run([sys.executable, str(self.repo / "catalog/publish_pages.py")],
                                capture_output=True, env=self.env)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(b"Unset GIT_DIR", result.stderr)
        self.assertFalse((self.base / "foreign-index").exists())
        self.assertIsNone(self.remote_head())


if __name__ == "__main__":
    unittest.main()
