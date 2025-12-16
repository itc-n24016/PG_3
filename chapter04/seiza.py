seiza = ["山羊座","水瓶座","魚座","牡羊座","牡牛座","双子座","蟹座","獅子座","乙女座","天秤座","蠍座","射手座"]

phrases = ["I keep ...","I solve ...","I believe ...","I exist.","I have ...","I choose ...","I sense ...","I will ...","I analyze ...","I balance ...","I want ...","I experience ..."]

birth_month = int(input("生まれた月は？"))
birth_day = int(input("生まれた日は？"))

if birth_month <= 12:
    if birth_day <= 31:
        if (birth_month == 1 and birth_day <= 19) or (birth_month == 12 and birth_day <= 22):
            print(seiza[0], phrases[0])
        elif (birth_month == 1 and birth_day >= 20) or (birth_month == 2 and birth_day <= 18):
            print(seiza[1], phrases[1])
        elif (birth_month == 2 and birth_day >= 19) or (birth_month == 3 and birth_day <= 20):
            print(seiza[2], phrases[2])
        elif (birth_month == 3 and birth_day >= 21) or (birth_month == 4 and birth_day <= 19):
            print(seiza[3], phrases[3])
        elif (birth_month == 4 and birth_day >= 20) or (birth_month == 5 and birth_day <= 20):
            print(seiza[4], phrases[4])
        elif (birth_month == 5 and birth_day >= 21) or (birth_month == 6 and birth_day <= 21):
            print(seiza[5], phrases[5])
        elif (birth_month == 6 and birth_day >= 22) or (birth_month == 7 and birth_day <= 22):
            print(seiza[6], phrases[6])
        elif (birth_month == 7 and birth_day >= 23) or (birth_month == 8 and birth_day <= 22):
            print(seiza[7], phrases[7])
        elif (birth_month == 8 and birth_day >= 23) or (birth_month == 9 and birth_day <= 22):
            print(seiza[8], phrases[8])
        elif (birth_month == 9 and birth_day >= 23) or (birth_month == 10 and birth_day <= 23):
            print(seiza[9], phrases[9])
        elif (birth_month == 10 and birth_day >= 24) or (birth_month == 11 and birth_day <= 22):
            print(seiza[10], phrases[10])
        elif (birth_month == 11 and birth_day >= 23) or (birth_month == 12 and birth_day <= 21):
            print(seiza[11], phrases[11])
    else:
        print('超えています')

else:
    print('超えています')