def f():
    try:
        num = int(input("Число: "))
        print(num * num)
    except ValueError:
        print("Ой, ошибка")

f()