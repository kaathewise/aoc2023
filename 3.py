from itertools import groupby
from math import prod
from operator import itemgetter
from re import finditer,search

#(f:=open(0).read()) and (N:=f.find('\n')+1) and (s:='.'*N+f+'.'*N) and print(sum(int(x[0]) for x in finditer(r'\d+',s) if any(search(r'[^0-9.\n]',s[i+x.start()-1:i+x.end()+1]) for i in [-N,0,N])))

(f:=open(0).read()) and (N:=f.find('\n')+1) and (s:='.'*N+f+'.'*N) and print(sum((t:=[*g]) and len(t)==2 and t[0][1]*t[1][1] for _,g in groupby(sorted((j,int(x[0])) for x in finditer(r'\d+',s) for i in [-N,0,N] for j in range(i+x.start()-1,i+x.end()+1) if s[j]=='*'),itemgetter(0))))
