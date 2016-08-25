import sys

def generate_pair(pair_length, my_list):
    mainlist = []
   # if pair_length == 2:
    for i in range(0,len(my_list)-1):
	pairs = [my_list[i],my_list[i+1]]
        mainlist.append(pairs)
    return mainlist

list_num = []
pair_length = 2
for i in range(1,len(sys.argv)):
	list_num.append(int(sys.argv[i]))
result = generate_pair(pair_length,list_num)
print(result)
