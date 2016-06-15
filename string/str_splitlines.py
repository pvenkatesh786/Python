#!/bin/python

## Syntax :- str.splitlines() :: This will return all the string optionally including the line breaks..!!

## Python knows "\n & \r" so its splitting lines acording to that.I used "\t" as python didn't understand "\t" its print value of the string as it is.

str = 'Welcome\nto\npython\nworld'
print "Splitlines function :",str.splitlines()

str1 = 'hi\tthis\tis\tvenky'
print "Splitlines function :",str1.splitlines()

str2 = 'hi\rthis\ris\rvenky'
print "Splitlines function :",str2.splitlines()

str3 = 'ab c\n\nde fg\rkl\r\n'
print "Splitlines function :",str3.splitlines()

str4 = ''
print "Splitlines function :",str4.splitlines()
