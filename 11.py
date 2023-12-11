from itertools import count
from math import sumprod

#(m:=[(i,j) for i,s in enumerate(open(0)) for j,c in enumerate(s) if c=='#']) and print(sum((a:=sorted(x[i] for x in m)) and (c:=dict(zip(sorted({*a}),count()))) and sumprod((2*x-c[x] for x in a),range(-len(m)+1,len(m),2)) for i in [0,1]))

(m:=[(i,j) for i,s in enumerate(open(0)) for j,c in enumerate(s) if c=='#']) and print(sum((a:=sorted(x[i] for x in m)) and (c:=dict(zip(sorted({*a}),count()))) and sumprod((x+999999*(x-c[x]) for x in a),range(-len(m)+1,len(m),2)) for i in [0,1]))
