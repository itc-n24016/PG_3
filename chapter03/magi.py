import random, time

# 関数casper
def casper():
    kekka = random.randint(0, 1)
    mati = random.randint(1, 3)
    time.sleep(mati)
    if kekka == 0:
        print('casper...可決')
        return 0
    else:
        print('casper...否決')
        return 1
    return kekka


# 関数balthasar
def balthasar():
    kekka = random.randint(0, 1)
    mati = random.randint(1, 3)
    time.sleep(mati)
    if kekka == 0:
        print('balthasar...可決')
        return 0
    else:
        print('balthasar..否決')
        return 1
    return kekka


# 関数melchior
def melchior():
    kekka = random.randint(0, 1)
    mati = random.randint(1, 3)
    time.sleep(mati)
    if kekka == 0:
        print('melchior...可決')
        return 0
    else:
        print('melchior...否決')
        return 1
    return kekka


#ここから
gidai = input('議題を入力してください ->')
print('審議中...')
#各関数を呼び出す# 多数決を取る
result = casper() + balthasar() + melchior()

# 結果を表示する
print('[決議]')
if result > 1:
    print(f'決議 {gidai}は否決されました')
else:
    print(f'決議{gidai}は可決')