from turtle import Turtle
HEIGHT = 600
class Paddle(Turtle):
    y_position = 0
    def __init__(self, x_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(x_cor, 0)
        self.setheading(90)

    def move_up(self):
        if self.y_position < HEIGHT/2 - 50:
            self.y_position += 25
            self.forward(25)

    def move_down(self):
        if self.y_position > HEIGHT/2 * -1 + 50:
            self.y_position -= 25
            self.backward(25)
        