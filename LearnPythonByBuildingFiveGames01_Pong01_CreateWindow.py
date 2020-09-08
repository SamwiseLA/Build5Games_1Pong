# Learn Python by Building Five Games - Full Course - freeCodeCamp.org - YouTube
#
# Game 01: Pong
#
# Lesson 01 - Create the window
#
import turtle
print("* Pong *")

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer()  # Stops window from updating

# Main game loop
while True:  # Keeps app active & so window active, without loop it just opens and closes
    wn.update()