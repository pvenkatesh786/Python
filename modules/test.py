import sys

def sum_list(mylist):
	sum = mylist[0]
	mul = mylist[0]
	for i in range(1,len(mylist)):
		sum = sum + mylist[i]
		mul = mul * mylist[i]
	return sum,mul
list_num = []
for i in range(1,len(sys.argv)):
	list_num.append(int(sys.argv[i]))
value = sum_list(list_num)
print (list_num)
print (value)
