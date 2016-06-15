#!/bin/bash

## This will wheather the enter digit is mention in the list or not..!!

list_digit=[0,1,2,3,4,5,6,7,8,9,10]
input_digit=int(input("enter a digit:"))

for i in list_digit:
        if input_digit == i:
                print "Digit is in the list"
                break
else:
        print "Digit is not in the list"

