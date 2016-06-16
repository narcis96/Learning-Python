s="NO"
for _ in xrange(int(input())):
	_,b,c=input().split()
	if int(c)>int(b)>=2400:s="YES"
print(s)