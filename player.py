from turtle import Turtle
STARTING_POSITION = (0, -282)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        # self.hideturtle()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        # self.showturtle()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.showturtle()



