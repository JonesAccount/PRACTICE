glo = 100

def f():
    global glo
    glo /= 2
    return glo
    
glo = f()
print(int(glo))