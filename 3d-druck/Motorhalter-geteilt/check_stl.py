from pathlib import Path
from collections import Counter
import json, math
results=[]
for path in sorted(Path(__file__).parent.glob('*.stl')):
    vertices=[];ids={};triangles=[];face=[]
    for line in path.read_text().splitlines():
        fields=line.split()
        if fields and fields[0]=='vertex':
            v=tuple(float(x) for x in fields[1:]);key=tuple(round(x,5) for x in v)
            if key not in ids: ids[key]=len(vertices);vertices.append(v)
            face.append(ids[key])
            if len(face)==3:triangles.append(face);face=[]
    edges=Counter();orientation=Counter();parent=list(range(len(vertices)))
    def root(i):
        while i!=parent[i]:parent[i]=parent[parent[i]];i=parent[i]
        return i
    volume=0
    for a,b,c in triangles:
        for i,j in ((a,b),(b,c),(c,a)):
            edges[tuple(sorted((i,j)))]+=1;orientation[tuple(sorted((i,j)))]+=1 if i<j else -1
            parent[root(i)]=root(j)
        v,w,u=vertices[a],vertices[b],vertices[c]
        volume+=(v[0]*(w[1]*u[2]-w[2]*u[1])+v[1]*(w[2]*u[0]-w[0]*u[2])+v[2]*(w[0]*u[1]-w[1]*u[0]))/6
    bounds=[round(max(v[i] for v in vertices)-min(v[i] for v in vertices),3) for i in range(3)]
    bad=sum(x!=2 for x in edges.values());winding=sum(x!=0 for x in orientation.values());components=len({root(i) for i in range(len(vertices))})
    result=dict(file=path.name,triangles=len(triangles),dimensions_mm=bounds,volume_mm3=round(volume,2),nonmanifold_edges=bad,inconsistent_edges=winding,components=components)
    results.append(result)
    assert bad==0 and winding==0 and components==1 and volume>0 and max(bounds)<100, result
Path(__file__).with_name('Pruefbericht.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
