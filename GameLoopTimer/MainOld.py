from graphics import *
from time import *
from math import *

###########
# Classes #
###########


class RectangleButton():
    def __init__(self, topLeftX, topLeftY, width, height, text):
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.width = width
        self.height = height
        self.text = text
        self.rectangle = Rectangle(Point(topLeftX, topLeftY), Point(topLeftX + width, topLeftY + height))
        self.textBox = Text(Point(topLeftX + width / 2, topLeftY + height / 2), text)

    def draw(self, graphicsWindow):
        self.rectangle.draw(graphicsWindow)
        self.textBox.draw(graphicsWindow)

    def clickedInside(self, x, y):
        if(
            x > self.topLeftX and
            x < self.topLeftX + self.width and
            y > self.topLeftY and
            y < self.topLeftY + self.height
        ):
            return True
        else:
            return False

    def getCanvas(self):
        return self.rectangle.canvas

    def undraw(self):
        self.rectangle.undraw()
        self.textBox.undraw()

class CircleButton():
    def __init__(self, centerX, centerY, radius, text):
        self.centerX = centerX
        self.centerY = centerY
        self.radius = radius
        self.text = text
        self.circle = Circle(Point(centerX, centerY), radius)
        self.textBox = Text(Point(centerX, centerY), text)

    def draw(self, graphicsWindow):
        self.circle.draw(graphicsWindow)
        self.textBox.draw(graphicsWindow)

    def clickedInside(self, x, y):
        # if the "distance" is smaller than the radius...
        if(
            sqrt((x - self.centerX)**2 + (y - self.centerY)**2) <= self.radius
        ):
            return True
        else:
            return False

    def getCanvas(self):
        return self.circle.canvas

    def undraw(self):
        self.circle.undraw()
        self.textBox.undraw()

class CircleImageButton():
    def __init__(self, centerX, centerY, radius, imageURL):
        self.centerX = centerX
        self.centerY = centerY
        self.radius = radius
        self.imageURL = imageURL
        self.image = Image(Point(centerX, centerY), imageURL)

    def draw(self, graphicsWindow):
        self.image.draw(graphicsWindow)

    def clickedInside(self, x, y):
        # if the "distance" is smaller than the radius...
        if(
            sqrt((x - self.centerX)**2 + (y - self.centerY)**2) <= self.radius
        ):
            return True
        else:
            return False

    def getCanvas(self):
        return self.image.canvas

    def undraw(self):
        self.image.undraw()


###################
# Global Varubles #
###################


cookiesPerClick = 1
cookies = 0
grandmas = 0

cookieButton = CircleImageButton(200, 200, 150, "./images/cookie.png")
grandmabuying = RectangleButton(800, 50, 400, 100, "Click to buy a Grandma")
cookieDisplay = Text(Point(1000, 300), "0")


##################
# Helper Methods #
##################


def update(seconds):
    mouse = win.checkMouse()

    global cookiesPerClick
    global grandmas
    global cookies

    cookies = cookies + grandmas * seconds

    if mouse:
        if cookieButton.clickedInside(mouse.getX(), mouse.getY()):
            cookies = cookies + 1

        if (grandmabuying.clickedInside(mouse.getX(), mouse.getY()) and cookies >= 100 ):
            grandmas = grandmas + 1
            cookies = cookies - 100

    displayCookies = floor(cookies)
    cookieDisplay.setText(str(displayCookies))

def initsetup(graphicswindow):
    cookieButton.draw(graphicswindow)
    grandmabuying.draw(graphicswindow)
    cookieDisplay.draw(graphicswindow)


###################
# Executable code #
###################


win = GraphWin("Cookie Clicker (not for resale",1300 ,700)

initsetup(win)

lastTimestamp = time_ns()

while True:
    curentTimestamp = time_ns()
    secondsElapsed = (curentTimestamp - lastTimestamp) / 1000000000
    lastTimestamp = curentTimestamp

    update(secondsElapsed)