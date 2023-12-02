# With improvements from https://www.reddit.com/user/4HbQ/

from collections import Counter
from functools import reduce
from math import prod
from operator import or_
from re import findall

#print(sum(i+1 for i, s in enumerate(open(0)) if all(Counter({x[1]:int(x[0]) for x in findall(r'(\d+) (\w+)',c)})<=Counter(red=12,green=13,blue=14) for c in s.split(';'))))

print(sum(prod(reduce(or_,(Counter({x[1]:int(x[0]) for x in findall(r'(\d+) (\w+)',c)}) for c in s.split(';'))).values()) for s in open(0)))
