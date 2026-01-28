list = []

while True:
    el = input()
    list.append(el)
    if el == "stop":
        list.pop(-1)
        break
        
collector = ", ".join(list)

print(collector)