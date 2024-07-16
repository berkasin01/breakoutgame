from turtle import *
from ball import Ball
import time
import random
colors = [
    "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black",
    "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse",
    "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan", "darkblue",
    "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkkhaki", "darkmagenta",
    "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen",
    "darkslateblue", "darkslategray", "darkturquoise", "darkviolet", "deeppink", "deepskyblue",
    "dimgray", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro",
    "ghostwhite", "gold", "goldenrod", "gray", "green", "greenyellow", "honeydew", "hotpink",
    "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon",
    "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgreen", "lightgrey",
    "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightsteelblue",
    "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", "mediumblue",
    "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen",
    "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin",
    "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod",
    "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum",
    "powderblue", "purple", "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown",
    "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue", "slategray", "snow", "springgreen",
    "steelblue", "tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke",
    "yellow", "yellowgreen"
]
width = 6.0

turtle = Turtle()
screen = Screen()
ball = Ball()

screen.setup(1000, 800)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

turtle.shape("square")
turtle.color("white")
turtle.shapesize(1.0, width, 1)
turtle.penup()
turtle.goto(0, -350)


def move_right():
    new_x = turtle.xcor() + 25
    turtle.goto(new_x, turtle.ycor())


def move_left():
    new_x = turtle.xcor() - 25
    turtle.goto(new_x, turtle.ycor())


screen.listen()
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")

all_blocks = []
for c in range(-390, 390, 150):
    for i in range(10):
        block = Turtle()
        block.penup()
        block.color(random.choice(colors))
        block.shape("square")
        block_width = (random.randint(2, 3) + 1) * 1.75
        block.shapesize(1.0, block_width, 1)
        x_ini = c - random.randint(-10, 10)
        y_ini = (i * 30 + 100) - random.randint(-5, 5)
        block.goto(x_ini, y_ini)
        all_blocks.append(block)


the_game_on = True
while the_game_on:
    time.sleep(ball.mov_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 400:
        ball.bounce_y()

    if ball.xcor() > 450 or ball.xcor() < -500:
        ball.bounce_x()

    for b in all_blocks:
        if ball.distance(b) < 50:
            ball.bounce_x()
            b.reset()

    if ball.distance(turtle) < 55:
        ball.bounce_y()

screen.exitonclick()
