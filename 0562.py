import random
print("gob".capitalize())
print("jeis".upper())
print("COP".lower())
print("FAP".isupper())
print("FAP".islower())
list = []
for i in range(10):
    list.insert(random.randint(0, 9), random.randint(0, 9))

print(list)
list.sort()
print(list)
list.remove(5)
print(list)
print(list.count(4))