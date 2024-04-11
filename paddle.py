from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self, starting_location):
        super().__init__()
        self = Turtle("square")
        self.color("white")
        self.penup()
        self.goto(starting_location)
        self.shapesize(15, 2)

    def up(self):
        if self.heading() != UP:
            self.setheading(UP)
            self.forward(20)
        


    def down(self):
        if self.heading() != DOWN:
            self.setheading(DOWN)
            self.forward(20)
        


    

    
    