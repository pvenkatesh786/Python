#!/bin/python

str = raw_input("Enter anything :")
lst = str.split(',')
print lst
lst.sort()
print ','.join(lst)
