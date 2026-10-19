# Assignment 4 Promethean Technology Classification Agent

Student: Ishan Vaghani. Version 1.1, 19 October 2026.

This specialist applies the course's significance framework to GenAI, while keeping the lender application decision separate. It extends the Assignment 3 branch of the existing repository and preserves the frozen Brightspace scaffold. No API account, key or paid service is needed.

Start with `records/agent_record.md`, then `records/testing_and_handoff.md`. Criteria are in `specialist_instructions.md`; the four-source register is in `records/evidence_register.json`. Five inputs, prompt packets and saved responses are included, plus a deficient preliminary draft and revision note.

From the repository root:

```text
python tools/build_prompt.py --agent agents/promethean_classification_agent --case agents/promethean_classification_agent/cases/primary.json --out work/promethean_primary.txt
python tools/validate_response.py agents/promethean_classification_agent/responses/primary_response.json
python agents/promethean_classification_agent/verify.py
```

To perform a fresh interactive run, paste the generated packet into ChatGPT, save its JSON separately and validate it. Repeat for contrast_1, contrast_2_posture, hype_challenge and insufficient_component. Preserve the model/version if available, date, full response and any failure. The local scripts construct prompts and check files; they do not invoke a model.

The included responses were authored and reviewed in this Codex conversation using the generated packet and case contexts. They are transparent worked examples, not independent fresh-chat trials or operational deployment measurements. A fresh-chat replication is the strongest next test.

The Agent Record follows all sections A-E of the supplied template in Markdown. No separate student endorsement is fabricated. The student should review the proposed independent judgment before submission and confirm any Brightspace-specific format or case requirement.

