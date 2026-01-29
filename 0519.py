while True:
    letters = input("Напиши что-то до 10 букв: ")
    if len(letters) <= 10:
        break
    else:
        continue
    
let1 = ""
let2 = ""
let3 = ""
let4 = ""
let5 = ""
let6 = ""
let7 = ""
let8 = ""
let9 = ""
let10 = ""


for i in letters:
    if i == "a" or i == "b" or i == "d":
        if let1 == "":
            let1 = i
        elif let2 == "":
            let2 = i
        elif let3 == "":
            let3 = i
        elif let4 == "":
            let4 = i
        elif let5 == "":
            let5 = i

print(let1 + let2 + let3 + let4 + let5)