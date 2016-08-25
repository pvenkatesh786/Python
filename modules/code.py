import sys

def fun_pair(pair_length,*num):
    for i in range(0,len(num)-pair_length + 1):
        pairs =  (num[i:i+pair_length])
    return pairs

pair_length = []
#pair_length.append(int(sys.argv[1]))


list_num = []
for i in range(1,len(sys.argv)):
        list_num.append(int(sys.argv[i]))


result = fun_pair(pair_length,list_num)
print(result)
