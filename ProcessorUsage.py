import tkinter as tk
from CalculatingFunctions import *
from Window import *


root = tk.Tk()
root.configure(bg=bgColor)
root.title("Top CPU Processes")

UNITS = False
RESOURCE = 'cpu_percent'
fontHEAD = defineFont('Arial',14)
FONT = defineFont('Arial',13)

def heading_Main():
    return 'Current CPU usage %:'
def heading_High():
    return f'Highest CPU usage % (last {int(highMaxTime/60)} min):'

def START():
    global currHead,currFrame,lenCurr,highHead,highFrame,lenHigh,highData,unit,unitValue,decimal

    showOptionsRETURN = showOptions(root,MainScreen,SecondScreen,unitsIndex,fontHEAD,FONT,red,blue,UNITS)
    currHead,currFrame,lenCurr,highHead,highFrame,lenHigh,highData,unit,unitValue,decimal = showOptionsRETURN
    highHead.config(text=heading_High())
    currHead.config(text=heading_Main())

    update_process()

def update_process():
    UpdateProcess(RESOURCE,currFrame,lenCurr,highFrame,lenHigh,highData,highMaxTime,decimal,unit,unitValue)
    root.after(refreshRate, update_process)

MainScreen = MainScreenCreate(root,START, FONT,bgColor, unitsIndex,UNITS)

root.mainloop()