import turtle
joe = turtle.Turtle()
joe.speed(100)
colors = ("brown", "orange")

def circle(colors, counter):
    for i in range(counter):
        joe.color(colors[i % 2])
        joe.forward(100)
        joe.left(100)
        joe.circle(50)
        counter -= 1

counter = 200
for i in range(counter):
    if counter < 170:
              joe.right(10)
              joe.forward(200)
              circle(colors, counter)
    joe.color(colors[i % 2])
    joe.forward(100)
    joe.left(100)
    joe.circle(50)
    counter -= 1
    
# cicrcle() - для рисования окружностей. Черепашка рисует окружность, двигаясь против часовой стрелки.