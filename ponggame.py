import turtle
win= turtle.Screen()
win.title("Ponggame")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0) #it prevents window from updating...so we can manually update it
score_a=0
score_b=0
pad_a=turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("red")
pad_a.shapesize(stretch_wid=6, stretch_len=1)
pad_a.penup()
pad_a.goto(-350,0)

pad_b=turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("red")
pad_b.shapesize(stretch_wid=6, stretch_len=1)
pad_b.penup()
pad_b.goto(350,0)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=2

pen= turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("A: {}   B: {}".format(score_a, score_b) , align="center", font=("Courier", 24, "normal"))


def pad_a_up():
    y=pad_a.ycor()
    y+=20
    pad_a.sety(y)
    
def pad_a_down():
    y=pad_a.ycor()
    y-=20
    pad_a.sety(y)
    
def pad_b_up():
    y=pad_b.ycor()
    y+=20
    pad_b.sety(y)
    
def pad_b_down():
    y=pad_b.ycor()
    y-=20
    pad_b.sety(y)    
    
        
win.listen()
win.onkeypress(pad_a_up, "w")
win.onkeypress(pad_a_down, "s")
win.onkeypress(pad_b_up, "Up")
win.onkeypress(pad_b_down, "Down")
    
while True:
    win.update()
    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor()+ball.dx)
    
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1    
    
    if ball.xcor()>400:
        ball.goto(0,0)
        ball.dx *= -1
        score_a+=1
        pen.clear()
        pen.write("A: {}   B: {}".format(score_a, score_b) , align="center", font=("Courier", 24, "normal"))

    
    if ball.xcor()<-400:
        ball.goto(0,0)
        ball.dx *= -1   
        score_b+=1
        pen.clear()
        pen.write("A: {}   B: {}".format(score_a, score_b) , align="center", font=("Courier", 24, "normal"))

    
    
    if (ball.xcor()>330 and ball.xcor()<340) and (ball.ycor()<pad_b.ycor()+50 and ball.ycor()>pad_b.ycor()-50):
        ball.setx(330)
        ball.dx*=-1    
    if (ball.xcor()< -330 and ball.xcor()>-340) and (ball.ycor()<pad_a.ycor()+50 and ball.ycor()>pad_a.ycor()-50):
        ball.setx(-330)
        ball.dx*=-1                                    
                                    
                                    
                                    