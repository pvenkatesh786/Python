#!/bin/python

dct = {}
str = raw_input("Enter the string :")
for elem in str:
	if elem not in dct:
		dct[elem] = 1
	else:
		dct[elem] += 1
print dct
