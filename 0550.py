from random import randint as r

list = []
for i in range(10):
    list.append(r(1, 10))

num = r(1, 10)
list.remove(num)
print(num)
print(list)