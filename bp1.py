from math import *
c=50
h=30
d=[int(x) for x in input().split(',')]
for i in d :
	q=sqrt((2*c*i)/h)
	print(int(q),end=',')
