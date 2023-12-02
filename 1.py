from functools import reduce
from re import findall, search
from sys import stdin

#print(sum((d:=findall(r'\d', s)) and int(d[0]+d[-1]) for s in stdin.readlines()))

print(sum((r:='one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9') and int(''.join(str(r.split('|').index(search(x+'(%s)'%r,s)[1])%9+1) for x in ['', '.*'])) for s in stdin.readlines()))
