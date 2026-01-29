name = "Ellie"

def f1():
    def f2():
        surname = "William"
        return surname
    return f2()
surname = f1()

print(name, surname, sep=" ")