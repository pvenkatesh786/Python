#!/bin/python

lst = []
for num in range(1,5):
	fact = 1
	for elem in range(1,num):
		fact *= elem+1
	lst.append(str(fact))
print ','.join(lst)
	
