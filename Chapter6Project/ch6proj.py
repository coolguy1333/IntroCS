# Lab06Bst.py
# "The Graphics Library Program"
# This is the student, starting version of Lab 06B.

     
from Graphics import *

beginGrfx(1300,700)

# Substitute your own name here.
drawHeading("Lawson Fingland","6B")
    
# DRAW CUBE
drawRectangle(50, 100, 150, 200)
drawRectangle(100, 150, 200, 250)
drawLine(50, 100, 100, 150)
drawLine(150, 100, 200, 150)
drawLine(50, 200, 100, 250)
drawLine(150, 200, 200, 250)

# DRAW TARGET
fillCircle(500,200,100)
color("#FFFFFF")
fillCircle(500,200,80)
color("blue")
fillCircle(500,200,60)
color("red")
fillCircle(500,200,40)
color("yellow")
fillCircle(500,200,20)

# DRAW 7-SIDED DESIGN
color("black")
fillRegularPolygon(800,200,100,7)
color("#FFFFFF")
fillStar(800,200,100,7)
color("black")
drawBurst(800,200,100,7)

# DRAW STOPLIGHT
fillRectangle(1150,75,1250,375)
fillRectangle(1195,375,1205,1400)
color("red")
fillCircle(1200,125,40)
color("yellow")
fillCircle(1200,225,40)
color("green")
fillCircle(1200,325,40)

# DRAW JPIIHS
color("black")
#J
drawBigPoint(50,600)
drawBigPoint(50,620)
drawBigPoint(70,620)
drawBigPoint(90,620)
drawBigPoint(90,600)
drawBigPoint(90,580)
drawBigPoint(90,560)
drawBigPoint(90,540)
drawBigPoint(90,520)
#P
drawBigPoint(140,620)
drawBigPoint(140,600)
drawBigPoint(140,580)
drawBigPoint(140,560)
drawBigPoint(140,540)
drawBigPoint(140,520)
drawBigPoint(160,520)
drawBigPoint(180,520)
drawBigPoint(180,540)
drawBigPoint(180,560)
drawBigPoint(160,560)
drawBigPoint(140,560)
#II
drawBigPoint(230,520)
drawBigPoint(250,520)
drawBigPoint(270,520)
drawBigPoint(290,520)
drawBigPoint(310,520)

drawBigPoint(230,620)
drawBigPoint(250,620)
drawBigPoint(270,620)
drawBigPoint(290,620)
drawBigPoint(310,620)

drawBigPoint(250,600)
drawBigPoint(250,580)
drawBigPoint(250,560)
drawBigPoint(250,540)

drawBigPoint(290,600)
drawBigPoint(290,580)
drawBigPoint(290,560)
drawBigPoint(290,540)
#H
drawBigPoint(360,620)
drawBigPoint(360,600)
drawBigPoint(360,580)
drawBigPoint(360,560)
drawBigPoint(360,540)
drawBigPoint(360,520)

drawBigPoint(400,620)
drawBigPoint(400,600)
drawBigPoint(400,580)
drawBigPoint(400,560)
drawBigPoint(400,540)
drawBigPoint(400,520)

drawBigPoint(380,570)
#S
drawBigPoint(500,620)
drawBigPoint(500,600)
drawBigPoint(500,580)

drawBigPoint(450,560)
drawBigPoint(450,540)
drawBigPoint(450,520)

drawBigPoint(490,620)
drawBigPoint(470,620)
drawBigPoint(450,620)

drawBigPoint(500,520)
drawBigPoint(480,520)
drawBigPoint(460,520)

drawBigPoint(500,570)
drawBigPoint(490,570)
drawBigPoint(470,570)
drawBigPoint(450,570)

# DRAW SMILEY FACE
drawOval(600,500,75,125)
drawArc(600,525,60,25,90,270)
drawArc(560,450,20,10,270,90)
drawArc(640,450,20,10,270,90)
drawCircle(640,460,15)
drawCircle(560,460,15)
drawPoint(640,460)
drawPoint(560,460)

# DRAW WEIRD TRIANGLE
drawPolygon([1000,400,900,650,1100,650])
drawLine(1000,400,1000,650)
drawLine(950,525,1100,650)
drawLine(1050,525,900,650)



endGrfx()