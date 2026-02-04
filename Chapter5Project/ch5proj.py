# Lab05Ast.py
# "Turtle Graphics Shapes"
# This is the student, starting version of Lab 05A.


from turtle import * 
from time import sleep

setup(1300,700)

speed(9959894378589438534)

####################      
#  Thick Initials  #
####################

width(15)
left(90)
fd(100)
bk(100)
right(90)
fd(50)
penup()
fd(50)
pendown()
left(90)
fd(100)
right(90)
fd(50)
bk(50)
left(90)
bk(40)
right(90)
fd(35)

sleep(1)
reset()
speed(9959894378589438534)
##############
#  Pentagon  #
##############

forward(100)
right(72)
forward(100)
right(72)
forward(100)
right(72)
forward(100)
right(72)
forward(100)
right(72)



sleep(1)
reset()
speed(9959894378589438534)
####################
#  Double Diamond  #
####################

left(45)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(120)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)

sleep(1)
reset()
speed(9959894378589438534)
##################
#  8 Point Star  #
##################

forward(100)
right(135)
forward(100)
right(135)
forward(100)
right(135)
forward(100)
right(135)
forward(100)
right(135)
forward(100)
right(135)
forward(100)
right(135)
forward(100)
right(135)

sleep(1)
reset()
speed(9959894378589438534)
#######################
#  Box in Box in Box  #
#######################

forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
penup()
goto(150,-50)
pendown()
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
penup()
goto(125,-75)
pendown()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

sleep(1)
reset()
speed(9959894378589438534)
#####################
#  Solid Staircase  #
#####################

begin_fill()
forward(20)
right(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)
left(270)
forward(20*5)
right(90)
forward(20*5)
end_fill()

sleep(1)
reset()
speed(9959894378589438534)
################    
#  Weird Face  #
################

goto(0,-20)
goto(20,-60)
goto(120,-60)
goto(140,-20)
goto(140,0)
goto(120,-20)
goto(20,-20)
goto(0,0)
penup()
goto(10,30)
pendown()
fd(40)
left(120)
fd(40)
left(120)
fd(40)
left(120)
penup()
goto(90,30)
pendown()
fd(40)
left(120)
fd(40)
left(120)
fd(40)

sleep(1)
reset()
speed(9959894378589438534)
#######################
#  Gold 5 Point Star  #
#######################

color("gold")
begin_fill()
penup()
setpos(-90,30)
pendown()
for i in range(5):
    forward(200)
    right(144)
end_fill()

sleep(1)
reset()
speed(9959894378589438534)
##########################
# Thick Rainbow Hexagon  #
##########################

pensize(15)
color("red")
forward(100)
right(60)
color("orange")
forward(100)
right(60)
color("yellow")
forward(100)
right(60)
color("green")
forward(100)
right(60)
color("blue")
forward(100)
right(60)
color("purple")
forward(100)
right(60)


sleep(1)
reset()
speed(9959894378589438534)
####################################      
#  Half Thick Half Thin Snowflake  #
####################################

pensize(25)
right(90)
for i in range(6):
    fd(100)
    bk(100)
    right(60)
pensize(5)
right(30)
for i in range(6):
    fd(75)
    bk(75)
    right(60)

sleep(1)
reset()
speed(9959894378589438534)
#####################      
#  Thinning Spiral  #
#####################

dasway = 350
size = 32
for i in range(16):
    size = size - 2
    dasway = dasway - 20
    pensize(size)
    fd(dasway)
    right(90)

sleep(1)
reset()
speed(9959894378589438534)
###########
#  House  #
###########

width(20)
color("gold")
penup()
goto(-300,-200)
pendown()
goto(300,-200)
goto(300,100)
goto(0,250)
goto(-300,100)
goto(-300,-200)
goto(-250,-200)
goto(-250,0)
goto(-150,0)
goto(-150,-200)
penup()
goto(-50,0)
pendown()
fd(300)
right(90)
fd(125)
right(90)
fd(300)
right(90)
fd(125)
right(90)
fd(150)
right(90)
fd(125)
right(90)
fd(150)
right(90)
fd(63)
right(90)
fd(300)
penup()
goto(-300,100)
pendown()
goto(300,100)
penup()
goto(-165,-100)

update()
done()