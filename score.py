from turtle import Turtle


class scorebaord(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-170,250)
        self.hideturtle()
        self.color("brown")
        self.level = 1
        self.write(f"Level {self.level}" , False , "center" , ("Arial" , 17 , "bold") )

    def update_score(self):
        self.clear()
        self.goto(-170,250)
        self.write(f"Level {self.level}" , False , "center" , ("Arial" , 17 , "bold") )


    def inc_score(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.color("black")
        self.write("Game Over!", False, "center" , ("Arial" , 45 , "bold") )




