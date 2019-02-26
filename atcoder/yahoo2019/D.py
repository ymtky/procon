L = int(input())
stones_count = []
for i in range(0, L):
    A = int(input())
    if A % 2 == 1:
        stones_count.append(1)
    elif A == 0:
        stones_count.append(0)
    else:
        stones_count.append(2)

sub_count_0 = []
sub_count_1 = []
sub_count_2 = []
count_0 = 0
count_1 = 0
count_2 = 0
for i in range(0, L):
    if stones_count[i] == 0:
        if count_1 != 0:
            sub_count_1.append(count_1)
        if count_2 != 0:
            sub_count_2.append(count_2)
        count_1 = 0
        count_2 = 0
        
        count_0 += 1
    elif stones_count[i] == 1:
        if count_0 != 0:
            sub_count_0.append(count_0)
        if count_2 != 0:
            sub_count_2.append(count_2)
        count_2 = 0
        count_1 += 1
    else:
        if count_0 != 0:
            sub_count_0.append(count_0)
        count_1 += 1
        count_2 += 1

if count_0 != 0:
    sub_count_0.append(count_0)
if count_1 != 0:
    sub_count_1.append(count_1)
if count_2 != 0:
    sub_count_2.append(count_2)

result = min(len(sub_count_1) - 1, sum(sub_count_0))
print(result + len(sub_count_2) - 1)