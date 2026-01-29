class Cat:
    name = None # поле 1
    age = None # поле 2
    isHappy = None # поле 3

    def set_data(self, unname, unage, unisHappy):
        self.name = unname
        self.age = unage
        self.isHappy = unisHappy

    def get_data(self):
        print(f"Name: {self.name}\nAge: {self.age}\nHappy: {self.isHappy}")



cat1 = Cat()
cat1.set_data("Жопен", 3, False)
print(cat1.get_data())


class Edit:
    word = None

    def word_edit(self, userw):
        self.word = userw
        print(f"Upper: {self.word.upper()}")
        print(f"Lower: {self.word.lower()}")
        print(f"Capitalize: {self.word.capitalize()}")

edit = Edit()
edit.word_edit("pYthOn")