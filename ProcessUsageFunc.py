import time 

def update_text_current(processes,processNum):
    counterP = 0
    TEXT = '\nHighest CPU %:\n\n'
    for p in processes:
        if counterP>=processNum:
            return TEXT
        if p[0]!='':
            text = f"{p[0]} - CPU Usage: {p[1]}%\n"
            TEXT+=text
            counterP+=1

def update_text_high(cpuMax):
    TEXT_HIGH = '\n\nHighest CPU % (last 22 min):\n\n'
    for m in cpuMax:
        t = f"{m[0]} - CPU Usage: {m[1]}%\n"
        TEXT_HIGH+=t
    return TEXT_HIGH

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
