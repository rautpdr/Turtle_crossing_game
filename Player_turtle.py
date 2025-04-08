#Create a turtle player that starts at the bottom of the screen
# and listen for the "Up" keypress to move the turtle north.

from turtle import Turtle

class player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(0,-280)

    def move_fw(self):
        self.forward(10)

    def start_over(self):
        self.goto(0,-280)