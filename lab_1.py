#for i in range (2):
#	print("Rahaf Zorba")

# number1 = 4
# print(number1)
# number2 = 2
# print(number2)

# num = [3,2,1]
# for i in num:
# 	print(i)
# 	print(i*2)
# 	#print()
"""
for i in range(2):
	print(i*2)
"""
import turtle
# turtle.goto(100,100)
# this draws a square on the screen
turtle.begin_fill()
turtle.penup()
turtle.goto(100,100)
turtle.pendown()
for i in range(4):
	turtle.forward(100)
	turtle.left(90)
turtle.end_fill()
# this draws a circle on the screen
# for circle in range(5):
# 	turtle.pensize(25)
# 	turtle.color("blue")
# 	turtle.penup()
# 	turtle.goto(-110,-25)
# 	turtle.pendown()
# 	turtle.circle(100)
turtle.mainloop()