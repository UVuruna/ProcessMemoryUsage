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
    return 'Current usage {:,.{}f} {}: {:.1f}%'.format(memoryUsage,decimal,unit,memoryUsage*100/memory,decimal)

def START():
    global memory,refreshRate,removeRate,currHead,currFrame,lenCurr,highHead,highFrame,lenHigh,highData,unit,unitValue,decimal
    
    GetSettingRETURN = GetSetting(root,SettingScreen,MainScreen,unitsIndex,fontHEAD,FONT,red,blue,UNITS)
    PC,refreshRate,removeRate,currHead,currFrame,lenCurr,highHead,highFrame,lenHigh,highData,unit,unitValue,decimal = GetSettingRETURN
    highHead.config(text=heading_High(removeRate))
    memory = PC*(1024**3/unitsIndex[unit])
    
    update_process()

def update_process():
    UpdateProcess(RESOURCE,currFrame,lenCurr,highFrame,lenHigh,highData,removeRate,decimal,unit,unitValue,heading_Main,currHead)
    root.after(refreshRate, update_process)

SettingScreen = SettingScreenCreate(root,START, FONT,bgColor, unitsIndex,UNITS)

root.mainloop()