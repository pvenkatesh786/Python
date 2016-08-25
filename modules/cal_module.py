#/bin/python

import sys

def sum_args(*args):
	sum = args[0]
	for i in range(1,len(args)):
		sum = sum + args[i]
	return sum

mainlist = []
for i in range(1,len(sys.argv)):
	mainlist.append(int(*sys.argv[i]))
value = sum_args(mainlist)
print (mainlist)
