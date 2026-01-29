while not False:
    try:
        n1, n2 = input(), input()
        res = int(n1) / int(n2)
        print(f"Результат: {res}")
        break
    except ZeroDivisionError:
        print("На 0 делить нельзя!!!")
    except ValueError:
        print("Ошибка тип данных.")
    except TypeError:
        print("Преобразуй!")
        
print("\nПрограмма завершилась...")