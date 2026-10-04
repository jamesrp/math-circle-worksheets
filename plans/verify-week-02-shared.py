"""Reuse the independently checked finite models with the shared diagram data.

The four-lamp graph has been rotated/redrawn, not changed combinatorially.
This explicitly checks the shared data rather than silently checking old inputs.
The core ring/network verifier remains source/week-02/verify.py.
"""
from pathlib import Path
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('lamp_room_checks', HERE / 'verify-week-02-k1-aux.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)
checker.DATA = json.loads((HERE / 'week-02-shared-data.json').read_text())
checker.OUTPUT = HERE / 'week-02-shared-checks.json'
checker.main()
report = json.loads(checker.OUTPUT.read_text())
report['id'] = 'F02-S-v1'
report['data_source'] = 'plans/week-02-shared-data.json'
report['problem_numbering_note'] = 'Source target keys 1-14 retain their numbers; drawing keys 15-24 become shared Problems 33-42. Core ring/network keys are checked separately.'
checker.OUTPUT.write_text(json.dumps(report, indent=2) + '\n')
