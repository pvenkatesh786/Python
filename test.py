lst = [1,2,3,4,5,6]
lst1 = []
pos = len(lst)
for i in range(pos - 1):
	sum = lst[i]+lst[i+1]
	mul = lst[i]*lst[i+1]
	i = i+1
	print "Num are",sum,mul
