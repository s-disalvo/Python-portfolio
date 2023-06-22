# Simple Ping in Python 3 for Beginners
# By @TokyoEdTech
# Part 1: Getting Started

import turtle
import os

wn = turtle.Screen()
wn.title("Pong by s-disalvo")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
# wn.tracer stops the window from updating. This makes the game much faster
# wn means window

# Score
score_a = 0
score_b = 0


# Part 2: Adding paddles and ball
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) 
# speed of animation, not paddles
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() # Turtles draw a line by default. This removes it.
paddle_a.goto(-350, 0) # starting point for paddle

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() 
paddle_b.goto(350, 0) 

# Ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape("square")
ball.color("white")
ball.penup() 
ball.goto(0, 0)
ball.dx = 2 # dx means change
ball.dy = -2 # every time our ball moves, it moves 2 pixels
# to get the ball to actually move, we have to go inside the main game loop.

# Pen 
pen = turtle.Turtle()
pen.speed(0) 
pen.color("white")
pen.penup() # don't want to draw a line
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor() # .ychor returns the y coordinate
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() # .ychor returns the y coordinate
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() # .ychor returns the y coordinate
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() # .ychor returns the y coordinate
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen() # This tells it to listen for keyboard input
wn.onkeypress(paddle_a_up, "w") # When the user presses "w" call the fucntion paddle_a_up
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main game loop. This is the meat & potatoes of every game
while True:
    wn.update() #everythime this runs, it updates the screen.

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay pong_bounce.wav&") # & allows for the animation to keep going while sound plays

    # Bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay pong_bounce.wav&")

    # Left border
    if ball.xcor() > 390:
        ball.goto(0, 0) # bring it back to the center
        ball.dx *= -1 # reverse the ball direction
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Right border
    if ball.xcor() < -390:
        ball.goto(0, 0) # bring it back to the center
        ball.dx *= -1 # reverse the ball direction
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    # if the ball is touching the paddle at x => 340 and it's between the top and bottom of the paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1
            os.system("afplay pong_bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1
            os.system("afplay pong_bounce.wav&")