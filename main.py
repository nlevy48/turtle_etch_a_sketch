from turtle import Screen
from ball import Ball #when importing a class need to do from ____ import ___ and then the class
from paddle import Paddle

left_paddle_location = (-280, 0)

right_paddle_location = (280, 0)

UP = 90
DOWN = 270

s = Screen()

s.tracer(0)


s.bgcolor("black")

s.setup(width= 600, height= 600)

paddle_1 = Paddle(left_paddle_location)
paddle_2 = Paddle(right_paddle_location)







s.onkeypress(paddle_1.up, key= "w") #onkeypress() allows continual pressing
s.onkeypress(paddle_1.down, key= "s")
s.onkeypress(paddle_2.up, key= "Up")
s.onkeypress(paddle_2.down, key= "Down")

s.listen()











s.update()
s.exitonclick()