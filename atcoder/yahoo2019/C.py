import math

K, A, B = [int(i) for i in input().split()]

if B - A <= 2:
    print(K + 1)
else:
    numn_action = K - A + 1
    print((B - A) * math.floor(numn_action / 2) + numn_action % 2 + A)