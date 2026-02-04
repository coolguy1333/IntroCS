# Lab08Ast.py
# "Repetition with Turtle Graphics"
# This is the student, starting version of Lab 08A.
# After completing each shape, student need to "un-comment"
# the 4 commands which follow before they start the next shape.


from turtle import * 
from time import sleep

setup(1300,700)
tracer(0,0) 
speed(0)

#######################
#  Solid Red Octagon  #
#######################

hideturtle()
color("red")
begin_fill()
for i in range(8):
    forward(120)
    left(45)
end_fill()



update()
sleep(10)
reset()
tracer(0,0)


###################
#  12 Point Star  #
###################

hideturtle()
color("black")
for i in range(12):
    forward(120)
    right(150)



update()
sleep(1)
reset()
tracer(0,0)


###############
#  Plus Sign  #
###############

hideturtle()
color("black")
for i in range(8):
    forward(100)
    right(90)
    forward(50)
    right(90)
    forward(100)
    left(90)



update()
sleep(1)
reset()
tracer(0,0)


###############
#  Snowflake  #
###############

hideturtle()
color("black")
width(5)
for i in range(18):
    forward(200)
    backward(200)
    right(20)
width(1)
right(10)
for i in range(18):
    forward(150)
    backward(150)
    right(20)



update()
sleep(1)
reset()
tracer(0,0)


############
#  Circle  #
############

hideturtle()
circle(100)



update()
sleep(1)
reset()
tracer(0,0)


#############
#  Zig-Zag  #
#############

hideturtle()
penup()
goto(-625,-300)
pendown()
for i in range(12):
    left(90)
    forward(500)
    right(90)
    forward(50)
    right(90)
    forward(500)
    left(90)
    forward(50)



update()
sleep(1)
reset()
tracer(0,0)


##################
#  Cool Pattern  #
##################

hideturtle()
for i in range(36):
    forward(150)
    right(50)




update()
sleep(1)
reset()
tracer(0,0)


##########################
#  Flower of 10 Squares  #
##########################

hideturtle()
for i in range(12):
    for j in range(4):
        forward(100)
        right(90)
    right(36)



update()
sleep(1)
reset()
tracer(0,0)


##########################
#  Flower of 12 Circles  #
##########################

hideturtle()
for i in range(12):
    circle(100)
    right(30)



update()
sleep(1)
reset()
tracer(0,0)


##################################
#  Comet a.k.a. Thickening Line  #
##################################

hideturtle()
penup()
goto(-625,0)
pendown()
for i in range(1200):
    forward(1)
    width(i/10)



update()
sleep(1)
reset()
tracer(0,0)


################
#  Box Spiral  #
################

hideturtle()
forwardness = 10
for i in range(25):
    forwardness = forwardness+10
    forward(forwardness)
    right(90)



update()
sleep(1)
reset()
tracer(0,0)


##################
#  Round Spiral  #
##################

hideturtle()
for i in range(3600):
    circle(10+(i/20),.5)



update()
done()