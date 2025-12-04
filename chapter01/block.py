name = "Marry"

print("パスワードを入力してください", end = "")
password = input()
if name == "Marry":
    print("Hello Marry")
    if password == "swordfish":
        print("認証しました")
    else:
        print("間違っています")
else:
    print("名前が間違っています")