from pathlib import Path
import json, subprocess, sys
from zipfile import ZipFile
root=Path(__file__).resolve().parents[2]
agent=Path(__file__).resolve().parent
log=[]
def note(x):
 print(x); log.append(x)
def validate(value,schema,path='$'):
 types={'object':dict,'array':list,'string':str}
 if 'type' in schema:
  assert isinstance(value,types[schema['type']]),path+' wrong type'
 if isinstance(value,dict):
  for k in schema.get('required',[]): assert k in value,path+' missing '+k
  props=schema.get('properties',{})
  if schema.get('additionalProperties') is False: assert not set(value)-set(props),path+' extra fields'
  for k,v in value.items():
   if k in props: validate(v,props[k],path+'.'+k)
 if isinstance(value,list) and 'items' in schema:
  for i,v in enumerate(value): validate(v,schema['items'],path+'['+str(i)+']')
schema=json.loads((root/'core/output_schema.json').read_text())
inputs=json.loads((root/'core/input_schema.json').read_text())
for name in ['primary','contrast_1','contrast_2']:
 case=json.loads((agent/f'cases/{name}.json').read_text())
 validate(case,inputs)
 response=json.loads((agent/f'responses/{name}_response.json').read_text())
 validate(response,schema)
 result=subprocess.run([sys.executable,str(root/'tools/validate_response.py'),str(agent/f'responses/{name}_response.json')],capture_output=True,text=True)
 assert result.returncode==0,result.stdout+result.stderr
 note(name+': all supplied input/output schema constraints PASS; course validator PASS')
primary=json.loads((agent/'cases/primary.json').read_text())
resp=json.loads((agent/'responses/primary_response.json').read_text())
for name in ['contrast_1','contrast_2']:
 case=json.loads((agent/f'cases/{name}.json').read_text())
 assert [k for k in primary if case[k]!=primary[k]]==['adoption_posture']
 r=json.loads((agent/f'responses/{name}_response.json').read_text())
 for field in ['general_et_finding','application_finding','evidence']: assert r[field]==resp[field]
 assert r['recommendation_management_implication']!=resp['recommendation_management_implication']
 note(name+': posture-only input; stable general/application/evidence; changed timing PASS')
weak=agent/'responses/adversarial_weak_response.json'
result=subprocess.run([sys.executable,str(root/'tools/validate_response.py'),str(weak)],capture_output=True,text=True)
assert result.returncode==0
validate(json.loads(weak.read_text()),schema)
note('Weak adversarial fixture: structural validation PASS despite unsupported majority claim; documented semantic review REJECTS.')
for factor in ['Relative advantage','Compatibility','Complexity','Trialability','Observability']: assert factor in resp['application_finding']
note('All five named factors present PASS; factual and analytical quality require human review.')
invalid=dict(resp,unauthorized_field=True)
try: validate(invalid,schema)
except AssertionError: note('Additional top-level field rejected PASS')
else: raise AssertionError('Extra field was accepted')
result=subprocess.run([sys.executable,str(root/'tools/check_frozen_core.py')],capture_output=True,text=True)
assert result.returncode==0,result.stdout
note(result.stdout.strip())
note('Checker implements every validation keyword used by these supplied schemas; not a general JSON Schema library.')
(agent/'records/validation_log.txt').write_text('\n'.join(log)+'\n')
