from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard



screen = Screen()
screen.tracer(0)
screen.setup(height=600,width=800)
screen.title('PONG game!')
screen.bgcolor("black")
screen.listen()

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

screen.onkey(key='w',fun=l_paddle.move_up)
screen.onkey(key='s',fun=l_paddle.move_down)
screen.onkey(key='p',fun=r_paddle.move_up)
screen.onkey(key='l',fun=r_paddle.move_down)

ball = Ball()
scoreboard = Scoreboard()

duration = 0.1

game_is_on = True
while game_is_on:
    time.sleep(duration)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 380 :
        ball.set_right()
        scoreboard.left_score()
        scoreboard.update_score()
        duration = 0.1


    if ball.xcor() < -380:
        ball.set_left()
        scoreboard.right_score()
        scoreboard.update_score()
        duration = 0.1

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        duration *= 0.9



screen.exitonclick()