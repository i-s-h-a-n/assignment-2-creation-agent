from pathlib import Path
import json, subprocess, sys
root=Path(__file__).resolve().parents[2]
a=Path(__file__).resolve().parent
subprocess.run([sys.executable,str(root/'tools/check_frozen_core.py')],check=True)
for p in sorted((a/'responses').glob('*.json')):
 subprocess.run([sys.executable,str(root/'tools/validate_response.py'),str(p)],check=True)
try:
 import jsonschema
except ImportError:
 print('Full schema check unavailable; standard course validator only')
else:
 out=json.loads((root/'core/output_schema.json').read_text())
 ins=json.loads((root/'core/input_schema.json').read_text())
 for p in (a/'responses').glob('*.json'):jsonschema.validate(json.loads(p.read_text()),out)
 for p in (a/'cases').glob('*.json'):jsonschema.validate(json.loads(p.read_text()),ins)
 print('FULL INPUT AND OUTPUT SCHEMA CHECKS PASSED')
names=['primary','contrast_1','contrast_2']
c=[json.loads((a/f'cases/{n}.json').read_text()) for n in names]
r=[json.loads((a/f'responses/{n}_response.json').read_text()) for n in names]
for key in ['emerging_technology','intended_application','business_need','adoption_posture','risk_consequence_context','management_question','time_horizon','additional_context']:
 assert c[0][key]==c[1][key]==c[2][key],key
for key in ['general_et_finding','application_finding']:
 assert r[0][key]==r[1][key]==r[2][key],key
assert r[0]['evidence'][:3]==r[1]['evidence'][:3]==r[2]['evidence'][:3]
for res,label in zip(r,['NOT_READY','READY_FOR_BOUNDED_PILOT','INSUFFICIENT_INFORMATION']):
 assert res['organization_specific_finding'].startswith(label)
 assert 'P0' in res['recommendation_management_implication']
assert any('signed' in q and 'stop' in q for q in r[2]['abstention_or_more_information_needed'])
for key in ['organization_specific_finding','recommendation_management_implication']:
 assert r[0][key]!=r[1][key]
print('SAVED CASE INVARIANTS AND READINESS EXPECTATIONS PASSED')
print('Reasoning still requires human review; no model was executed by this script.')
