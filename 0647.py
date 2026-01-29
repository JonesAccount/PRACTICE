# сортировка
# модуль
# удалить буквы
# удалить дубдикаты
# перевернуть список
# в конце преобразовать в кортеж
from random import randint as r

class Type:
    lst = None
    
    def init(self, lst):
        print("Запуск...\n")
        print(f"Оригинал: {lst}")
        self.lst = lst
        self.sort_f()
    
    def sort_f(self):
        self.lst.sort()
        print(f"\nСортировка: {self.lst}")
        self.modul_f()
    
    def modul_f(self):
        for i in range(len(lst)):
            self.lst[i] = abs(self.lst[i])
        print(f"\nМодуль: {self.lst}")
        self.dubl_f()
    
    def dubl_f(self):
        mno = set(self.lst)
        counter = len(mno)
        for i in mno:
            counter -= 1
            self.lst[counter] = i
        print(f"\nУдаление дубликатов: {self.lst}")

lst = []
for i in range(8):
    lst.append(r(-5, 9))
    
type = Type(lst)