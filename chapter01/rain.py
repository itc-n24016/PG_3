print("雨は降っていますか yes or no:", end="")
rain = input()
if rain == "yes":
    print("傘は持っていますか:", end = "")
    umbrella = input()
    if umbrella == "yes":
        print("出かける")
    else:
        print("少し待つ")
        print("まだ降っているか yes or no:", end = "")
        still_rain = input()
        if still_rain == "yes":
            print("あきらめる")
        else:
            print("出かける")
else:
    print("出かける")