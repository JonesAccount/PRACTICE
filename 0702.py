print((lambda x="Word", y="This": x + " " + y)())
l = lambda x: pow(x, 3)
l2 = lambda x: round(x)

print(l(5))
print(l2(53.23))

word = "i"
w2 = "python"
w3 = "love"
w4 = "very"
w5 = 111

print(f"{word} {w4} {w3} {w2} {w5}")

li2 = [4, 6, 3, 5, 7, 7]
li3 = [2, 3, 5, 6, 7, 7]

li2 = set(li2)
li3 = set(li3)

print(li2 & li3)

