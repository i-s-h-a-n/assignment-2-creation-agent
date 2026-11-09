# Organizational Adoption Agent

Assignment 7, Ishan Vaghani, November 9, 2026, version 1.1.
Topic: passive back-support exoskeletons for manual palletizing. The same task is tested in two fictional organizations; a third case withholds governance evidence.

From the scaffold root, using Python 3:
```
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/organizational_adoption_agent --case agents/organizational_adoption_agent/cases/primary.json --out agents/organizational_adoption_agent/records/primary_prompt.txt
python tools/validate_response.py agents/organizational_adoption_agent/responses/primary_response.json
python agents/organizational_adoption_agent/check_package.py
```
Repeat packet construction with contrast_1 and contrast_2. Paste each complete packet into ChatGPT, save its JSON response, validate, then review reasoning against records/test_record.md. There is no API integration and no API key requirement. The included responses are representative model-authored analyses generated during assignment preparation in Codex, not independent ChatGPT reruns. Do not confuse the analyst agent with the physical exoskeleton technology it evaluates.

Read records/readiness_framework_and_profiles.md for ratings and gates, records/evidence_ledger.json for original sources and limits, records/decision_and_handoff.md for the independent judgment, and records/test_record.md for comparison and revision evidence. The check script verifies saved artifacts; it does not execute a model or prove safety. Prior branches preserve earlier labs; this branch adds this specialist to the Lab 6 tree without changing frozen files.
