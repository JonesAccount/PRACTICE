bo = True
while bo:
    nums = input("Числа через пробел: ")
    list = nums.split(" ")
    try:
        for i in range(len(list)):
            list[i] = int(list[i])
        print(list)
        bo = False
    except ValueError:
        print("Буквы не приветствуется!")

bo = True
while bo:
    try:
        num_del = int(input("Какое число удалить: "))
        list.remove(num_del)
        print(list)
        bo = False
    except ValueError:
        print("Буквы не любим!")

mina = min(list)
maxa = max(list)
summa = 0
for i in range(len(list)):
    summa += list[i]
print(f"Мин. число: {mina}")
print(f"Мax. число: {maxa}")
print(f"Сумма всех чисел: {summa}")

bo = True
while bo:
    try:
        list.append(int(input("Какое число добавить: ")))
        print(list)
        bo = False
    except ValueError:
        print("Буквам нет!!!")
    finally:
        print("Работа со списком завершена...")
    
print(list.sort())
print(list.count(5))