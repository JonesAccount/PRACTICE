class Car:
    brand = None
    color = None
    speed = None

    def drive(self, a, b, c):
        self.brand = a; self.color = b; self.speed = c

    def read(self):
        print(f"Car {self.brand} go this speed {self.speed} cm hour, this color: {self.color.lower()}")

car = Car()
car.drive("BMW", "Black", 98)
car.read()

line = "-" * 60
print(line)





class Dog:
    name = "Gabriel"
    age = 1.5

    def dog_edit(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Имя: {self.name.capitalize()}")
        print(f"Возраст: {self.age} годика")

dog1 = Dog()
dog1.show()
print(line)

dog1.dog_edit("Toples", 4)
dog1.show()
print(line)

dog2 = Dog()
dog2.dog_edit("Barbara", 6)
dog2.show()

print(line)



class BankAccount:
    owner = None
    balance = None

    def user(self, name, balan):
        self.owner = name; self.balance = balan

    def deposit(self, amount):
        self.balance += amount
        print(f"На счет добавлено {amount} теперь баланс {self.balance}")

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"Снято {amount} теперь баланс {self.balance}")
        else:
            print("Недостаточно средств")

bank = BankAccount()
bank.user("Jozefina", 50)
bank.deposit(100)
bank.deposit(200)

bank.withdraw(200)
bank.withdraw(151)
bank.deposit(1000)
bank.withdraw(1149)