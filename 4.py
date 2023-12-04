from functools import reduce
from itertools import repeat, zip_longest

#print(sum((1<<len(s)-len({*s}))//2 for s in map(str.split,open(0))))

print(reduce((lambda r,x:(c:=next(r[1])) and (r[0]+c,map(sum,zip_longest(r[1],repeat(c,x),fillvalue=0)))), (len(s)-len({*s}) for s in map(str.split,open(0))), (0,repeat(1)))[0])
