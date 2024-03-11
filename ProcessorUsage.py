import tkinter as tk
from CalculatingFunctions import *
from Window import *

RESOURCE = 'cpu_percent'

root = tk.Tk()
root.configure(bg=bgColor)
root.title("Top CPU Processes")

headingMain = 'Current CPU usage %:\t\n\n'
headingHigh = f'Highest CPU usage % (last {int(highMaxTime/60)} min):\t\n\n'
labelFont = defineFont('Arial',13)

def showOptionsUnit():
    global unit,processNum,highNum,cpuMax,formatNum,unitValue,redScreen,blueScreen
    
    unit,processNum,highNum,cpuMax,formatNum,unitValue,redScreen,blueScreen = showOptions(root,MainScreen,unitsIndex,SecondScreen,labelFont,red,blue,textColor,False)
    update_process()

def update_process():
    UpdateProcess(processNum,headingMain,formatNum,highNum,cpuMax,highMaxTime,headingHigh,redScreen,blueScreen,RESOURCE,unit,unitValue)
    root.after(refreshRate, update_process)

MainScreen = MainScreenCreate(root,labelFont,showOptionsUnit,unitsIndex,bgColor,units=False)

root.mainloop()