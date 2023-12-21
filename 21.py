from functools import reduce

(m:={i+1j*j:c for i,s in enumerate(open(0)) for j,c in enumerate(s)}) and print(len(reduce((lambda f,_:{x+d for x in f for d in [1,-1,1j,-1j] if m.get(x+d)=='.'}),range(64),{x for x in m if m[x]=='S'}))+1)

# Part 2 solved manually
