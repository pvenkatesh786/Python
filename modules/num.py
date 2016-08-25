import sys

def sum_mul_num(num1,num2):
    sum = 0
    mul = 1
    sum = num1 + num2
    mul = num1 * num2
    return sum,mul
   
values = sum_mul_num(int(sys.argv[1]),int(sys.argv[2]))
print (values)
