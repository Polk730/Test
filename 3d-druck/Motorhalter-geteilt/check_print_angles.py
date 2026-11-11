from pathlib import Path
import math,json
p=Path(__file__).with_name('03-Standfuss.stl')
vv=[tuple(map(float,line.split()[1:])) for line in p.read_text().splitlines() if line.strip().startswith('vertex ')]
bad=[];angles=[]
for i in range(0,len(vv),3):
 a,b,c=vv[i:i+3];u=[b[j]-a[j] for j in range(3)];v=[c[j]-a[j] for j in range(3)]
 n=(u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]);norm=math.sqrt(sum(x*x for x in n))
 if not norm:continue
 nz=n[2]/norm
 if nz<-.00001 and max(a[2],b[2],c[2])>.001:
  angle=math.degrees(math.acos(min(1,-nz)))
  angles.append(angle)
  if angle<45-0.01:bad.append((i//3,angle,min(a[2],b[2],c[2])))
assert not bad,bad
report={'file':p.name,'print_orientation':'as exported, flat base Z=0','unsupported_faces_above_bed_below_45_degrees':len(bad),'minimum_downward_surface_angle_degrees':round(min(angles),2) if angles else None,'minimum_supported_angle_required_degrees':45,'scope':'Geometric surface-angle check only; no slicer or physical print test.'}
p.with_name('Druckwinkelpruefung.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
