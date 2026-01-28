def function(a):
    x = a.isupper()
    y = a.islower()
    return x, y
    
word = input()

result = function(word)
print(result)
