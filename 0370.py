class Dog:
    def __init__(self, color, breed):
        self.color = color
        self.breed = breed

my_dog = Dog("White", "Husky")

print("My dog color: " + my_dog.color + "\nBreed: " + my_dog.breed)

# Класс — шаблон, с помощью которого удобно описывать однотипные объекты.