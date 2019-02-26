paths = []
for i in range(0, 3):
    a, b = [int(i) for i in input().split()]
    paths.append(a)
    paths.append(b)

if set(paths) != set([1, 2, 3, 4]):
    print("NO")
elif paths.count(1) >= 3 or paths.count(2) >= 3 or paths.count(3) >= 3 or paths.count(4) >= 3:
    print("NO")
else:
    print("YES")
