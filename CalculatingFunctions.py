import time
from datetime import datetime, timedelta
import psutil
from collections import defaultdict

maxUsage = (0, 0)
# DATA Functions


def UpdateProcess(RESOURCE: str, currentFrame, lenCurr: int, highestFrame, lenHigh: int, highData: list, removeRate: int, decimal: int, unit: str, unitValue: int, headTxt: callable, headFrame, PC=None):
    global maxUsage
    processesRaw = defaultdict(int)
    # Creating/Updating DATA
    if RESOURCE == 'memory_info':
        memoryUsage = 0
        for p in psutil.process_iter(['name', RESOURCE]):
            name = p.info['name'][:-
                                  4] if p.info['name'][-4:].lower() == '.exe' else p.info['name']
            mem = p.info[RESOURCE].rss/unitValue
            memoryUsage += mem
            if name:
                name = 'Visual Studio Code' if name[:4] == 'Code' else 'Logi Options+' if name[:4] == 'logi' else 'Steam' if name[:5] == 'steam' \
                    else 'NVIDIA' if name[:2].lower() == 'nv' else 'Microsoft Edge' if name[:6] == 'msedge' else name
                processesRaw[name] += mem
        maxUsage = (memoryUsage, datetime.now()
                    ) if maxUsage[0] < memoryUsage else maxUsage
        headFrame.config(text=headTxt(memoryUsage))

    elif RESOURCE == 'cpu_percent':
        for p in psutil.process_iter(['name', RESOURCE]):
            name = p.info['name'][:-
                                  4] if p.info['name'][-4:].lower() == '.exe' else p.info['name']
            if name:
                if name == 'System Idle Process':
                    cpuUsage = PC-p.info[RESOURCE]
                name = 'Visual Studio Code' if name[:4] == 'Code' else 'Logi Options+' if name[:4] == 'logi' else 'Steam' if name[:5] == 'steam' \
                    else 'NVIDIA' if name[:2].lower() == 'nv' else 'Microsoft Edge' if name[:6] == 'msedge' else name
                processesRaw[name] += p.info[RESOURCE]
        maxUsage = (cpuUsage, datetime.now()
                    ) if maxUsage[0] < cpuUsage else maxUsage
        headFrame.config(text=headTxt(cpuUsage))

    processes = sorted(processesRaw.items(), key=lambda x: x[1], reverse=True)
    delete_old_high_process(highData, lenHigh, removeRate)
    update_high_process(processes, highData, lenHigh)
    highData.sort(key=lambda x: x[1], reverse=True)

    # Creating TEXT
    txtCurr = update_text_current(processes, lenCurr, unit, decimal)
    txtHigh = update_text_high(highData, lenHigh, unit, decimal)

    # Updating TEXT
    currentFrame.config(text=txtCurr)
    highestFrame.config(text=txtHigh)


def delete_old_high_process(highData: list, lenHigh: int, removeRate: int):
    now = time.time()
    for i in range(lenHigh):
        if now-highData[i][2] >= (removeRate*60):
            # Brise clan koji dugo stoji po indeksu (preko x minuta)
            del highData[i]
            highData.append((0, 0, 0))  # Dodaje prazan clan na kraj


def update_high_process(processes: list, highData: list, lenHigh: int):
    # Pomera se ka kraju liste (ne proverava stalno odradjene segmente)
    pos = 0
    for p in processes:
        # Prekida prevremeno ako je trenutni najveci clan manji od poslednjeg iz liste
        if p[1] <= highData[-1][1]:
            return
        for pozicija in range(pos, lenHigh):
            if p[0] not in ['System Idle Process', ''] and p[1] > highData[pozicija][1]:
                if pozicija == 0:
                    # Ubacuje na konkretnu poziciju
                    highData.insert(pozicija, (p[0], p[1], time.time()))
                    pos += 1  # U sustini pos postaje 1+POZICIJA ako se dodaje clan. Ali posto je pozicija 0 : pos+=1
                    if not checkAfter(highData, p, pozicija):
                        # Brise po indeksu (Brise POSELEDNJI clan)
                        del highData[-1]
                    break
                else:
                    pos = checkBefore(highData, p, pozicija, lenHigh)
                    break


# Desava se uvek nakon ubacivanja (osim ako se ubaciju na POCETAK liste)
def checkBefore(highData: list, proces: tuple, currentPos: int, lenHigh: int):
    for posBefore in range(currentPos):
        # Proverava da li ima clan sa istim imenom pre (onda ne ubacuje)
        if highData[posBefore][0] == proces[0]:
            return currentPos
    else:
        # Ubacuje na konkretnu poziciju
        highData.insert(currentPos, (proces[0], proces[1], time.time()))
        if currentPos != (lenHigh-1):
            if not checkAfter(highData, proces, currentPos):
                del highData[-1]  # Brise po indeksu (Brise POSELEDNJI clan)
        else:
            del highData[-1]  # Brise po indeksu (Brise POSELEDNJI clan)
        return currentPos+1


# Desava se uvek nakon ubacivanja (osim ako se ubacuje na KRAJ liste)
def checkAfter(highData: list, proces: tuple, currentPos: int):
    for posAfter in highData[currentPos+1:]:
        # Proverava da li ima clan sa istim imenom posle (onda ga brise)
        if posAfter[0] == proces[0]:
            highData.remove(posAfter)  # Brise po sadrzaju
            highData.append((0, 0, 0))  # Ubacuje na kraj
            return True

# OUTPUT Text Functions


def heading_High(unit, decimal):
    return 'Highest usage {:,.{}f} {}: {}'.format(maxUsage[0], decimal, unit, maxUsage[1].strftime("%H:%M"))


def update_text_current(processes: list, lenCurr: int, unit: str, decimal: int):
    text = str()
    obj = 'CPU' if unit == '%' else 'RAM'
    for p in range(lenCurr):
        end = '' if p == (lenCurr-1) else '\n'
        try:
            text += "{} - {}: {:,.{}f} {}".format(
                processes[p][0], obj, processes[p][1], decimal, unit)+end
        except IndexError:
            return text
    return text


def update_text_high(highData: list, lenHigh: int, unit: str, decimal: int):
    text = str()
    obj = 'CPU' if unit == '%' else 'RAM'
    for i in range(lenHigh):
        if not highData[i][0]:
            break
        timeOccurance = datetime.fromtimestamp(
            highData[i][2]).strftime('%H:%M')
        # Dodavlja novi red svuda osim na kraj
        end = '' if i == (lenHigh-1) else '\n'
        text += "{} : {}  -  {}: {:,.{}f} {}".format(
            highData[i][0], timeOccurance, obj, highData[i][1], decimal, unit)+end
    return text
