from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.xspeed = 10
        self.yspeed = 10
        self.move_speed = .1

    def move(self):
        x = self.xcor() + self.xspeed
        y = self.ycor() + self.yspeed
        self.goto(x, y)

    def bounce_y(self):
        self.yspeed *= -1

    def bounce_x(self):
        self.xspeed *= -1
        self.move_speed *= .5

    def reset(self):
        self.goto(0,0)
        self.bounce_x()
        self.yspeed *= random.choice([-1, 1])
        self.move_speed = .1