#!/bin/python

## Syntax : str.isalpha() :: This will check whether the string consist of alphabetic or not..!!

## The first two check is "false" because it contains space, as we know that isalpha() doesn't take space as alphabetic.
## The last check is "true" becuase it doesn't have any space and digit.

str = "Hi this is venky"
print "First string check :",str.isalpha()

str1 = "Hi this is venky..!!"
print "Second Strig check :",str1.isalpha()

str2 = "venky"
print "Third String Check :",str2.isalpha()
