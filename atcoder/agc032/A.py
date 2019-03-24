import sys
N = int(input())
b = [int(i) for i in input().split()]

result = []

for j in range(0, N):
    b_length = len(b)
    for i in range(0, b_length):
        if b[b_length - 1 - i] == b_length - i:
            result.append(str(b[b_length - 1 - i]))
            b.pop(b_length - 1 - i)
            break

if len(result) < N:
    print(-1)
else:
    result.reverse()
    for r in result:
        print(r)





