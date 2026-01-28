name = input()
second_name = input()
age = input()

def registration(name, name2, age):
    if name == "":
        print("Добро пожаловать, гость!")
    elif name != " ":
        print("Добро пожаловать, " + name + "!")
    if name2 == "":
        print("Ваше фамилие: не определено")
    elif name2 != " ":
        print("Ваше фамилие: " + name2)
    if age == "":
        print("Ваш возраст: не определен")
    elif age != " ":
        print("Ваш возраст: " + age)

registration(name, second_name, age)