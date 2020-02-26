x=[int(x) for x in input().split(',')]
for i in x :
	f=1
	for j in range (1,i+1):
		f=f*j
	print(f,end=',')
