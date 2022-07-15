import time
from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer()

scoreboard = Scoreboard()
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()

screen.onkeypress(paddle1.up, "Up")
screen.onkeypress(paddle1.down, "Down")
screen.onkeypress(paddle2.up, "w")
screen.onkeypress(paddle2.down, "s")
screen.listen()

# while PRESSED:
#     screen.tracer()
#     screen.update()
#     print("up")
#
#
game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # if -350 < ball.xcor() < -330 or 330 < ball.xcor() < 350:
    #     if ball.distance(paddle1.position()) < 55 or ball.distance(paddle2.position()) < 55:
    #         ball.bounce_x()

    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if -400 > ball.xcor():
        ball.reset()
        scoreboard.score2 += 1
        scoreboard.update_scores()

    if 400 < ball.xcor():
        ball.reset()
        scoreboard.score1 += 1
        scoreboard.update_scores()

screen.exitonclick()
