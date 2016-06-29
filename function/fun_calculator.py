#/bin/python

def add(a,b):
	return a+b
def sub(a,b):
	return a-b
print "Select ur operation"
print "1)Add"
print "2)Sub"

choice = input("Entr ur choice :  ")
if choice >2:
	print "invalid"
else:
	a = input("Enter no : ")
	b = input("Enter another no : ")
	if choice == 1:
		print add(a,b)
	elif choice == 2:
		print sub(a,b)
