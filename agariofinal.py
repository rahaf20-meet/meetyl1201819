import turtle
from turtle import *
import time
import random
import math
from ball import Ball


score = 0
turtle.pu()
turtle.color("blue")
turtle.goto(-50,200)
turtle.goto(-50,200)

turtle.tracer(0)
turtle.hideturtle()

RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = getcanvas().winfo_width()//2
SCREEN_HEIGHT = getcanvas().winfo_height()//2

MY_BALL = Ball(12,12,10,15,23, "blue")
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=7
MAXIMUM_BALL_RADIUS=60
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5

def collide(ball_a, ball_b):
	if ball_a == ball_b:
		return False
	distance = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(), 2)+math.pow(ball_a.ycor()-ball_b.ycor(), 2))
	if(distance+10 < ball_a.r + ball_b.r):
		return True
	else:
		return False


	

BALLS = []

for i in range(NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
	dx= random.randint(MINIMUM_BALL_DX,MINIMUM_BALL_DX)
	while dx == 0:
		dx= random.randint(MINIMUM_BALL_DX,MINIMUM_BALL_DX)
	dy= random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	while dy == 0:
		dy= random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
	color = (random.random(),random.random(),random.random())



	new_ball= Ball(x,y,dx,dy,radius,color)
	#check colision between bew-ball and my ball. if coliding - 
	while collide(MY_BALL,new_ball):
		x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
		y = random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
		dx= random.randint(MINIMUM_BALL_DX,MINIMUM_BALL_DX)
		while dx == 0:
			dx= random.randint(MINIMUM_BALL_DX,MINIMUM_BALL_DX)
		dy= random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
		while dy == 0:
			dy= random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
		radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
		new_ball.x = x
		new_ball.y = y
		new_ball.dx = dx
		new_ball.dy = dy
		new_ball.r = radius
		new_ball.shapesize(new_ball.r/10)
		new_ball.goto(x, y)


	print(new_ball)
	BALLS.append(new_ball)

def move_all_balls():
	for o in BALLS:
		o.move(SCREEN_WIDTH, SCREEN_HEIGHT)



def check_all_balls_collision(BALLS):
	for ball_a in BALLS:
		for ball_b in BALLS:
			if ball_a != ball_b:
				if collide(ball_a,ball_b)==True:
					ball_a_radius=ball_a.r
					ball_b_radius=ball_b.r	
					X_COORDINATE=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
					Y_COORDINATE=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
					X_AXISSPEED = random.randint( MINIMUM_BALL_DX , MAXIMUM_BALL_DX )
					Y_AXISSPEED = random.randint( MINIMUM_BALL_DY , MAXIMUM_BALL_DY )
					while X_AXISSPEED or Y_AXISSPEED == 0:
						X_AXISSPEED = random.randint( MINIMUM_BALL_DX , MAXIMUM_BALL_DX )
						Y_AXISSPEED = random.randint( MINIMUM_BALL_DY , MAXIMUM_BALL_DY )

					radius =random.randint(MINIMUM_BALL_RADIUS , MY_BALL.r+10)

					color = (random.random(),random.random(),random.random())

					if ball_a.r  > ball_b.r:
						if ball_b.r < MAXIMUM_BALL_RADIUS:
							ball_b.r = ball_b.r + 1
						else:
							ball_b.r = 10
						ball_b.goto(X_COORDINATE, Y_COORDINATE)
						# ball_b.dx = X_AXISSPEED
						# ball_b.dy = Y_AXISSPEED
						ball_b.color(color)
						ball_b.shapesize(ball_b.r/10)
						ball_a.r = ball_a.r + 2
						ball_a.shapesize(ball_a.r/10)
					else:
						if ball_a.r < MAXIMUM_BALL_RADIUS:
							ball_a.r = ball_a.r + 1
						else:
							ball_a.r = 10
						
						ball_a.goto(X_COORDINATE, Y_COORDINATE)
						# ball_a.dx = X_AXISSPEED
						# ball_a.dy = Y_AXISSPEED
						ball_a.color(color)
						ball_a.shapesize(ball_a.r/10)
						ball_b.r = ball_b.r + 2
						ball_b.shapesize(ball_b.r/10)

def check_myball_collision(MY_BALL):
	for ball in BALLS:
		if collide(MY_BALL,ball) == True:
			ball_r4 = ball.r 
			my_ball_r4 = MY_BALL.r
			X_COORDINATE=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
			Y_COORDINATE=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
			X_AXISSPEED = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
			Y_AXISSPEED = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
			while X_AXISSPEED and Y_AXISSPEED == 0:
				X_AXISSPEED = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DY)
				Y_AXISSPEED = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

			radius = random.randint(MINIMUM_BALL_RADIUS , MY_BALL.r)
			

			color = (random.random(),random.random(),random.random())
			global score
			score += 1
			turtle.undo()
			turtle.write("score = " + str(score), font = ("Comic Sans MS", 25 , "normal"))

			

			if my_ball_r4 > ball_r4:
				
				ball.r = radius
				ball.x = X_COORDINATE
				ball.y = Y_COORDINATE
				ball.goto(X_COORDINATE, Y_COORDINATE)
				ball.dx = X_AXISSPEED
				ball.dy = Y_AXISSPEED
				ball.color(color)
				ball.shapesize(ball.r/10)
				MY_BALL.r = my_ball_r4 + 2
				MY_BALL.shapesize(MY_BALL.r/10)

			else:
				return False

			

	return True		

def movearound(event):
	X = event.x - round(SCREEN_WIDTH)
	Y = round(SCREEN_HEIGHT) - event.y
	MY_BALL.goto(X,Y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()
turtle.update()
time.sleep(1)
while RUNNING:
		move_all_balls()
		turtle.update()
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()//2
		SCREEN_HEIGHT =  turtle.getcanvas().winfo_height()//2
		RUNNING=check_myball_collision(MY_BALL)
		check_all_balls_collision(BALLS)
		
		time.sleep(SLEEP+.01)
if RUNNING == False:
	quit()


turtle.mainloop()