l = [1,2,3,4,5,6,7,8,9]
m = set()
m.update(l)
print(m)

l2 = []
for i in range(5):
    num = int(input())
    l2.append(num)
m.update(l2)
print(m)

l3 = []
for i in range(5):
    w = input()
    l3.insert(i - 1, w)
m.update(l3)
print(m)