from collections import Counter

#print(sum((i+1)*int(x) for i,(_,x) in enumerate(sorted(map(str.split,open(0)),key=lambda x:(sum(x*x for x in Counter(x[0]).values()),*(map('23456789TJQKA'.find,x[0])))))))

print(sum((i+1)*int(x) for i,(_,x) in enumerate(sorted(map(str.split,open(0)),key=lambda x:(str({5:12,7:244,9:356,11:4606,13:5077,17:67007,25:700007}[sum(x*x for x in Counter(x[0]).values())])[x[0].count('J')],*(map('J23456789TQKA'.find,x[0])))))))
