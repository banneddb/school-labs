import turtle
jon = turtle.Turtle()
jon.speed(1)


squareSize = 150

def drawSquare(jon, squareSize):
    for i in range(4):
        jon.forward(squareSize)
        jon.rt(90)


drawSquare(jon, squareSize)

turtle.done()