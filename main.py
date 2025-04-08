#constants
finish_line = 260
current_car_speed = 5

#create screen and create turtle object
import time

from Player_turtle import player
from turtle import Turtle , Screen
from car import car_class
from score import scorebaord


#creating 600*600 screen
screen = Screen()
screen.setup(width=600 , height= 600)
screen.tracer(0)#shutting down screen update



#creating player object
player_turtle = player()

#creating score object
level = scorebaord()

#creating car list to save objects
car_list = []
car_counter = 0



#game_flag
is_game_on = True

#binding_game_keys
screen.listen()
screen.onkey(player_turtle.move_fw , "w")

while is_game_on:
    time.sleep(0.1)#will update screen in 0.1s
    screen.update()#manually handling screen update
    car_counter += 1#to count loop iteration to spawn new car

    #if loop executes 6 times,new car is spawned
    if car_counter % 6 == 0:
        car = car_class(current_car_speed)
        car_list.append(car)#saving car object in list

    #move all cars
    for car in car_list:
        car.move_car()

        #detect when player collides with car
        if player_turtle.distance(car) < 25:
            is_game_on = False
            level.game_over()



    if player_turtle.ycor() >= finish_line:
        player_turtle.start_over()
        current_car_speed += 10
        level.inc_score()





screen.exitonclick()