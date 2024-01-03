import serial

import time

with open("env_secure.json", "rb+") as infile:
    data=infile.read()
    data=data
    infile.close()

serialcomm = serial.Serial('COM3', 9600)

serialcomm.timeout = 1

while True:

    i = input("Enter Input: ").strip()

    if i == "Done":
        print('finished')
        break

    elif i == "File":
        serialcomm.writelines(data)

    else:
        serialcomm.write(i.encode())

    print(serialcomm.readline())

serialcomm.close()

