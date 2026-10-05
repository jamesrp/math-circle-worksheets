# Optional local reference inputs

The canonical owned source is [jamesrp/math-circle-worksheets](https://github.com/jamesrp/math-circle-worksheets), branch `main`. Printable activities, guides, editable sources, portable source ZIPs, mathematical data and authored source notes are committed. Wholesale downloaded books, activity collections, vendor downloads and private classroom records are excluded from the current tree and published history.

[RESOURCE-MANIFEST.tsv](RESOURCE-MANIFEST.tsv) lists each excluded reference's relative placement, purpose, exact bytes and SHA-256. It contains no private account links or credentials. Authored indexes and download metadata remain in `external-resources/`, along with the two owned generated Weeks 11–51 ZIP collections. Owned PDFs in the year folders remain tracked. The small style examples in `exemplars.md` remain by the organizer's explicit choice; [REPUBLISHING.md](REPUBLISHING.md) records their known source caveat.

## Retained archive and reference lookup

The original local `math-circle/` working folder is deprecated. It retains the downloaded references, private records, original authored snapshot and original Git metadata for recovery. It is an archive, with no publishing remote; the canonical repository above is the source for new work. No Git metadata replacement or worker-lock release is needed for this cutover. Read the archive's local `DEPRECATED.md` for the machine-specific canonical path and retained resource location.

Use `MATH_CIRCLE_RESOURCE_ROOT` as a local reference lookup convention: set it to the directory containing the optional reference libraries, normally the active checkout's `external-resources/` or the retained archive's `external-resources/`. For example, after choosing an authorized location:

```sh
export MATH_CIRCLE_RESOURCE_ROOT="/path/to/reference-archive/external-resources"
```

Resolve a manifest entry such as `external-resources/jrmf/example.pdf` as `$MATH_CIRCLE_RESOURCE_ROOT/jrmf/example.pdf`, and verify its SHA-256 before using it. This convention supplies paths for opening references; worksheet builds use the editable sources in the active canonical checkout and each package's build instructions. Relative reference links in source notes work when authorized references occupy their ignored paths in that checkout. Historical workflow prompts and audit records retain their original execution paths; use the active checkout's files when starting new work.

An authorized private Drive resource store is another optional source of inputs. Obtain only the requested references through the user's authorized access, verify the manifest hashes, and keep local copies in ignored paths. No private store URL or credential belongs in this repository.

## Private records

The private session use logs and October 3 forecast remain in the retained archive's `plans/` folder. They are excluded from GitHub. Use the local archive or an explicitly authorized private copy when those records are required; report missing access.

A cloud clone does not contain these ignored files. Before reference-dependent research, check the required inputs and arrange the user's explicitly authorized private access or transfer. Verify manifest hashes and place any transferred references in their ignored relative paths. Local agents can read the preserved originals directly when authorized. Do not add whole books to Git, and do not silently substitute a source when an input is required but unavailable.

The worksheet generation workflow, its owned outlines and portable source packages can be inspected without the downloaded libraries. Rebuilding a package needs its documented TeX/Python dependencies; source research needs the references actually cited. Follow each package README and distinguish missing dependencies from missing reference inputs. GitHub source, private resources and chat attachments do not synchronize automatically.
