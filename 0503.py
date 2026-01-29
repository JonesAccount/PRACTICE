booling = True

def func():
    global booling
    num = int(input("Число: "))
    if num < 10:
        booling = False
    else:
        booling = True
    print("\n", booling)
    
    
func()