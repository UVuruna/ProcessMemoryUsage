import psutil
import tkinter as tk
from tkinter import font
from ProcessUsageFunc import *

processNum = 7        # rows
highNum=4             # rows
highMaxTime = 3960    # sec
refreshRate = 1333    # ms
cpuMax = [(0,0,0) for _ in range(highNum)]

red = '#FFE2E2'
blue = '#E2F1FF'
bgColor = '#ECF5F9'
textColor = "#060606"

root = tk.Tk()
root.configure(bg=bgColor)
root.title("Top CPU Process")
root.geometry("396x330")

labelFont = font.Font(family="Arial", size=13, weight="normal")
headingHigh = f'Highest CPU usage % (last {int(highMaxTime/60)} min):\t\n\n'
headingMain = 'Current CPU usage %:\t\n\n'

currProc_label = tk.Label(root, font=labelFont, text="", justify="right", background=red, width=41, height=9, foreground=textColor)
currProc_label.place(x=11,y=11)
highProc_label = tk.Label(root, font=labelFont, text="", justify="right", background=blue, width=41, height=6, foreground=textColor)
highProc_label.place(x=11,y=198)

def update_process():
    processes = [(p.info['name'], p.info['cpu_percent']) for p in psutil.process_iter(['name', 'cpu_percent'])]
    processes.sort(key=lambda x: x[1], reverse=True)

    txtCurr = update_text_current(processes,processNum,headingMain)  

    delete_old_high_process(highNum,cpuMax,highMaxTime)
    update_high_process(processes,cpuMax,highNum)
    cpuMax.sort(key=lambda x: x[1], reverse=True)

    txtHigh = update_text_high(cpuMax,headingHigh,highNum)

    currProc_label.config(text=txtCurr)
    highProc_label.config(text=txtHigh)
    root.after(refreshRate, update_process)

update_process()
root.mainloop()