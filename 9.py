from operator import sub

#(n:=lambda*s:len(s) and s[-1]+n(*map(sub,s[1:],s))) and print(sum(n(*map(int,s.split())) for s in open(0)))

(n:=lambda*s:len(s) and s[0]-n(*map(sub,s[1:],s))) and print(sum(n(*map(int,s.split())) for s in open(0)))
