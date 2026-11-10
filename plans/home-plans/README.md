# Home plans

A home plan is a short plan for kitchen-table math: one adult, two or three children aged about 5 to 9, no set length, and a route that can stop anywhere and be picked up next time. Home plans serve the [home-table collection](../../catalog/collections.toml) ("Kitchen-table math"), whose bar is a short plan, setup in under 10 minutes and a 20 to 30 minute route, tried once at home.

They differ from [room plans](../room-plans/README.md), which run a full Wednesday hour for eleven children. A home plan has no timetable or table jobs. Children play against each other and the adult, choose boards and rules, and record nothing beyond what helps them win. Each plan opens with a short theorem-first overview for the adult, every factual claim is checked by a script in [src/](src/), and the youngest child gets a version they can win or own.

Started November 5, 2026, after the organizer said the school circle will probably give way to informal sessions at home after fall quarter. Plans are unpiloted until tried; after a session, add a dated line under "How it went" in the plan, in the organizer's words, and a line in `catalog/use-log.toml`.

To rebuild a plan's printable PDF after editing: `python3 plans/room-plans/build/build.py plans/home-plans/<plan>.md` (pandoc and LibreOffice; the room plans' style). Pictures beside the plan are embedded; the Sprouts picture is drawn by `python3 plans/home-plans/src/sprouts_figure.py` (matplotlib). Board pages are LaTeX in `src/`, built with `pdflatex` in a scratch folder and copied here.

| Weekend | Plan | Theme | Status |
|---|---|---|---|
| November 7 and 8, 2026 | [Poisoned cookie (Chomp)](2026-11-08-poisoned-cookie.md) ([printable](2026-11-08-poisoned-cookie.pdf), 3 pages; [boards](2026-11-08-poisoned-cookie-boards.pdf), 2 pages, 30 mm squares; checker [src/chomp_check.py](src/chomp_check.py)) | draft `poisoned-cookie` | unpiloted |
| November 8, 2026 (Sunday) | [Sprouts](2026-11-08-sprouts.md) ([printable](2026-11-08-sprouts.pdf), 3 pages; worked example [picture](2026-11-08-sprouts-example.png) from [src/sprouts_figure.py](src/sprouts_figure.py); checker [src/sprouts_check.py](src/sprouts_check.py)) | the Sprouts part of draft `games-decided-before-they-start` | played once at home, November 8 |
