a = [11,22,33,44,55]

a = a[:3]

print(a)
a.insert(0,99)
print(a)

a.remove(22)
a.append(4)

print(a)

a.insert(2,55)
del a[-1]

print(a)


print('afroMan'.capitalize())


x = [1,2,3,4]
x.insert(3,10)
del x[-1]
print(x)

x.insert(1,20)
del x[-1]
print(x)

MAXLENGTH = 'CodeSetup-stable-863d2581ecda6849923a2118d93'
print(len(MAXLENGTH))


import tkinter as tk
from tkinter import ttk

def on_slider_move(event):
    value = int(slider.get())
    label.config(text=f"{value} ms")

print(len('max time for tracking processes with highest resource usage'),'max process')

root = tk.Tk()
root.title("Slider Primer")

slider = ttk.Scale(root, from_=100, to=200, orient=tk.HORIZONTAL, length=200)
slider.pack()

label = tk.Label(root, text="")
label.pack()

slider.bind("<Motion>", on_slider_move)

root.mainloop()

'''
0 System Idle Process
4 System
212 Registry
728 smss.exe
888 svchost.exe
996 csrss.exe
1032 wininit.exe
1040 csrss.exe
1104 services.exe
1112 svchost.exe
1116 LsaIso.exe
1136 svchost.exe
1140 lsass.exe
1200 chrome.exe
1216 svchost.exe
1220 Code.exe
1272 svchost.exe
1300 fontdrvhost.exe
1364 svchost.exe
1416 svchost.exe
1492 winlogon.exe
1516 chrome.exe
1544 fontdrvhost.exe
1608 dwm.exe
1620 msedgewebview2.exe
1756 svchost.exe
1784 svchost.exe
1788 svchost.exe
1848 svchost.exe
1892 svchost.exe
1900 svchost.exe
1908 svchost.exe
2020 svchost.exe
2040 svchost.exe
2116 svchost.exe
2168 svchost.exe
2172 svchost.exe
2324 svchost.exe
2344 NVDisplay.Container.exe
2472 svchost.exe
2492 svchost.exe
2516 svchost.exe
2524 svchost.exe
2532 svchost.exe
2540 msedgewebview2.exe
2628 MemCompression
2640 CodeSetup-stable-863d2581ecda6849923a2118d93a088b0745d9d6.exe
2676 svchost.exe
2716 svchost.exe
2724 svchost.exe
2892 NVDisplay.Container.exe
2916 svchost.exe
3192 svchost.exe
3220 svchost.exe
3236 Code.exe
3360 svchost.exe
3368 svchost.exe
3376 svchost.exe
3396 WmiPrvSE.exe
3492 svchost.exe
3616 backgroundTaskHost.exe
3696 svchost.exe
3824 svchost.exe
3912 ApplicationFrameHost.exe
3916 audiodg.exe
3956 spoolsv.exe
4080 svchost.exe
4196 chrome.exe
4200 RTSS.exe
4256 svchost.exe
4304 svchost.exe
4312 svchost.exe
4320 svchost.exe
4328 Agent.exe
4340 FNPLicensingService64.exe
4348 svchost.exe
4360 MigrationService.exe
4376 nvcontainer.exe
4392 SecurityHealthService.exe
4404 logioptionsplus_updater.exe
4412 sqlwriter.exe
4420 svchost.exe
4432 svchost.exe
4440 OfficeClickToRun.exe
4456 RtkAudUService64.exe
4464 MsMpEng.exe
4472 svchost.exe
4484 svchost.exe
4496 ensserver.exe
4504 AggregatorHost.exe
4520 SamsungMagicianSVC.exe
4548 Code.exe
4564 mysqld.exe
4596 svchost.exe
4612 Code.exe
4724 MpDefenderCoreService.exe
4996 logioptionsplus_agent.exe
5136 svchost.exe
5304 CodeSetup-stable-863d2581ecda6849923a2118d93a088b0745d9d6.tmp
5352 chrome.exe
5376 dasHost.exe
5452 conhost.exe
5540 mysqld.exe
5612 conhost.exe
6000 sihost.exe
6260 unsecapp.exe
6308 Code.exe
6416 Code.exe
6428 svchost.exe
6444 conhost.exe
6448 cmd.exe
6496 Code.exe
6724 svchost.exe
6816 taskhostw.exe
6864 Code.exe
6876 RtkAudUService64.exe
6896 svchost.exe
7160 rundll32.exe
7176 svchost.exe
7236 svchost.exe
7740 svchost.exe
7788 explorer.exe
8008 chrome.exe
8108 Code.exe
8136 EncoderServer.exe
8140 svchost.exe
8248 unsecapp.exe
8280 nvcontainer.exe
8324 nvcontainer.exe
8512 logi_crashpad_handler.exe
8528 logi_crashpad_handler.exe
8712 SystemSettings.exe
8984 svchost.exe
9044 svchost.exe
9052 Code.exe
9084 msedge.exe
9204 logioptionsplus_appbroker.exe
9292 pwsh.exe
9368 Code.exe
9436 svchost.exe
9452 vds.exe
9512 WidgetService.exe
9560 svchost.exe
9692 SearchIndexer.exe
9776 StartMenuExperienceHost.exe
9780 msedge.exe
9832 svchost.exe
9856 SearchHost.exe
10116 LockScreenContentServer.exe
10248 pwsh.exe
10308 RuntimeBroker.exe
10368 RuntimeBroker.exe
10384 Widgets.exe
10432 RuntimeBroker.exe
10440 svchost.exe
10540 svchost.exe
10868 svchost.exe
10912 msedgewebview2.exe
10932 msedgewebview2.exe
11044 LockApp.exe
11104 ctfmon.exe
11108 svchost.exe
11204 python.exe
11284 msedgewebview2.exe
11424 dllhost.exe
11500 msedgewebview2.exe
11612 Code.exe
12032 OneDrive.exe
12420 RuntimeBroker.exe
12432 conhost.exe
12576 NVIDIA Share.exe
12648 svchost.exe
12780 cmd.exe
12848 chrome.exe
12924 msedgewebview2.exe
12956 svchost.exe
13080 chrome.exe
13088 svchost.exe
13176 svchost.exe
13224 NVIDIA Web Helper.exe
13236 FanControl.exe
13244 svchost.exe
13308 RTSSHooksLoader64.exe
13368 conhost.exe
13544 svchost.exe
13624 SecurityHealthSystray.exe
13788 HWiNFO64.EXE
13800 steamwebhelper.exe
13804 msedge.exe
14012 ShellExperienceHost.exe
14228 NisSrv.exe
14324 TodoBackupService.exe
14808 svchost.exe
14952 NVIDIA Share.exe
14972 MemoryUsage.exe
15208 conhost.exe
15212 svchost.exe
15236 nvsphelper64.exe
15252 NVIDIA Share.exe
15408 chrome.exe
15432 msedge.exe
15436 msedge.exe
15568 msedge.exe
15744 AdskLicensingService.exe
16072 svchost.exe
16108 Notepad.exe
16148 lmgrd.exe
16172 steam.exe
16228 msedge.exe
16248 chrome.exe
16288 msedge.exe
16420 svchost.exe
16484 msedge.exe
16500 steamservice.exe
16636 steamwebhelper.exe
16728 steamwebhelper.exe
16932 steamwebhelper.exe
17052 steamwebhelper.exe
17068 FxSound.exe
17084 svchost.exe
17096 UserOOBEBroker.exe
17116 TrayProcess.exe
17208 pwsh.exe
17248 adskflex.exe
17332 steamwebhelper.exe
17356 steamwebhelper.exe
17716 msedge.exe
17880 CCXProcess.exe
17896 node.exe
17904 conhost.exe
17988 MemoryUsage.exe
18176 svchost.exe
18292 AdobeIPCBroker.exe
18372 Code.exe
18660 ProcessorUsage.exe
18764 ProcessorUsage.exe
18796 svchost.exe
18816 msedge.exe
18892 Code.exe
18980 RuntimeBroker.exe
19152 chrome.exe
19192 conhost.exe
'''