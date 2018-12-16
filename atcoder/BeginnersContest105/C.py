import math
import sys

N = int(input())
if N == 0:
    max = 1
else:
    max = math.ceil(math.log(abs(N), 2)) + 3

result = []
numerator = N
for i in range(0, max):
    if numerator % (math.pow(2, i + 1)) == 0:
        result.append(str(0))
    else:
        result.append(str(1))
        numerator -= math.pow(-2, i)

    if numerator == 0:
        break

result.reverse()
print("".join(result))