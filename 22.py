from functools import reduce
from itertools import product, starmap
from operator import add, and_, sub
from re import findall

#(m:=sorted([(d:=map(int,findall(r'\d+',s))) and (*((*map(add,x,(0,1)),) for x in zip(*zip(d,d,d))),)[::-1] for s in open(0)])) and (H:={}) or (C:=set()) or [(F:={*product(*starmap(range,b[1:]))}) and (h:=max([H[x][0] for x in F&{*H}]+[0])) and (B:={H[x][1:] for x in F&{*H} if H[x][0]==h}) and len(B)==1 and C.add(B.pop()) or [H.update({x:(h-sub(*b[0]),*b)}) for x in F] for b in m] and print(len(m)-len(C))

(m:=sorted([(d:=map(int,findall(r'\d+',s))) and (*((*map(add,x,(0,1)),) for x in zip(*zip(d,d,d))),)[::-1] for s in open(0)])) and (H:={}) or (C:={}) or [(F:={*product(*starmap(range,b[1:]))}) and C.update({b:(h:=max([H[x][0] for x in F&{*H}]+[0])) and {b,*reduce(and_,map(C.get,{H[x][1:] for x in F&{*H} if H[x][0]==h}))} or {b}}) or [H.update({x:(h-sub(*b[0]),*b)}) for x in F] for b in m] and print(sum(map(len,C.values()))-len(C))
