from functools import reduce

#print(sum(reduce((lambda a,c:(a+ord(c))*17%256),w,0) for w in open(0).read()[:-1].split(',')))

(m:={i:{} for i in range(256)}) and [b.pop(l,0) if w[-1]=='-' else b.update({l:int(w[-1])}) for w in open(0).read()[:-1].split(',') for l in [w[:-1-(w[-2]=='=')]] for b in [m[reduce((lambda a,c:(a+ord(c))*17%256),l,0)]]] and print(sum((i+1)*(j+1)*v for i in m for j,v in enumerate(m[i].values())))
