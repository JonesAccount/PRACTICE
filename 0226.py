length = int(input("Enter the length of the list: "))

# придумать условие на неправильный ввод

list = []
i = 0

while i < length:
    i += 1
    string = "Element " + str(i) + ": "
    el = input(string)
    list.append(el)

print("\nYour list is ready:\n", list, sep="")

functions = [
"1. append",
"2. insert",
"3. extend",
"4. reverse",
"5. sort",
"6. len",
"7. count",
"8. pop",
"9. remove",
"10. clear"
]

extend_list = []

print("\nSelect list setting: ")

for i in functions:
    print(i)
    
setting = input("\nChoice: ")
print("————————————————————————————————")

if setting == "1":
    print("append setting selected ✅\n")
    append_qu = input("Element value: ")
    list.append(append_qu)
    print("\nYour list:")
    print(list)
elif setting == "2":
    print("insert setting selected ✅\n")
    insert_qu = input("Element value: ")
    location_insert = int(input("Element location: "))
    list.insert(location_insert, insert_qu)
    print("\nYour list:")
    print(list)
elif setting == "3":
    print("extend setting selected ✅")
    print("When you're done adding elements, write \"stop\" to complete the operation.\n")
    batton = True
    while batton:
        extend_qu = input("Element value: ")
        extend_list.append(extend_qu)
        if extend_qu == "stop":
            batton = False
    list.extend(extend_list)
    list.pop(-1)
    print("\nYour list:")
    print(list)
elif setting == "4":
    print("reverse setting selected ✅")
    print("Reverse completed")
    list.reverse()
    print("\nYour list:")
    print(list)
elif setting == "5":
    print("sort setting selected ✅")
    print("Sorry, sorting is temporarily not working 😕")
elif setting == "6":
    print("len setting selected ✅")
    print("\nThere are ", len(list), " elements in your list", sep="")
elif setting == "7":
    print("count setting selected ✅\n")
    print("Your list:")
    print(list)
    count_qu = int(input("\nSelect an element's index to count its quantity: "))
    print(list.count(count_qu))
elif setting == "8":
    print("pop setting selected ✅\n")
    pop_qu = int(input("Select the index of the element you want to delete: "))
    list.pop(pop_qu)
    print("\nYour list:")
    print(list)
elif setting == "9":
    print("remove setting selected ✅\n")
    remove_qu = input("Specify the value you want to delete: ")
    list.remove(remove_qu)
    print("\nYour list:")
    print(list)
elif setting == "10":
    print("clear setting selected ✅\n")
    list.clear()
    print("Your list has been deleted")
    print("\nYour list:")
    print(list)
else:
    print("Invalid input 🫤")