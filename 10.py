import sys
from itertools import accumulate

sys.setrecursionlimit(20000)

#(m:={j-i*1j:c for i,s in enumerate(open(0)) for j,c in enumerate(s)}) and (g:=lambda x,p:m[x]=='S' or 1+g((d:=1j**'|L-J|7-F'.find(m[x])/p)+x,-d)) and print(next(g(x+d,-d)//2 for x in m if m[x]=='S' for d in [1,-1,-1j] if x+d in m and (1j**('|L-J|7-F'.find(m[x+d])/2)/d).real<0.5))

(f:=[*open(0)]) and (m:={j-i*1j:c for i,s in enumerate(f) for j,c in enumerate(s)}) and (g:=lambda x,p:m[x]=='S' and p or (d:=1j**'|L-J|7-F'.find(m[x])/p) and m.update({x:' #'[m[x]in'|LJ']}) or g(x+d,-d)) and print(next(m.update({x:' #'[1j==g(x+d,-d)]}) or sum(c*s for i in range(N) for c,s in accumulate(range(M),(lambda a,j:((a[0]+(m[j-i*1j]=='#'))%2,(m[j-i*1j] not in ' #'))),initial=(0,0))) for N,M in [[len(f),len(f[0])-1]] for x in m if m[x]=='S' for d in [1,-1,-1j] if x+d in m and (1j**('|L-J|7-F'.find(m[x+d])/2)/d).real<0.5))
