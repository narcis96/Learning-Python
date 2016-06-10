import time
import sys
f = open('test.txt', 'r')
while(1):
	f.seek(0, 0)
	var = int(f.read())
	print "var = ", var	
	time.sleep(1) 