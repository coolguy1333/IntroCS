from math import *
"""
Functions and Procedures are premade blocks of code meant to be reused. This is similar to a common formula you would learn in a math class. The area of a circle A = pi * r^2 is a function, it relates Area to Radius for a circle.
"""
def circleArea(radius):
    print(pi * radius**2)

def triangleArea(base, height):
    print(.5 * base * height)

circleArea(5)
triangleArea(10, 2)

"""
Python has built in functions we'll use pretty often. One of the more common ones when we first start programming is input() so that we can take text from the user.

The input function RETURNS the answered text. That means it saves it and spits it back to us so we can use it how we need to.
"""
name = input("What is your name?\n")
print("Nice to meet you, " + name + ".")


def convertFtoC(f):
    # subtract 32, then multiply by 5/9
    return (f - 32) * (5.0 / 9.0)
    # this function won't print anything, instead it sends the value back
def convertCtoF(c):
    return (9.0 / 5.0) * c + 32

tempF = float(input("Nice to meet you, I'm from a not America country, so we don't use the same temperature. What's the temperature in Fahrenheit for you right now?"))
print("Wow, that's pretty cold! For me, that would be " + str(convertFtoC(tempF)) + " degrees celsius.")

# this function should calculate and return the slope of a line that goes through the points (x1, y1) and (x2, y2)
def calcslope(x1, y1, x2, y2):
    return ((x1 - x2)/(y1 -y2))

x1 = float(input("What is your first x cordnit:"))
y1 = float(input("What is your first y cordnit:"))
x2 = float(input("What is your second x cordnit:"))
y2 = float(input("What is your second y cordnit:"))

print("Your slope is:" + str(calcslope(x1, y1, x2, y2)))