from turtle import *
import random
import time
import turtle

right_side_ball = 0
left_side_ball = 0
up_side_ball = 0
down_side_ball = 0

# global right_side_ball
# global left_side_ball
# global up_side_ball
# global down_side_ball

def random_color(self):
	r =random.randint(0,255) 
	g =random.randint(0,255) 
	b =random.randint(0,255)
	self.color(r,g,b)

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shape("circle")
		self.shapesize(r/10)
		self.color(color)


	def __eq__(self, other):
		return self.xcor() == other.xcor() and self.ycor() == other.ycor() and self.r == other.r and self.dx == other.dx and self.dy == other.dy
			
			
	def move(self,screen_width,screen_height):
		current_x=self.xcor()
		new_x=current_x+self.dx
		current_y=self.ycor()
		new_y=current_y+self.dy
		right_side_ball=new_x+self.r
		left_side_ball=new_x-self.r
		up_side_ball=new_y+self.r
		down_side_ball=new_y-self.r
		self.screen_width=screen_width
		self.screen_height=screen_height
		self.goto(new_x,new_y)
		if (new_x>screen_width) or (new_x<-screen_width):
			self.dx = -self.dx
		if (new_y>screen_height) or (new_y<-screen_height):
			self.dy=-self.dy


# jana=Ball(0,20,3,2,30,"red")
# while True:
# 	jana.move(420,350)
