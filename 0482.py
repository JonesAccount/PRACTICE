counter = 0

def increase_counter():
    global counter
    counter += 1
    
increase_counter()
print(counter)