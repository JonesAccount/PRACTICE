length = int(input("Введите длину списка: "))

list = []
i = 0

while i < length:
    print("Элемент", i, end="")
    el = input(". Введите значение: ")
    list.append(el)
    i += 1

print(list)