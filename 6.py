from math import prod,sqrt

#print(prod((sqrt(t*t-4*d-4)+t%2)//2*2+1-t%2 for t,d in zip(*(map(int,s.split()[1:]) for s in open(0)))))

print([(sqrt(t*t-4*d-4)+t%2)//2*2+1-t%2 for t,d in [[int(''.join(s.split()[1:])) for s in open(0)]]][0])
