while not False:
    x = int(input("Продолжить цикл?\nДа-1\nНет-0\n>>>"))
    if not x != 1:
        print("\nЦикл продолжается.", end="\n\n")
    elif x == 0:
        print("\nЦикл закрывается.", end="\n\n")
        break
    else:
        print("\nНе понимаю запрос", end="\n\n")