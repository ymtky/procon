import sys

target_price = int(input())
cake_price = 4
donut_price = 7
max_donut_count = int(target_price / 7)

for i in range(max_donut_count + 1):
    target_cake_price = target_price - (donut_price * i)
    if target_cake_price % cake_price == 0:
        print("Yes")
        sys.exit()
print("No")
