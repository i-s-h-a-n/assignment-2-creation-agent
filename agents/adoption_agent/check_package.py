"""Check contract and preserved case relationships, not factual truth or model repeatability."""
from pathlib import Path
import json, subprocess, sys
a=Path(__file__).resolve().parent
root=a.parents[1]
def read(p): return json.loads((a/p).read_text())
def validate(value,schema,path='response'):
 t=schema.get('type')
 assert {'object':lambda:isinstance(value,dict),'array':lambda:isinstance(value,list),'string':lambda:isinstance(value,str)}.get(t,lambda:True)(),f'{path}: invalid type'
 if t=='object':
  assert all(k in value for k in schema.get('required',[])),f'{path}: missing required keys'
  if schema.get('additionalProperties') is False: assert set(value)<=set(schema['properties']),f'{path}: extra keys'
  for k,v in value.items():
   if k in schema.get('properties',{}): validate(v,schema['properties'][k],path+'.'+k)
 if t=='array':
  for i,v in enumerate(value): validate(v,schema['items'],f'{path}[{i}]')
subprocess.run([sys.executable,str(root/'tools/check_frozen_core.py')],check=True)
ins=json.loads((root/'core/input_schema.json').read_text());out=json.loads((root/'core/output_schema.json').read_text())
categories={'ADOPT_IMPLEMENT','BOUNDED_EXPERIMENT','PROOF_OF_CONCEPT','MONITOR','DEFER','REJECT_FOR_PRESENT'}
for case in ['primary','contrast_1','contrast_2']:
 validate(read(f'cases/{case}.json'),ins,case)
 r=read(f'responses/{case}_response.json');validate(r,out,case)
 assert r['evidence'] and r['abstention_or_more_information_needed']
 assert r['recommendation_management_implication'].split(':')[0] in categories
 subprocess.run([sys.executable,str(root/'tools/validate_response.py'),str(a/f'responses/{case}_response.json')],check=True)
 print(case+': full contract check passed')
p=read('cases/primary.json');c=read('cases/contrast_1.json')
assert {k for k in p if p[k]!=c[k]}=={'adoption_posture','management_question'}
pr=read('responses/primary_response.json');cr=read('responses/contrast_1_response.json')
assert pr['general_et_finding']==cr['general_et_finding']
assert pr['application_finding']==cr['application_finding']
assert pr['evidence']==cr['evidence']
assert pr['recommendation_management_implication'].startswith('PROOF_OF_CONCEPT:')
assert cr['recommendation_management_implication'].startswith('DEFER:')
validate(read('responses/constructed_weak_response.json'),out,'weak fixture')
print('Weak fixture also passes structure: semantic review rejects its adoption conclusion')
print('Contrast invariants passed. These checks do not certify evidence, run a model or prove repeatability.')
