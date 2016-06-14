#!/bin/python

## Syntax:- str.strip() :: This will return copy of the string in which all the char have been stripped from the begining and the end of the string.

str = " Hello World..!! "
print "After Stripping :",str.strip()

str1 = "Hi this is venky Hi"
print "After Stripping :",str1.strip('Hi')

str2 = "7777Venky777777"
print "After Stripping :",str2.strip('7')

str3= "123Venky123"
print "After Stripping :",str3.strip('1')

str4 = "123Venky123"
print "After Stripping :",str4.strip('123')
