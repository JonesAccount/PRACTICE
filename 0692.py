d = dict(name="tom", age=20, height=40, weight=50)

print(d.keys())
print(d.values())

print()
for key, value in d.items():
    print(key.capitalize(), ": ", value, sep="")

