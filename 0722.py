a, b = 5, "word"
c, d = 4.5, True

lst = []
tupl = ()
st = {1, }
fron = frozenset(st)
dct = {}

print("|5|", type(a))
print("|word|", type(b))
print("|4.5|", type(c))
print("|True|", type(d))

print()

print(type(lst))
print(type(tupl))
print(type(st))
print(type(fron))
print(type(dct))