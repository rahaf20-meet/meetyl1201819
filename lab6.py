
import turtle
import random
from turtle import Turtle
turtle.colormode(255)

class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")
	def random_color(self):
		R = random.randrange(0, 257, 10)
		B = random.randrange(0, 257, 10)
		G = random.randrange(0, 257, 10)

		self.color(R, G, B)
square1 = Square(3)

square1.random_color()

class hexagon(Square):
	
turtle.mainloop()

