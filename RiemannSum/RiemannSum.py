
import math


def getValueOfY(x: float) -> float:
    return ((-x**2) + 1)**0.5

def riemannSum(numPoints: int):
    delta_x = 2/numPoints
    position = -1
    total = 0
    while(position <= 1):
        total += (getValueOfY(position)*delta_x)
        position+=delta_x

    pi = total *2
    output = "Approximation of Pi: " + str(pi) + " Deviation: " + str(pi - math.pi)
    print(output)

riemannSum(int(input("Enter number of Rectangles to sum: ")))
