from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_vel = 10
        self.y_vel = -10
        self.mov_speed = 0.1


    def move(self):
        self.goto(self.xcor()+self.x_vel, self.ycor()+self.y_vel)

    def bounce_y(self):
        self.y_vel *= -1

    def bounce_x(self):
        self.x_vel *= -1
        # self.mov_speed *= 0.9

    def reset_pos(self):
        self.goto(0,0)
        self.bounce_x()
        self.mov_speed = 0.1