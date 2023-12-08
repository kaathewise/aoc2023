from re import findall
from itertools import accumulate,cycle

(f:=[*open(0)]) and (m:={a:b for s in f[2:] for a,*b in [findall(r'\w+',s)]}) and print(next(i for i,x in enumerate(accumulate(cycle(f[0][:-1]),(lambda a,d:m[a][d=='R']),initial='AAA')) if x=='ZZZ'))

# No part 2, because it doesn't feel right to include a solution heavily tied to a particular input (LCM-based).
