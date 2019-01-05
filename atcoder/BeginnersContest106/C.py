S = input()
K = int(input())

one_count = 0
first_not_one = 0

for i in S:
    num = int(i)
    if num != 1:
        first_not_one = num
        break
    else:
        one_count += 1

if K <= one_count:
    print(1)
else:
    print(first_not_one)


