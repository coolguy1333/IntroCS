# Lab08Bst.py
# "Repetition With Traditional Graphics"
# This is the student, starting version of Lab 08B.


from Graphics import *

beginGrfx(1300,700)

# Substitute your own name here.
drawHeading("Lawson Fingland","8B")

# Draw Grid
drawLine(325,50,325,700)
drawLine(650,50,650,700)
drawLine(975,50,975,700)
drawLine(1300,50,1300,700)
drawLine(0,375,1300,375)
drawLine(0,700,1300,700)

# Draw Red Horizontal Lines
setColor("red")
x1 = 0
y1 = 55
x2 = 325
y2 = 55
for i in range(32):
   drawLine(x1,y1,x2,y2)
   y1 += 10
   y2 += 10


# Draw Blue Vertical Lines
setColor("blue")
y1 = 50
x1 = 330
y2 = y1+325
x2 = x1
for i in range(32):
   drawLine(x1,y1,x2,y2)
   x1 += 10
   x2 += 10

# Draw Magenta Diagonal Dots
setColor("magenta")
x = 660
y = 360
drawPoint(660, 360)
for i in range(30):
   x += 10
   y -= 10
   drawPoint(x,y)

# Draw Green Concentric Circles
color("green")
rads1 = 300
for i in range(15):
   drawCircle(1137.5,212.5,rads1/2)
   rads1 -= 25

# Draw Purple Concentric Ovals
color("purple")
rads2 = 300
for i in range(15):
   drawOval(162.5,537.5,rads2/3,rads2/2)
   rads2 -= 25

# Draw Brown Concentric Squares
color("brown")
size1 = 320
for i in range(15):
   drawRegularPolygon(487.5,537.5,size1/1.5,4)
   size1 -= 25
  
# Draw Black Concentric Regular Polygons
color("black")
size2 = 320
sides = 10
for i in range(8):
   drawRegularPolygon(812.5,537.5,size2/2,sides)
   size2 -= 35
   sides -= 1
  
# Draw Gold Sphere
color("gold")
xrad = 150
yrad = 150
for i in range(30):
   drawArc(1137.5,537.5,xrad,150,0,180)
   drawArc(1137.5,537.5,150,yrad,270,90)
   xrad -= 10
   yrad -= 10
   if xrad == 0:
      xrad -= 10
      yrad -= 10

endGrfx()