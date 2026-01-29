from random import randint

list = []
size = int(input("Длина списка: "))

for i in range(size):
    list.append(int(input(str(i + 1) + " Элемент: ")))

print("\n", list, sep="", end="\n\n"); print("1. Добавить элемент в конец списка \n2. Очистить список \n3. Добавить элемент по индексу \n4. Удалить случайный элемент")

def func_action():
    while True:
        action = input("Твое дейтсвие: ")
        if action == "1":
            func_append()
        elif action == "2":
            func_clear()
        elif action == "3":
            func_insert()
        elif action == "4":
            func_pop()
        elif action == "5":
            pass
        elif action == "6":
            pass
        elif action == "7":
            pass
        elif action == "8":
            pass
        else:
            continue

def func_append():
    global list
    list.append(randint(1, 10))
    print("\n", list, sep="")

def func_clear():
    global list
    list.clear()
    print("\n", list, sep="")

def func_insert():
    global list
    list.insert(0, randint(1, 10))
    print("\n", list, sep="")

def func_pop():
    global list
    list.pop(randint(0, len(list) - 1))
    print("\n", list, sep="")

func_action()


