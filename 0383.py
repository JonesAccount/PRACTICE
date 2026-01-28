import turtle
pen = turtle.Turtle()

def figura(ugol, dlina):
    n = 360 / ugol
       for i in range(ugol):
              pen.forward(dlina)
        pen.left(n)
        
    
figura(5, 100)