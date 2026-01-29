try:
    5 / 9
except ZeroDivisionError:
    print("На ноль делить нельзя!")
else:
    print("Сработало!")
finally:
    print("Программа выполнена!")

print("\n" * 2)

try:
    a = int(input())
except ValueError:
    print("Число введи")
finally:
    print("end.")
    
print("\n" * 2)

try:
    print(8 + 8)
except TypeError:
    print("Не совместимы")
else:
    print("о да")