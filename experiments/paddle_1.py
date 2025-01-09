from turtle import Turtle, Screen

STARTING_POSITION = [(0, 0), (0, -20), (0, -40), (0, -60), (0, -80)]

class Paddle1():

    def __init__(self):
        self.paddles = []
        self.create_paddle_1()

    def create_paddle_1(self):
        pad = Turtle("square")
        pad.color("white")
        pad.penup()
        pad.shapesize(5, 1)
        pad.goto(350, 0)
        self.paddles.append(pad)

    def up(self):
        self.paddles[0].left(90)
        self.paddles[0].forward(20)
        self.paddles[0].right(90)

    def down(self):
        self.paddles[0].right(90)
        self.paddles[0].forward(20)
        self.paddles[0].left(90)

    def quit(self):
        screen = Screen()
        screen.bye()




