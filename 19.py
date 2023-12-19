from collections import Counter
from functools import reduce
from math import prod
from re import findall

#(F:=open(0).read().split('\n\n')) and (m:={n:c for f in F[0].split('\n') for n,c in [f[:-1].split('{')]}) and (D:=map(int,findall(r'\d+',F[1]))) and print(sum((g:=lambda n:g(next((t for p,o,v,t in findall(r'(\w)(.)(\d+):(\w+)',m[n]) if c['xmas'.find(p)]*(s:=[1,-1][o=='<'])>int(v)*s),m[n].split(',')[-1])) if n in m else (n=='A')*sum(c))('in') for c in zip(*[D]*4)))

(M:=4001) and (F:=open(0).read().split('\n\n')[0]) and (m:={n:[(' xmas'.find(p)*(s:=[1,-1][o=='<']),int(v)*s,t) for p,o,v,t in findall(r'(\w)(.)(\d+):(\w+)',c)]+[c.split(',')[-1]] for f in F.split('\n') for n,c in [f[:-1].split('{')]}) and print((g:=lambda n,c:n!='R' and (prod(max(M-1-c[i]-c[-i],0) for i in range(1,5)) if n=='A' else (a:=reduce(lambda a,r:(a[0]+g(r[2],a[1]|Counter({r[0]:r[1]%M})),a[1]|Counter({-r[0]:(-r[1]-1)%M})),m[n][:-1],(0,c))) and (a[0]+g(m[n][-1],a[1]))))('in',Counter()))
