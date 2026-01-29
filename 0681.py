from random import randint as r
print("1 - Работа с текстом"); print("2 - Работа с числами"); print("3 - Работа со списком"); print("4 - Случайная игра"); print("0 - Выход")

option = input(">>> ")

def func_str():
    word = input("Строка >>> ")
    print(len(word))
    print(word.upper())
    print(word.lower())
    print(word.capitalize())
    print(word.isupper())
    print(word.islower())
    print(word.find(word[r(0, len(word) - 1)]))
    list = word.split()
    print(list)
    print("|".join(list))

if option == "1":
    func_str()