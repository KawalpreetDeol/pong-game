from turtle import Turtle
ALPHA = 2 # Accelartion
class Ball(Turtle):
    angle = 45
    direction = -1
    speed = 20
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(to_angle=self.angle)

    def move(self):
        self.forward(self.speed)

    def bounce(self):
        self.angle *= -1
        self.setheading(to_angle=self.angle)
    
    def collide(self):
        self.direction *= -1
        self.angle = self.angle + 90 * self.angle / abs(self.angle) * self.direction
        self.setheading(self.angle)
        self.speed+=ALPHA
    
    def ball_to_center(self):
        # self.angle = 45
        # self.direction = -1
        # self.setheading(self.angle)
        self.speed = 20
        self.goto(0,0)
        self.collide()
        self.bounce()