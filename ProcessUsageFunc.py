import time 
import datetime

def update_text_current(processes,processNum,text):
    counter=0
    for p in processes:
        if counter==(processNum-1):
            t = f"{p[0]} - CPU Usage: {p[1]}%"
            text+=t
            return text
        if p[0]!='':
            t = f"{p[0]} - CPU Usage: {p[1]}%\n"
            text+=t
            counter+=1

def update_text_high(cpuMax,text,highNum):
    for i in range(highNum):
        if i == (highNum-1):
            t = f"{str(cpuMax[i][0])} : {datetime.datetime.fromtimestamp(cpuMax[i][2]).strftime('%H:%M')}  -  CPU: {cpuMax[i][1]}%"
        else:
            t = f"{str(cpuMax[i][0])} : {datetime.datetime.fromtimestamp(cpuMax[i][2]).strftime('%H:%M')}  -  CPU: {cpuMax[i][1]}%\n"
        text+=t
    return text

def delete_old_high_process(lenCpuMax,cpuMax,highMaxTime):
    now = time.time()    
    for i in range(lenCpuMax):
        if now-cpuMax[i][2]>=highMaxTime:
            cpuMax[i] = (0,0,0)

def update_high_process(processes,lista,lenCpuMax):
    for p in processes:
        if p[1]<lista[-1][1]:
            return
        for pozicija in range(lenCpuMax):
            if p[0] not in ['System Idle Process',''] and p[1]>lista[pozicija][1]:
                if pozicija==0:
                    lista[pozicija] = (p[0],p[1],time.time())
                    checkAfter(lista,p,pozicija)
                    break
                else:
                    checkBefore(lista,p,pozicija,lenCpuMax)
                    break

def checkBefore(lista,proces,currentPos,lenCpuMax):
    for posBefore in range(currentPos):
        if lista[posBefore][0] == proces[0]:
            return
    else:
        lista[currentPos] = (proces[0],proces[1],time.time())
        if currentPos!=(lenCpuMax-1):
            checkAfter(lista,proces,currentPos)
        return
        
def checkAfter(lista,proces,currentPos):
    for posAfter in lista[currentPos+1:]:
        if posAfter[0] == proces[0]:
            lista[lista.index(posAfter)] = (0,0,0)