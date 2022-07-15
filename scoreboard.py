from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.create_player_score("Player 1", (-300, 270), self.score1)
        self.create_player_score("Player 2", (300, 270), self.score2)

    def create_player_score(self, name, position, score):
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.color("white")
        self.speed("fastest")
        self.write(f"{name}: {score}", align=ALIGNMENT, font=FONT)

    def update_scores(self):
        self.clear()
        self.create_player_score("Player 1", (-300, 270), self.score1)
        self.create_player_score("Player 2", (300, 270), self.score2)
