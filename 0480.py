def fun1():
    x = 5
    def fun2():
        nonlocal x
        x *= x
        print(x)
    fun2()
    
fun1()