# Learn Python by Building Five Games - Full Course - freeCodeCamp.org - YouTube
#
# Game 01: Pong
#
# Lesson 02 - Create Paddles and Ball
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
paddle_a.penup()  # Turle defaults to draws a line as moving, we don't want that
paddle_a.goto(-350, 0)  # Coordinate: -350 [width is 800, 1/2 - 50] 50 away from right wall & 0, centered

# Create Paddle B
paddle_b: Turtle = turtle.Turtle()
paddle_b.speed(0)  # Animation Speed - Max Possible Speed
paddle_b.shape("square")  # Turtle Class has build in shapes, default (20x20)
paddle_b.color("silver")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # multiply the wid(up,down) by 5 & Len(left, right) by 1
paddle_b.penup()  # Turle defaults to draws a line as moving, we don't want that
paddle_b.goto(350, 0)  # Coordinate: +350 [width is 800, 1/2 + 50] 50 away from left wall & 0, centered

# Create Ball
ball: Turtle = turtle.Turtle()
ball.speed(0)  # Animation Speed - Max Possible Speed
ball.shape("circle")  # Turtle Class has build in shapes, default (20x20)
ball.color("lightgreen")
ball.penup()  # Turle defaults to draws a line as moving, we don't want that
ball.goto(0, 0)  # Coordinate: 0 & 0, centered
# Main game loop
while True:  # Keeps app active & so window active, without loop it just opens and closes
    wn.update()
