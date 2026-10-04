#!/usr/bin/env python3
"""Deterministic surface metrics for a packet (Layer A of EVAL-v1). Descriptive, not a quality verdict.

Usage: lint.py SRC_DIR OUT_JSON
"""
import json, re, sys, collections, subprocess
import pdfplumber

BANDS = ["k-1", "grades-2-3", "grades-4-5"]

ENCOURAGE = [r"great (job|work)", r"awesome", r"amazing", r"fantastic", r"you('ve| have) got this", r"have fun",
             r"good luck", r"way to go", r"well done", r"\bsuper\b", r"\bcool\b", r"you did it", r"nice work",
             r"keep going", r"don'?t give up", r"you can do (it|this)", r"\bbrilliant\b", r"\bexciting\b", r"\byay\b"]
META = [r"in this (activity|worksheet|lesson|packet)", r"\btoday (we|you)\b", r"\byou will (learn|explore|discover)",
        r"\blet'?s\b", r"your (mission|job|quest|challenge) (is|today)", r"\bwelcome\b", r"\bready\?",
        r"we('ll| will) (explore|learn|discover)"]
LABELS = [r"\bhint\b", r"\bbonus\b", r"\bchallenge\b", r"fun fact", r"did you know", r"think about it", r"warm[- ]?up",
          r"\bextension\b", r"go further", r"\bremember\b", r"\btip\b", r"try this", r"super challenge", r"\bstretch\b",
          r"wonder", r"big idea", r"\bmission\b", r"\bdetective", r"\bexplorer"]
NOTXBUTY = [r"\bnot (just|only|merely|simply) [^.?!]{1,60}?\bbut\b", r"\bisn'?t (just|only)? ?[^.?!]{1,40}?[,;—-] ?(it'?s|it is)\b",
            r"\bit'?s not [^.?!]{1,40}?[,;—-] ?it'?s\b", r"\bnot [a-z]+, but\b"]
NAMEDATE = [r"\bname\s*:", r"\bdate\s*:"]
EXPLAIN = [r"\bexplain\b", r"\bwhy\b", r"how do you know", r"how can you be sure", r"convince"]
FOLLOWUP = [r"what do you notice", r"what do you wonder", r"compare (with|your)", r"share (with|your)", r"talk (with|to) (a|your) partner",
            r"check (with|your) (a )?partner"]
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⭕]")
PROBLEM = re.compile(r"\bproblem\s+\d+", re.I)

def count(pats, text):
    return sum(len(re.findall(p, text, flags=re.I)) for p in pats)

def hits(pats, text):
    out = []
    for p in pats:
        for m in re.finditer(p, text, flags=re.I):
            s = max(0, m.start() - 30); e = min(len(text), m.end() + 30)
            out.append(text[s:e].replace("\n", " "))
    return out

def heading_lines(pdf):
    """Lines of >=3 words set in bold or larger-than-body type, excluding 'Problem N' starts and the
    page header/footer bands. Short bold labels under diagrams (e.g. 'Board A') are not counted."""
    sizes = collections.Counter()
    pages_words = []
    for page in pdf.pages:
        ws = page.extract_words(x_tolerance=1.5, extra_attrs=["fontname", "size"])
        for w in ws:
            sizes[round(w["size"], 1)] += len(w["text"])
        pages_words.append((page, ws))
    body = sizes.most_common(1)[0][0] if sizes else 10
    heads = []
    for page, ws in pages_words:
        H = page.height
        lines = collections.defaultdict(list)
        for w in ws:
            lines[round(w["top"] / 4)].append(w)
        for key, line in lines.items():
            line = sorted(line, key=lambda w: w["x0"])
            top = line[0]["top"]
            if top < 0.08 * H or top > 0.92 * H:
                continue
            # split a visual line into runs separated by big gaps (side-by-side labels)
            runs, cur = [], [line[0]]
            for a, b in zip(line, line[1:]):
                if b["x0"] - a["x1"] > 25:
                    runs.append(cur); cur = [b]
                else:
                    cur.append(b)
            runs.append(cur)
            for run in runs:
                text = " ".join(w["text"] for w in run).strip()
                if len(run) < 3 or PROBLEM.match(text):
                    continue
                bold = sum(1 for w in run if "bold" in w["fontname"].lower() or "black" in w["fontname"].lower()) / len(run)
                big = sum(1 for w in run if w["size"] > body + 1.0) / len(run)
                if bold > 0.8 or big > 0.8:
                    heads.append(text[:80])
    return body, heads

def band_metrics(path):
    pdf = pdfplumber.open(path)
    text = subprocess.run(["pdftotext", "-layout", path, "-"], capture_output=True, text=True, check=True).stdout
    words = re.findall(r"[A-Za-z’']+", text)
    body, heads = heading_lines(pdf)
    m = {
        "pages": len(pdf.pages),
        "words": len(words),
        "problems": len(set(int(x) for x in re.findall(r"\bproblem\s+(\d+)", text, flags=re.I))),
        "exclamations": text.count("!"),
        "em_dashes": text.count("—"),
        "questions": text.count("?"),
        "emoji": len(EMOJI.findall(text)),
        "encouragement": count(ENCOURAGE, text),
        "meta": count(META, text),
        "labels": count(LABELS, text),
        "not_x_but_y": count(NOTXBUTY, text),
        "name_date": count(NAMEDATE, text),
        "explain_prompts": count(EXPLAIN, text),
        "followups": count(FOLLOWUP, text),
        "extra_headings": len(heads),
        "body_font_size": body,
        "examples": {
            "encouragement": hits(ENCOURAGE, text)[:6], "meta": hits(META, text)[:6], "labels": hits(LABELS, text)[:8],
            "not_x_but_y": hits(NOTXBUTY, text)[:6], "headings": heads[:12],
        },
    }
    tells = (m["exclamations"] + m["em_dashes"] + m["emoji"] + m["encouragement"] + m["meta"] + m["labels"]
             + m["not_x_but_y"] + m["name_date"] + m["extra_headings"])
    m["tells"] = tells
    m["tells_per_100w"] = round(100 * tells / max(1, m["words"]), 2)
    return m

def main():
    src, out = sys.argv[1], sys.argv[2]
    res = {b: band_metrics(f"{src}/{b}.pdf") for b in BANDS}
    tot = {k: sum(res[b][k] for b in BANDS) for k in ["pages", "words", "problems", "tells", "extra_headings",
                                                       "exclamations", "em_dashes", "encouragement", "meta", "labels",
                                                       "not_x_but_y", "explain_prompts", "followups"]}
    tot["tells_per_100w"] = round(100 * tot["tells"] / max(1, tot["words"]), 2)
    res["total"] = tot
    json.dump(res, open(out, "w"), indent=1)
    print(json.dumps(tot))

if __name__ == "__main__":
    main()
