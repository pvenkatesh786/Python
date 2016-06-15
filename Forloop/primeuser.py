#!/bin/bash

## This program will check wheather the user entered no is "Prime or not"

num=int(input("Enter a no to check wheather its prime or not : "))

for i in range(2,num):
	if num % i == 0:
		print "This no is not a prime no:",num
		break
else:
	print "This no is prime no:",num
