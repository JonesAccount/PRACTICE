find_min = lambda a: min(a)
find_max = lambda a, b, c, d: max(a, b, c, d)

numbers1 = "41 78 2 77 48 45 91 29 85 4"
numbers2 = "86 46 3 9 75 81 36 71 34 35"
numbers3 = "2 65 96 68 80 1 33 16 98 48"
numbers4 = "99 68 6 9 11 16 96 15 82 61"

list1 = numbers1.split(" ")
list2 = numbers2.split(" ")
list3 = numbers3.split(" ")
list4 = numbers4.split(" ")

l1 = find_min(list1)
l2 = find_min(list2)
l3 = find_min(list3)
l4 = find_min(list4)
l5 = find_max(l1, l2, l3, l4)

print("1 список| мин. число: " + str(l1))
print("2 список| мин. число: " + str(l2))
print("3 список| мин. число: " + str(l3))
print("4 список| мин. число: " + str(l4) + "\n")

print("все списки: мах. число: " + str(l5))
