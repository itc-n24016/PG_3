import random

cards = []

for i in range(1, 53):
    cards.append(i)

suit = ["♠", "♥", "♦", "♣"]

print(cards)
random.shuffle(cards)
print(cards)

pick = int(input("何枚目のカードを引きますか(1-52) ->"))

s = cards[pick -1]//13
print(s)

number = cards[pick -1] % 13
if number == 0:
    s -= 1
    number = 13


print(f"あなたが引いたのは{suit[s]}の{number}です")