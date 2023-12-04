from functools import reduce
from itertools import chain, repeat
from operator import add

#print(sum((1<<len(s)-len({*s}))//2 for s in map(str.split,open(0))))

print(reduce((lambda r,x:(c:=next(r[1])) and (r[0]+c,chain(map(add,repeat(c,x),r[1]),r[1]))), (len(s)-len({*s}) for s in map(str.split,open(0))), (0,repeat(1)))[0])
