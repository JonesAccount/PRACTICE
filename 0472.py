operation = None

def plus(i1, i2):
    print()
    print(i1, "+", i2, "=", i1 + i2)
    menu()

def minus(i1, i2):
    print()
    print(i1, "-", i2, "=", i1 - i2)
    menu()

def umno(i1, i2):
    print()
    print(i1, "*", i2, "=", i1 * i2)
    menu
    
def dele(i1, i2):
    print()
    print(i1, "/", i2, "=", i1 / i2)
    menu()

def menu():
    print("-" * 20)
    print("1|Сложение\n2|Вычитание\n3|Умножение\n4|Деление")
    operation = int(input("Действие: "))
    num1 = int(input("\nПервое число: "))
    num2 = int(input("\nВторое число: "))

    if operation == 1:
        plus(num1, num2)
    elif operation == 2:
        minus(num1, num2)
    elif operation == 3:
        umno(num1, num2)
    elif operation == 4:
        dele(num1, num2)
    else:
        print("Ошибка ввода...")
        menu()

menu()