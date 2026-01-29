coin = int(input("Введи число монет: "))

while coin > 0:
    print("\nКоличество: " + str(coin) + "\n–1 монета")
    coin -= 1
else:
    print("\nМонеты нет, ты нищеброд:)")