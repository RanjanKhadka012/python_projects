import turtle 
score_A=0
score_B=0

wn=turtle.Screen()
wn.title("Ranjan")
wn.setup(width=800,height=600)
wn.bgcolor("black")
wn.tracer(0)

#paddle A
paddle_A= turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.penup()
paddle_A.goto(-350,0)
paddle_A.shapesize(stretch_wid=5,stretch_len=1)


#paddle B
paddle_B= turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.penup()
paddle_B.goto(350,0)
paddle_B.shapesize(stretch_wid=5,stretch_len=1)

#ball
Ball= turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)
Ball.dx =4
Ball.dy=-4

#pen
pen=turtle.Turtle()
pen.speed()
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)


#function
def paddle_A_up():
    y = paddle_A.ycor()
    y=y+20
    paddle_A.sety(y)

def paddle_A_down():
    y = paddle_A.ycor()
    y=y-20
    paddle_A.sety(y)

def paddle_B_up():
    y = paddle_B.ycor()
    y=y+20
    paddle_B.sety(y)

def paddle_B_down():
    y = paddle_B.ycor()
    y=y-20
    paddle_B.sety(y)


#keyboard_binding
wn.listen()
wn.onkeypress(paddle_A_up,"w")
wn.onkeypress(paddle_A_down,"s")
wn.onkeypress(paddle_B_up,"Up")
wn.onkeypress(paddle_B_down,"Down")



#main game loop
while True:
    wn.update()
    
    #move ball
    Ball.setx(Ball.xcor()+Ball.dx)
    Ball.sety(Ball.ycor()+Ball.dy)

    # border checking
    if Ball.ycor()>290:
        Ball.sety(290)
        Ball.dy*=-1
        
    if Ball.ycor()<-290:
        Ball.sety(-290)
        Ball.dy*=-1
        
    if Ball.xcor()>390:
        Ball.goto(0,0)
        Ball.dx *= -1
        score_A +=1
    
    
    if Ball.xcor()<-390:
        Ball.goto(0,0)
        Ball.dx *= -1
        score_B+= 1
    pen.clear() 
    pen.write(f"Player A = {score_A} Player B = {score_B} " ,align= "center",font=("Courier",24,"normal"))
        
    #paddle and ball collission
    if Ball.xcor() > 340 and Ball.xcor() < 350 and (Ball.ycor()<paddle_B.ycor()+50 and Ball.ycor()> paddle_B.ycor() - 50):
        Ball.dx *= -1
        
    if Ball.xcor() <- 340 and Ball.xcor() >- 350 and (Ball.ycor()<paddle_A.ycor()+50 and Ball.ycor()> paddle_A.ycor() - 50):
        Ball.dx *= -1