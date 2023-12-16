from itertools import accumulate,chain,count
from operator import not_

#(m:={j-1j*i:c for i,s in enumerate(open(0)) for j,c in enumerate(s[:-1])}) and print((s:=set()) or next(filter(not_,accumulate(count(),lambda f,_:{*chain(*(s.add(x) or [(x[0]+d,d) for d in [[x[1]],[1j,-1j],[1,-1],[-1j/x[1]],[1j/x[1]]]['.|-\\/'.find(m[x[0]])]] for x in f-s if x[0] in m))},initial={(0,1)}))) or len({x[0] for x in s}))

(m:={j-1j*i:c for i,s in enumerate(open(0)) for j,c in enumerate(s[:-1])}) and print(max((s:=set()) or next(filter(not_,accumulate(count(),lambda f,_:{*chain(*(s.add(x) or [(x[0]+d,d) for d in [[x[1]],[1j,-1j],[1,-1],[-1j/x[1]],[1j/x[1]]]['.|-\\/'.find(m[x[0]])]] for x in f-s if x[0] in m))},initial={(x,d)}))) or len({x[0] for x in s}) for x in m for d in [1,-1,1j,-1j] if x-d not in m))
