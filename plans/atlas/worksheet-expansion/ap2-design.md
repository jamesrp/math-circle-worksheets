# AP2: eight mathematical-physics investigations

Design and mathematical-check handoff, September 25, 2026. Files contain exactly AP-11 through AP-18, with **24 proposed student pages, 48 fully keyed prompts and eight fully keyed guide extensions**. No renderer or PDF has been created for this batch. The original cards and the accepted first ten are unchanged.

The drafts keep the physics assumptions as mathematical hypotheses. They do not present a counting game as a derivation of continuum mechanics, thermodynamics, quantum theory or relativity. The finite/concrete stages still have actual payoffs: underdetermination, optimal construction, a complete attainable range, an exact sampler, an invariant, or identifiability. Every family includes meaningful choices, delayed hints, full solutions, source evidence, materials, timing, prerequisite gates and diagram specifications.

## Arcs and decisions

| Family | Student arc and proof destination | Gate and candid fit |
| --- | --- | --- |
| AP-11 — flow | Invent a conserving and nonconserving tube label → design distinct area-weighted velocity profiles → classify every nonnegative branch split → distinguish storage, leaks and compressible mass conservation. The payoff is both a rejection certificate and an explicit family of indistinguishable possibilities. | Fractions, units and weighted means; algebra for the full line of branch solutions. Vector calculus is a separate guide extension. Promising with a facilitator attentive to mean normal velocity. |
| AP-12 — refraction | Choose trial crossings and distinguish time from distance → derive the exact x=3 candidate → prove a unique global optimum → solve a closed shoreline gate → choose a speed that makes a learner’s crossing optimal. | Calculus is core. Numerical trials alone are not described as a satisfactory proof. The endpoint task prevents a rote “differentiate and set zero” worksheet. Advanced/specialist. |
| AP-13 — coherent waves | Choose a phase to dim one detector → design exact cancellation with a changed amplitude → derive every attainable intensity → exhibit phase ambiguity → choose a reference wave that distinguishes it → recover and audit arbitrary phase coordinates. | Trigonometry and squared amplitudes; the full-period averages are supplied and optionally proved by integration. Promising at that gate; signed-wave addition alone is an earlier stop. |
| AP-14 — heat engines | Create energy-balanced but entropy-forbidden claims → derive a sharp ideal work bound → compare learner-chosen intermediate reservoirs → prove cascade independence → locate irreversibility and derive lost work = cold temperature × entropy generation. | Algebra with the second law visibly supplied. Reversible equality is an ideal model; passing necessary conditions is not an engine construction. Promising with careful heat signs and kelvin temperatures. |
| AP-15 — quantum questions | Choose a measurement order and construct actual Born/update trees → diagnose a no-update shortcut → compare repeated and interrupted questions → verify projector noncommutation → choose the single basis maximizing a changed final answer. | Vectors, dot products and finite probability; matrices and trig are marked continuations. The exact restricted quantum model is retained. Advanced/specialist; no unexplained classical coin surrogate. |
| AP-16 — finite Ising model | Choose equal-magnetization patterns with different weights → distinguish favored individual from favored class → certify enumeration by a reversible link encoding → design an exact small sampler → close the ring and discover its parity obstruction → prove a rejection sampler. | Counting and weighted fractions. Strongest first-pilot candidate in this batch, with ring conditioning later. Finite partition functions are not marketed as phase transitions. |
| AP-17 — reunited clocks | Choose legal turn events → compute 10 versus 8 → design a six-unit reading → prove the stationary route maximizes proper time among all finite allowed routes → transform every event and recheck the entire journey in another inertial frame. | Algebra, squares, roots and coordinate conventions. Actual relativistic interval and Lorentz transformation are supplied; fixed-distance turnaround optimization uses calculus only in the extension. Promising with a carefully read spacetime plot. |
| AP-18 — orbital inverse problem | Infer one mass from selected exact cards → construct an inconsistency certificate → characterize a bounded-error compatible set → design a guaranteed separating measurement → expose a projection ambiguity → prove one independently measured orbital period resolves it. | Algebra, positive roots and units; physical force balance is supplied and optionally derived with calculus. Promising with clear measured versus inferred quantities. This is a conditional inverse problem, not proof of a gravity law. |

## Changes beyond the atlas cards

The cards provided useful anchors, but each became a sequence with a later mathematical turn. AP-11 adds area weighting and complete nonuniqueness, AP-12 adds constrained and inverse optimization, AP-13 adds phase retrieval, AP-14 adds telescoping and a quantitative loss certificate, AP-15 adds an optimal-disturbance bound with a scope-breaking two-question extension, AP-16 adds an exact generative sampler and its cycle repair, AP-17 adds a full coordinate-invariance audit, and AP-18 adds a constructive nonidentifiability/identification pair.

No table has been sized to reveal the number of final solutions. Some tasks intentionally supply their full finite domain (four-spin agreement counts, for example); their class weights remain unknown. The first AP-13 wave sums, AP-12 minimizing crossing, AP-15 optimal angle, AP-16 ring parity and AP-17 legal-turn region are not printed as initial answers. Diagrams are specified explicitly in each family’s `figures`; production must preserve those stage boundaries.

## Sources and scientific scope

Specialized claims were freshly revisited, rather than inherited from the original cards. Source fields give inspected sections and exact adaptation scope. The refraction source is now MIT’s direct Fermat/Snell derivation, and the orbit source is the official OpenStax circular-force/period derivation; these better support the actual new questions than the original broader citations. Tong’s continuity, wave/energy, thermodynamics, quantum measurement, Ising and relativity expositions were reread at the named passages.

Student laws are hypotheses, and the keys distinguish necessary tests from complete physical solutions. In particular:

- AP-11’s velocity is the area-weighted mean normal velocity; density is uniform on each section only in the stated gas example. Continuity does not determine pressure or momentum dynamics.
- AP-12 optimizes only one straight segment in each constant-speed half-plane, with one flat-interface crossing; its strict second derivative supplies the global result.
- AP-13 uses one location, one frequency, one scalar/polarization channel and stable relative phase. The same averaging normalization is used for every observation.
- AP-14 uses cyclic devices and fixed positive kelvin reservoir temperatures, with no net intermediate storage and explicit heat directions.
- AP-15 normalizes states, includes the projection update and specifies which recorded Z outcome is compared. It does not claim the final unconditional mixed states differ for the two mutually unbiased orders.
- AP-16 counts only the displayed links, uses independent replacement draws in its sampler, and explicitly conditions on successful ring closure.
- AP-17 uses future timelike segments with c=1 and a stated instantaneous-turn idealization. The primed turnaround is (4,0), the primed reunion (25/2,−15/2); the same one inertial frame covers both legs.
- AP-18 distinguishes exact true speeds, guaranteed-error intervals, and a separately stipulated common projection factor. Error intervals carry no probability law. True radii are never substituted by projected radii or diameters.

## Mathematical evidence

`ap2-checks.py` passes and writes `ap2-checks-results.json`. It audits the exact family/schema/prompt set; all chosen finite numerical instances; the two optimal-refraction time comparison and inverse-design regressions; exact phasor coordinates; heat cascades and loss identity; noncommuting projector products and all four-state histories; every four-spin open/ring configuration and its sampler probability; general finite partition sums for n=3…8 at four rational weights; the exact Lorentz metric identity and transformed events; and orbit interval/projection/period calculations. Printed-key anchors guard important constants against later editorial corruption.

Finite regressions are not promoted to general proofs. The keys separately provide strict convexity, attainable phase range, telescoping for any finite cascade, the single-question probability bound, path/cycle encoding, every-route proper-time inequality and the necessary-and-sufficient inverse-model compatibility statements. Sources supply the physical laws, not the new instance answers.

The independent design/math review is closed in `review-ap2-design.md`. None of the activities has been classroom-piloted; timing is a staged facilitation proposal. Two or three meetings may be appropriate for some three-page investigations.

## Independent review repairs

The reciprocal reviewer independently derived all 48 prompts and eight extensions and requested three clarifications. AP-16's spoken launch now says “large weighted ticket bag,” withholding the total the learner must derive. AP-17's first chosen turnaround explicitly has nonzero spatial coordinate, `T=(t,d)` with `d≠0`. AP-13's dimming-phase key now includes all `2πk` translates of its representative interval, covering the stated real phase domain. The exact checker passes after these changes; the reviewer reread and closed all three.

The editor also requested phase-identification precision: AP-13 prompt 5 now asks for the compatible phases “modulo 2π,” since adding a full period leaves the signal unchanged. This matches the existing key and supplies no phase values.
