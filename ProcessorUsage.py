import tkinter as tk
from tkinter import font
from CalculatingFunctions import *
from Window import *

RESOURCE = 'cpu_percent'
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
root.title("Top CPU Processes")

labelFont = font.Font(family="Arial", size=13, weight="normal")
unitsIndex = {'KB':1024,'MB':1024**2,'GB':1024**3}

headingHigh = f'Highest CPU usage % (last {int(highMaxTime/60)} min):\t\n\n'
headingMain = 'Current CPU usage %:\t\n\n'

def showOptionsUnit():
    global unit,processNum,highNum,cpuMax,formatNum,unitValue,redScreen,blueScreen
    
    unit,processNum,highNum,cpuMax,formatNum,unitValue,redScreen,blueScreen = showOptions(root,MainScreen,unitsIndex,SecondScreen,labelFont,red,blue,textColor,False)
    update_process()

def update_process():
    UpdateProcess(processNum,headingMain,formatNum,highNum,cpuMax,highMaxTime,headingHigh,redScreen,blueScreen,RESOURCE,unit,unitValue)
    root.after(refreshRate, update_process)

MainScreen = MainScreenCreate(root,labelFont,showOptionsUnit,unitsIndex,bgColor,units=False)

root.mainloop()