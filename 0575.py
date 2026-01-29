s = set("sambol")
print(s)

s1 = {6, 4, 8, 8.9, True, "Golp"}
print(s1)

s.add(9)
print(s)

c = (60, 47, 68, 23)
s1.update(c)
s1.update([467, 2246, 9754, 45])
print(s1)

s1 = frozenset(s1)
print(s1)

print()
s3 = frozenset([4, 3, 9, 6, 4])
print(s3)
print(s.clear())