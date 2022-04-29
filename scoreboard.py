import turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
FONT2 = ("Courier", 15, "normal")


class Scoreboard(turtle.Turtle):

    def __init__(self, score):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = score

    def scoring(self):
        self.goto(0, 250)
        self.write("Score: 0", False, align=ALIGNMENT, font=FONT)

    def scoring_refresh(self):
        self.score += 1
        new_score = "Score:0" + str(self.score)
        self.write(new_score, False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game over",False,align=ALIGNMENT,font=FONT2)
