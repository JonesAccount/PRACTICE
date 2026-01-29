list = ["Маша", "Коля", "Ералаш", "Катя"]
print(list)

name = input("\nИмя: ")
index = int(input("Куда поставить: "))

list.insert(index, name)
print("\n", list, sep="")