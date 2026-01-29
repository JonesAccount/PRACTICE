num_str = input("Введи числа через пробел: ")

l = num_str.split(" ")
print("Список:", l)
print("Мин. число:", min(l))
print("Макс. число:", max(l))
print("Разница между ними:", int(max(l)) - int(min(l)))
print("Округление:", round(int(max(l)) - int(min(l))))