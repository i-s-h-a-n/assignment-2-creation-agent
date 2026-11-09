# Tests and revision record

November 9, 2026. Runtime: representative analyses authored by the model in Codex against the frozen common contract and included specialist/case packets. No API call, independent second model run, physical device test or worker interview occurred. Local scripts construct packets and validate saved files only.

## Comparison and manual reasoning review
| Case | Expected decision | Saved result | Reasoning review |
|---|---|---|---|
| Primary HarborLane | NOT_READY | NOT_READY | Ownership, assessment and worker-governance gaps block exposure; interest, money and aids are acknowledged as strengths. |
| Contrast 1 CedarBridge | READY_FOR_BOUNDED_PILOT | READY_FOR_BOUNDED_PILOT | Existing staffing, funding, task review, worker input and daily care enable limited learning; no scale approval. |
| Contrast 2 missing governance evidence | INSUFFICIENT_INFORMATION | INSUFFICIENT_INFORMATION | Requests signed assessment and actual stop authority; does not invent approval or mark unknown as absent. |

Held fixed: technology, application, business need, adoption posture, consequences, decision horizon and external evidence. Changed: organizational capabilities, ownership and controls. General ET and application findings are identical in all three final responses. The readiness conclusion and prioritized actions change. Several capabilities vary together, so the first contrast shows context sensitivity, not the causal contribution of any single factor. The third case isolates the governance-evidence omission.

## Informative failure and revision
constructed_weak_response.json is a deliberately constructed negative control representing the v1.0 failure mode, not a spontaneous failed model run. It says enthusiasm and purchase funding justify immediate use and postpones training, despite explicit governance/ownership gaps. It passes the common structural validator because all required fields and types exist. Manual review rejects it: no accountable stop authority, no qualified fit/task assessment, no protected withdrawal and no daily owner. This demonstrates a reasoning defect, not a broken JSON format.

Version 1.1 adds explicit stage gates, UNKNOWN separate from GAP, eight evidence-linked assessments, no averaged readiness score, and owner/dependency/closure requirements for prioritized actions. Applying the revised rules to the unchanged primary case yields NOT_READY with P0 actions before worker exposure. No test input was relaxed to obtain a favorable result. The negative control is preserved to make this limitation inspectable.

## Verification limits
The check script validates all saved responses, full JSON Schema when available, frozen hashes, fixed-context invariants, expected readiness labels and an evidence request in the withheld-governance case. Manual review additionally checks that each recommendation addresses a stated gap and that existing contrast capabilities are used. Exact text assertions verify these saved fixtures; they are not a general semantic evaluator or proof of model reliability. Repeat model runs with new organizations are still needed before integration.
