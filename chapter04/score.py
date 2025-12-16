names = ['相沢いわし', '伊藤うずら', '上野えのき']

total = [0, 0, 0]

index = 0

for i in range(3):
    point = int(input(f'{names[i]}さんの点数は？'))
    total[index] += point
    index += 1


list_all = []
for j in range(3):
    list_all.append(f'{names[j]}さん：{total[j]}点')

print(list_all)
