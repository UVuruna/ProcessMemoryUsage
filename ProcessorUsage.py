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

def heading_Main(percent):
    return f'Current usage {percent:,.1f}% / {cpu}%'

def START():
    global cpu,refreshRate,removeRate,currHead,currFrame,lenCurr,highHead,highFrame,lenHigh,highData,unit,unitValue,decimal
    GetSettingRETURN = GetSetting(root,SettingScreen,MainScreen,unitsIndex,fontHEAD,FONT,red,blue,UNITS)
    PC,refreshRate,removeRate,currHead,currFrame,lenCurr,highHead,highFrame,lenHigh,highData,unit,unitValue,decimal = GetSettingRETURN
    cpu = PC*100

    update_process()

def update_process():
    UpdateProcess(RESOURCE,currFrame,lenCurr,highFrame,lenHigh,highData,removeRate,decimal,unit,unitValue,heading_Main,currHead,cpu)
    highHead.config(text=heading_High(unit,decimal))

    root.after(refreshRate, update_process)

for p in psutil.process_iter(['name', RESOURCE]):
    pass

SettingScreen = SettingScreenCreate(root,START, FONT,bgColor, unitsIndex,UNITS)

root.mainloop()