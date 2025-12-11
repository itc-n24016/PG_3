import random



def daikiti():
    print('大吉')
def tyukiti():
    print('中吉')
def shokiti():
    print('小吉')
def kiti():
    print('吉')
def kyo():
    print('凶')

kekka = random.randint(1, 10)
if kekka == 1:
    daikiti()
elif kekka == 2 or kekka == 3:
    tyukiti()
elif kekka >= 4 and kekka <=7:
    shokiti()
elif kekka == 8 or kekka == 9:
    kiti()
else:
    kyo()