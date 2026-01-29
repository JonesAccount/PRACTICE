lot = 3
pincode = None

def f():
    global pincode, lot
    while True:
        print("Попытка:", lot)
        if lot > 0:
            pincode = int(input("Введи пин-код: "))
            if pincode > 99 and pincode < 1000:
                f1()
            else:
                print("\nНедопустимо")
        else:
            break
            
def f1():
    global lot
    v = lot
    def f2():
        global lot
        nonlocal v
        lot -= 1
        if v == 123:
            print("\nПин-код правильный")
        else:
            print("\nНе тот пин-код")
            f()
    f2() if lot > 0 else print("Попытки нет")

def f0():
    f()

if lot > 0:
    f0()