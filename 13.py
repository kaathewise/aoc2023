from operator import ne

#print(sum(i*q for s in map(str.split,open(0).read().split('\n\n')) for m,q in [(s,1),([*zip(*s)],100)] for i in range(len(m[0])) if sum(sum(map(ne,l[i-1::-1],l[i:])) for l in m)==0))

print(sum(i*q for s in map(str.split,open(0).read().split('\n\n')) for m,q in [(s,1),([*zip(*s)],100)] for i in range(len(m[0])) if sum(sum(map(ne,l[i-1::-1],l[i:])) for l in m)==1))
