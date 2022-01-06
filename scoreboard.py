from turtle import Turtle


FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-220, 260)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)


    def level_up(self):
        self.level += 1
        self.update_scoreboard()
    

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)