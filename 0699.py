from random import randint as r
s = set()

while True:
    v = input("::")
    if v != "m":
        s.add(int(v))
    else:
        break

#counter = 10 - len(s)
#for i in range(counter):
    #num = r(1, 9)
    #if num not in s:
        s.add(num)
    #else:
        counter += 1

while True:
    if len(s) < 11:
        s.add(r(1, 10))
    else:
        break


print(s)
print(len(s))