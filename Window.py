import tkinter as tk
from tkinter import ttk,font

def defineFont(familyF,sizeF,weightF='normal'):
    return font.Font(family=familyF, size=sizeF, weight=weightF)
unitsIndex = {'KB':1024,'MB':1024**2,'GB':1024**3}

WIDTH = 396
padding = 7
fontWidthLength = 9.4
fontHEADWidthLength = 12
highMaxTime = 3960      # sec
refreshRate = 1333      # ms
fontHeight = 19

red = '#FFE2E2'
redHead = '#FFC6C6'
blue = '#E2F1FF'
blueHead = '#A2D2FF'
bgColor = '#ECF5F9'
txtColor = "#060606"

def showOptions(root, MainScreen:list, SecondScreen:callable, unitsIndex:int, fontHEAD, FONT, red:str, blue:str, units:bool):
    unit = MainScreen[3].get() if units else '%'
    unitValue = unitsIndex[unit] if units else 1
    decimal = 2 if unit=='GB' else 1 if unit=='%' else 0

    lenCurr = int(MainScreen[1].get())
    lenHigh = int(MainScreen[2].get())
    highData = [(0,0,0) for _ in range(lenHigh)]
    HEIGHT = (lenCurr+lenHigh+4)*fontHeight+4*padding
    
    window = f"{WIDTH}x{HEIGHT}"
    root.geometry(window)
    for frame in MainScreen:
        frame.grid_forget()
    currHead,currFrame,highHead,highFrame = SecondScreen(root,fontHEAD,FONT,red,blue,lenCurr,lenHigh)
    return [currHead,currFrame,lenCurr, highHead,highFrame,lenHigh, highData,unit,unitValue,decimal]

def MainScreenCreate(root, START:callable, FONT, bgColor:str, unitsIndex:int, units:bool):
    MainScreen = []

    SaveButton = tk.Button(root, font=FONT,text="Start", height=2,width=12, command=START)
    SaveButton.grid(row=4,column=1, padx=5, pady=5)
    MainScreen.append(SaveButton)

    currentRows = ttk.Combobox(root, width=6, font=FONT, values=[i+1 for i in range(13)])
    currentRows.grid(row=1, column=1, padx=5, pady=5)
    currentRows.set(7)
    MainScreen.append(currentRows)

    highestRows = ttk.Combobox(root, width=6, font=FONT, values=[i+1 for i in range(13)])
    highestRows.grid(row=2, column=1, padx=5, pady=5)
    highestRows.set(4)
    MainScreen.append(highestRows)

    if units: # Only for Memory, not for CPU
        optionsUnit = ttk.Combobox(root, width=6, font=FONT, values=list(unitsIndex.keys()))
        optionsUnit.grid(row=0, column=1, padx=5, pady=5)
        optionsUnit.set('MB')
        MainScreen.append(optionsUnit)

        optionsUnitTxt = tk.Label(root, bg=bgColor, font=FONT, text="Choose units: ", justify='right')
        optionsUnitTxt.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        MainScreen.append(optionsUnitTxt)

    currentRowsTxt = tk.Label(root, bg=bgColor, font=FONT, text="Choose number of\ncurrent processes: ", justify='right')
    currentRowsTxt.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    MainScreen.append(currentRowsTxt)

    highestRowsTxt = tk.Label(root, bg=bgColor, font=FONT, text="Choose number of\nhighest processes: ", justify='right')
    highestRowsTxt.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    MainScreen.append(highestRowsTxt)
    return MainScreen

def SecondScreen(root, fontHEAD, FONT, red:str, blue:str, lenCurr:int, lenHigh:int):
    HighestHEAD_startY = int((lenCurr+2)*fontHeight+2*padding
)
    currHead = tk.Label(root, anchor='n', font=fontHEAD, text="", background=redHead, width=int(WIDTH/fontHEADWidthLength), height=2, foreground=txtColor)
    currHead.place(x=padding*2,y=padding*2)
    currFrame = tk.Label(root, font=FONT, text="", justify="right", background=red, width=int(WIDTH/fontWidthLength), height=lenCurr, foreground=txtColor)
    currFrame.place(x=padding,y=padding+2*fontHeight)

    highHead = tk.Label(root, anchor='n', font=fontHEAD, text="", background=blueHead, width=int(WIDTH/fontHEADWidthLength), height=2, foreground=txtColor)
    highHead.place(x=padding*2,y=HighestHEAD_startY+padding)
    highHead
    highFrame = tk.Label(root, font=FONT, text="", justify="right", background=blue, width=int(WIDTH/fontWidthLength), height=lenHigh, foreground=txtColor)
    highFrame.place(x=padding,y=HighestHEAD_startY+2*fontHeight)
    return currHead,currFrame,highHead,highFrame