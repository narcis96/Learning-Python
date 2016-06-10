def Pow(x, n):
	ret = 1
	for i in range (1, n+1):
		ret = ret*x
	return ret;
def Pow_Log(x, n):
	if(n == 0):
		return 1
	y = Pow_Log(x,n/2)
	if(n%2 == 0):
		return y*y
	return Pow_Log(x,n-1)*x

print Pow_Log(2,9)
