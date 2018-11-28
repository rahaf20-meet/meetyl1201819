from turtle import *
import random

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
ball1=(10, "red", 0)
ball2=(20, "yellow", 5)


def check_collision(ball1, ball2):
	D = math.sqrt(math.pow((x2-x1),2)  + math.pow((y2-y1),2))

