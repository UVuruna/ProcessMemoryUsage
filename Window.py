import tkinter as tk
from tkinter import ttk,font

def defineFont(familyF,sizeF,weightF='normal'):
    return font.Font(family=familyF, size=sizeF, weight=weightF)
unitsIndex = {'KB':1024,'MB':1024**2,'GB':1024**3}

processNum = int()      # rows
highNum= int()          # rows
unit = str()
highMaxTime = 3960      # sec
refreshRate = 1333      # ms

red = '#FFE2E2'
blue = '#E2F1FF'
bgColor = '#ECF5F9'
textColor = "#060606"

def showOptions(root,MainScreen,unitsIndex,SecondScreen,labelFont,red,blue,textColor,unitsChoice=False):
    unit = MainScreen[3].get() if unitsChoice else '%'
    unitValue = unitsIndex[unit] if unitsChoice else 1
    formatNum = 2 if unit=='GB' else 1 if unit=='%' else 0

    processNum = int(MainScreen[1].get())
    highNum = int(MainScreen[2].get())
    cpuMax = [(0,0,0) for _ in range(highNum)]
    
    window = f"466x{(processNum+highNum+4)*19+44}"
    root.geometry(window)
    for frame in MainScreen:
        frame.grid_forget()
    redScreen,blueScreen = SecondScreen(root,labelFont,red,blue,textColor,33+(processNum+2)*19,processNum+2,highNum+2)

    return unit,processNum,highNum,cpuMax,formatNum,unitValue,redScreen,blueScreen

def MainScreenCreate(root,labelFont,showOptionsUnit,unitsIndex,bgColor,units):
    lista = []

    SaveButton = tk.Button(root, font=labelFont,text="Start", height=2,width=12, command=showOptionsUnit)
    SaveButton.grid(row=4,column=1, padx=5, pady=5)
    lista.append(SaveButton)

    currentRows = ttk.Combobox(root, width=6, font=labelFont, values=[i for i in range(1,13)])
    currentRows.grid(row=1, column=1, padx=5, pady=5)
    currentRows.set(7)
    lista.append(currentRows)

    highestRows = ttk.Combobox(root, width=6, font=labelFont, values=[i for i in range(1,13)])
    highestRows.grid(row=2, column=1, padx=5, pady=5)
    highestRows.set(4)
    lista.append(highestRows)

    if units:
        optionsUnit = ttk.Combobox(root, width=6, font=labelFont, values=list(unitsIndex.keys()))
        optionsUnit.grid(row=0, column=1, padx=5, pady=5)
        optionsUnit.set('MB')
        lista.append(optionsUnit)

        optionsUnitTxt = tk.Label(root, bg=bgColor, font=labelFont, text="Choose units: ", justify='right')
        optionsUnitTxt.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        lista.append(optionsUnitTxt)

    currentRowsTxt = tk.Label(root, bg=bgColor, font=labelFont, text="Choose number of\ncurrent processes: ", justify='right')
    currentRowsTxt.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    lista.append(currentRowsTxt)

    highestRowsTxt = tk.Label(root, bg=bgColor, font=labelFont, text="Choose number of\nhighest processes: ", justify='right')
    highestRowsTxt.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    lista.append(highestRowsTxt)

    return lista

def SecondScreen(root,labelFont,red,blue,textColor,pixY,currH,highH):
    currProc_label = tk.Label(root, font=labelFont, text="", justify="right", background=red, width=48, height=currH, foreground=textColor)
    currProc_label.place(x=12,y=12)
    highProc_label = tk.Label(root, font=labelFont, text="", justify="right", background=blue, width=48, height=highH, foreground=textColor)
    highProc_label.place(x=12,y=pixY)

    return currProc_label,highProc_label