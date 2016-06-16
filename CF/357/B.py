from sys import *
n=int(input())
for a in xrange(n//1234567+1):
   for b in xrange((n-a*1234567)//123456+1):
      if (n-a*1234567-b*123456)%1234==0: 
      	print("YES");
      	exit()
print("NO")