
import random

#constants
#declaring colors for cars
colors = ["red" , "blue" , "yellow" , "pink" , "green"]

from turtle import Turtle



class car_class(Turtle):
    def __init__(self , speed):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid= 1 , stretch_len= 2)
        self.color(random.choice(colors))
        self.penup()
        car_y_cor = random.randint(-190,190)
        self.goto(270 , car_y_cor)
        self.left(180)
        self.starting_move_distance = speed
        self.increment_distance = 2

    def move_car(self):
        self.forward(self.starting_move_distance)

    def increment_speed(self):
        self.starting_move_distance += self.increment_distance









