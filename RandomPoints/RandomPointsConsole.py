
import math
import random as rand
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)




def isInCircle(x: float, y: float)-> bool:
    return math.sqrt(x**2 + y**2) < 1
        

def estimatePi(numPoints):

    pointsInCircle = 0
    pointsOutCircle = 0

    for i in range(1, numPoints+1):

        x = rand.uniform(-1.0, 1.0)
        y = rand.uniform(-1.0, 1.0)
        inCircle = isInCircle(x, y)

        if inCircle:
            pointsInCircle +=1
            #self.canvas.create_oval(x*300, y*300, x*300+10, y*300+10, fill="#33FF00")
        else:
            pass
            #self.canvas.create_oval(x*300, y*300, x*300+10, y*300+10, fill="#FF0000")

        pi = (pointsInCircle*4)/i

        outputStr = "Points tested: " + str(i) + "\nApproximation of Pi: " + str(pi) + " Deviation: " + str(pi - math.pi)

        print(outputStr)
        clearConsole()
        

    

estimatePi(int(input("Enter Number of Points to test: ")))

