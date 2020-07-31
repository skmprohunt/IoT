import pandas as pd
import sys
file_name = sys.argv[1]
tempData = pd.read_csv(file_name)
df = tempData[tempData['locationReliable']==True]
print(df.head())

tamperList = df['input117'].to_list()
ioStateList = df['ioState'].to_list()
vehicleBattery = df['vehicleBatteryLevel'].to_list()
print(df.head())
ioStatebit3 = []
ignitionList = []
for ioState in ioStateList:
    if len(ioState) > 8:
        ioState = ioState[:8]
    elif len(ioState) < 8:
        while len(ioState < 8):
            ioState = '0'+ioState
    ignitionList.append(int(ioState[1]))
    ioStatebit3.append(int(ioState[2]))

speed = df['speed'].to_list()
sensor = input("Is sensor connected on DIN (Yes/No)")
print(type(ignitionList[0]))
print(type(tamperList[0]))
print(type(ioStateList[0]))
print(type(ioStatebit3[0]))
print(type(speed[0]))
print(type(vehicleBattery[0]))


for i in range(0, len(tamperList), 10):
    tamperToggle = 0
    looseConnectionFlag = 0
    for j in range((i+1), (i+10)):
        if tamperList[j] != tamperList[j-1]:
            tamperToggle += 1
    if tamperToggle >= 5:
        looseConnectionFlag = 1

    thsingleflag = 0
    thdoubleflag = 0
    for j in range((i+1), (i+10)):
        if speed[j] == 0:
            if vehicleBattery[j] > 12.5 and vehicleBattery[j] < 13:
                if ignitionList[j] == 1 and ignitionList[j-1] == 0:
                    thsingleflag = 1
            if vehicleBattery[j] >24.5 and vehiclebattery[j] < 25:
                if ignitionList[j] == 1 and ignitionList[j-1] == 0:
                    thdoubleflag = 1

    voltageCount = 0
    batteryMisbehaveFlag = 0
    for j in range((i+1), (i+10)):
        if speed[j]>0:
            if vehicleBattery[j]>13.2:
                voltageCount += 1
    if voltageCount > 5:
        batteryMisbehaveFlag = 1

    ignitionConnflag = 0
    if sensor == "No":
        for j in range((i+1), (i+10)):
            if speed[j]>0:
                if ioStatebit3[j] == 1 and ioStatebit3[j-1] == 0:
                    ignitionConnflag = 1

    if looseConnectionFlag == 1:
        print("Loose Connection with Battery -->> Align Installer")
    if thsingleflag == 1:
        print("Threshold change required to 13.2 V")
    if thdoubleflag == 1:
        print("Threshold change required to 25.2 V")
    if batteryMisbehaveFlag == 0:
        print("To Manual Check!!")
    if sensor == "Yes":
        print("Sensor Connected!!")
    if ignitionConnflag == 1:
        print("Mark BM : Ignition Wire Connected")
        print("Run command - setparam 101:1 (wire source only)")
    else:
        print("Mark BM : Ignition wire to be connected")
        print("Align Installer")
