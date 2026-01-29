from random import randint as r

words = "Python, Java, C++, Java"
list = words.split(", ")

num = 1
for i in list:
    print(str(num) + ". " + i)
    num += 1

list2 = []
for i in range(50):
    list2.append(r(1, 100))

print(list2)
nums = ""
for i in list2:
    nums += str(i)
print(nums)
print(len(nums))
print(nums.split("0"))
wordsus = "Fruit car map top python"
w = wordsus.upper()
print(w.split())
print(w.isupper())
print(w.islower())
