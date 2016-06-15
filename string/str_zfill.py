#!/bin/python

## Syntax:- str.zfill() :: This will fillup the left with "0".We can use different argument as well instead of "0"

str = "venky"
print "str.zfill() :",str.zfill(10)

str1 = "venky"
print "str.zfill() :",str1.rjust(10,'H')

str2 = "venky"
print "str.zfill() :",str2.ljust(10,'H')

str3 = "venky"
print "str.zfill() :",str3.zfill(10,'#') ## This will show error because zfill() will take only one argument.

