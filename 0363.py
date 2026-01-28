names = ["alisa", "chack", "kuplinov", "ellie"]

def capitalized(name):
    return name.capitalize()

capitalized = map(capitalized, names)

result = list(capitalized)

print(result)

# Функция map позволяет эффективно и лаконично обработать коллекцию данных. Она применит функцию к каждому элементу коллекции и вернет новый список с преобразованными значениями.