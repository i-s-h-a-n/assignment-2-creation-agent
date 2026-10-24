# Assignment 5 Emerging Technology Diffusion Agent

This agent assesses RAG diffusion for the internal financial-research assistant carried forward from Assignment 2. It supports timing judgment, not final adoption approval.

Start with records/agent_record.md, records/diffusion_factor_assessment.md and records/test_record.md. Dated evidence is in records/evidence_ledger.json and embedded in every case. Read records/validation_log.txt for executed checks.

From the scaffold root, with Python 3:
```
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/diffusion_agent --case agents/diffusion_agent/cases/primary.json
python tools/validate_response.py agents/diffusion_agent/responses/primary_response.json
python agents/diffusion_agent/check_package.py
```
Repeat the builder for contrast_1 and contrast_2; use the generated packet in ChatGPT and save its JSON. No API account is required. Prepared prompt packets are also preserved under records/.

The saved responses were authored in the current Codex conversation from the assembled case, source ledger and specialist instructions. They are representative interactive analyses, not independent repeated model trials, deployed software telemetry, or empirical organizational results. The constructed adversarial fixture is explicitly labeled.

Before submission, review and personally endorse or revise the judgment, supply team details if applicable, and check Brightspace due dates and submission rules.
