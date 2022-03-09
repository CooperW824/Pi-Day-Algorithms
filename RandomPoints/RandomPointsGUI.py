
import math
import tkinter as tk
from tkinter import messagebox
import random as rand

class app:

    def __init__(self):
        self.root =  tk.Tk()

        self.root.title("Approximating Pi using Random Points")

        self.root.geometry("400x425")

        self.label1 = tk.Label(self.root, text="Enter a number of points to estimate Pi")
        self.label1.pack()

        self.textInput = tk.Text(self.root, height=1, width=40)
        self.textInput.pack()

        self.startBtn = tk.Button(self.root, text="Click Here to Start: ", command=self.estimatePi)
        self.startBtn.pack()
        

        self.canvas = tk.Canvas(self.root, background="#d3ddfa", width=300, height=300)
        self.canvas.pack()

        self.canvas.create_oval(2,2,300,300,outline="#0000ff")
        self.canvas.create_rectangle(2,2,300,300, outline="#0000ff")

        self.outputLabel = tk.Label(self.root, text="Points tested:  \nApproximation of Pi: " )
        self.outputLabel.pack()

        self.root.mainloop()

    def isInCircle(self, x: float, y: float)-> bool:
         return math.sqrt(x**2 + y**2) < 1

    def estimatePi(self):
        numPoints = self.textInput.get(1.0, "end-1c")
        try:
            numPoints = int(numPoints)
        except:
            messagebox.showerror("Error", "Error: Invalid input for Number of points")

        pointsInCircle = 0
        pointsOutCircle = 0

        for i in range(1, numPoints+1):

            x = rand.random()
            y = rand.random()
            inCircle = self.isInCircle(x, y)

            if inCircle:
                pointsInCircle+=1
                if i%100==0:
                    self.canvas.create_oval(x*300, y*300, x*300+10, y*300+10, fill="#33FF00")
            else:
                pointsOutCircle += 1
                if i%100==0:
                    self.canvas.create_oval(x*300, y*300, x*300+10, y*300+10, fill="#FF0000")

        pi = (pointsInCircle*4)/numPoints

        outputStr = "Points tested: " + str(i) + "\nApproximation of Pi: " + str(pi) + "\nDeviation: " + str(pi - math.pi)
        self.outputLabel.configure(text=outputStr)



if __name__ == "__main__":
    process = app()
