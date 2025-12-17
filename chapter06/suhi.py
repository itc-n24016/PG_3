
year = input("生まれた年は->")
month = input("生まれた月は->")
day = input("生まれた日は->")
all = year + month + day


index = 0
for i in range(len(all)):
    type = int(all[i])
    index += type
    if index >= 10:
        index_str = str(index)
        score = 0
        for r in range(len(index_str)):
            score += int(index_str[r])
    else:
        score = index

print(f"あなたの運命数は{score}です")

'''
# ① まず全部足す
index = 0
for i in range(len(all)):
    index += int(all[i])

# ② 1桁になるまで繰り返す
while index >= 10:
    index_str = str(index)
    score = 0
    for r in range(len(index_str)):
        score += int(index_str[r])
    index = score
'''