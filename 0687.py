d = dict(name="Piter", age=34, hobby="coding")

for key in d:
    print(key)

for key in d:
    print(key.capitalize(), ": ", d[key], sep="")

print(d.items())