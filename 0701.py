s = {3, 5, 6, 3, 2, 5, 4, 4}
s.remove(4)
print(s)
s.pop()
print(s)
s.clear()
print(s)

l = [1, 2, 4, 4, 5, 2, 1, 6]
print(l)
s = set(l)
l.clear()
for i in s:
    l.append(i)
print(l)

l4 = ["a", "b", "c"]
f = frozenset(l)
f = frozenset(l)
f = frozenset(l4)
f = frozenset([3, 5, 7, 34.34, True, not False, "Hey"])
print(f)