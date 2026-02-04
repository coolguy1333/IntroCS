from turtle import *


#creates a 800 by 600 px window
setup(800,600)

#speeed
speed(99999999999999999)

# #of pixles wide the line is 
width(10)

#Pen Up
penup()

#goes 200 back
back(200)

#puts pen down
pendown()

#L
left(90)
fd(100)
bk(100)
right(90)
fd(50)

#Pen Up
penup()

#goes 25 forward
forward(25)

#puts pen down
pendown()

#A
left(90)
fd(100)
right(90)
fd(50)
right(90)
fd(50)
right(90)
fd(50)
right(180)
fd(50)
right(90)
fd(50)
left(90)

#Pen Up
penup()

#goes 25 forward
forward(25)

#puts pen down
pendown()

#W
left(90)
fd(100)
bk(100)
right(90)
fd(25)
left(90)
fd(50)
right(90)
fd(20)
right(90)
fd(50)
left(90)
fd(20)
left(90)
fd(100)
bk(100)
right(90)

#Pen Up
penup()

#goes 25 forward
forward(25)

#puts pen down
pendown()

#S
fd(50)
left(90)
fd(50)
left(90)
fd(50)
right(90)
fd(50)
right(90)
fd(50)

#Pen Up
penup()

#goes 25 forward
forward(25)

#puts pen down
pendown()

#O
fd(50)
right(90)
fd(100)
right(90)
fd(50)
right(90)
fd(100)
right(90)
fd(50)

#Pen Up
penup()

#goes 25 forward
forward(25)

#puts pen down
pendown()

#N
right(90)
fd(100)
bk(100)
left(30)
fd(115)
left(180-30)
fd(100)

#Updates the screen
update()

#keeps the screen open
done()