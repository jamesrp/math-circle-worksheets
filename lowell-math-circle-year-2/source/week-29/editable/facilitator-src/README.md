# Adult facilitator guide

Edit `guide.json`, then run `python3 build.py` from this directory. Requires Python 3, ReportLab, and DejaVu Sans fonts. Output is `../facilitator-guide.pdf`. The builder fails if a page overflows. Mathematical tables were independently enumerated; see `checks.json`. Final student files were not altered.

Render for review with `pdftoppm -r 110 -png ../facilitator-guide.pdf ../facilitator-qa/page`. Inspect every page after changes.

Run `python3 check_math.py` for independent standard-library verification of the finite cases across this five-week set. It writes nothing.
