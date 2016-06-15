#!/bin/python 

## Syntax:- str.translate(table[, deletechars]) :: It returns a copy of the string in which all chracters have been translated using table and deleting all characters found in the string deletechars.

from string import maketrans

var1 = "aeiou"
var2 = "54321"
trantab = maketrans(var1,var2)

str = "Hi this is venky"
print str.translate(trantab,'is')
