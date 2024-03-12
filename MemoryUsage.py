import tkinter as tk
from CalculatingFunctions import *
from Window import *

root = tk.Tk()
root.configure(bg=bgColor)
root.title("Top Memory Processes")

UNITS = True
RESOURCE = 'memory_info'
fontHEAD = defineFont('Arial',14)
FONT = defineFont('Arial',13)

def heading_Main(memoryUsage):
    return 'Current Memory usage {:,.{}f} {}:'.format(memoryUsage,decimal,unit)
def heading_High():
    return f'Highest Memory usage {unit} (last {int(highMaxTime/60)} min):'

def START():
    global currHead,currFrame,lenCurr,highHead,highFrame,lenHigh,highData,unit,unitValue,decimal
    
    showOptionsRETURN = showOptions(root,MainScreen,SecondScreen,unitsIndex,fontHEAD,FONT,red,blue,UNITS)
    currHead,currFrame,lenCurr,highHead,highFrame,lenHigh,highData,unit,unitValue,decimal = showOptionsRETURN
    highHead.config(text=heading_High())
    update_process()

def update_process():
    UpdateProcess(RESOURCE,currFrame,lenCurr,highFrame,lenHigh,highData,highMaxTime,decimal,unit,unitValue,heading_Main,currHead)
    root.after(refreshRate, update_process)

MainScreen = MainScreenCreate(root,START, FONT,bgColor, unitsIndex,UNITS)

root.mainloop()