def loop():
    for i in range(1, 10):
        print(i)
    print()
    menu()
        
def menu():
    do = input("Твое действие:\n1|Цикл\n2|Завершить программу\n\n")
    if do == "1":
        print("\nВызов цикла...", end="\n\n")
        loop()
    elif do == "2":
        print("\nЗавершение программы...")
    else:
        print("\nНеверный ввод.")
        menu()
    
menu()