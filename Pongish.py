# Learn Python by Building Five Games - Full Course - freeCodeCamp.org - YouTube
#
# Game 01: Pong
#
# Lesson 07 - Adding Sound
#
import time
import turtle
import os  # System Operating System to add sound


# from turtle import Turtle

print("* Pong *")

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech ... Massaged by Samwise Aaron")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer()  # Stops window from updating

play_again = False

# Score

score_a = 0
score_b = 0
score_win = 0

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
ball.dy = 4  # Create ball attribute to hold, ball y change (d for delta or change & y) speed
ball.play_again_check = False
ball.score_win = score_win

# pen - Create Headings ------------- Headings ------------
heading_top = 270
heading_2 = 200
heading_3 = 120
top_of_game = 230


penGold = turtle.Turtle()
penGold.speed(0)
penGold.color("gold")
penGold.penup()
penGold.hideturtle()
penGold.goto(-370, heading_top)

penSilver = turtle.Turtle()
penSilver.speed(0)
penSilver.color("silver")
penSilver.penup()
penSilver.hideturtle()
penSilver.goto(-100, heading_top)

pen_win = turtle.Turtle()
pen_win.speed(0)
pen_win.color("White")
pen_win.penup()
pen_win.hideturtle()
pen_win.goto(230, heading_top + 10)

pen_speed = turtle.Turtle()
pen_speed.speed(0)
pen_speed.color("White")
pen_speed.penup()
pen_speed.hideturtle()
pen_speed.goto(230, heading_top - 5p)

pen_win_heading = turtle.Turtle()
pen_win_heading.speed(0)
pen_win_heading.color("white")
pen_win_heading.penup()
pen_win_heading.hideturtle()
pen_win_heading.goto(0, heading_2)

pena = turtle.Turtle()
pena.speed(0)
pena.color("white")
pena.penup()
pena.hideturtle()
pena.goto(0, heading_3)

#  Movement Functions


def f_play_again():
    ball.play_again_check = True
    print("Play Again 1")


def speed_up():
    if abs(ball.dx) < 8:
        ball.dx *= 2
        ball.dy *= 2
        main_display()


def speed_down():
    if abs(ball.dx) > 2:
        ball.dx /= 2
        ball.dy /= 2
        main_display()


def main_display():
    penGold.clear()
    penSilver.clear()
    pen_win.clear()
    pen_speed.clear()

    penGold.write(f"Gold Player: {score_a} (w:s)", align="left", font=("Courier", 20, "underline"))
    penSilver.write(f"Silver Player: {score_b} (Up/Down) ", align="left", font=("Courier", 20, "underline"))
    pen_win.write(f"[{ball.score_win}] # to Win X", align="left", font=("Courier", 16, "underline"))
    if abs(ball.dx) == 2:
        speed_display = "Slow"
    elif abs(ball.dx) == 8:
        speed_display = "Dbl"
    else:
        speed_display = "Reg"
    pen_speed.write(f"(<\>) Ball Speed: {speed_display}", align="left", font=("Courier", 12, "underline"))


def score_max_inc_up():
    ball.score_win += 1
    main_display()


def score_max_inc_down():
    ball.score_win -= 1
    main_display()


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if y < top_of_game:
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if y > -260:
        paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if y < top_of_game:
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
wn.onkeypress(f_play_again, "space")  # when user enters Space Bar Key, call function f_play_again
wn.onkeypress(score_max_inc_up, "Right")  # when user enters Right Key, call function score_max_inc_up
wn.onkeypress(score_max_inc_down, "Left")  # when user enters Left Key, call function score_max_inc_down
wn.onkeypress(speed_down, "<")  # when user enters < Key, call function speed_down
wn.onkeypress(speed_up, ">")  # when user enters > Key, call function speed_up

main_display()


# Main game loop
while True:  # Keeps app active & so window active, without loop it just opens and closes
    wn.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > heading_top - 10:
        #  ball.sety(top_of_game - 10)
        ball.dy *= -1
        os.system("afplay pongblipg5.wav&")

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        os.system("afplay pongblipg5.wav&")

# Players Side B
    if ball.xcor() > 390:
        score_a += 1
        main_display()
        ball.goto(0, 0)
        time.sleep(1)
        ball.dx *= -1

    # Players Side A
    if ball.xcor() < -390:
        score_b += 1
        main_display()
        ball.goto(0, 0)
        time.sleep(1)
        ball.dx *= -1

# Paddle and Ball Collisions
    paddle_width = 130
    if (340 < ball.xcor() < 350) or \
            (-340 > ball.xcor() > -350):
        print(f"----->\nBall(x): {ball.xcor()} Ball(y): {ball.ycor()} \n"
              f"Paddle a(y): {paddle_a.ycor()} {int(paddle_a.ycor() + paddle_width / 2)}:{int(paddle_a.ycor() - paddle_width / 2) }\n"
              f"Paddle b(y): {paddle_b.ycor()} {int(paddle_b.ycor() + paddle_width / 2)}:{int(paddle_b.ycor() - paddle_width / 2) } ")

    if (-340 > ball.xcor() > -350) and \
            (ball.ycor() < (paddle_a.ycor() + paddle_width / 2) and
             (ball.ycor() > paddle_a.ycor() - paddle_width / 2)):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay pong.wav&")

    if (340 < ball.xcor() < 350) and \
            (ball.ycor() < (paddle_b.ycor() + paddle_width / 2) and
             (ball.ycor() > paddle_b.ycor() - paddle_width / 2)):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay pong.wav&")

    if (-360 > ball.xcor()) or (ball.xcor() > 370):
        if (ball.xcor() < 0 and -365 < ball.xcor()) or (ball.xcor() > 0 and ball.xcor() < 375):
            os.system("afplay match4.wav&")
            os.system("afplay losepoints.mp3&")
            print(ball.xcor())

    if ball.score_win != 0:
        if score_a == ball.score_win:
            main_display()
            pen_win_heading.clear()
            pen_win_heading.color("gold")
            pen_win_heading.write(f"Gold PLAYER WINS!!!", align="center", font=("Courier", 24, "normal"))

        if score_b == ball.score_win:
            main_display()
            pen_win_heading.clear()
            pen_win_heading.color("silver")
            pen_win_heading.write(f"Silver PLAYER WINS!!!", align="center", font=("Courier", 24, "normal"))

    if ball.score_win in (score_a, score_b):
        pena.write(f"( --- Press Space Bar to play again! --- )\n\n     *** L/R:+/- # of games to win ***",
                   align="center", font=("Courier", 18, "normal"))
        os.system("afplay jingle-achievement-00.wav&")
        a = 0
        ball.goto(0, 0)
        ball.setx(0)
        ball.sety(0)

        while not ball.play_again_check:  # Loop until space is pressed
            wn.update()
            if ball.play_again_check:
                print("Play Again 2")
        ball.play_again_check = False
        if ball.score_win == 0:
            ball.score_win = 1
        score_a = 0
        score_b = 0
        main_display()
        pen_win_heading.clear()
        pen_win_heading.write(f"*** GOOD LUCK!!! ***", align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        pen_win_heading.clear()
        pena.clear()
