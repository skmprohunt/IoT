import pandas as pd
import sys
file_name = sys.argv[1]
csvData = pd.read_csv(file_name)
df = csvData[csvData['locationReliable'] == True]
print(df.head())

tamperList = df['input117'].to_list()
ioStateList = df['ioState'].to_list()
ingestionTime = df['ingestionTime'].to_list()
vehicleBattery = df['vehicleBatteryLevel'].to_list()
ioStatebit3 = []
ignitionList = []

for ioState in ioStateList:
    ioState = str(ioState)
    if len(ioState) > 8:
        ioState = ioState[:8]
    elif len(ioState) < 8:
        while len(ioState) < 8:
            ioState = '0'+ioState
    ignitionList.append(int(ioState[1]))
    ioStatebit3.append(int(ioState[2]))

speed = df['speed'].to_list()
sensor = input("Is sensor connected on DIN (Yes/No): \n")

print(type(ignitionList[0]))
print(type(tamperList[0]))
print(type(ioStateList[0]))
print(type(ioStatebit3[0]))
print(type(speed[0]))
print(type(vehicleBattery[0]))
print("Number of A packets -->> ", len(ioStateList))

batchSize = 100
batchCount = 1
print(batchSize)

for itr in range(0, len(tamperList), batchSize):

    print(batchCount)
    print(ingestionTime[itr])

    batchCount += 1
    tamperToggle = 0
    looseConnectionFlag = 0

    for j in range((itr+1), (itr+batchSize)):
        if tamperList[j] != tamperList[j-1]:
            tamperToggle += 1
    if tamperToggle >= 5:
        looseConnectionFlag = 1

    thsingleflag = 0
    thdoubleflag = 0

    for k in range((itr+1), (itr+batchSize)):

        if speed[k] == 0:

            if vehicleBattery[k] > 12.5 and vehicleBattery[k] < 13:
                if ignitionList[k] == 1 and ignitionList[k-1] == 0:
                    thsingleflag = 1

            if vehicleBattery[k] > 24.5 and vehicleBattery[k] < 25:
                if ignitionList[k] == 1 and ignitionList[k-1] == 0:
                    thdoubleflag = 1

    voltageCount = 0
    batteryMisbehaveFlag = 0

    for l in range((itr+1), (itr+batchSize)):

        if speed[l] > 0:
            if vehicleBattery[l] < 13.2:
                voltageCount += 1

    if voltageCount > 5:
        batteryMisbehaveFlag = 1

    ignitionConnflag = 0
    if sensor == "No":
        for m in range((itr+1), (itr+batchSize)):
            if speed[m] > 0:
                if ioStatebit3[m] == 1 and ioStatebit3[m-1] == 0:
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
