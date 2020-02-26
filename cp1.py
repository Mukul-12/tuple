x=[int(a) for a in input().split(',')]
y=[]
for i in x:
	if i!=0:
	    y.append(i)
b=len(x)
c=len(y)
d=b-c
for i in range(d):
	y.append(0)
print(y)
	

