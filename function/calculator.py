#!/bin/python
loop = 1
choice = 0

while loop == 1:
	print "Welcome to Pthon Calculator"

	print "Your option are"

	print "Addition"
	print "Subtraction"
	print "Multiplication"
	print "Division"
	print "Quit calculator.py"

	choice = input("Choose your option:")
	if choice == 1:
		a1 = input("Enter no")
		a2 = input("Enter another no.")
		print a1, "+", a2, "=", a1 + a2
	elif choice == 2:
		s1 = input("Enter no")
		s2 = input("Enter another no.")
		print s1, "+", s2, "=", s1 - s2
	elif choice == 3:
        	mul1 = input("Multiply this: ")
	        mul2 = input("with this: ")
        	print mul1, "*", mul2, "=", mul1 * mul2
	elif choice == 4:
        	div1 = input("Divide this: ")
	        div2 = input("by this: ")
        	print div1, "/", div2, "=", div1 / div2
	elif choice == 5:
        	loop = 0
print "Thankyou for using calculator.py!"
