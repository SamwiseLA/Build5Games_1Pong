# Learn Python by Building Five Games - Full Course - freeCodeCamp.org - YouTube
#
# Game 01: Pong
#
# Lesson 06 - Scoring
#
import time
import turtle
from turtle import Turtle

print("* Pong *")

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer()  # Stops window from updating

# Score

score_a = 0
score_b = 0
score_win = 2

# Create Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # Animation Speed - Max Possible Speed
paddle_a.shape("square")  # Turtle Class has build in shapes, default (20x20)
paddle_a.color("gold")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # multiply the wid(up,down) by 5 & Len(left, right) by 1
paddle_a.penup()  # Turtle defaults to draws a line as moving, we don't want that
paddle_a.goto(-350, 0)  # Coordinate: -350 [width is 800, 1/2 - 50] 50 away from right wall & 0, centered

# Create Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # Animation Speed - Max Possible Speed
paddle_b.shape("square")  # Turtle Class has build in shapes, default (20x20)
paddle_b.color("silver")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # multiply the wid(up,down) by 5 & Len(left, right) by 1
paddle_b.penup()  # Turtle defaults to draws a line as moving, we don't want that
paddle_b.goto(350, 0)  # Coordinate: +350 [width is 800, 1/2 + 50] 50 away from left wall & 0, centered

# Create Ball
ball = turtle.Turtle()
ball.speed(0)  # Animation Speed - Max Possible Speed
ball.shape("circle")  # Turtle Class has build in shapes, default (20x20)
ball.color("lightgreen")
ball.penup()  # Turtle defaults to draws a line as moving, we don't want that
ball.goto(0, 0)  # Coordinate: 0 & 0, centered
# Ball Movement
ball.dx = 4  # Create ball attribute to hold, ball x change (d for delta or change & x) speed
ball.dy = -4  # Create ball attribute to hold, ball y change (d for delta or change & y) speed

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a}  Player B: {score_b} [{score_win}] Wins!!!", align="center", font=("Courier", 24, "normal"))

penw = turtle.Turtle()
penw.speed(0)
penw.color("white")
penw.penup()
penw.hideturtle()
penw.goto(0, 210)


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

wn.onkeypress(paddle_a_up, "w")  # when user enters "w", call function paddle_a_up
wn.onkeypress(paddle_a_down, "s")  # when user enters "s", call function paddle_a_down
wn.onkeypress(paddle_b_up, "Up")  # when user enters Up Arrow Key, call function paddle_a_up
wn.onkeypress(paddle_b_down, "Down")  # when user enters Down Arrow Key, call function paddle_a_down

# Main game loop
while True:  # Keeps app active & so window active, without loop it just opens and closes
    wn.update()

    # Move the Bll
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

# Players Side B
    if ball.xcor() > 390:
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b} [{score_win}] Wins!!!", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        time.sleep(1)
        ball.dx *= -1

    # Players Side A
    if ball.xcor() < -390:
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b} [{score_win}] Wins!!!", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        time.sleep(1)
        ball.dx *= -1

# Paddle and Ball Collisions

    if (ball.xcor() > 340 and ball.xcor() < 350) and \
            (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() < -350) and \
            (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    if score_a == score_win:
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        penw.write(f"PLAYER A WINS", align="center", font=("Courier", 24, "normal"))

    if score_b == score_win:
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        penw.write(f"PLAYER B WINS", align="center", font=("Courier", 24, "normal"))

    if score_win in (score_a, score_b):
        input("Enter")
        score_a = 0
        score_b = 0
        pen.clear()
        penw.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b} [{score_win}] Wins!", align="center",
                  font=("Courier", 24, "normal"))
        penw.write(f"GOOD LUCK", align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        penw.clear()
