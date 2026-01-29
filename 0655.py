word = input()

l = word.split(",")

for i in range(len(l)):
        l[i] = int(l[i])

c = tuple(l)
print(l)
print(c)