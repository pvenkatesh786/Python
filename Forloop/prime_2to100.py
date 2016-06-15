#!/bin/python

## This will print prime nos between 2 to 100.

for i in range(2,100):
	for num in range(2,i):
		if i%num == 0:
			print "This is not a prime no :",i
			break
	else:
		print "This is prime no :",i
