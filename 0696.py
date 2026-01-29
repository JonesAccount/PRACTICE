l = ["1", "0"]
while 1 == 1:
    p = input()
    s = set(l)
    for i in s:
        l.append(i)
    if l[0] == "1":
        print(True)
    else:
        print(False)
    s.clear()