from functools import reduce
from re import findall, search
from sys import stdin

#print(sum((d:=findall(r'\d', s)) and int(d[0]+d[-1]) for s in stdin.readlines()))

print(sum((t:='one two three four five six seven eight nine'.split()) and (r:='|'.join(t)) and int(''.join(x if len(x)==1 else str(t.index(x)+1) for x in [search(r'\d|'+r, s)[0], search(r'\d|'+r[::-1], s[::-1])[0][::-1]])) for s in stdin.readlines()))
