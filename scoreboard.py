from turtle import Turtle


class Scoreboard(Turtle):
    """This creates scoreboards and display it on screen and updates the score also check winner."""

    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.winner_score = 10
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 190)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(150, 190)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.goto(0, 250)
        self.write(f"Score {self.winner_score} to Win", align="center", font=("Courier", 12, "bold"))
        self.goto(0, 230)
        self.write(f"the Game", align="center", font=("Courier", 12, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def check_winner(self):
        if self.l_score == self.winner_score:
            self.goto(0, 0)
            self.write("Left player wins", align="center", font=("Courier", 20, "bold"))
            return True

        if self.r_score == self.winner_score:
            self.goto(0, 0)
            self.write("Right player wins", align="center", font=("Courier", 20, "bold"))
            return True

    # def update_score(self):
    #     self.clear()
    #     self.goto(-100, 190)
    #     self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
    #     self.goto(100, 190)
    #     self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
