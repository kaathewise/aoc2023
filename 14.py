from functools import reduce
from re import finditer, sub

#print(sum((d:=g[0].count('O'))*(2*g.end()-d+1)//2 for c in zip(*open(0)) for g in finditer('[.O]+',''.join(c[::-1]))))

(m:={}) or reduce((lambda a,i:a and (print(a[0][int(j+(1e9-j)%(i/4-j))]) if not i%4 and (j:=m.get(a[1])) else (a[0] if i%4 else m.update({a[1]:i/4}) or a[0]+[sum(i+1 for c in a[1] for i,p in enumerate(c) if p=='O')],(*map(''.join,zip(*(sub('[.O]+',lambda m:''.join(sorted(m[0])),c) for c in a[1][::-1]))),)))),range(1000),[[],(*(''.join(c)[::-1] for c in zip(*open(0).read().split())),)])
