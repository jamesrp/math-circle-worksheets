#!/usr/bin/env python3
"""Make guide-stage run folders for drafts that belong to an existing week.

The return-visit drafts (plans/return-visit-drafts/) get a full return-visit
guide; the K-1 drafts (plans/k1-drafts/) get a K-1 guide section that will
replace their week guide's adult-led K-1 route. Each run folder gets
WRITER.md, CRITIC.md and REVISE.md with every placeholder filled; run them in
order, each in a fresh agent, as worksheet-workflow/guide/README.md says.

    python3 worksheet-workflow/guide/make_week_runs.py            # all eleven
    python3 worksheet-workflow/guide/make_week_runs.py rv-53 k1-91
"""
import os
import sys

GUIDE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(GUIDE))

# kind-week: (header topic, guide footer id)
RUNS = {
    "rv-53": ("Connecting networks", "W53-RV-FAC-v1"),
    "rv-58": ("Fair division", "W58-RV-FAC-v1"),
    "rv-62": ("Conflict networks", "W62-RV-FAC-v1"),
    "rv-63": ("Cards away from home", "W63-RV-FAC-v1"),
    "k1-57": ("Area from dots", "N57-K-FAC-v1"),
    "k1-66": ("Lamplighter streets", "GGT66-K-FAC-v1"),
    "k1-81": ("Buckets of Fish", "W81-K-FAC-v1"),
    "k1-87": ("Voting and agendas", "W87-K-FAC-v1"),
    "k1-91": ("Rotor-router machines", "F91-K-FAC-v1"),
    "k1-97": ("Square remainders", "W97-K-FAC-v1"),
    "k1-98": ("Growing from a few seeds", "W98-K-FAC-v1"),
}


def fill(text, values):
    for key, value in values.items():
        text = text.replace("{" + key + "}", value)
    left = [line for line in text.splitlines() if "{" in line and "}" in line]
    assert not left, f"unfilled placeholder: {left[0]}"
    return text


def make(name):
    kind, week = name.split("-")
    topic, guide_id = RUNS[name]
    run = os.path.join(REPO, "tmp", "guide-runs", f"{name}-v1")
    os.makedirs(os.path.join(run, "draft", "src"), exist_ok=True)
    if kind == "rv":
        draft = os.path.join(REPO, "plans", "return-visit-drafts", f"week-{week}")
        pages = ", ".join(f"`{draft}/{band}.pdf`" for band in ("k-1", "grades-2-3", "grades-4-5"))
        outline = os.path.join(REPO, "worksheet-workflow", "outlines", f"week-{week}-return-visit.md")
        readme = os.path.join(REPO, "plans", "return-visit-drafts", "README.md")
        out, writer, kind_name = "facilitator.pdf", "RV-GUIDE-WRITER.md", "return-visit facilitator guide"
    else:
        draft = os.path.join(REPO, "plans", "k1-drafts", f"week-{week}")
        pages = f"`{draft}/k-1.pdf`"
        outline = os.path.join(REPO, "worksheet-workflow", "outlines", f"week-{week}-k1.md")
        readme = os.path.join(REPO, "plans", "k1-drafts", "README.md")
        out, writer, kind_name = "k1-guide.pdf", "K1-GUIDE-WRITER.md", "K–1 guide section"
    week_dir = os.path.join(REPO, "lowell-math-circle-year-2", f"week-{week}")
    base_guide = os.path.join(week_dir, f"week-{week}-facilitator.pdf")
    materials = os.path.join(week_dir, f"week-{week}-materials.pdf")
    for path in (draft, outline, readme, base_guide):
        assert os.path.exists(path), path
    values = {
        "REPO": REPO, "WEEK": week, "TOPIC": topic, "RUN": run, "OUT": out, "PAGES": pages,
        "DRAFT": draft, "OUTLINE": outline, "README": readme, "BASEGUIDE": base_guide,
        "BASEMAT": f" and its materials file `{materials}`" if os.path.exists(materials) else "",
        "GUIDEID": guide_id, "KIND": kind_name,
    }
    for stage, template in (("WRITER", writer), ("CRITIC", "WEEK-GUIDE-CRITIC.md"), ("REVISE", "WEEK-GUIDE-REVISE.md")):
        with open(os.path.join(GUIDE, template)) as f:
            text = fill(f.read(), values)
        with open(os.path.join(run, f"{stage}.md"), "w") as f:
            f.write(text)
    print(run)


if __name__ == "__main__":
    for name in sys.argv[1:] or RUNS:
        make(name)
