from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(0, 260)
        self.score = 0

    def write_new_score(self):
        argument = f"Level: {self.score}"
        self.write(argument, False, "center", FONT)

    def game_over(self):
        self.home()
        self.write(f"Game Over - Level {self.score}", False, "center", FONT)


    def change_score(self):
        self.clear()
        self.score += 1
        self.write_new_score()

