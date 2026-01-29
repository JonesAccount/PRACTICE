l = [7, 3, 8, 3, 5]
l2 = [5, 3, 67, 7.8, -5, 5]

def f(list):
    list.sort()
    return list[0]

print(f(l))
print(f(l2))