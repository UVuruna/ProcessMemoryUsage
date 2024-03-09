import psutil
import tkinter as tk
from ProcessUsageFunc import *

processNum = 6      # rows
highNum=4           # rows
highMaxTime = 1333    # sec
refreshRate = 666   # ms
cpuMax = [(0,0,0) for i in range(highNum)]

root = tk.Tk()
root.title("Top CPU Process")
process_label = tk.Label(root, font=('Arial',13), text="")
process_label.pack()

def update_process():
    # Dobijanje listu procesa sa njihovom upotrebom CPU-a
    processes = [(p.info['name'], p.info['cpu_percent']) for p in psutil.process_iter(['name', 'cpu_percent'])]

    # Sortiranje procesa po upotrebi CPU-a
        # Sortira po 2. clanu tupla, tj. po procentu ; reverse true znaci da prvo slaze najvece a ne najmanje
    processes.sort(key=lambda x: x[1], reverse=True)

    TEXT = update_text_current(processes,processNum)  

    delete_old_high_process(highNum,cpuMax,highMaxTime)
    update_high_process(processes,cpuMax,highNum)
    cpuMax.sort(key=lambda x: x[1], reverse=True)

    TEXT += update_text_high(cpuMax)

    process_label.config(text=TEXT)
    root.after(refreshRate, update_process)

update_process()
root.mainloop()