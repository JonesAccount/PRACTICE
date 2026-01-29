class Io:
    def init(self, x="япердоле"):
        print(x)
    
    def cor(self, x):
        self.x = tuple(x)
        return self.x
    
    def mno(self, z):
        self.x = set(z)
        return self.x
    
    def fro(self, x):
        self.x = frozenset(x)
        return self.x

io = Io("Запуск программы")

lst = []

try:
    size = int(input("Длина: "))
except ValueError:
    print("Нужно ввести число.")

try:
    for i in range(size):
        while 1 == 1:
            try:
                lst.append(int(input(f"#{i + 1} Число: ")))
                break
            except ValueError:
                print("Нужно ввести число.")
except NameError:
    print("Не то...")
print(lst)
    
print("1 | Кортеж\n2 | множества\n3 | фрозенсет")
while True:
    try:
        coice = int(input("Выбери: "))
        break
    except ValueError:
        print("Нужно ввести число.")

if coice == 1:
    t = io.cor(lst)
elif coice == 2:
    t = io.mno(lst)
elif coice == 3:
    t = io.fro(lst)

print(t)