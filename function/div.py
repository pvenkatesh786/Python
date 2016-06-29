#!/bin/python

x = input("Eneter the no : ")
y = input("Eneter the no : ")

def dev(x,y):
	if x>=y:
		if x % y == 0:
			print "x is divisble by y"
		else:
			print "x is not divisible y"
	else:
		print "Enter first no greater that or equal to y"
dev(x,y)
