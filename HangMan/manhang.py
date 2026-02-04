from graphics import *
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
        self.rectangle = Rectangle(p(topLeftX, topLeftY), p(topLeftX + width, topLeftY + height))
        self.textBox = Text(p(topLeftX + width / 2, topLeftY + height / 2), text)
   
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
        self.circle = Circle(p(centerX, centerY), radius)
        self.textBox = Text(p(centerX, centerY), text)
   
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
        

# Class Uses

    #testButton1 = RectangleButton(50, 300, 200, 100, "Click me!")
    #testButton1.draw(win)

    #testButton2 = CircleButton(500, 300, 100, "Click me!")
    #testButton2.draw(win)


##########################
# Global Vars (Constant) #
##########################


GRID_LINES = [
    Line(p(0, 250), p(1300, 250)),
    Line(p(0, 466), p(1300, 466)),
    Line(p(437, 0), p(437, 250))
]

LETTER_BUTTONS = [
    CircleButton(32, 32, 28, "A"), # Row Won
    CircleButton(94, 32, 28, "B"),
    CircleButton(156, 32, 28, "C"),
    CircleButton(218, 32, 28, "D"),
    CircleButton(280, 32, 28, "E"),
    CircleButton(342, 32, 28, "F"),
    CircleButton(404, 32, 28, "G"),
    CircleButton(32, 94, 28, "H"), # Row Tow
    CircleButton(94, 94, 28, "I"),
    CircleButton(156, 94, 28, "J"),
    CircleButton(218, 94, 28, "K"),
    CircleButton(280, 94, 28, "L"),
    CircleButton(342, 94, 28, "M"),
    CircleButton(404, 94, 28, "N"),
    CircleButton(32, 156, 28, "O"), # Row Tree
    CircleButton(94, 156, 28, "P"),
    CircleButton(156, 156, 28, "Q"),
    CircleButton(218, 156, 28, "R"),
    CircleButton(280, 156, 28, "S"),
    CircleButton(342, 156, 28, "T"),
    CircleButton(404, 156, 28, "U"),
    CircleButton(94, 218, 28, "V"), # Row Door (Smaller)
    CircleButton(156, 218, 28, "W"),
    CircleButton(218, 218, 28, "X"),
    CircleButton(280, 218, 28, "Y"),
    CircleButton(342, 218, 28, "Z")
]

PHRASE_SUBMIT = RectangleButton(1000, 500, 290, 166, "Submit Phrase")
PHRASE_ENTRY = Entry(p(500, 533),100)

HEART = [
    Image(p(500, 70), "./gifs/heart.gif"),
    Image(p(616, 70), "./gifs/heart.gif"),
    Image(p(732, 70), "./gifs/heart.gif"),
    Image(p(500, 179), "./gifs/heart.gif"),
    Image(p(616, 179), "./gifs/heart.gif"),
    Image(p(732, 179), "./gifs/heart.gif"),
]

GALLOW_LINES = [
    Line(p(1025, 245), p(1175, 245)),
    Line(p(1100, 245), p(1100, 10)),
    Line(p(1100, 10), p(950, 10)),
    Line(p(950, 10), p(950, 30))
]

HANG_MAN_PARTS = [
    Circle(p(950, 55), 25), # head
    Line(p(950, 80), p(950, 190)), # body
    Line(p(950, 100), p(1000, 140)), # arm 1
    Line(p(950, 100), p(900, 140)), # arm 2
    Line(p(950, 190), p(1000, 230)), # leg 1
    Line(p(950, 190), p(900, 230)) # leg 2
]

masterphrase = []
displayphrase = []
hint = Text(p(650,350), '')
hint.setSize(18)

livesremaning = 6

REPLAY_BUTTON = RectangleButton(550, 533, 200, 100, "Replay?")

##################
# Helper methods #
##################


# Draws items on the screen the whole time
def InitSetup(graphicsWindow):
    # Line Setup
    for line in GRID_LINES:
        line.draw(graphicsWindow)
    # Hangifyer
    for item in GALLOW_LINES:
        item.draw(graphicsWindow)

# undraws hearts and man and letter buttons. Draws phrase submition button and text box
def PhraseSub(graphicsWindow):
    # Live Graphics
    for item in HEART:
        if item.canvas:
            item.undraw()
    # Hung Man
    for item in HANG_MAN_PARTS:
        if item.canvas:
            item.undraw()
    # Letter Buttonas
    for item in LETTER_BUTTONS:
        if item.getCanvas():
            item.undraw()
    # Phrase Submit Stuff
    PHRASE_SUBMIT.draw(graphicsWindow)
    PHRASE_ENTRY.draw(graphicsWindow)

# Undraw text input and the submit button. Draw hearts and letters. Set lives remaining to 6. Fill in masterPhrase and displayPhrase using text from the text submission. Use display phrase to draw the hint.
def phrasesubmitted(graphicsWindow, text):
    text = text.lower()
    PHRASE_ENTRY.undraw()
    PHRASE_SUBMIT.undraw()
    for item in HEART:
        item.draw(graphicsWindow)
    for item in LETTER_BUTTONS:
        item.draw(graphicsWindow)
    hint.draw(graphicsWindow)
    # filling in master and displayPhrase
    for i in range(len(text)):
        masterphrase.append(text[i])
        if text[i] == ' ':
            displayphrase.append(' ')
        else:
            displayphrase.append('_')
    updayhint()

# Update the hint using what is currently in the displayPhrase
def updayhint():
    currentHint = ""
    for letter in displayphrase:
        currentHint = currentHint + letter + " "
    hint.setText(currentHint)

# Submiting a Guess - the letter button that has 1 letter that will be sent thru this method and fills in maches and updates the hint. If no match is found louse a life
def GuessSub(graphicsWindow, letter):
    global livesremaning
    global displayphrase
    global masterphrase
    letter = letter.lower()
    found = False
    for i in range(len(masterphrase)):
        if(letter == masterphrase[i]):
            displayphrase[i] = letter
            found = True

    if(not found):
        livesremaning -= 1
        HEART[livesremaning].undraw()
        HANG_MAN_PARTS[5 - livesremaning].draw(graphicsWindow)
        if(livesremaning == 0):
            displayphrase = masterphrase
            GameLost(graphicsWindow)

    updayhint()

#
def GameLost(graphicsWindow):
    for item in LETTER_BUTTONS:
        if item.getCanvas():
            item.undraw()
    REPLAY_BUTTON.draw(graphicsWindow)

#
def restarGame(graphicsWindow):
    global livesremaning
    global masterphrase
    global displayphrase
    global hint

    REPLAY_BUTTON.undraw()

    PhraseSub(graphicsWindow)

    livesremaning = 6

    masterphrase = []
    displayphrase = []

    hint.undraw()

    


###################
# Executable code #
###################


# Open Window
win = GraphWin("Hangman", 1300, 700)

InitSetup(win)
  
# Phrase Stuff
PhraseSub(win)


#############
# Main Loop #
#############


while(True):
    mouse = win.checkMouse()
    if(mouse):
    # When we click the submit button, AND there is text inside the entry box, that text gets used as the phrase. the letter buttons, gallows, and hearts appear. The hint appears. The entry box and submit button disappear.
        if(
            PHRASE_SUBMIT.getCanvas() and
            PHRASE_SUBMIT.clickedInside(mouse.getX(),mouse.getY()) and
            PHRASE_ENTRY.getText()        
        ):
            phrasesubmitted(win, PHRASE_ENTRY.getText())

    for item in LETTER_BUTTONS:
        if(
            mouse and
            item.getCanvas() and
            item.clickedInside(mouse.getX(),mouse.getY())
        ):
            GuessSub(win, item.text)
            item.undraw()

    if(
        mouse and
        REPLAY_BUTTON.getCanvas() and
        REPLAY_BUTTON.clickedInside(mouse.getX(),mouse.getY())
    ):
        restarGame(win)