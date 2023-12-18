from functools import reduce

#(a:=reduce(lambda a,d:(a[0]+d,a[1]+a[0].real*d.imag*1j+abs(d)/2),(int(s[2:-11])*1j**'RUL'.find(s[0]) for s in open(0)),(0,1))[1]) and print(a.real+abs(a.imag))

(a:=reduce(lambda a,d:(a[0]+d,a[1]+a[0].real*d.imag*1j+abs(d)/2),(int(s[-8:-3],16)*1j**int(s[-3]) for s in open(0)),(0,1))[1]) and print(a.real+abs(a.imag))
