from orca.settings import orcaModifierKeys

okinawa = {
    "県花": "デイゴ",
    "県鳥": "ノグチゲラ",
    "県魚": "タカサゴ",
    "県のお菓子": "サーターアンダギー"
}
print(okinawa.keys())
keys = input(f"選択したのは？ -> ")

if keys in okinawa:
    print(okinawa[keys])
else:
    print("それはないよ")