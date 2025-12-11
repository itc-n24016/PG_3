# 乱数は1~100
import random
set_number = random.randint(1, 10)
point = 5
print('1から10までの数をあてて！')

for roop in range(1, 11):
    print('数を入力して')
    guess = int(input())

    if guess < set_number:
        point -= 1
        print('あなたの推定値は小さい')
    elif guess > set_number:
        point -= 1
        print('あなたの推定値は大きいです。')
    elif guess == set_number:
        point += 10
        break # あたり！

    if guess == set_number:
        print(f'{str(roop)}回であたり')
    else:
        print(f'残念 {str(roop)}でした')