from collections import Counter

#print(sum((i+1)*int(x) for i,(_,x) in enumerate(sorted(map(str.split,open(0)),key=lambda x:(sorted(Counter(x[0]).values())[::-1],*map('23456789TJQKA'.find,x[0]))))))

print(sum((i+1)*int(x) for i,(_,x) in enumerate(sorted(map(str.split,open(0)),key=lambda x:(max(sorted(Counter(x[0].replace('J',w)).values())[::-1] for w in x[0]),*(map('J23456789TQKA'.find,x[0])))))))
