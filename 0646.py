class Book:
    title = None
    author = None
    year = None
    
    def init(self):
        self.title, self.author, self.year = input("Название: "), input("Автор: "), int(input("Год: "))
        self.edit()
    
    def edit(self):
        self.books = {"Название": self.title, "Автор": self.author, "Год": self.year}
        for k, v in self.books.items():
            print(f"{k}: {v}")
    
book = Book()