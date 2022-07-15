from turtle import Turtle

# PLAYER1_START = [(-570, 30), (-570, 10), (-570, -10), (-570, -30)]
# PLAYER2_START = [(570, 30), (570, 10), (570, -10), (570, -30)]
PLAYER1_START = (-350, 0)
PLAYER2_START = (350, 0)
UP = 90
DOWN = 270
MOVE_SPEED = 10


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.speed("fastest")
        self.setposition(position)
        self.penup()
        self.color("white")

    def up(self):
        # if turn == 1:
        self.sety(self.pos()[1] + MOVE_SPEED)
        # else:
        #     self.player2.sety(self.player1.pos()[1] + MOVE_SPEED)

    def down(self):
        # if turn == 2:
        self.sety(self.pos()[1] - MOVE_SPEED)
        # else:
        #     self.player2.sety(self.player1.pos()[1] - MOVE_SPEED)
