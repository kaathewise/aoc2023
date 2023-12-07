from collections import Counter

#print(sum((i+1)*int(x) for i,(_,x) in enumerate(sorted(map(str.split,open(0)),key=lambda x:('111212211323145'.find(''.join(map(str,sorted(Counter(x[0]).values())))),*(map('23456789TJQKA'.find,x[0])))))))

print(sum((i+1)*int(x) for i,(_,x) in enumerate(sorted(map(str.split,open(0)),key=lambda x:(str({11111:12,1112:244,122:356,113:4606,23:5077,14:67007,5:700007}[int(''.join(map(str,(sorted(Counter(x[0]).values())))))])[x[0].count('J')],*(map('J23456789TQKA'.find,x[0])))))))
