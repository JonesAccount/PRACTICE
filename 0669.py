word = "globus"
print(word.islower())

w = word.upper()
print(w.islower())

print(w.lower())

w = w.lower()
print(w.islower())

# name = input("Enter your name: ")
# print(name.capitalize())
print(word.capitalize())
index = word.find("b")
list = []
for i in word:
    list.append(i)
list.pop(index)
word99 = ""
for i in list:
    word99 += i

print(word99)

a = word99.find("s")
print(a)
print(word.find("Tuta"))
print(word.find("lob"))
new_word = "Globusisbetterbig"
print(new_word.find("isbe"))
print(new_word.find("bus"))