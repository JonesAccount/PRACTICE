import os

# глобальные переменные
resources = [coal = 0, iron = 0, copper = 0, gold = 0, diamond = 0]
different = [coin = 0, experience = 0]

# очистка консоли
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

 # ЛОКАЦИЯ: ДОМ
def home(): 
    print("────── ТЕЛЕЖКА ──────"); print("1) Деревянная кирка"); print("2) Железо: 0"); print("3) Уголь: 0"); print("4) Медь: 0")
    print("\n────── КОМАНДЫ ──────"); print("1) Шахта"); print("2) Продать руды"); print("\n────────────────────")
    while not False:
        action = input("\nДействие: ")
        if action == "шахта":
            clear_console()
            mine()

# ЛОКАЦИЯ: ШАХТА
def mine():
    print("\n────── КОМАНДЫ ──────"); print("1) Копать"); print("2) Домой"); print("\n────────────────────")
    while not False:
        action = input("\nДействие: ")
        if action == "дом":
            clear_console()
            home()
home()