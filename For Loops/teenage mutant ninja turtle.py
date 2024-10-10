import turtle
jon = turtle.Turtle()
jon.speed(10)
numSides = 8
sideLength = 50
numShapes = 20

def drawNgonSpiral(jon, numSides, sideLength,numShapes):
    for i in range(sideLength*numShapes):
        jon.lt(360/numSides)
        jon.forward(sideLength+i)
        jon.lt(i)


drawNgonSpiral(jon, numSides, sideLength,numShapes)

turtle.done()