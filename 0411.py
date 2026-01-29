password = input()

if password == "bubu":
    print(not False, "Открыто")
elif password != "bubu":
    print(not True, "Закрыто")
else:
    print("Ошибка ввода")