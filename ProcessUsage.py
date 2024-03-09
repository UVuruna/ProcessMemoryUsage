import psutil
import tkinter as tk
import time 

processNum = 6
highNum=4
highMaxTime = 666
refreshRate = 666
cpuMax = [(0,0,0) for i in range(highNum)]


def update_process():
    # Dobijanje listu procesa sa njihovom upotrebom CPU-a
    processes = [(p.info['name'], p.info['cpu_percent']) for p in psutil.process_iter(['name', 'cpu_percent'])]

    # Sortiranje procesa po upotrebi CPU-a
        # Sortira po 2. clanu tupla, tj. po procentu ; reverse true znaci da prvo slaze najvece a ne najmanje
    processes.sort(key=lambda x: x[1], reverse=True)
    
    
    def update_text_current(processes):
        counterP = 0
        TEXT = '\nHighest CPU %:\n\n'
        for p in processes:
            if counterP>=processNum:
                return TEXT
            if p[0]!='':
                text = f"{p[0]} - CPU Usage: {p[1]}%\n"
                TEXT+=text
                counterP+=1

    TEXT = update_text_current(processes)  
    
    # Prikazivanje informacija o procesu sa najvećom upotrebom CPU-a
    def delete_old_high_process(highNum,cpuMax):
        now = time.time()    
        for i in range(highNum):
            if now-cpuMax[i][2]>=highMaxTime:
                cpuMax[i] = (0,0,0)
 
    def checkBefore(lista,proces,currentPos):
        for posBefore in range(currentPos):
            if lista[posBefore][0] == proces[0]:
                return
        else:
            lista[currentPos] = (proces[0],proces[1],time.time())
            if currentPos!=(highNum-1):
                checkAfter(lista,proces,currentPos)
            return
            

    def checkAfter(lista,proces,currentPos):
        for posAfter in lista[currentPos+1:]:
            if posAfter[0] == proces[0]:
                posAfter = (0,0,0)


    def update_high_process(processes,cpuMax,highNum):
        for p in processes:
            if p[1]<cpuMax[-1][1]:
                #print("prosao break")
                break
            for pozicija in range(highNum):
                #print('pozicija ',pozicija)
                if p[0] not in ['System Idle Process',''] and p[1]>cpuMax[pozicija][1]:
                    if pozicija==0:
                        cpuMax[pozicija] = (p[0],p[1],time.time())
                        checkAfter(cpuMax,p,pozicija)
                        break
                    else:
                        checkBefore(cpuMax,p,pozicija)
                        break
    
    def update_text_high(cpuMax):
        TEXT_HIGH = '\n\nHighest CPU % (last 10 min):\n\n'
        for m in cpuMax:
            t = f"{m[0]} - CPU Usage: {m[1]}%\n"
            TEXT_HIGH+=t
        return TEXT_HIGH

    delete_old_high_process(highNum,cpuMax)
    update_high_process(processes,cpuMax,highNum)
    cpuMax.sort(key=lambda x: x[1], reverse=True)

    TEXT += update_text_high(cpuMax)

    #textMax[counterH] = f'\nHighest CPU Usage:\n{p[0]} - CPU Usage: {p[1]}%'
    #TEXT += textMax
    process_label.config(text=TEXT)

    # Postavljanje funkcije da se poziva svake sekunde
    root.after(refreshRate, update_process)

# Kreiranje Tkinter prozora
root = tk.Tk()
root.title("Top CPU Process")

# Kreiranje labela za prikaz procesa sa najvećom upotrebom CPU-a
process_label = tk.Label(root, font=('Arial',13), text="")
process_label.pack()

# Poziv funkcije za ažuriranje labela
update_process()

# Pokretanje Tkinter petlje
root.mainloop()
