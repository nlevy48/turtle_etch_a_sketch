from turtle import Turtle, Screen

s = Screen()
s.listen()
#make etch a sketch
turt = Turtle()

def move_right():
    if turt.heading != 0:
        turt.setheading(0)
        turt.forward(10)
    else:
        turt.forward(10)


def move_up():
    if turt.heading != 90:
        turt.setheading(0)
        turt.setheading(90)
        turt.forward(10)
    else:
        turt.forward(10)


def move_left():
    if turt.heading != 180:
        turt.setheading(0)
        turt.setheading(180)
        turt.forward(10)
    else:
        turt.forward(10)


def move_down():
    if turt.heading != 270:
        turt.setheading(0)
        turt.setheading(270)
        turt.forward(10)
    else:
        turt.forward(10)


s.onkey(move_right, key="Right")
s.onkey(move_left, key="Left")
s.onkey(move_down, key="Down")
s.onkey(move_up, key="Up")


s.exitonclick()