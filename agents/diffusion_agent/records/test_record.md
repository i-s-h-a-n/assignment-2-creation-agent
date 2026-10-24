# Test and revision record

Date 2026-10-23. Runtime: this interactive Codex conversation. The frozen builder produced three complete prompt packets. Responses were authored in this conversation using their components; no separate API calls or independent fresh-chat replications were performed.

## Cases and outcomes

| Case | Changed input | Stable conclusion | Changed timing implication |
|---|---|---|---|
| Primary | Moderate fast follower | Implementations exist; peer majority stage unproven | References and readiness first, then conditional shadow evaluation |
| Contrast 1 | Adoption posture only to aggressive | Identical general and application findings and sources | Earlier bounded learning with peer evidence gathered in parallel |
| Contrast 2 | Adoption posture only to conservative | Identical general and application findings and sources | Offline preparation and evidence gates before analyst-facing pilot |

The comparison deliberately controls all other fields. General/application paragraphs are reused to preserve the same evidence-grounded assessment. This tests the consistency of the saved analytical examples; it is not evidence of model repeatability or resistance to every prompt variation. The timing differences are reasoned proposals, not observed outcomes.

## Preserved weakness and revision

responses/adversarial_weak_response.json is a CONSTRUCTED adversarial fixture, not a spontaneous failed model run. Its general finding falsely extrapolates from broad AI use and within-firm assistant uptake to RAG early-majority diffusion. Both structural checks accepted it during the actual validation run. Semantic review rejected it: its populations, technology definitions and denominators do not match the conclusion.

Version 1.0's general evidence instruction did not expressly prevent these extrapolations. Version 1.1 adds technology/denominator checks, separate observation and publication dates, recency flags, explicit peer-stage abstention, and a weak-claim correction. The three final responses preserve the rejected claim as a caution and avoid endorsing it. A structural validator cannot enforce this reasoning; the control is explicit instructions plus source review.

A further observed tool limitation: the course validator omits extra-property checks. check_package.py, kept within the editable specialist folder, checks every validation constraint used by the supplied schemas and rejects a deliberately added top-level field. It uses the standard library because the optional jsonschema package was unavailable. The frozen tool was not modified.

## Executed checks and limits

See validation_log.txt: all three case/response pairs passed the supplied schema constraints and course validator; posture-only variation, fixed evidence, named factors, timing differences and frozen-core integrity passed. These checks establish structure and saved-example consistency, not truth, safety or empirical business benefit.

Still needed for stronger evaluation: independent fresh-chat reruns, a missing-evidence case, a different application, a current comparable-peer source, and review by the student. Preserve failures from those runs. No claims are made that they have already occurred.
