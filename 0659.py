m = {6, 4, 8, 6, 8}
m.update([5, 3, 8, 9])
print(m)
m = frozenset(m)
print(m)

l = [True, False, not True, not False]
m2 = set(l)
print(m2)
m2.add(5.7)
print(m2)

f = lambda x, y: pow(x, y)
    
l2 = []
#for i in range(2):
    #l2.append(int(input()))

#print(f(l2[0], l2[1]))
t = "\n"
print(t * 5)
from random import randint as r
print((lambda c=r(-10, 100), i=r(-10, 100), d=r(-10, 100): min(abs(c), abs(i), d))())
    
lg = []
for i in range(8):
    lg.insert(r(0, 11), r(1, 9))
print(lg)

lg = set(lg)
li = []
for i in lg:
    li.append(i)
    
print(li)
z = li[r(0, len(li))]
print(z)
b = li.remove(z)
print(li)
print(z)