grades = dict(Математика=0, ФизиКа=0, химия=0, БиоЛОГия=0)

class Student:

    def __init__(self, grades):
        for k in grades.keys():
            while True:
                res = int(input(f"Оценка Паше по {k}: "))
                if res > 1 and res < 6:
                    grades[k] = res
                    break
                else:
                    print("\nОт 2 до 5")

student = Student(grades)

print()
for k, v in grades.items():
    print(f"{k}: {v}")
