list = [1, 2, 3, 4, 5]
list.reverse()
print(list)

for i in range(5):
    list.pop()
print(list)

for i in range(1, 6):
    list.append(i)
list.reverse()
print(list)

list.insert(1, 6)
list.insert(-1, 9)
list.insert(3, 2)
print(list)

list.sort()
print(list)

list.reverse()
print(list)