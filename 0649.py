class Group:
    students = {0, }
    counter = True
    
    def init(self):
        print("Программа работает...\n")
    
    def add_student(self, name):
        if self.counter == True:
            self.students.pop()
            self.counter = False
        self.students.add(name)
    
    def remove_student(self):
        self.students.pop()
        
    def show(self):
        for i in self.students:
            print(i)

group = Group()
group.add_student("Ellie")
group.add_student("Jozefina")
group.add_student("Baltimur")
group.show()
print("\n")
group.remove_student()
group.show()