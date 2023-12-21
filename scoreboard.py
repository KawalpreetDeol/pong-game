from turtle import Turtle
class Scoreboard(Turtle):
    score_left = 0
    score_right = 0
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 265)
        self.display_score()

    def display_score(self):
        self.write(f'{str(self.score_left) + " "*5 + str(self.score_right)}', False, align="center", font=("Courier", 24,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f'{"RIGHT" if self.score_right > self.score_left else "LEFT" } WINS!', False, align="center", font=("Courier", 24,"normal"))
    
    def increment_score_left(self):
        self.score_left+=1
        self.clear()
        self.display_score()

    def increment_score_right(self):
        self.score_right+=1
        self.clear()
        self.display_score()
    
    def refresh_score(self):
        self.score = 0
        self.clear()
        self.display_score()