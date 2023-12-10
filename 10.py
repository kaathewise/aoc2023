import sys
from itertools import accumulate

sys.setrecursionlimit(20000)

#(m:={j-i*1j:c for i,s in enumerate(open(0)) for j,c in enumerate(s)}) and print(next((g:=lambda x,y:x==s or 1+g((d:=1j**'|L-J|7-F'.find(m[x])/(y-x))+x,x))(s+d,s)//2 for s in m if m[s]=='S' for d in [1,-1,1j] if s+d in m and (1j**('|L-J|7-F'.find(m[s+d])/2)/d).real<0.5))

(f:=[*open(0)]) and (m:={j-i*1j:c for i,s in enumerate(f) for j,c in enumerate(s)}) and print(next((g:=lambda x,y:(y*(x-x.imag*1j*2)).imag-1+(x!=s and g((d:=1j**'|L-J|7-F'.find(m[x])/(y-x))+x,x)))(s+d,s)/2+1 for s in m if m[s]=='S' for d in [1,-1,1j] if s+d in m and (1j**('|L-J|7-F'.find(m[s+d])/2)/d).real<0.5))
