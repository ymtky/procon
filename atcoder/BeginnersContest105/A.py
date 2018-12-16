num_senbei, num_people = [int(i) for i in input().split()]

if num_senbei % num_people == 0:
    print(0)
else:
    print(1)
