from re import findall

(m:=[(x+1j*y,u+1j*v,2j*v) for s in open(0) for x,y,z,u,v,_ in [[*map(int,findall(r'-?\d+',s))]]]) and print(sum((d:=-(u*(w:=v-r)).imag)!=0 and (t:=((x-y)*w).imag/d)>0 and (s:=((x-y)*(u-q)).imag/d)>0 and all(2e14<=p<=4e14 for g in [x+t*u,y+s*v] for p in [g.imag,g.real]) for x,u,q in m for y,v,r in m)//2)
