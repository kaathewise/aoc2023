from functools import cache
from re import findall, match

print(sum((g:=cache(lambda m,d: not d if not m else (m[0]!='#' and g(m[1:],d))+(d and match(r'[#?]{%d}[.?]'%d[0],m) and g(m[d[0]+1:],d[1:]) or 0)))(s[0]+'.',(*map(int,findall(r'\d+',s[1])),)) for s in map(str.split,open(0))))

#print(sum((g:=cache(lambda m,d: not d if not m else (m[0]!='#' and g(m[1:],d))+(d and match(r'[#?]{%d}[.?]'%d[0],m) and g(m[d[0]+1:],d[1:]) or 0)))('?'.join([s[0]]*5)+'.',(*map(int,findall(r'\d+',s[1])),)*5) for s in map(str.split,open(0))))
