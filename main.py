import os
device_type = input("Enter device type (FMB/Wetrack) : \n")
print(type(device_type))

csvFile = input("Enter CSV file name: \n")
print(type(csvFile))

if device_type == "FMB":
    comm = "python parse3.py " + csvFile
    os.system(comm)

elif device_type == "Wetrack":
    print("Run script for Wetrack. \n")

else:
    print("Invalid device type. \n")
