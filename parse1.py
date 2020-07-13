import pandas as pd
df = pd.read_csv('deviceData2930June.csv')
data = df['ioState'].to_list()
flag=(data[0]/1000000)%10
count=0
for i in range(1, len(data)):
    value = (data[i]/1000000)%10
    if value==1:
        if flag==0:
            count+=1
        flag=1
    else:
        if flag==1:
            count += 1
        flag=0

print(count)
