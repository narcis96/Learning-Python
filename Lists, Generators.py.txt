#list
mylist = [x*x for x in xrange(5)]
mylist.append(25)

print mylist
l2 = [2, 4, 6, 8]
mylist = mylist + l2

for i in mylist:
	print i,
print 

div6 = [x for x in range (20) if x%2 == 0 and x%3 == 0]
print 'div = ',div6[0:5]

v = [1] * 10
v[0] = 33
print v

s = "python is awesome"
v = s.split()
print v

#read-only list

print '..................'

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
print tuple

for x in tuple:
	print x, 
print x

for x in tuple:
	print x, 
print x



print '..................'

#generator
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step		

mygenerator = (x for x in my_range(1,4,0.5) )
for x in mygenerator:
    print x,
print 

for x in mygenerator:
    print x,
print 


