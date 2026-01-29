while True:
    name = input("Введи имя до 10 букв: ")
    if len(name) <= 10:
        print("\nСепас, " + name + "!")
        break
    else:
        print("\nДо 10 букв!\n")