import turtle
def rectangle(color):
    tr.begin_fill()
    tr.fillcolor(color)
    for i in range(2):
        tr.forward(200)
        tr.right(90)
        tr.forward(50)
        tr.right(90) 
    tr.end_fill()
    
tr = turtle.Turtle()
tr.up()
tr.pensize(2)
tr.goto(0,-150)
tr.down()
tr.goto(0,200)
rectangle("orange")

tr.goto(0,150)
tr.forward(100)
tr.color("blue")
tr.circle(-25)
tr.setheading(270)
tr.forward(25)
tr.setheading(0)
for i in range(24):
    tr.forward(20)
    tr.bk(20)
    tr.left(15)
tr.setheading(90)
tr.forward(25)
tr.setheading(0)
tr.color("black")
tr.forward(100)
tr.right(90)
tr.forward(50)
tr.right(90)
tr.forward(200)
tr.right(90)
tr.forward(50)
tr.right(90)

tr.goto(0,100)
rectangle("green")

tr.done()