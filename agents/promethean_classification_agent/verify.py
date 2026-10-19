"""Validate saved artifacts; does not call a model or prove future reliability."""
from pathlib import Path
import json, subprocess, sys, hashlib
a=Path(__file__).resolve().parent
root=a.parents[1]
def get(p):return json.loads(p.read_text(encoding='utf-8'))
subprocess.run([sys.executable,str(root/'tools/check_frozen_core.py')],check=True,cwd=root)
required=get(root/'core/input_schema.json')['required']
schema=get(root/'core/output_schema.json')
for p in sorted((a/'cases').glob('*.json')):
 c=get(p)
 assert all(isinstance(c.get(k),str) and c[k].strip() for k in required),p
 print('INPUT PASS',p.name)
for p in sorted((a/'responses').glob('*.json')):
 subprocess.run([sys.executable,str(root/'tools/validate_response.py'),str(p)],check=True)
 c=get(p)
 assert set(c)==set(schema['required']),p
 for key in ['contrary_evidence_or_limitations','change_monitoring_triggers','abstention_or_more_information_needed']:
  assert all(isinstance(x,str) for x in c[key]),(p,key)
 print('OUTPUT CONTRACT PASS',p.name)
p=get(a/'responses/primary_response.json')
for name in ['contrast_1','contrast_2_posture','hype_challenge']:
 c=get(a/f'responses/{name}_response.json')
 assert c['general_et_finding']==p['general_et_finding']
 print('SAVED GENERAL FINDING INVARIANT',name)
assert get(a/'responses/contrast_1_response.json')['recommendation_management_implication']!=p['recommendation_management_implication']
assert get(a/'responses/hype_challenge_response.json')['recommendation_management_implication']==p['recommendation_management_implication']
assert 'ABSTAIN' in get(a/'responses/insufficient_component_response.json')['general_et_finding']
draft=get(a/'responses/initial_incomplete_draft.json')
markers=['Mode:','Suppression:','10X','democratization','irreversibility']
assert not all(m in draft['general_et_finding'] for m in markers)
assert all(m in p['general_et_finding'] for m in markers)
print('EXPECTED DRAFT WEAKNESS DETECTED; corrected response contains required analytical markers')
print('PASS: saved artifact checks. Same-chat examples; no independent or repeated model evaluation claimed.')

