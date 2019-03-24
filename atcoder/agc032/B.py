N = int(input())

if N % 2 == 1:
    M = N * (N - 1) / 2 - (N - 1) / 2
    print(int(M))
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            if i != j and i + j != N:
                print(str(i) + " " + str(j))

else:
    M = N * (N - 1) / 2 - N / 2
    print(int(M))
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            if i != j and i + j != N + 1:
                print(str(i) + " " + str(j))
