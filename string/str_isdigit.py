#!/bin/python

## Sytnax :- str.isdigit() :: This mwill check whether the string consist of digits only..!!

## The first string check is "True" because it doesn't have alpha and spaces.
## The last 2 check is "False" because it has combination of alpha and digit.

str = "123456"
print "First string check :", str.isdigit()

str1 = "Hi this is venky 786"
print "Second string check :", str1.isdigit()

str2 = "venky786"
print "Third String Check :",str2.isdigit()

