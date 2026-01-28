word = "SoloLearn"

def up_word(a):
    b = a.upper()
    return b
    
def low_word(a):
    b = a.lower()
    return b
    
cap_word = lambda a: a.capitalize()

print(up_word(word))
print(low_word(word))
print(cap_word(word))
