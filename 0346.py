list1 = [i * "|" for i in range(20)]
for i in list1:
    print(i)

list2 = [list1.pop() for i in range(20)]
for i in list2:
    print(i)