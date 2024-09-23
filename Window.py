import tkinter as tk
from tkinter import ttk, font


def defineFont(familyF, sizeF, weightF='normal'):
    return font.Font(family=familyF, size=sizeF, weight=weightF)


unitsIndex = {'KB': 1024, 'MB': 1024**2, 'GB': 1024**3}
fontWidthLength = 9.4
fontHEADWidthLength = 12
fontHeight = 19

WIDTH = 396
margin = 7
defaultRefresh = 2000
defaultRemove = 120

red = '#FFE2E2'
redHead = '#FFC6C6'
blue = '#E2F1FF'
blueHead = '#A2D2FF'
bgColor = '#ECF5F9'
txtColor = "#060606"


def GetSetting(root, SettingScreen: list, MainScreen: callable, unitsIndex: int, fontHEAD, FONT, red: str, blue: str, units: bool):
    unit = SettingScreen[-2].get() if units else '%'
    PC = int(SettingScreen[-1].get())
    unitValue = unitsIndex[unit] if units else 1
    decimal = 2 if unit == 'GB' else 1 if unit == '%' else 0
    refreshRate = int(SettingScreen[3].get())*10
    removeRate = int(SettingScreen[4].get())

    lenCurr = int(SettingScreen[1].get())
    lenHigh = int(SettingScreen[2].get())
    highData = [(0, 0, 0) for _ in range(lenHigh)]
    HEIGHT = (lenCurr+lenHigh+4)*fontHeight+4*margin

    window = f"{WIDTH}x{HEIGHT}"
    root.geometry(window)
    for frame in SettingScreen:
        frame.grid_forget()
    currHead, currFrame, highHead, highFrame = MainScreen(
        root, fontHEAD, FONT, red, blue, lenCurr, lenHigh)

    return [PC, refreshRate, removeRate, currHead, currFrame, lenCurr, highHead, highFrame, lenHigh, highData, unit, unitValue, decimal]


def SettingScreenCreate(root, START: callable, FONT, bgColor: str, unitsIndex: int, units: bool):
    SettingScreen = []
    padding = 5
    # SAVE BUTTON
    SaveButton = tk.Button(root, font=FONT, text="Start",
                           height=2, width=12, command=START)
    SaveButton.grid(row=13, column=1, padx=padding, pady=padding)
    SettingScreen.append(SaveButton)

    # INPUT DROPBOX
    currentRows = ttk.Combobox(root, width=6, font=FONT, values=[
                               i+1 for i in range(13)])
    currentRows.grid(row=2, column=1, padx=padding, pady=padding)
    currentRows.set(7)
    SettingScreen.append(currentRows)

    highestRows = ttk.Combobox(root, width=6, font=FONT, values=[
                               i+1 for i in range(13)])
    highestRows.grid(row=3, column=1, padx=padding, pady=padding)
    highestRows.set(4)
    SettingScreen.append(highestRows)

    # INPUT SLIDER
    def getRefreshRate(event):
        refreshRate = int(refreshRateScale.get())*10
        refreshRateNum.config(text=f"{refreshRate} ms")

    def getRemoveRate(event):
        removeRate = int(removeRateScale.get())
        removeRateNum.config(text=f"{removeRate} min")

    varRef = tk.StringVar(value=int(defaultRefresh/10))
    refreshRateScale = ttk.Scale(
        root, from_=50, to=500, orient=tk.HORIZONTAL, length=200, variable=varRef)
    refreshRateScale.grid(row=4, column=1, columnspan=2,
                          padx=padding, pady=padding)
    refreshRateScale.bind("<Motion>", getRefreshRate)
    SettingScreen.append(refreshRateScale)

    varRem = tk.StringVar(value=defaultRemove)
    removeRateScale = ttk.Scale(
        root, from_=10, to=360, orient=tk.HORIZONTAL, length=200, variable=varRem)
    removeRateScale.grid(row=6, column=1, columnspan=2,
                         padx=padding, pady=padding)
    removeRateScale.bind("<Motion>", getRemoveRate)
    SettingScreen.append(removeRateScale)

    refreshRateNum = tk.Label(
        root, bg=bgColor, font=FONT, text=f"{defaultRefresh} ms")
    refreshRateNum.grid(row=5, column=1, columnspan=2,
                        padx=padding, pady=padding)
    SettingScreen.append(refreshRateNum)

    removeRateNum = tk.Label(root, bg=bgColor, font=FONT,
                             text=f'{defaultRemove} min')
    removeRateNum.grid(row=7, column=1, columnspan=2,
                       padx=padding, pady=padding)
    SettingScreen.append(removeRateNum)

    # LABELS
    currentRowsTxt = tk.Label(root, bg=bgColor, font=FONT,
                              text="Number of current processes:", justify='right')
    currentRowsTxt.grid(row=2, column=0, padx=padding,
                        pady=padding, sticky="ne")
    SettingScreen.append(currentRowsTxt)

    highestRowsTxt = tk.Label(root, bg=bgColor, font=FONT,
                              text="Number of highest processes:", justify='right')
    highestRowsTxt.grid(row=3, column=0, padx=padding,
                        pady=padding, sticky="ne")
    SettingScreen.append(highestRowsTxt)

    refreshRateTxt = tk.Label(root, bg=bgColor, font=FONT,
                              text='Refresh Rate:\nTime for updating processes', justify='right')
    refreshRateTxt.grid(row=4, rowspan=2, column=0,
                        padx=padding, pady=padding, sticky='ne')
    SettingScreen.append(refreshRateTxt)

    removeRateTxt = tk.Label(root, bg=bgColor, font=FONT,
                             text='Time for keeping processes\nwith highest resource usage', justify='right')
    removeRateTxt.grid(row=6, rowspan=2, column=0,
                       padx=padding, pady=padding, sticky="ne")
    SettingScreen.append(removeRateTxt)

    if units:  # Only for Memory
        totalRAMtxt = tk.Label(root, bg=bgColor, font=FONT,
                               text="Amount of RAM in PC", justify='right')
        totalRAMtxt.grid(row=0, column=0, padx=padding,
                         pady=padding, sticky="ne")
        SettingScreen.append(totalRAMtxt)

        optionsUnitTxt = tk.Label(
            root, bg=bgColor, font=FONT, text="Choose units", justify='right')
        optionsUnitTxt.grid(row=1, column=0, padx=padding,
                            pady=padding, sticky="ne")
        SettingScreen.append(optionsUnitTxt)

        totalRAMunit = tk.Label(root, bg=bgColor, font=FONT, text="GB")
        totalRAMunit.grid(row=0, column=2, padx=padding,
                          pady=padding, sticky='w')
        SettingScreen.append(totalRAMunit)

        optionsUnit = ttk.Combobox(
            root, width=6, font=FONT, values=list(unitsIndex.keys()))
        optionsUnit.grid(row=1, column=1, padx=padding, pady=padding)
        optionsUnit.set('MB')
        SettingScreen.append(optionsUnit)

        totalRAM = ttk.Combobox(root, width=6, font=FONT,
                                values=list(2**i for i in range(2, 8)))
        totalRAM.grid(row=0, column=1, padx=padding, pady=padding)
        totalRAM.set(32)
        SettingScreen.append(totalRAM)

    else:  # Only for CPU
        totalCoresTxt = tk.Label(
            root, bg=bgColor, font=FONT, text='Amount of Threads in CPU:\nAMD: Threads = Cores count x 2', justify='right')
        totalCoresTxt.grid(row=0, column=0, padx=padding,
                           pady=padding, sticky="ne")
        SettingScreen.append(totalCoresTxt)

        totalCores = ttk.Combobox(
            root, width=6, font=FONT, values=list(2**i for i in range(1, 7)))
        totalCores.grid(row=0, column=1, padx=padding, pady=padding)
        totalCores.set(16)
        SettingScreen.append(totalCores)

    return SettingScreen


def MainScreen(root, fontHEAD, FONT, red: str, blue: str, lenCurr: int, lenHigh: int):
    HighStartY = int((lenCurr+2)*fontHeight+2*margin)

    currHead = tk.Label(root, anchor='n', font=fontHEAD, text="", background=redHead, width=int(
        WIDTH/fontHEADWidthLength), height=2, foreground=txtColor)
    currHead.place(x=margin*2, y=margin*2)
    currFrame = tk.Label(root, anchor='ne', font=FONT, text="", justify="right", background=red, width=int(
        WIDTH/fontWidthLength), height=lenCurr, foreground=txtColor)
    currFrame.place(x=margin, y=margin+2*fontHeight)

    highHead = tk.Label(root, anchor='n', font=fontHEAD, text="", background=blueHead, width=int(
        WIDTH/fontHEADWidthLength), height=2, foreground=txtColor)
    highHead.place(x=margin*2, y=HighStartY+margin)
    highHead
    highFrame = tk.Label(root, anchor='ne', font=FONT, text="", justify="right", background=blue, width=int(
        WIDTH/fontWidthLength), height=lenHigh, foreground=txtColor)
    highFrame.place(x=margin, y=HighStartY+2*fontHeight)

    return currHead, currFrame, highHead, highFrame
