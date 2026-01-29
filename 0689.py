d = dict(name="Tom", age=24, city="New York")

x = d.get("age")
y = d["city"]

print(x, y)

d.clear()
print(d)