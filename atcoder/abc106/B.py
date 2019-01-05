import sys
import math

N = int(input())

if N < 105:
    print(0)
    sys.exit()

odd_num = 105
result = 0

while odd_num <= N:
    divisor_count = 0
    for i in range(1, odd_num + 1):
        if odd_num % i == 0:
            divisor_count += 1

    if divisor_count == 8:
        result += 1
        
    odd_num += 2

print(result)
        

