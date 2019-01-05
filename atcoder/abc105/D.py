numBox, numClild = [int(i) for i in input().split()]
numCandies = [int(i) for i in input().split()]

subsequences = {}
acc = 0
for i in range(0, numBox):
    acc += numCandies[i]
    if (acc % numClild) in subsequences:
        subsequences[acc % numClild].append(i)
    else:
        subsequences[acc % numClild] = [i]

count = 0
for k, v in subsequences.items():
    count += int(len(v) * (len(v) - 1) / 2)
    if k == 0:
        count += len(v)
print(count)