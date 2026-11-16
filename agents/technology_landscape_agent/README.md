# Satellite methane landscape specialist

Assignment 8 | Ishan Vaghani | 16 November 2026

From the repository root, build a packet with `python tools/build_prompt.py --agent agents/technology_landscape_agent --case agents/technology_landscape_agent/cases/primary.json`. Submit the resulting text to ChatGPT, save its JSON response and run `python tools/validate_response.py agents/technology_landscape_agent/responses/primary.json`. Repeat for contrast_1 and contrast_2. Run `python tools/check_frozen_core.py` from the root.

Use cases/ for the full intake, records/ for source register, dated prompt snapshots and diagnosis, and responses/ for all four interactive outputs. Cases and management thresholds are fictional. Replace the case and refresh the evidence for any new site. The agent neither polls satellite feeds nor performs automatic inspections.
