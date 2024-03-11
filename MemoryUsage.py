import tkinter as tk
from tkinter import font
from CalculatingFunctions import *
from Window import *

RESOURCE = 'memory_info'
processNum = int()      # rows
highNum= int()          # rows
unit = str()
highMaxTime = 3960      # sec
refreshRate = 1333      # ms

red = '#FFE2E2'
blue = '#E2F1FF'
bgColor = '#ECF5F9'
textColor = "#060606"

root = tk.Tk()
root.configure(bg=bgColor)
root.title("Top Memory Processes")

labelFont = font.Font(family="Arial", size=13, weight="normal")
unitsIndex = {'KB':1024,'MB':1024**2,'GB':1024**3}

def headingMain(memoryUsage):
    return 'Current Memory usage {:,.{}f} {}:\t\n\n'.format(memoryUsage,formatNum,unit)
headingHigh = f'Highest Memory usage {unit} (last {int(highMaxTime/60)} min):\t\n\n'

def showOptionsUnit():
    global unit,processNum,highNum,cpuMax,formatNum,unitValue,redScreen,blueScreen
    
    unit,processNum,highNum,cpuMax,formatNum,unitValue,redScreen,blueScreen = showOptions(root,MainScreen,unitsIndex,SecondScreen,labelFont,red,blue,textColor,True)
    update_process()

def update_process():
    UpdateProcess(processNum,headingMain,formatNum,highNum,cpuMax,highMaxTime,headingHigh,redScreen,blueScreen,RESOURCE,unit,unitValue)
    root.after(refreshRate, update_process)

MainScreen = MainScreenCreate(root,labelFont,showOptionsUnit,unitsIndex,bgColor,units=True)

root.mainloop()