from itertools import accumulate,chain,count,repeat,takewhile

(m:={n[1:]:(n[0],*t.split(', ')) for s in open(0) for n,t in [s[:-1].split(' -> ')]}) and (s:={n:0 for n in m}) and (c:=1000+sum(1j**v for i in range(1000) for q in takewhile(len,accumulate(count(),(lambda q,_:[*chain(*(s.update({x:[1-all(s[y] for y in m if x in m[y][1:]),1-s[x]][m[x][0]=='%']}) or zip(m[x][1:],repeat(s[x])) if x in m and (m[x][0]!='%' or 1-v) else [] for x,v in q))]),initial=[*zip(m['roadcaster'][1:],repeat(0))])) for _,v in q)) and print(c.imag*c.real)

# Part 2 solved manually 
