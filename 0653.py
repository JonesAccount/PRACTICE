d1 = {"n1": 4, "n2": 6, "n3": 0}
d2 = {"w1": "London", "w2": "Capitan", "w3": "Plane"}
d3 = {"x1": True, "x2": False, "x3": None, "x4": not False}
    
l = []
l.extend(d1.values())
l.extend(d2.values())
l.extend(d3.values())
print(l)

d = {}
for i in range(len(l)):
    d["key" + str(i + 1)] = l[i]

for k, v in d.items():
    print(k, v)