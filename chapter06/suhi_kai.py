year = input("生まれた年は->")
month = input("生まれた月は->")
day = input("生まれた日は->")

all = int(year + month + day)

total = 0

while all > 0:
    total += all % 10
    all //= 10

while total >= 10:
    new_total = 0
    while total > 0:
        new_total += total % 10
        total //= 10
    total = new_total
print(f"あなたの運命数は{total}です")