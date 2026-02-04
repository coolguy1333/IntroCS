from graphics import *


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

# make sure your width and height match the width and height of the image you include
class RectangleImageButton():
    def __init__(self, topLeftX, topLeftY, width, height, imageURL):
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.width = width
        self.height = height
        self.imageURL = imageURL
        self.image = Image(Point(topLeftX + width / 2, topLeftY + height / 2), imageURL)

    def draw(self, graphicsWindow):
        self.image.draw(graphicsWindow)

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
        return self.image.canvas

    def undraw(self):
        self.image.undraw()

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

# the image should have a square height and width, double the planned radius
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

# each upgrade is a 500x100 rectangle a 500x100 background is used the upgrade image should be a 90x90 file
class TrainUpgrade():
    def __init__(self, topLeftX, topLeftY, upgradeURL, startCost, typeText, VarToMesure, costMulti):
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.width = 500
        self.height = 100
        self.upgradeURL = upgradeURL
        self.backgroundURL = "./images/upgrade_background.png"
        self.backgroundImage = Image(Point(topLeftX + self.width / 2, topLeftY + self.height / 2), self.backgroundURL)
        self.upgradeImage = Image(Point(topLeftX + 50, topLeftY + 50), self.upgradeURL)
        self.startCost = startCost
        self.nextCost = startCost
        self.typeText = typeText
        self.var = VarToMesure
        self.costMulti = costMulti
        self.numOwned = 0
        self.costText = Text(Point(topLeftX + 225, topLeftY + 16.5), "Cost:")
        self.costText.setSize(18)
        self.ownedText = Text(Point(topLeftX + 225, topLeftY + 49.5), "Level:")
        self.ownedText.setSize(18)
        self.CPSText = Text(Point(topLeftX + 225, topLeftY + 82.5), str(self.typeText))
        self.CPSText.setSize(18)
        self.costLable = Text(Point(topLeftX + 375, topLeftY + 16.5), "$" + str(self.nextCost))
        self.costLable.setSize(18)
        self.ownedLable = Text(Point(topLeftX + 375, topLeftY + 49.5), str(self.numOwned))
        self.ownedLable.setSize(18)
        self.CPSLable = Text(Point(topLeftX + 375, topLeftY + 82.5), str(self.var))
        self.CPSLable.setSize(18)

    def draw(self, graphicsWindow):
        self.backgroundImage.draw(graphicsWindow)
        self.upgradeImage.draw(graphicsWindow)
        self.costText.draw(graphicsWindow)
        self.costLable.draw(graphicsWindow)
        self.ownedText.draw(graphicsWindow)
        self.ownedLable.draw(graphicsWindow)
        self.CPSText.draw(graphicsWindow)
        self.CPSLable.draw(graphicsWindow)

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

    def purchase(self):
        self.numOwned = self.numOwned + 1
        self.nextCost = round(self.nextCost * self.costMulti)
        self.ownedLable.setText(str(self.numOwned))
        self.costLable.setText("$" + str(self.nextCost))

    def undraw(self):
        self.backgroundImage.undraw()
        self.upgradeImage.undraw()
        self.costText.undraw()
        self.costLable.undraw()
        self.ownedText.undraw()
        self.ownedLable.undraw()
        self.CPSText.undraw()
        self.CPSLable.undraw()

class FPSCounter:
    def __init__(self, averaging_window=30):
        self.frametimes = []
        self.averaging_window = averaging_window

    def update(self):
        self.frametimes.append(time.time())
        if len(self.frametimes) > self.averaging_window:
            self.frametimes.pop(0)

    def get_fps(self):
        if len(self.frametimes) < 2:
            return 0.0
        else:
            time_elapsed = self.frametimes[-1] - self.frametimes[0]
            return len(self.frametimes) / time_elapsed

#class Track():
    #def __init__(self, Point(x, y), directions):
        #self.center = Point(x, y)
        #self.directions = directions

#class TrackMap():
    #def __init__(self, map):
        #self.map = map


