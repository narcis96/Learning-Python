import sys
print sys.argv[1] + " + " + sys.argv[2] + " = " + str(int(sys.argv[1]) + int(sys.argv[2]))

for i in range (1, 5):
    print "We're on time %d" % (i)

for x in xrange(3):
    print x
else:
    print 'Final x = %d' % (x)

for x in range(1, 11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
	
list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
    for x in list:
        print x, 
	print

#var = raw_input("Please enter something: ")
#print "you entered:", var	
#print ('Hello')