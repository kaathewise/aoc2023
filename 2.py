# With improvements from https://www.reddit.com/user/4HbQ/

from collections import Counter
from functools import reduce
from math import prod
from operator import or_
from re import findall

#print(sum(i+1 for i,s in enumerate(open(0)) if all('rgb'.find(w)+12>=int(n) for n,w in findall(r'(\d+) (\w)',s))))

print(sum(prod(reduce(or_,(Counter({w:int(n)}) for n,w in findall(r'(\d+) (\w)',s))).values()) for s in open(0)))
