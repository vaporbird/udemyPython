from turtle import *
s = Screen()
t = Turtle()

colors = ["red", "green", "blue", "brown", "black", "purple", "pink", "orange"]

for i in range (3,11):
	rotation = 360/i
	for _ in range (i) :
		t.color(colors[i-3])
		t.fd(100)
		t.right(rotation)
	
