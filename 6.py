from math import prod,sqrt

#print(prod(t-(t-sqrt(t*t-4*d))//2*2-1 for t,d in zip(*(map(int,s.split()[1:]) for s in open(0)))))

print([t-(t-sqrt(t*t-4*d))//2*2-1 for t,d in [[int(''.join(s.split()[1:])) for s in open(0)]]][0])
