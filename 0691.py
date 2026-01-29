d = {"name":"John", "age":20, "city":"New York"}

print(d.keys())

list = []
for i in d.keys():
    list.append(i)
print(list)

for i in d.keys():
    print("Key:", i)