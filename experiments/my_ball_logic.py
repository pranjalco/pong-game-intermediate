from turtle import Turtle, Screen
from paddle import Paddle
import time
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "o")
screen.onkey(r_paddle.go_down, "l")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Turtle("circle")
ball.color("white")



angle = random.randint(0, 360)
while 145 > angle > 35 or 325 > angle > 215:
    angle = random.randint(0, 360)
# print(angle)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    # angle = 35
    if ball.distance(l_paddle) < 10:
        angle = random.randint(0, 360)
        while 325 > angle > 35:
            angle = random.randint(0, 360)
        print(angle)
    if ball.distance(r_paddle) < 10:
        angle = random.randint(145, 215)
        print(angle)


    ball.setheading(angle)
    ball.forward(10)


screen.exitonclick()
