from turtle import Turtle, Screen
import random

s = Screen()
s.setup(width= 500, height=400)


y_positions = [ -70, -40, -10, 20, 50, 80]
turtle_color = ["red", "orange", "yellow", "green", "blue", "purple"]
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color[turtle_index])
    new_turtle.goto(x=-200, y=y_positions[turtle_index] )






s.exitonclick()