from math import inf
import sys

sys.setrecursionlimit(100000)

#(m:={i+1j*j:c for i,s in enumerate(open(0)) for j,c in enumerate(s) if c!='#'}) and (T:=max(x.real for x in m)) and (S:={0}) and print((g:=lambda x,d:x in S or x not in m and -inf or x.real!=T and [S.add(x) or max([-inf]+[g(x+e,e) for e in [[1j**'v>^'.find(m[x])],[1,-1,1j,-1j]][m[x]=='.'] if d+e])+1,S.remove(x)][0])(1j,1))

(m:={i+1j*j for i,s in enumerate(open(0)) for j,c in enumerate(s) if c!='#'}) and (T:=max(x.real for x in m)) and (S:={0}) and (C:={}) or (j:=lambda x,d:[(x,d) not in C and C.update({(x,d):(len(o:=[e for e in [1,-1,1j,-1j] if e+d and x+e in m])>1 or x.real==T) and (x,0) or o and (r:=j(x+o[0],o[0])) and (r[0],r[1]+1) or (0,0)}),C[x,d]][1]) and print((g:=lambda *X:[not s or x in S and -inf or x.real==T and s or [S.add(x) or max(g(x+d,d) for d in [1,-1,1j,-1j] if x+d in m)+s+1,S.remove(x)][0] for x,s in [j(*X)]][0])(1j,1))
