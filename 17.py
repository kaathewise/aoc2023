from heapq import heappop, heappush
from itertools import count
from operator import not_

#(m:={i+1j*j:int(c) for i,s in enumerate(open(0)) for j,c in enumerate(s[:-1])}) and (T:=[*m][-1]) and (q:=[(0,0,0,1,3)]) and (s:=set()) or next(filter(not_,([print(v) if x==T else [heappush(q,(m[y]+v,id(y),y,e,n)) or s.add((y,e,n)) for t in [0,1,-1] if (k or t) and (y:=x+(e:=d*1j**t)) in m and ((y,e,(n:=[k-1,2][t])) not in s)] or 1 for v,_,x,d,k in [heappop(q)]][0] for _ in count())))

(m:={i+1j*j:int(c) for i,s in enumerate(open(0)) for j,c in enumerate(s[:-1])}) and (T:=[*m][-1]) and (q:=[(0,0,0,1,0),(0,1,0,1j,0)]) and (s:=set()) or next(filter(not_,([print(v) if x==T and k<7 else [heappush(q,(m[y]+v,id(y),y,e,n)) or s.add((y,e,n)) for t in [0,1,-1] if [k,k<7][t] and (y:=x+(e:=d*1j**t)) in m and ((y,e,(n:=[k-1,9][t])) not in s)] or 1 for v,_,x,d,k in [heappop(q)]][0] for _ in count())))
