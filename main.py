from turtle import Screen
import time as Time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle(360)
paddle_left = Paddle(-360)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(paddle_right.move_up,"Up")
screen.onkey(paddle_right.move_down, "Down")


screen.onkey(paddle_left.move_up,"w")
screen.onkey(paddle_left.move_down, "s")

game_is_on = True

def exit_game():
    global game_is_on 
    game_is_on = False

screen.onkeypress(exit_game, "e")
direction = 1
while game_is_on:
    screen.update()
    
    ball.move()
    Time.sleep(0.1)

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    if ball.xcor() > 370:
        scoreboard.increment_score_left()
        ball.ball_to_center()

    if ball.xcor() < -370:
        scoreboard.increment_score_right()
        ball.ball_to_center()

    if ball.xcor() >= 340 and ball.distance(paddle_right) <= 50:
        ball.collide()
    
    # if ball.xcor() <= paddle_left.xcor() + 20 and ball.ycor() < paddle_left.ycor() + 50 and ball.ycor() > paddle_left.ycor() - 50:
    if ball.xcor() <= -340 and ball.distance(paddle_left) <= 50:
        ball.collide()
    
    if scoreboard.score_left >= 5 or scoreboard.score_right >= 5:
        scoreboard.game_over()
        game_is_on = False
    

screen.exitonclick()