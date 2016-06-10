import time
import sys
f = open('test.txt', 'r+')
while (1):
	f.seek(0, 0)
	var = int(f.read())
	var -= 20
	f.seek(0, 0)
	f.write(str(var))
	time.sleep(3) 
