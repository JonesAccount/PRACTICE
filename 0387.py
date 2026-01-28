import turtle
joe = turtle.Turtle()
window = turtle.Screen()
window.setup(500, 500)

def block():
    for i in range(100):
        joe.fd(20)
        joe.left(200)

def move(x, y):
    joe.up()
    joe.setposition(x, y)
    joe.down()
    block()

window.onclick(move)
window.listen()
window.mainloop()

# turtle.setup() - устанавливает размеры окна в пикселях.