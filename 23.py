from functools import cache
from itertools import accumulate, count
from math import inf
import sys

sys.setrecursionlimit(100000)

#(m:={i+1j*j:c for i,s in enumerate(open(0)) for j,c in enumerate(s) if c!='#'}) and (T:=max(x.real for x in m)) and (S:={0}) and print((g:=lambda x,d:x in S or x not in m and -inf or x.real!=T and [S.add(x) or max([-inf]+[g(x+e,e) for e in [[1j**'v>^'.find(m[x])],[1,-1,1j,-1j]][m[x]=='.'] if d+e])+1,S.remove(x)][0])(1j,1))

(m:={i+1j*j for i,s in enumerate(open(0)) for j,c in enumerate(s) if c!='#'}) and (T:=max(x.real for x in m)) and (t:=lambda a,_:[(len(o:=[e for e in [1,-1,1j,-1j] if e+d and x+e in m])>1 or x.real==T) and (x,0,s) or o and (x+o[0],o[0],s+1) or (0,0,0) for x,d,s in [a]][0]) and (k:=cache(lambda X:next((x,s) for x,d,s in accumulate(count(),t,initial=(*X,0)) if not d))) and (S:={0}) and print((g:=lambda *X:[not s or x in S and -inf or x.real==T and s or [S.add(x) or max(g(x+d,d) for d in [1,-1,1j,-1j] if x+d in m)+s+1,S.remove(x)][0] for x,s in [k(X)]][0])(1j,1))
