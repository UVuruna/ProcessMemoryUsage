import tkinter as tk
from CalculatingFunctions import *
from Window import *

RESOURCE = 'memory_info'

root = tk.Tk()
root.configure(bg=bgColor)
root.title("Top Memory Processes")

def headingMain(memoryUsage):
    return 'Current Memory usage {:,.{}f} {}:\t\n\n'.format(memoryUsage,formatNum,unit)
headingHigh = f'Highest Memory usage {unit} (last {int(highMaxTime/60)} min):\t\n\n'
labelFont = defineFont('Arial',13)

def showOptionsUnit():
    global unit,processNum,highNum,cpuMax,formatNum,unitValue,redScreen,blueScreen
    
    unit,processNum,highNum,cpuMax,formatNum,unitValue,redScreen,blueScreen = showOptions(root,MainScreen,unitsIndex,SecondScreen,labelFont,red,blue,textColor,True)
    update_process()

def update_process():
    UpdateProcess(processNum,headingMain,formatNum,highNum,cpuMax,highMaxTime,headingHigh,redScreen,blueScreen,RESOURCE,unit,unitValue)
    root.after(refreshRate, update_process)

MainScreen = MainScreenCreate(root,labelFont,showOptionsUnit,unitsIndex,bgColor,units=True)

root.mainloop()