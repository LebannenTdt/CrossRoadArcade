from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE = 280


class Player(Turtle):
    

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.reset()
        self.setheading(90)
    

    def move(self):
        self.forward(MOVE_DISTANCE)


    def reset(self):
        self.goto(STARTING_POSITION)
