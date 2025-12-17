seiza = ["山羊座","水瓶座","魚座","牡羊座","牡牛座","双子座","蟹座","獅子座","乙女座","天秤座","蠍座","射手座"]

phrases = ["I keep ...","I solve ...","I believe ...","I exist.","I have ...","I choose ...","I sense ...","I will ...","I analyze ...","I balance ...","I want ...","I experience ..."]

birth_month = int(input("生まれた月は？"))
birth_day = int(input("生まれた日は？"))

start_days = [1222, 120, 219, 321, 420, 521, 622, 723, 823, 923, 1024, 1123]

birth_all = birth_month * 100 + birth_day

index = 0
for i in range(len(start_days)):
    if birth_all >= start_days[i]:
        index = i

print(f"あなたの星座は{seiza[index]}です")
print(f'キーワードは"{phrases[index]}"です')

