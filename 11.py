from itertools import count
from math import sumprod

#print(sum((c:=dict(zip(sorted({*a}),count()))) and sumprod((2*x-c[x] for x in sorted(a)),range(-len(a)+1,len(a),2)) for a in zip(*((i,j) for i,s in enumerate(open(0)) for j,c in enumerate(s) if c=='#'))))

print(sum((c:=dict(zip(sorted({*a}),count()))) and sumprod((x+999999*(x-c[x]) for x in sorted(a)),range(-len(a)+1,len(a),2)) for a in zip(*((i,j) for i,s in enumerate(open(0)) for j,c in enumerate(s) if c=='#'))))
