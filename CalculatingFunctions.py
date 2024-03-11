import time 
import datetime
import psutil
from collections import defaultdict

def UpdateProcess(processNum,headingMain,formatNum,highNum,cpuMax,highMaxTime,headingHigh,currProc_label,highProc_label,OBJ_TYPE,unit,unitValue):
    processesRaw = defaultdict(int)
    memoryUsage = 0

    # Creating/Updating DATA
    if OBJ_TYPE == 'memory_info':
        for p in psutil.process_iter(['name', OBJ_TYPE]):
            mem = p.info[OBJ_TYPE].rss/unitValue
            processesRaw[p.info['name']] +=mem
            memoryUsage +=mem
    elif OBJ_TYPE == 'cpu_percent':
        for p in psutil.process_iter(['name', OBJ_TYPE]):
            processesRaw[p.info['name']] += p.info[OBJ_TYPE]
    processes = sorted(processesRaw.items(), key=lambda x: x[1], reverse=True)
    delete_old_high_process(highNum,cpuMax,highMaxTime)
    update_high_process(processes,cpuMax,highNum)
    cpuMax.sort(key=lambda x: x[1], reverse=True)

        # Creating TEXT
    heading = headingMain(memoryUsage) if OBJ_TYPE == 'memory_info' else headingMain
    txtCurr = update_text_current(processes,processNum,heading,unit,formatNum) 
    txtHigh = update_text_high(cpuMax,headingHigh,highNum,unit,formatNum)
    
        # Updating TEXT
    currProc_label.config(text=txtCurr)
    highProc_label.config(text=txtHigh)

def update_text_current(processes,processNum,text,unit,formatNum):
    counter=0
    for p in processes:
        if p[0]!='':
            if counter==(processNum-1):
                t = "{} - CPU Usage: {:,.{}f} {}".format(p[0], p[1], formatNum, unit)
                text+=t
                return text
            t = "{} - CPU Usage: {:,.{}f} {}\n".format(p[0], p[1], formatNum, unit)
            text+=t
            counter+=1

def update_text_high(cpuMax,text,highNum,unit,formatNum):
    for i in range(highNum):
        name = cpuMax[i][0]
        timeOccurance = datetime.datetime.fromtimestamp(cpuMax[i][2]).strftime('%H:%M')
        usage = cpuMax[i][1]
        end = '' if i == (highNum-1) else '\n'
        t = "{} : {}  -  Memory: {:,.{}f} {}".format(name,timeOccurance,usage,formatNum,unit)+end
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