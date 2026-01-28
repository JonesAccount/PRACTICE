import turtle, time
joe = turtle.Turtle()
window = turtle.Screen()
joe.hideturtle()
joe.speed(100)
colors = ["red", "blue", "green", "brown"]

def object():
    for i in range(80):
        joe.color(colors[i % 4])
        joe.fd(100)
        joe.left(9999)
    
def move(x, y):
    joe.up()
    joe.setposition(x, y)
    joe.down()
    object()

window.onclick(move)
window.listen()
window.mainloop()

time.sleep(5)

# Метод turtle.listen() устанавливает фокус на текущий холст TurtleScreen для прослушивания событий. Для передачи listen() методу onclick.