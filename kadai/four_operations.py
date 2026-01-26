a = int(input(f"1つ目の整数を入力"))
b = int(input(f"2つ目の整数を入力"))
print(f"和：{a + b}")
print(f"差：{a - b}")
print(f"積：{a * b}")
if b != 0:
    print(f"商：{a // b}")
    print(f"剰余：{a % b}")
    print(f"exit")
else:
   print(f"exit")