from random import randint as v

d1 = dict(num1=v(10, 100), num2=v(10, 100), num3=v(10, 100))

d2 = {"el1": "первое", "el2": "вТорое", "el3": "третЬЕ"}

for i in range(len(d1)):
    print(d2["el" + str(i + 1)].capitalize() + " число: " + str(d1["num" + str(i + 1)]))