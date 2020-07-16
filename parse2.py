import pandas as pd
df = pd.read_csv('deviceData2930June.csv')
data = df['ioState'].to_list()
ignition=(data[0]/1000000)%10
tamper=(data[0]/10000000)%10

ignitionCount=0
tamperCount=0
combCount=0
counter = 0
for i in range(1, len(data)):
    ignitionValue = (data[i]/1000000)%10
    tamperValue = (data[i]/10000000)%10
    comb=(str(ignitionValue)+str(tamperValue))
    if comb=='11':
        combCount+=1

    if ignitionValue==1:
        counter+=1
        if counter==1000:
            print("Panic")
            counter=0
        if ignition==0:
            ignitionCount+=1
        ignition=1
    else:
        counter=0
        if ignition==1:
            ignitionCount += 1
        ignition=0

    if tamperValue == 1:
        if tamper == 0:
            tamperCount+=1
        tamper = 1
    else:
        if tamper == 1:
            tamperCount += 1
        tamper = 0

print(ignitionCount)
print(tamperCount)
print(combCount)
