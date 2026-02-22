from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto((0,0))
        self.y_step = 10
        self.x_step = 10

    def move_ball(self):
        x_cor = self.xcor() + self.x_step
        y_cor = self.ycor() + self.y_step
        self.goto(x_cor,y_cor)

    def bounce_y(self):
        self.y_step *= -1

    def bounce_x(self):
        self.x_step *= -1

    def set_right(self):
        self.x_step *= -1
        self.goto(0,0)

    def set_left(self):
        self.x_step *= -1
        self.goto(0,0)