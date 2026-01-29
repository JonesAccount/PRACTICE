def plus(a, b):
    print(x, "+", y, "=", x + y)
    
x = int(input("Первое число: "))
y = int(input("Второе число: "))
plus(x, y)

do = input("\nНажми 1: ")
if do == "1":
    plus()