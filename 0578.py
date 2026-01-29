import random

a = {1, 2, 3, 4}
b = {3, 4, 5, 5}
print(a & b)

c = {" ", "-"}
for i in range(10):
    c.add(random.randint(0, 9))

c.remove(" ")
c.remove("-")
print(c)

d = {" ", "-"}
for i in range(10):
    d.add(random.randint(0, 9))

d.remove(" ")
d.remove("-")
print(d)

print("Пересичение:", c & d)