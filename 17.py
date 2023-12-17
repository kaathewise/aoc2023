from heapq import heappop, heappush
from itertools import count
from operator import not_

#(m:={i+1j*j:int(c) for i,s in enumerate(open(0)) for j,c in enumerate(s[:-1])}) and (T:=max((x.real,x.imag) for x in m)) and (q:=[(0,0,0,0,3)]) and (s:=set()) or next(filter(not_,([print(v) if (i,j)==T else [heappush(q,(m[w]+v,w.real,w.imag,e,n)) or s.add((w,e,n)) for t in [0,1,-1] if k|t and (w:=i+1j*j+1j**(e:=(d+t)%4)) in m and ((w,e,(n:=[k-1,2][t])) not in s)] or 1 for v,i,j,d,k in [heappop(q)]][0] for _ in count())))

(m:={i+1j*j:int(c) for i,s in enumerate(open(0)) for j,c in enumerate(s[:-1])}) and (T:=max((x.real,x.imag) for x in m)) and (q:=[(0,0,0,0,0),(0,0,0,1,0)]) and (s:=set()) or next(filter(not_,([print(v) if (i,j)==T and k<7 else [heappush(q,(m[w]+v,w.real,w.imag,e,n)) or s.add((w,e,n)) for t in [0,1,-1] if [k,k<7][t] and (w:=i+1j*j+1j**(e:=(d+t)%4)) in m and ((w,e,(n:=[k-1,9][t])) not in s)] or 1 for v,i,j,d,k in [heappop(q)]][0] for _ in count())))
