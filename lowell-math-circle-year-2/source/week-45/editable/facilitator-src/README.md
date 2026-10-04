Run `python3 build.py` here to rebuild ../facilitator-guide.pdf from guide.json. Student files remain separate. Prepared October 3, 2026; unpiloted.

Verification: uses final K-1 P4 repaired wording (student SHA256 3ca35bc6177849da080aa873f083aef2e40d7d93713a8f952d9b5858acbc1d86). The numbered face is shown and only red-showing rounds are compared.

Source audit: supplied probability.md identifies Mintz’s Bertrand box section. Direct retrieval returned 403 during preparation; Dartmouth seminar/outreach pages and search indexing verify title, author, and Fall 2022 provenance. The adult PDF therefore attributes general background only and gives no unverified locator. All six-ticket mathematics independently enumerated.

Mathematical audit: run `python3 check_math.py` to regenerate checks.json using exhaustive finite enumerations (not simulation). Build requires Python reportlab and DejaVu Sans fonts in /usr/share/fonts/truetype/dejavu/. The editable guide.json and build.py are authoritative; no other source is needed to rebuild.
