import turtle

wn = turtle.Screen()
wn.title("Anirudh")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2 #everytime the ball moves it moves by 2 pixels
ball.dy = -2

# Pen

# Function
def paddle_a_up():
    y = paddle_a.ycor() #.ycor() returns the y cordinate of the function
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #.ycor() returns the y cordinate of the function
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #.ycor() returns the y cordinate of the function
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()  # .ycor() returns the y cordinate of the function
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen() # listen for keyboard input from the user
wn.onkeypress(paddle_a_up, "w") # when user presses w, call the function paddle_a_up
wn.onkeypress(paddle_a_down, "s") # when user presses s, call the function paddle_a_down
wn.onkeypress(paddle_b_up, "Up") # when user presses Up key, call the function paddle_b_up
wn.onkeypress(paddle_b_down, "Down") # when user presses Down key, call the function paddle_b_down


# Main Game Loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290) #set the coordiantes of the ball to 290
        ball.dy *= -1 #reverses the direction of the ball

    if ball.ycor() < -290:
        ball.sety(-290) #set the coordiantes of the ball to 290
        ball.dy *= -1 #reverses the direction of the ball

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1