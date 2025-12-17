def aisatsu(names, times):
    if times == 1:
        print(f'{names}さん、おはよ！')
    elif times == 2:
        print(f'{names}さん、こんちわ')
    elif times == 3:
        print(f'{names}さん、こんばんわ')
    else:
        print(f'{names}さん、おやすみ')


name = input('名前を入力してください ->')
print('朝:1, 昼:2, 夜:3, 寝る前:4')
jikan = int(input('時間帯を入力してください ->'))
aisatsu(name, jikan)
