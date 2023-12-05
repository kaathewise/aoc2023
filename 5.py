from functools import reduce
from itertools import chain
from re import findall

#(f:=open(0).read().split('\n\n')) and print(min(reduce((lambda s,m:[next((u+x-v for u,v,w in zip(*[map(int,findall(r'\d+',m))]*3) if v<=x<v+w),x) for x in s]),f[1:],map(int,findall(r'\d+',f[0])))))

(f:=open(0).read().split('\n\n')) and print(min(reduce((lambda s,m:(p:=[*zip(*[map(int,findall(r'\d+',m))]*3)]) and [next(((u+x-v,l) for u,v,w in p if v<=x<v+w),(x,l)) for x,l in reduce((lambda r,a:{*chain(*([(x,a-x),(a,x+l-a)] if x<a<x+l else [(x,l)] for x,l in r))}),chain(*((v,v+w) for _,v,w in p)),s)]),f[1:],zip(*[map(int,findall(r'\d+',f[0]))]*2)))[0])
