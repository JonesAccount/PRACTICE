class Tree:
    def __init__(self, view, age, height):
        self.view = view
        self.age = age
        self.height = height
    
big_tree = Tree("Sequoia", 234, 19)

print(big_tree.view + " tree:\nAge: " + str(big_tree.age) + "\nHeight: " + str(big_tree.height))

# Метод __init__ является конструктором класса. Этот метод вызывается автоматически при создании нового объекта класса и используется для инициализации его атрибутов. 