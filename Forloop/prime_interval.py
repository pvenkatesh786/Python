#!/bin/python

int1 = int(input("Enter first interval :"))
int2 = int(input("Enter Second Interval :"))

for num in range(int1,int2+1):
	for i in range(2,num):
		if num % i == 0:
			break
	else:
		print num
		
