d = {"name": "Johnny", "age": 25, "gender": "male"}
d = dict(name="Johnny", age=25, gender="male")

for key, value in d.items():
    print(key, value)

print("-" * 20)

for key in d:
    print(key, d[key])