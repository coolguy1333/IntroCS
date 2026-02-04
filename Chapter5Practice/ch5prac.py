from turtle import *


#creates a 800 by 600 px window
setup(800,600)

# #of pixles wide the line is 
width(10)

#sets the color of the line
color("blue")

#makes a filled in equallatral triangle
begin_fill()
forward(50)
right(120)
forward(50)
right(120)
forward(50)
right(120)
end_fill()

#Pen Up
penup()

#goes 200 back
back(200)

#puts pen down
pendown()

#makes a filled in equallatral triangle
begin_fill()
forward(50)
right(120)
forward(50)
right(120)
forward(50)
right(120)
end_fill()

#Updates the screen
update()

#keeps the screen open
done()