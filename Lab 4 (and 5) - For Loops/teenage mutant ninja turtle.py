import turtle
jon = turtle.Turtle()
jon.speed(1)


squareSize = 100
length = 5

def drawSquare(jon, squareSize):
    for i in range(4):
        jon.forward(squareSize)
        jon.rt(90)


def drawRow(jon, length, squareSize):
    for i in range(length):
        drawSquare(jon, squareSize)
        jon.forward(100)



drawRow(jon, length, squareSize)


jon.done()