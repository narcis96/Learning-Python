import time
import sys
f = open('test.txt', 'r+')
print "server is up",
while (1):
	print ".",
	f.seek(0, 0)
	var = int(f.read())
	var -= 20
	f.seek(0, 0)
	f.write(str(var))
	time.sleep(3) 
