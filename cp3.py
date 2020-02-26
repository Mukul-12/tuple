x=[int(a) for a in input().split(',')]
a=max(x)
b=min(x)
y=[]
for i in range(b,a+1):
	if i not in x:
		y.append(i)
print(y)
	
