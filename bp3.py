s=input()
r=input()
a=len(r)
c=0
for i in range(0,len(s)):
	if s[i:a+i]==r:
		c+=1
print(c)
