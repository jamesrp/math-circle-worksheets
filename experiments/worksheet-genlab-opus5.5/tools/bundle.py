#!/usr/bin/env python3
"""Create a blinded evaluation bundle from a packet directory.

Usage: bundle.py SRC_DIR SOURCE_LABEL [--pid PID]
SRC_DIR must contain k-1.pdf, grades-2-3.pdf, grades-4-5.pdf.
Writes eval/bundles/<PID>/<band>/page-NN.png (110 dpi) + text.txt, and records
PID -> SOURCE_LABEL in eval/private/blind-map.json (never shown to judges).
"""
import json, os, random, shutil, string, subprocess, sys, glob, datetime

ROOT = "/home/claude/genlab"
BANDS = ["k-1", "grades-2-3", "grades-4-5"]
MAP = f"{ROOT}/eval/private/blind-map.json"

def load_map():
    if os.path.exists(MAP):
        return json.load(open(MAP))
    return {}

def new_pid(existing):
    while True:
        pid = "P" + "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
        if pid not in existing:
            return pid

def main():
    src, label = sys.argv[1], sys.argv[2]
    m = load_map()
    pid = sys.argv[4] if len(sys.argv) > 4 and sys.argv[3] == "--pid" else None
    for k, v in m.items():
        if v["source"] == label and pid is None:
            print(f"label {label} already bundled as {k}; reusing")
            pid = k
    pid = pid or new_pid(m)
    out = f"{ROOT}/eval/bundles/{pid}"
    if os.path.exists(out):
        shutil.rmtree(out)
    info = {}
    for b in BANDS:
        pdf = f"{src}/{b}.pdf"
        if not os.path.exists(pdf):
            raise SystemExit(f"missing {pdf}")
        d = f"{out}/{b}"
        os.makedirs(d)
        subprocess.run(["pdftoppm", "-r", "110", "-png", pdf, f"{d}/page"], check=True)
        # normalize names to page-NN.png
        pngs = sorted(glob.glob(f"{d}/page-*.png"))
        for p in pngs:
            n = int(p.rsplit("-", 1)[1].split(".")[0])
            os.rename(p, f"{d}/page-{n:02d}.png")
        txt = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True, check=True).stdout
        open(f"{d}/text.txt", "w").write(txt)
        info[b] = len(pngs)
    m[pid] = {"source": label, "src_dir": os.path.abspath(src), "pages": info,
              "bundled": datetime.datetime.now().isoformat(timespec="seconds")}
    os.makedirs(os.path.dirname(MAP), exist_ok=True)
    json.dump(m, open(MAP, "w"), indent=1)
    print(json.dumps({"pid": pid, "pages": info}))

if __name__ == "__main__":
    main()
