# Learn Python by Building Five Games - Full Course - freeCodeCamp.org - YouTube
#
# Game 01: Pong
#
# Lesson 03 - Move Paddles using Keyboard
#
import turtle
from turtle import Turtle

print("* Pong *")

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer()  # Stops window from updating

# Create Paddle A
paddle_a: Turtle = turtle.Turtle()
paddle_a.speed(0)  # Animation Speed - Max Possible Speed
paddle_a.shape("square")  # Turtle Class has build in shapes, default (20x20)
paddle_a.color("gold")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # multiply the wid(up,down) by 5 & Len(left, right) by 1
paddle_a.penup()  # Turtle defaults to draws a line as moving, we don't want that
paddle_a.goto(-350, 0)  # Coordinate: -350 [width is 800, 1/2 - 50] 50 away from right wall & 0, centered

# Create Paddle B
paddle_b: Turtle = turtle.Turtle()
paddle_b.speed(0)  # Animation Speed - Max Possible Speed
paddle_b.shape("square")  # Turtle Class has build in shapes, default (20x20)
paddle_b.color("silver")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # multiply the wid(up,down) by 5 & Len(left, right) by 1
paddle_b.penup()  # Turtle defaults to draws a line as moving, we don't want that
paddle_b.goto(350, 0)  # Coordinate: +350 [width is 800, 1/2 + 50] 50 away from left wall & 0, centered

# Create Ball
ball: Turtle = turtle.Turtle()
ball.speed(0)  # Animation Speed - Max Possible Speed
ball.shape("circle")  # Turtle Class has build in shapes, default (20x20)
ball.color("lightgreen")
ball.penup()  # Turtle defaults to draws a line as moving, we don't want that
ball.goto(0, 0)  # Coordinate: 0 & 0, centered

#  Movement Functions


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if y < 260:
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if y > -260:
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if y < 260:
        paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    if y > -260:
        paddle_b.sety(y)

# Keyboard Binding
wn.listen()  # Listen for keyboard input

wn.onkeypress(paddle_a_up,"w")  # when user enters "w", call function paddle_a_up
wn.onkeypress(paddle_a_down,"s")  # when user enters "s", call function paddle_a_down
wn.onkeypress(paddle_b_up,"Up")  # when user enters Up Arrow Key, call function paddle_a_up
wn.onkeypress(paddle_b_down,"Down")  # when user enters Down Arrow Key, call function paddle_a_down

# Main game loop
while True:  # Keeps app active & so window active, without loop it just opens and closes
    wn.update()
