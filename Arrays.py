from array import *

def Print(a):
	for x in a:
		print x,
	print

a = array('I',[i for i in range(0,5)]) #Integer 4 bytes

'''
'b' -> Represents signed integer of size 1 byte
'B' -> Represents unsigned integer of size 1 byte
'c' -> Represents character of size 1 byte
'u' -> Represents unicode character of size 2 bytes
'h' -> Represents signed integer of size 2 bytes
'H' -> Represents unsigned integer of size 2 bytes
'i' -> Represents signed integer of size 2 bytes
'I' -> Represents unsigned integer of size 2 bytes
'w' -> Represents unicode character of size 4 bytes
'l' -> Represents signed integer of size 4 bytes
'L' -> Represents unsigned integer of size 4 bytes
'f' -> Represents floating point of size 4 bytes
'f' -> Represents floating point of size 4 bytes
'd' -> Represents floating point of size 8 bytes
'''

Print(a)
Print(a)

