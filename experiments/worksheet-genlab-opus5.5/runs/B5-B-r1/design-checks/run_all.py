"""Runs every design check and writes the combined log to output.txt.
Also confirms the 'no broken problem' guard: every rule on every page allows taking 1,
so no non-empty position is ever stuck and 'whoever takes the last counter wins' (or loses,
in the K-1 poison game) always decides the game."""
import subprocess
import sys
from pathlib import Path
from games import losing_table

here = Path(__file__).parent

RULES_ON_PAGES = {
    "K-1": [(1, 2), (1, 2, 3), (1, 3)],
    "2-3": [(1, 2), (1, 3, 4), (1, 3), (1, 2, 3), (1, 4)],
    "4-5": [(1, 2), (1, 2, 3), (1, 3, 4), (1, 4), (1, 4, 5), (1, 2, 4), (1, 3, 5), (1, 2, 6),
            (1, 2, 3, 4), (1, 6, 9)],
}

log = []
allok = True
for band, rules in RULES_ON_PAGES.items():
    good = all(1 in S for S in rules)
    # every non-empty pile has a legal move, so every game ends with someone taking the last counter
    good &= all(any(s <= n for s in S) for S in rules for n in range(1, 200))
    log.append(f"[{band}] all rules on the pages allow taking 1 (no stuck positions): "
               f"{'ok' if good else 'FAIL'}")
    allok &= good

for script in ["check_k1.py", "check_23.py", "check_45.py"]:
    r = subprocess.run([sys.executable, str(here / script)], capture_output=True, text=True,
                       cwd=here)
    log.append(f"\n===== {script} (exit {r.returncode}) =====\n{r.stdout}{r.stderr}")
    allok &= r.returncode == 0

log.append("\nEVERYTHING PASSED" if allok else "\nSOMETHING FAILED")
(here / "output.txt").write_text("\n".join(log) + "\n")
print("\n".join(log[:3]))
print("EVERYTHING PASSED" if allok else "SOMETHING FAILED")
sys.exit(0 if allok else 1)
